# -*- coding: utf-8 -*-
# @Project: MIma
# @Author: dingjun
# @File name: des.py
# @Create time: 2022/1/2 22:05
# ECB
import fun as f


# 按照DES算法的流程图进行运算
def des(text, key_, flag_):  # text 2进制列表
    text = f.f_IP(text) # 初始置换
    sub_keys = f.f_sub_keys(key_)  # 16个子密钥
    if flag_ == 1:
        sub_keys.reverse()  # 如果是解密就把子密钥倒转
    L, R = text[:32], text[32:]
    # 进行16轮
    for net in range(16):
        temp = R
        temp = f.f_expand(temp)
        temp = f.f_xor(temp, sub_keys[net])
        temp = f.f_s_boxes(temp)
        temp = f.f_p_box(temp)
        temp = f.f_xor(temp, L)
        L, R = R, temp  # 交换左右分组L和R
    res = f.f_IP_(R + L) # 逆IP置换
    return res


# 传入明文和填充比特
def des_input_plain(plain_text):
    input_ = plain_text  # 明文赋值
    n_ = len(input_) // 64  # 有n组64位的数据
    mod = len(input_) % 64
    if mod != 0:
        n_ = n_ + 1
        input_ = f.f_zero_fill(input_, mod, 64, 'r')  # 最后一组不足64位补0
    return input_, n_


# 传入密文
def des_input_cipher(cipher_text):
    input_ = cipher_text
    n_ = len(input_) // 64
    return input_, n_


def des_output_cipher(cipher_str_):
    print("---------加密----------")
    print("2进制密文：" + cipher_str_)
    # print("16进制密文：", p.bin_to_hex(cipher_str_))
    print()


def des_output_plain(plain_str_):
    print("---------解密----------")
    print("2进制明文：" + plain_str_)
    # print("明文：", p.bin_to_str(plain_str_))
    print()


d_xor = f.f_xor

d_zero_fill = f.f_zero_fill

