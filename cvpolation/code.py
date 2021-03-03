import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from prettytable import PrettyTable

class Interpolation:
    
    def __init__(self):
        pass
    
    def get_image(self, show = False):
        print("Current working directory:", os.getcwd())
        print("Files in CWD: ", os.listdir())
        self.file_name = input("Enter the Image name/Path including extention : ")
        if show:
            self.display_img()
            
    def display_img(self):
        self.im = Image.open(self.file_name)
        plt.imshow(self.im)
        
    def display_stats(self):
        img = Image.open(self.file_name)
        self.im = img.convert("RGB")
        self.width, self.height = self.im.size
        print("Image Height is", self.height)
        print("Image Width is", self.width)
        
        print("Image Format is", self.im.format)  
        print("Image Mode is", self.im.mode)
    
    def get_user_input(self):
        
        self.get_image(show = False)
        self.display_stats()
        
        t = PrettyTable(['Interpolation Method', 'Option'])
        t.add_row(['Zeroth Order', 1])
        t.add_row(['First Order', 2])
        t.add_row(['Bi-Linear', 3])
        t.add_row(['Bi-Cubic', 4])
        print(t)
        
        option = int(input("Enter the Option : "))
        
        if option == 1:
            self.zeroth_order()
        elif option == 2:
            self.first_order()
        elif option == 3:
            self.bi_linear()
        else:
            self.bi_cubic()
        
    
    def zeroth_order(self):
        print("ZEROTH ORDER INTERPOLATION")
        data = np.asarray(self.im)
        
        a = np.zeros((2*self.im.size[1], 2*self.im.size[0], 3))

        for i,channel in enumerate(data):
            for j,row in enumerate(channel):
                for k,column in enumerate(row):
                    a[2*i,2*j,k] = column
                    a[2*i+1,2*j,k] = column
                    a[2*i+1,2*j+1,k] = column
                    a[2*i,2*j+1,k] = column
                    
        self.dt = Image.fromarray((a).astype(np.uint8)).convert('RGB')
        plt.imshow(self.dt)
    
    def first_order(self):
        print("FIRST ORDER INTERPOLATION")
        data = np.asarray(self.im)
        
        a = np.zeros((2*self.im.size[1]+1, 2*self.im.size[0]+1, 3))

        for i,channel in enumerate(data):
            for j,row in enumerate(channel):
                for k,column in enumerate(row):

                    a[2*i,2*j,k] = column

        for i,channel in enumerate(data):
            for j,row in enumerate(channel):
                for k,column in enumerate(row):

                    a[2*i+1,2*j,k] = (a[2*i,2*j-1,k]+a[2*i+2,2*j+1,k])/2
                    a[2*i+1,2*j+1,k] = (a[2*i,2*j,k]+a[2*i+2,2*j+2,k])/2
                    a[2*i,2*j+1,k] = (a[2*i-1,2*j,k]+a[2*i+1,2*j+2,k])/2
        
        self.dt = Image.fromarray((a).astype(np.uint8)).convert('RGB')
        plt.imshow(self.dt)
        
    
    def bi_linear(self):
        print("BI-LINEAR INTERPOLATION")
        data = np.asarray(self.im)
        
        a = np.zeros((2*self.im.size[1]+1, 2*self.im.size[0]+1, 3))

        for i,channel in enumerate(data):
            for j,row in enumerate(channel):
                for k,column in enumerate(row):

                    a[2*i,2*j,k] = column

        for i,channel in enumerate(data):
            for j,row in enumerate(channel):
                for k,column in enumerate(row):

                    a[2*i+1,2*j,k] = (a[2*i,2*j-1,k]+a[2*i+2,2*j+1,k]+
                                      a[2*i+1,2*j-1,k]+a[2*i+1,2*j+1,k])/4
                    
                    a[2*i+1,2*j+1,k] = (a[2*i,2*j,k]+a[2*i+2,2*j+2,k]+
                                        a[2*i+1,2*j,k]+a[2*i+1,2*j+2,k])/4
                    
                    a[2*i,2*j+1,k] = (a[2*i-1,2*j,k]+a[2*i+1,2*j+2,k]+
                                      a[2*i,2*j,k]+a[2*i,2*j+2,k])/4
    
        self.dt = Image.fromarray((a).astype(np.uint8)).convert('RGB')
        plt.imshow(self.dt)
        
    def bi_cubic(self):
        print("BI-CUBIC INTERPOLATION")
        data = np.asarray(self.im)
        
        a = np.zeros((2*self.im.size[1]+1, 2*self.im.size[0]+1, 3))

        for i,channel in enumerate(data):
            for j,row in enumerate(channel):
                for k,column in enumerate(row):

                    a[2*i,2*j,k] = column

        for i,channel in enumerate(data):
            for j,row in enumerate(channel):
                for k,column in enumerate(row):

                    a[2*i+1,2*j,k] = (a[2*i,2*j-1,k]+a[2*i+2,2*j+1,k]+
                                      a[2*i+1,2*j-1,k]+a[2*i+1,2*j+1,k]+
                                      a[2*i,2*j,k]+a[2*i+2,2*j,k])/8

                    a[2*i+1,2*j+1,k] = (a[2*i,2*j,k]+a[2*i+2,2*j+2,k]+
                                        a[2*i+1,2*j,k]+a[2*i+1,2*j+2,k]+
                                           a[2*i+2,2*j+1,k]+a[2*i,2*j+1,k])/8



                    a[2*i,2*j+1,k] = (a[2*i-1,2*j,k]+a[2*i+1,2*j+2,k]
                                      +a[2*i,2*j,k]+a[2*i,2*j+2,k]+
                                      a[2*i-1,2*j+1,k]+a[2*i+1,2*j+1,k])/8
                    
        
        self.dt = Image.fromarray((a).astype(np.uint8)).convert('RGB')
        plt.imshow(self.dt)
    