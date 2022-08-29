#!/usr/bin/env python
# coding: utf-8

import torch
from torch import nn, optim
from torchvision import models


class MyCustomModel(nn.Module) :
    #input_size = 128
    
    def __init__(self) :
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Flatten()
        )
        self.fc = nn.Sequential(
            nn.Linear(in_features=2048, out_features=1024),
            nn.ReLU(),
            nn.Linear(in_features=1024, out_features=7),
            nn.LogSoftmax(1)
        )
    def forward(self, x) :
        x = self.conv(x)
        x = self.fc(x)
        return x

    
class CustomResnet152(nn.Module) :
    #input size = 224
    
    def __init__ (self) :
        super().__init__()
        self.resnet152 = models.resnet152(pretrained=True)
        self.freeze()
        # custom Linear
        self.resnet152.fc = nn.Sequential(
            nn.Linear(in_features=2048, out_features=7, bias=True),
            nn.LogSoftmax(1)
        )
    
    def forward(self, x) :
        x = self.resnet152(x)
        return x
    
    def freeze(self) :
        for param in self.resnet152.parameters() :
            param.requires_grad = False
            
    def unfreeze(self) :
        for param in self.resnet152.parameters() :
            param.requires_grad = True     
