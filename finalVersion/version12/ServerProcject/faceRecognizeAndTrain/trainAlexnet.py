from torch.nn  import CrossEntropyLoss
from torch.optim import Adam
import torch
import os
from faceRecognizeAndTrain.loaddata import load_data
from PyQt5.QtCore import pyqtSignal,Qt,QObject
from torchvision.models import resnet18, resnet34, resnet50, resnet101, resnet152, alexnet, googlenet
class ConvNetTrainer(QObject):
    sign_ReturnStaffInfo = pyqtSignal(dict)
    def __init__(self, model_path="faceRecognizeAndTrain/alexnet.pt", lr=0.0001, num_classes=100):
        super(ConvNetTrainer,self).__init__()
        # 定义训练集/定义测试集
        
        # 网络模型
        self.net = alexnet(num_classes=num_classes)
        self.CUDA = torch.cuda.is_available() 
        if self.CUDA:
            self.net.cuda()    # 训练参数
        # 模型文件
        self.filename = model_path
        if os.path.exists(self.filename):
            state_dict = torch.load(self.filename)
            self.net.load_state_dict(state_dict)
        # 损失函数
        self.loss_f = CrossEntropyLoss()
        # 优化器
        self.lr = lr
        self.optimizier = Adam(self.net.parameters(), lr=self.lr)

    def train_one(self):
        print("train one")
        self.net.train()
        print("start")
        for x_, y_ in self.loader_train:
            if self.CUDA:
                x_ = x_.cuda()
                y_ = y_.cuda()
            # 向前
            y = self.net(x_)
            # 计算损失
            loss = self.loss_f(y, y_)
            # 求导
            self.optimizier.zero_grad()
            loss.backward()
            # 更新梯度
            self.optimizier.step()
            # print(F"损失值：{loss:8.6f}")
    
    @torch.no_grad()
    def valid(self):
        
        all_num = 0.0
        acc = 0.0
        all_loss = 0.0
        self.net.eval()
        for v_x, v_y in self.loader_valid:
            all_num += len(v_y)
            if self.CUDA:
                v_x = v_x.cuda()
                v_y = v_y.cuda()
            y = self.net(v_x) 
            all_loss += self.loss_f(y, v_y)
            prob = torch.softmax(y, dim=1)  # 分类判别是可选
            y_cls = torch.argmax(prob, dim=1) 
            # 统计正确数
            acc += (y_cls == v_y).float().sum()
        print(F"测试集损失：{all_loss:8.6f}")
        print(F"\t|- 验证集识别正确率：{100.0 * acc/all_num:5.2f}%")
            

    def train(self, epoch, interval=1):
        print("Enter Train")
        self.loader_train, self.loader_valid, staffInfo = load_data(ds_path="./images", batch_size=40)
        self.sign_ReturnStaffInfo.emit(staffInfo)
        print("Return To Server")
        for e in range(epoch):
            self.train_one()
            print("真正训练")
            if e % interval ==0:
                self.valid()
                torch.save(self.net.state_dict(), self.filename)


if __name__ == "__main__":
    trainer = ConvNetTrainer()
    trainer.train(epoch=4)
