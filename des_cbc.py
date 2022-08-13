# -*- coding: utf-8 -*-
# @Project: MIma
# @Author: dingjun
# @File name: des_ctr
# @Create time: 2022/1/2 22:06
# des_ctr
# des_cbc
import sys

from rx.linq.observable import catch

import des as d
import os
import base as b

# 二重des两个加密密钥key1和key2
key1 = '01010010100110010101000100101001001101000101011001111000'
key2 = '00101011010101010101000111010010101001010110101010101010'
IV = '0101110001000010100101000101110110001000100110010001111000010000'


# 加密图片函数
def encryption(pic_name, secret_name):
    print("开始加密图片" + pic_name)
    img_bytes, w, h = b.get_img_bin(pic_name)  # 返回图片对于RGB值的二进制组合， 宽和高
    plain, n = d.des_input_plain(img_bytes)
    # b.get_bin_img(plain)
    iv1 = IV
    cipher_str = ''
    for i in range(n):
        plain_text = plain[i * 64: (i + 1) * 64]
        flag = 0
        iv1 = d.des(d.d_xor(iv1, plain_text), key1, flag)  # 加密所得的密文, 上一次密文与这一次明文异或
        iv1 = d.des(iv1, key2, flag)  # 对第一次加密的密文第二次加密
        cipher_str = cipher_str + ''.join(iv1)  # 密文链接起来
    # print(len(cipher_str))
    # d.des_output_cipher(cipher_str)
    b.get_bin_img(cipher_str, secret_name, w, h)  # 按照原图片w和h来生成加密图片，省去了多余的填充数据


# 解密图片函数
def decryption(pic_name, plain_name):
    print("开始解密图片"+pic_name)
    # ############### 解密 ##################  #
    img_bytes2, w2, h2 = b.get_img_bin(pic_name)
    cipher, n = d.des_input_cipher(img_bytes2)
    iv2 = IV
    plain_str = ''
    for i in range(n):
        cipher_text = cipher[i * 64: (i + 1) * 64]
        flag = 1  # 解密
        # t_ = d.d_xor(iv, d.des(cipher_text, key1, flag))
        fir = d.des(cipher_text, key2, flag)  # 第一次解密用key2
        t_ = d.d_xor(iv2, d.des(fir, key1, flag))  # 第二次解密用key1得到t_明文
        iv2 = cipher_text
        plain_str = plain_str + ''.join(t_)
    # d.des_output_plain(plain_str)
    b.get_bin_img(plain_str, plain_name, w2, h2)


# ECB加密模式
def encryption_ECB(pic_name, secret_name):
    img_bytes, w, h = b.get_img_bin(pic_name)
    plain, n = d.des_input_plain(img_bytes) # 明文和组数
    cipher_txt = ''
    for i in range(n):
        plain_txt = plain[i * 64 : (i + 1)*64]
        flag = 0
        cipher_t = d.des(plain_txt, key1, flag)
        cipher_t = d.des(cipher_t, key2, flag)
        cipher_txt = cipher_txt + ''.join(cipher_t)
    b.get_bin_img(cipher_txt, secret_name, w, h)

def decryption_ECB(pic_name, plain_name):
    img_bytes2, w2, h2 = b.get_img_bin(pic_name)
    cipher, n = d.des_input_cipher(img_bytes2)  # 明文和组数
    plain_str = ''
    for i in range(n):
        cipher_text = cipher[i * 64 : (i + 1) * 64]
        flag = 1
        fir = d.des(cipher_text, key2, flag)
        fir = d.des(fir, key1, flag)
        plain_str = plain_str + ''.join(fir)
    b.get_bin_img(plain_str, plain_name, w2, h2)

# CTR加密模式
def encryption_CTR(pic, secret):
    img_bytes, w, h = b.get_img_bin(pic)
    plain, n = d.des_input_plain(img_bytes)
    iv = IV
    cipher_str = ''
    for i in range(n):
        plain_text = plain[i * 64 : (i + 1) * 64]
        flag = 0
        # 加密两次
        _t = d.des(iv, key1, flag)
        _t = d.des(_t, key2, flag)
        # 异或
        cipher_str = cipher_str + ''.join(d.d_xor(plain_text, _t))
        iv = bin(int(iv, 2) + 1)[2:]
        iv = d.d_zero_fill(iv, len(iv), 64, 'l') # 左边填充
    b.get_bin_img(cipher_str, secret, w, h)

# def decryption_CTR(pic, plain):
#     img_bytes2, w2, h2 = b.get_img_bin(pic)
#     cipher, n = d.des_input_cipher(img_bytes2)
#     iv = IV
#     plain_str = ''
#     for i in range(n):
#         cipher_text = cipher[i * 64 : (i + 1) * 64]
#         flag = 1
#         _t = d.des(iv, key1, flag)
#         _t = d.des(_t, key2, flag)
#         plain_str = plain_str + ''.join(d.d_xor(cipher_text, _t))
#         iv = bin(int(iv, 2) + 1)[2:]
#         iv = d.d_zero_fill(iv, len(iv), 64, 'l')  # 左边填充
#     b.get_bin_img(plain_str, plain, w2, h2)

if __name__ == '__main__':
    while True:
        print("欢迎来到二重des图片加密系统   作者：丁俊  学号：8003119100")
        print("--------------1:加密图片----------------")
        print("--------------2:解密图片----------------")
        choice = input("------------请输入你要选择的功能(输入其他选项退出程序)----------")
        if choice == '1':
            picName = input("--------请输入你要加密的图片名----------")
            secretName = input("------------请输入你要保存的加密图片名称---------------")
            try:
                encryption_CTR(picName, secretName)
                print("加密成功，文件名为" + secretName)
            except FileNotFoundError:
                print("不存在该图片，请重新选择图片路径")

        elif choice == '2':
            secretName = input("--------请输入你要解密的图片名----------")
            plainName = input("------------请输入你要保存的解密后的图片名称---------------")
            try:
                encryption_CTR(secretName, plainName)
                print("解密成功，文件名为" + plainName)
            except FileNotFoundError:
                print("不存在该图片，请重新选择图片路径")
        else:
            sys.exit()  # 退出程序


