# -*- coding: utf-8 -*-
# @Project: MIma
# @Author: dingjun
# @File name: base.py
# @Create time: 2022/1/2 22:04
# 字符变成2进制
from PIL import Image


def str_to_bin(s):
    res = []
    for c in s:
        tem = bin(ord(c)).replace('b', '')
        # 转为字符串时，后7位中，如果存在前面为0，会自动去掉，需要加回来，使之满足8位
        if len(tem) < 8:
            tem = "0" + tem
        res.append(tem)
    return ''.join(res)  # 返回二进制字符串


# 2机制到16进制
def bin_to_hex(s):
    return ''.join([hex(e).replace('0x', '') for e in
                    [int(b, 2) for b in [s[4 * j: 4 * (j + 1)] for j in range(int(len(s) / 4))]]]).upper()


# 16进制到2进制
def hex_to_bin(s):
    res = []
    for c in s:
        tem = bin(int(c, 16)).replace('0b', '')
        while True:
            if len(tem) < 4:
                tem = "0" + tem
            else:
                break
        res.append(tem)
    return ''.join(res)


# 2进制到10进制,指定8位二进制
def dec_to_bin(s):
    bin_chars = ""
    temp = s
    num = 8
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串


# 二进制转十进制
def bin_to_dec(n):
    return int(n, 2)


# print(dec_to_bin(214)) # 指定输出8位二进制数字

# 根据图像像素点,并返回二进制串每八位 == 一个十进制
def get_img_bin(img):
    # f = open("img.txt", 'w+')
    im2 = Image.open(img)
    w = im2.size[0]
    h = im2.size[1]

    rgb_im = im2.convert('RGB')
    img_chars = ""
    for i in range(w):
        for j in range(h):
            rgb = rgb_im.getpixel((i, j))  # 遍历像素点
            for r in rgb:  # 遍历rgb
                img_chars = img_chars + dec_to_bin(r)
    return img_chars, w, h  # 返回图片的二进制数据 和 w h


# 根据像素点的值成图像
def get_bin_img(img_s, img_name, w, h):
    print(len(img_s))
    image1 = []
    image2 = []
    for i in range(0, len(img_s), 8):
        image1.append(bin_to_dec(img_s[i + 0: i + 8]))  # 每次转8位二进制--一个十进制
    print(len(image1))
    for i in range(0, len(image1), 3):
        image2.append(image1[i:i + 3])
    print(len(image2))
    print("准备创建图片")
    img = Image.new("RGB", (w, h))
    j = 0
    for x in range(0, w):
        for y in range(0, h):
            img.putpixel((x, y), (image2[j][0], image2[j][1], image2[j][2]))
            # print(image2[j][0], image2[j][1], image2[j][2])
            # print(x, y, j)
            j = j + 1
    img.save(img_name)  # 自定义图像名称
    print("创建成功")

# get_img_bin("sss.png")  # 图片不存在
# get_img_bin("3.png")

# print(str_to_bin('abcdefgh'))
