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
f=open("label.txt","w") #创建用于训练的标签文件
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

标签文件保存为label.txt，存放了每类图片对应的标签。
至此，训练集图片以及对应的标签文件解析完成........

## 二、生成Caffe用于训练的LMDB数据库
caffe训练之前要将图片数据转化为lmdb或者leveldb，现主要为lmdb，编译好的caffe中包含了转化程序convert_imageset,其路径在caffe/build/tools
格式如下：

convert_imageset [FLAGS] ROOTFOLDER/ LABELFILE DB_NAME  

    ROOTFOLDER为图片集的根目录
    LABELFILE为对应的标签文件
    DB_NAME为生成lmdb的根目录

另外还有一些可选参数：

    gray：bool类型，默认为false，如果设置为true，则代表将图像当做灰度图像来处理，否则当做彩色图像来处理

    shuffle：bool类型，默认为false，如果设置为true，则代表将图像集中的图像的顺序随机打乱

    backend：string类型，可取的值的集合为{"lmdb", "leveldb"}，默认为"lmdb"，代表采用何种形式来存储转换后的数据

    resize_width：int32的类型，默认值为0，如果为非0值，则代表图像的宽度将被resize成resize_width

    resize_height：int32的类型，默认值为0，如果为非0值，则代表图像的高度将被resize成resize_height

    check_size：bool类型，默认值为false，如果该值为true，则在处理数据的时候将检查每一条数据的大小是否相同

    encoded：bool类型，默认值为false，如果为true，代表将存储编码后的图像，具体采用的编码方式由参数encode_type指定

    encode_type：string类型，默认值为""，用于指定用何种编码方式存储编码后的图像，取值为编码方式的后缀（如'png','jpg',...)

生成lmdb：
```bash
sudo /home/gengjia/caffe/build/tools/convert_imageset --resize_height 96 --resize_width 96 /media/gengjia/DATA/PycharmProjects/HWDB/IMG/ /media/gengjia/DATA/PycharmProjects/HWDB/label.txt /media/gengjia/DATA/PycharmProjects/HWDB/train_lmdb/
```
脚本执行完后进入目录查看lmdb：

![](https://github.com/gengjia007/Caffe-HWDB/blob/master/img/lmdb.png)

到此用于训练的lmdb文件完成.......

###未完待续.....
