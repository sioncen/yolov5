import glob
import os
import random
import shutil
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy
import math
import imgaug.augmenters as iaa
import random

rootdir = r'/content/yolov5/all/train'
trainimg = r'/content/yolov5/mydata/images/train'
valimg = r'/content/yolov5/mydata/images/val'
trainlabel = r'/content/yolov5/mydata/labels/train'
valimglabel = r'/content/yolov5/mydata/labels/val'
listfile = ['city', 'desert', 'farmland', 'lake', 'mountain', 'ocean']
rootdir2 = r'/content/yolov5/all/test'
testimg = r'/content/yolov5/mydata/images/test'
for i in range(0, len(listfile)):
    if not os.path.exists(testimg):
        os.makedirs(testimg)
    path = os.path.join(rootdir2, listfile[i])
    pic_path = path + r'/*.jpg'
    image_files = glob.glob(pic_path)
    print(i,len(image_files))
    for listT in image_files:
        shutil.copy(listT, testimg)

for i in range(0, len(listfile)):
    path = os.path.join(rootdir, listfile[i])
    print(path)
    pic_path = path + r'/*.jpg'
    image_files = glob.glob(pic_path)
    random.shuffle(image_files)
    if math.ceil(0.8 * len(image_files)) - 0.8 * len(image_files) < 0.5:
        tlen = math.ceil(0.8 * len(image_files))
    else:
        tlen = math.floor(0.8 * len(image_files))
    train_list = image_files[:tlen]
    val_list = image_files[tlen:]  # math.ceil(0.8 * len(image_files)):

    for listT in train_list:
        img = Image.open(listT)
        # plt.figure(figsize=(6, 6))
        img2 = img.transpose(Image.ROTATE_90)
        img3 = img.transpose(Image.ROTATE_180)
        img4 = img.transpose(Image.ROTATE_270)

        # 水平翻转
        img50 = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
        img51 = cv2.flip(img50, 1)
        img5 = Image.fromarray(cv2.cvtColor(img51, cv2.COLOR_BGR2RGB))
        img6 = img5.transpose(Image.ROTATE_90)
        img7 = img5.transpose(Image.ROTATE_180)
        img8 = img5.transpose(Image.ROTATE_270)
        # 垂直翻转
        img90 = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
        img91 = cv2.flip(img90, 0)
        img9 = Image.fromarray(cv2.cvtColor(img91, cv2.COLOR_BGR2RGB))
        img10 = img9.transpose(Image.ROTATE_90)
        img11 = img9.transpose(Image.ROTATE_180)
        img12 = img9.transpose(Image.ROTATE_270)
        # 水平加垂直翻转
        img30 = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
        img31 = cv2.flip(img30, -1)
        img13 = Image.fromarray(cv2.cvtColor(img31, cv2.COLOR_BGR2RGB))
        img14 = img13.transpose(Image.ROTATE_90)
        img15 = img13.transpose(Image.ROTATE_180)
        img16 = img13.transpose(Image.ROTATE_270)

        imglist = []
        imglist.append(img)
        imglist.append(img2)
        imglist.append(img3)
        imglist.append(img4)
        imglist.append(img5)
        imglist.append(img6)
        imglist.append(img7)
        imglist.append(img8)
        imglist.append(img9)
        imglist.append(img10)
        imglist.append(img11)
        imglist.append(img12)
        imglist.append(img13)
        imglist.append(img14)
        imglist.append(img15)
        imglist.append(img16)

        if not os.path.exists(trainimg):
            os.makedirs(trainimg)
        if not os.path.exists(trainlabel):
            os.makedirs(trainlabel)
        imgname = os.path.splitext(os.path.basename(listT))[0]
        for index, imgT in enumerate(imglist):
            a1 = cv2.cvtColor(numpy.asarray(imgT), cv2.COLOR_RGB2BGR)
            nameT = trainimg + str('/') + imgname + str('_') + str(index) + '.jpg'
            #数据增强
            randp = random.random()
            if randp < 0.125:
                seq = iaa.Sequential([
                    iaa.ChannelShuffle(0.35)
                ])
                a1 = seq(image=a1)
            elif randp < 0.25:
                seq = iaa.Sequential([
                    iaa.SaltAndPepper(0.1)
                ])
                a1 = seq(image=a1)
            elif randp < 0.375:
                seq = iaa.Sequential([
                    iaa.Dropout(p=(0, 0.2))
                ])
                a1 = seq(image=a1)
            elif randp < 0.5:
                seq = iaa.Sequential([
                    iaa.GammaContrast((0.5, 2.0))
                ])
                a1 = seq(image=a1)
            cv2.imwrite(nameT, a1)
            label_pathT = trainlabel + '/' + imgname + str('_') + str(index) + '.txt'
            f = open(label_pathT, 'w')
            f.write(str(i) + ' 0.5 0.5 1 1')
    # for listT in train_list:
    #     if not os.path.exists(trainimg):
    #         os.makedirs(trainimg)
    #     if not os.path.exists(trainlabel):
    #         os.makedirs(trainlabel)
    #     imgname=os.path.splitext(os.path.basename(listT))[0]
    #     shutil.copy(listT, trainimg)
    #     label_pathT=trainlabel+'/'+imgname+'.txt'
    #     f = open(label_pathT, 'w')
    #     f.write(str(i)+' 0.5 0.5 1 1')
    for listT in val_list:
        if not os.path.exists(valimg):
            os.makedirs(valimg)
        if not os.path.exists(valimglabel):
            os.makedirs(valimglabel)
        imgname = os.path.splitext(os.path.basename(listT))[0]
        shutil.copy(listT, valimg)
        label_pathT = valimglabel + '/' + imgname + '.txt'
        f = open(label_pathT, 'w')
        f.write(str(i) + ' 0.5 0.5 1 1')

