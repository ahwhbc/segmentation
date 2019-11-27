# -*- coding: utf-8 -*-

from torch.utils.data import Dataset
import PIL.Image as Image
import os
import pandas as pd
import pdb

import os
import torch
import torchvision
from torchvision import datasets,transforms,models
from torch.utils import data
from PIL import Image
import config as cfg
import matplotlib.pyplot as plt
import copy

image_path="/dataset/images/"
label_path="/dataset/labels/"
train_data="/dataset/train.txt"

def make_dataset(image_path,label_path,train_data):
    dataset_path=[]
    with open(train_data,'r') as f:
        lines=f.readlines()
        for line in lines:
            if(line=="" or line=="\n"):
                continue
            dataset_path.append(line.split(" , ")[1].strip())
    imgs=[]      
    for i in dataset_path:
        img=os.path.join(image_path,str(i)+".jpg")
        mask=os.path.join(label_path,str(i)+"\\"+str(i)+"_lbl01.png")
        imgs.append((img,mask))
    return imgs   

#imgs=make_dataset(image_path,label_path,train_data)

class MyDataset(Dataset):
    def __init__(self, image_path,label_path,train_data, transform=None, target_transform=None):
        imgs = make_dataset(image_path,label_path,train_data)
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform

    def __getitem__(self, index):
        x_path, y_path = self.imgs[index]
        img_x = Image.open(x_path)
        img_y = Image.open(y_path)
        img_x = img_x.convert('RGB')
        if self.transform is not None:
            img_x = self.transform(img_x)
        if self.target_transform is not None:
            img_y = self.target_transform(img_y)
        return img_x, img_y

    def __len__(self):
        return len(self.imgs)
    
    
"""

x_transforms = transforms.Compose([
    #transforms.Resize(size=(224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

# mask只需要转换为tensor
y_transforms = transforms.Compose([
    #transforms.Resize(size=(224, 224)),
    transforms.ToTensor(),
])

dataset = MyDataset(image_path,label_path,train_data,transform=x_transforms, target_transform=y_transforms)
data_loader = data.DataLoader(dataset,  batch_size=1, shuffle=True, num_workers=0)


for step, (images,target) in enumerate(data_loader):
    print(images.size())
    print(target.size())
    print("=========") 
    #break
"""
    