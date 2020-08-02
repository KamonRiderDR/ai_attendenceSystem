from torchvision.models import resnet18, resnet34, resnet50, resnet101, resnet152, alexnet, googlenet
from torchvision.transforms import Normalize, Resize
import torch
import cv2
import numpy

class ConvNetRecognizier:

    def __init__(self, filename="faceRecognizeAndTrain/alexnet.pt"):
        super(ConvNetRecognizier, self).__init__()
        self.filename = filename
        self.net = alexnet(num_classes=100)  # 聚合关系/包含关系
        self.CUDA = torch.cuda.is_available()
        if self.CUDA:
            self.net.cuda()
        self.state = torch.load(filename)   # 判定
        self.net.load_state_dict(self.state)

    

    def recoginize(self, img_file):   # 责任分配
        """
            img:ndarray: opencv打开的图像：摄像头抓取的图像
            img_file：图像文件
        """
        # 1. 打开图像
        #img = cv2.imread(img_file)   # ndarray
        img = img_file.astype("uint8")
        #img = img_file
        img = cv2.resize(img, (224, 224))
        # 2. 图像处理- 灰度/float/归一化/张量 (反色/去噪)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img.astype("float32")
        # img = img / 255.0
        
        img = img.transpose(2, 0, 1)
        img = torch.from_numpy(img).float().clone()  # img 类型Tensor
        # norm = Normalize(mean=(0.0, 0.0, 0.0), std=(1.0, 1.0, 1.0))
        # img = norm(img)
        # 3. 格式（NCHW）
        img = img.view(1, 3, 224, 224)
        # print(img)
        # 4. 输入预测模型
        if self.CUDA:
            img = img.cuda()
        self.net.eval()
        y = self.net(img)
        # 5. 判别类型，输出概率
        prob = torch.softmax(y, dim=1)
        cls_id = torch.argmax(prob,dim=1)
        cls_prob = prob[0, cls_id] 
        #print(cls_id, cls_prob)
        return (cls_id.cpu().detach().numpy()[0], cls_prob.cpu().detach().numpy()[0])


if __name__ == "__main__":
    recoginizer = ConvNetRecognizier()
    img = cv2.imdecode(numpy.fromfile("images/安典坤/001_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/安典坤/002_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/安典坤/002_2.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)
    print("")
    #=======================
    #
    #======================
    img = cv2.imdecode(numpy.fromfile("images/陈嘉博/001_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/陈嘉博/002_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/陈嘉博/002_2.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)
    print("")

    #=======================
    #
    #======================
    img = cv2.imdecode(numpy.fromfile("images/蔡林希/001_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/蔡林希/002_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/蔡林希/002_2.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)
    print("")

    #=======================
    #
    #======================
    img = cv2.imdecode(numpy.fromfile("images/董睿/001_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/董睿/002_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/董睿/002_2.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)
    print("")

    #=======================
    #
    #======================
    img = cv2.imdecode(numpy.fromfile("images/涂煜洋/001_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/涂煜洋/002_1.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)

    img = cv2.imdecode(numpy.fromfile("images/涂煜洋/002_2.jpg",dtype=numpy.uint8),-1)
    cls_id, prob = recoginizer.recoginize(img)
    print(cls_id, prob)
   
