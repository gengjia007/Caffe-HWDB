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
～下载数据集:http://www.nlpr.ia.ac.cn/databases/handwriting/Offline_database.html 此数据集共有3755个汉字种类

～解析数据集：
  下载的数据集并非图片格式，而是gnt的自定义文件类型，官网给出的gnt文件格式如下：
  
  这里我们写一个python脚本，将文件里的tag code与bitmap解析转化为对应的标签与图片：
  
