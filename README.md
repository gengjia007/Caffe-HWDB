# Caffe-HWDB
training HWDB1.1 with Caffe
## Tools
* Caffe 深度学习框架 
* HWDB1.1 手写训练集
* python 3.4 
* struct包: bytes解析
* PIL包：bytes-img转化
* numpy包：数据分析

## 一、获取HWDB训练集
#### 下载数据集:http://www.nlpr.ia.ac.cn/databases/handwriting/Offline_database.html 此数据集共有3755个汉字种类

#### 解析数据集：
下载的数据集并非图片格式，而是gnt的自定义文件类型，官网给出的gnt文件格式如下：
![](https://github.com/gengjia007/Caffe-HWDB/blob/master/img/gnt_format.png)

这里我们写一个python脚本，将文件里的tag code与bitmap解析转化为对应的标签与图片：
```python
#coding=utf-8
import struct
import os
from PIL import Image
DATA_PATH="/media/gengjia/DATA/PycharmProjects/HWDB/HWDB1.1" #gnt数据文件路径
IMG_PATH="/media/gengjia/DATA/PycharmProjects/HWDB/IMG"#解析后的图片存放路径
files=os.listdir(DATA_PATH)
num=0
for file in files:
    tag = []
    img_bytes = []
    img_wid = []
    img_hei = []
    f=open(DATA_PATH+"/"+file,"rb")
    while f.read(4):
        tag_code=f.read(2)
        tag.append(tag_code)
        width=struct.unpack('<h', bytes(f.read(2)))
        height=struct.unpack('<h',bytes(f.read(2)))
        img_hei.append(height[0])
        img_wid.append(width[0])
        data=f.read(width[0]*height[0])
        img_bytes.append(data)
    f.close()
    for k in range(0, len(tag)):
        im = Image.frombytes('L', (img_wid[k], img_hei[k]), img_bytes[k])
        if os.path.exists(IMG_PATH + "/" + tag[k].decode('gbk')):
            im.save(IMG_PATH + "/" + tag[k].decode('gbk') + "/" + str(num) + ".jpg")
        else:
            os.mkdir(IMG_PATH + "/" + tag[k].decode('gbk'))
            im.save(IMG_PATH + "/" + tag[k].decode('gbk') + "/" + str(num) + ".jpg")
    num = num + 1
print(tag.__len__())

files=os.listdir(IMG_PATH)
n=0
f=open("label.txt","w")
for file in files:
    files_d=os.listdir(IMG_PATH+"/"+file)
    for file1 in files_d:
        f.write(file+"/"+file1+" "+str(n)+"\n")
    n=n+1
```
一杯coffee的时间执行完毕后，查看目录：
![](https://github.com/gengjia007/Caffe-HWDB/blob/master/img/p_dir.png)

每个目录下有120张训练手写图片:
![](https://github.com/gengjia007/Caffe-HWDB/blob/master/img/p_img.png)
