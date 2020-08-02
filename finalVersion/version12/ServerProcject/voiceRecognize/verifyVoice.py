# coding: utf-8
import os, time
import numpy as np
import librosa
import soundfile as sf 
import voiceRecognize.model
import scipy.misc

import numpy as np
import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from concurrent.futures import ThreadPoolExecutor

# ===========================================
#            初始化模型
# ===========================================
class Mymodel(object):
    """docstring for Mymodel"""
    def __init__(self, network):
        super(Mymodel, self).__init__()
 
        self.network = network
    def get_feats(self, specs):
        feats = []
        feats = self.network.predict(specs)
        return feats

# ===========================================
#            声学特征处理
# ===========================================
def wav2spec(wav):
    wav = np.append(wav, wav[::-1])
    wav = wav.astype(np.float)
    linear_spect = librosa.stft(wav, n_fft=512, win_length=400, hop_length=160).T  #快速傅里叶变换
    mag, _ = librosa.magphase(linear_spect)  
    spec_mag = mag.T
    mu = np.mean(spec_mag, 0, keepdims=True)
    std = np.std(spec_mag, 0, keepdims=True)
    specs = (spec_mag - mu) / (std + 1e-5)
    specs = np.expand_dims(np.expand_dims(specs, 0), -1)  #增加一个维度
    return specs
    
def verifyVoiceVgg16(fileName1,fileName2):#fileName 1 正确文件
    print("开始验证！！！")
    os.environ["CUDA_VISIBLE_DEVICES"] = "0" # 如有GPU的话取消注释该行，GPU会加速特征提取.
    print("使用GPU")
    network_eval = model.vggvox_resnet2d_icassp(input_dim=(257, None, 1),num_class=5994, mode='eval')
    print("加载权重文件")
    network_eval.load_weights(os.path.join('model/weights.h5'), by_name=True)
    print("构造模型")
    my_model = Mymodel(network_eval)

    wav1_path = "audio/"+fileName1
    wav2_path = fileName2
    print("读取音频",wav1_path,wav2_path)
    audio1, sr = sf.read(wav1_path) # sr 采样率
    audio2, sr = sf.read(wav2_path)
    print("\n*\n*\n*\n*\n  获得音频")
    spec1 = wav2spec(audio1)
    spec2 = wav2spec(audio2)
    t0 = time.time()
    feat1 = my_model.get_feats(spec1)
    t1 = time.time()
    print("{} 语音时长: {}s，提取该语音所需时间: {} s".format(wav1_path, len(audio1)/sr, t1-t0))
    feat2 = my_model.get_feats(spec2)
    print("{} 语音时长: {}s，提取该语音所需时间: {} s".format(wav2_path, len(audio2)/sr, time.time()-t1))

    # 打分，参考阈值为0.82左右，即小于0.82则认为不是同一个说话人
    score = np.sum(feat1*feat2) 
    print(score)
    return score