# pic_path=r'F:\MyData\mydata\images\test\*.jpg'
# label_path=r'F:\MyData\mydata\labels\test/'
# image_files = glob.glob(pic_path)#sorted(glob.glob(pic_path))
# for index, image_file in enumerate(image_files):
#     filename=image_file
#     file=os.path.basename(filename)
#     label_pathT=label_path+file[:-4]+'.txt'
#     f = open(label_pathT, 'w')
#     if('City' in filename):
#         f.write('0 0.5 0.5 1 1')
#     elif ('Desert' in filename):
#         f.write('1 0.5 0.5 1 1')
#     elif ('Farmland' in filename):
#         f.write('2 0.5 0.5 1 1')
#     elif ('Lake' in filename):
#         f.write('3 0.5 0.5 1 1')
#     elif ('Mountain' in filename):
#         f.write('4 0.5 0.5 1 1')
#     elif ('Ocean' in filename):
#         f.write('5 0.5 0.5 1 1')

# pic_path=r'F:\MyData\train\ocean\*.jpg'
# pic_save1=r'F:\MyData\mydata\images\train'
# pic_save2=r'F:\MyData\mydata\images\val'
# label_path=r'F:\MyData\mydata\labels\train/'
# label2_path=r'F:\MyData\mydata\labels\val/'
# image_files = glob.glob(pic_path)#sorted(glob.glob(pic_path))
# random.shuffle(image_files)
# train_list = image_files[:int(0.8*len(image_files))]
# val_list = image_files[int(0.8*len(image_files)):]
# for index, image_file in enumerate(train_list):
#     filename=image_file
#     file=os.path.basename(filename)
#     shutil.copy(filename, pic_save1)
#     label_pathT=label_path+file[:-4]+'.txt'
#     f = open(label_pathT, 'w')
#     if('City' in filename):
#         f.write('0 0.5 0.5 1 1')
#     elif ('Desert' in filename):
#         f.write('1 0.5 0.5 1 1')
#     elif ('Farmland' in filename):
#         f.write('2 0.5 0.5 1 1')
#     elif ('Lake' in filename):
#         f.write('3 0.5 0.5 1 1')
#     elif ('Mountain' in filename):
#         f.write('4 0.5 0.5 1 1')
#     elif ('Ocean' in filename):
#         f.write('5 0.5 0.5 1 1')
# for index, image_file in enumerate(val_list):
#     filename=image_file
#     file=os.path.basename(filename)
#     shutil.copy(filename, pic_save2)
#     label_pathT=label2_path+file[:-4]+'.txt'
#     f = open(label_pathT, 'w')
#     if('City' in filename):
#         f.write('0 0.5 0.5 1 1')
#     elif ('Desert' in filename):
#         f.write('1 0.5 0.5 1 1')
#     elif ('Farmland' in filename):
#         f.write('2 0.5 0.5 1 1')
#     elif ('Lake' in filename):
#         f.write('3 0.5 0.5 1 1')
#     elif ('Mountain' in filename):
#         f.write('4 0.5 0.5 1 1')
#     elif ('Ocean' in filename):
#         f.write('5 0.5 0.5 1 1')


# pic_path='F:\MyData\image\/train1\*.jpg'
# label_path='F:\MyData\label\/train1/'
# image_files = sorted(glob.glob(pic_path))
# for index, image_file in enumerate(image_files):
#     filename=image_file
#     if('City' in filename):
#         file=os.path.basename(filename)
#         label_pathT=label_path+file[:-4]+'.txt'
#         f = open(label_pathT, 'w')
#         f.write('0 128 128 256 256')
#     elif ('Desert' in filename):
#         file = os.path.basename(filename)
#         label_pathT = label_path + file[:-4] + '.txt'
#         f = open(label_pathT, 'w')
#         f.write('1 128 128 256 256')
#     elif ('Farmland' in filename):
#         file = os.path.basename(filename)
#         label_pathT = label_path + file[:-4] + '.txt'
#         f = open(label_pathT, 'w')
#         f.write('2 128 128 256 256')
#     elif ('Lake' in filename):
#         file = os.path.basename(filename)
#         label_pathT = label_path + file[:-4] + '.txt'
#         f = open(label_pathT, 'w')
#         f.write('3 128 128 256 256')
#     elif ('Mountain' in filename):
#         file = os.path.basename(filename)
#         label_pathT = label_path + file[:-4] + '.txt'
#         f = open(label_pathT, 'w')
#         f.write('4 128 128 256 256')
#     elif ('Ocean' in filename):
#         file = os.path.basename(filename)
#         label_pathT = label_path + file[:-4] + '.txt'
#         f = open(label_pathT, 'w')
#         f.write('5 128 128 256 256')


# plt.subplot(441)
# plt.imshow(img)
# plt.subplot(442)
# plt.imshow(img2)
# plt.subplot(443)
# plt.imshow(img3)
# plt.subplot(444)
# plt.imshow(img4)
#
# plt.subplot(445)
# plt.imshow(img5)
# plt.subplot(446)
# plt.imshow(img6)
# plt.subplot(447)
# plt.imshow(img7)
# plt.subplot(448)
# plt.imshow(img8)
#
# plt.subplot(449)
# plt.imshow(img9)
# plt.subplot(4,4,10)
# plt.imshow(img10)
# plt.subplot(4,4,11)
# plt.imshow(img11)
# plt.subplot(4,4,12)
# plt.imshow(img12)
#
# plt.subplot(4,4,13)
# plt.imshow(img13)
# plt.subplot(4,4,14)
# plt.imshow(img14)
# plt.subplot(4,4,15)
# plt.imshow(img15)
# plt.subplot(4,4,16)
# plt.imshow(img16)
#
# plt.show()
