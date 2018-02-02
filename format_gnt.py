#coding=utf-8
import struct
import os
from PIL import Image
DATA_PATH="/media/gengjia/DATA/PycharmProjects/HWDB/HWDB1.1" #gnt数据文件路径
IMG_PATH="/media/gengjia/DATA/PycharmProjects/HWDB/IMG"#解析后的图片存放路径
#iles=os.listdir(DATA_PATH)
num=0
flag=0
'''
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
'''

files=os.listdir(IMG_PATH)
n=0
f=open("label.txt","w")
for file in files:
    files_d=os.listdir(IMG_PATH+"/"+file)
    for file1 in files_d:
        f.write(file+"/"+file1+" "+str(n)+"\n")
    n=n+1
