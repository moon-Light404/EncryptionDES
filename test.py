# -*- coding: utf-8 -*-
# @Project: MIma
# @Author: dingjun
# @File name: test
# @Create time: 2022/1/2 20:29
# from PIL import Image
# import numpy as np
#
# from PIL import Image
# import math
#
# x = 320  # width    #x坐标  通过对txt里的行数进行整数分解
# y = 320  # height    #y坐标  x * y = 行数
#
#
# def img_to_rgb():
#     f = open("3.txt", 'w+')
#     im = Image.open('3.png')
#
#     width = im.size[0]
#     height = im.size[1]
#
#     rgb_im = im.convert('RGB')
#     for i in range(width):
#         for j in range(height):
#             r, g, b = rgb_im.getpixel((i, j))
#             print(r, g, b, file=f)
#
#
# def rgb_to_img():
#     im1 = Image.new("RGB", (x, y))  # 创建图片
#     file = open('3.txt')  # 打开rbg值的文件
#     # 通过每个rgb点生成图片
#     for i in range(0, x):
#         for j in range(0, y):
#             line = file.readline()  # 获取一行的rgb值
#             rgb = line.split(" ")  # 分离rgb，文本中逗号后面有空格
#             im1.putpixel((i, j), (int(rgb[0]), int(rgb[1]), int(rgb[2])))  # 将rgb转化为像素(i,j)表示坐标
#     im1.save("flag.png")  # im.save('flag.jpg')保存为jpg图片


sts = "fwa_aa"
print(sts.split('_')[0])
print(sts)