import glob
import os
import random
import shutil

rootdir = r'/content/yolov5/UCMerced_LandUse/Images'
trainimg = r'/content/yolov5/ucmdata/images/train'
valimg = r'/content/yolov5/ucmdata/images/val'
testimg = r'/content/yolov5/ucmdata/images/test'
trainlabel = r'/content/yolov5/ucmdata/labels/train'
valimglabel = r'/content/yolov5/ucmdata/labels/val'
testimglabel = r'/content/yolov5/ucmdata/labels/test'
fileslist = os.listdir(rootdir)
fileslist.sort()
for i in range(0, len(fileslist)):
    path = os.path.join(rootdir, fileslist[i])
    pic_path = path + r'/*.tif'
    image_files = glob.glob(pic_path)
    random.shuffle(image_files)
    train_list = image_files[:int(0.8 * len(image_files))]
    val_list = image_files[int(0.8 * len(image_files)):int(0.9 * len(image_files))]
    test_list = image_files[int(0.9 * len(image_files)):]

    for listT in train_list:
        if not os.path.exists(trainimg):
            os.makedirs(trainimg)
        if not os.path.exists(trainlabel):
            os.makedirs(trainlabel)
        imgname=os.path.splitext(os.path.basename(listT))[0]
        shutil.copy(listT, trainimg)
        label_pathT=trainlabel+r'/'+imgname+'.txt'
        f = open(label_pathT, 'w')
        f.write(str(i)+' 0.5 0.5 1 1')
    for listT in val_list:
        if not os.path.exists(valimg):
            os.makedirs(valimg)
        if not os.path.exists(valimglabel):
            os.makedirs(valimglabel)
        imgname=os.path.splitext(os.path.basename(listT))[0]
        shutil.copy(listT, valimg)
        label_pathT=valimglabel+r'/'+imgname+'.txt'
        f = open(label_pathT, 'w')
        f.write(str(i)+' 0.5 0.5 1 1')
    for listT in test_list:
        if not os.path.exists(testimg):
            os.makedirs(testimg)
        if not os.path.exists(testimglabel):
            os.makedirs(testimglabel)
        imgname=os.path.splitext(os.path.basename(listT))[0]
        shutil.copy(listT, testimg)
        label_pathT=testimglabel+r'/'+imgname+'.txt'
        f = open(label_pathT, 'w')
        f.write(str(i)+' 0.5 0.5 1 1')



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
