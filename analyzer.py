#! /usr/bin/env python
# -*- coding: utf-8 -*-

from IPy import IP


def ip_analyzer(input):
    '''分析ip地址是否合法
    
    Args:
        input: 用户输入的端口号
    '''
    try:
        ip_list = IP(input)
        return ip_list
    except:
        print '请输入正确的ip地址'
        exit()

def port_analyzer(input):
    '''分析端口号是否合法
    
    Args:
        input: 用户输入的端口号
    '''
    error = False  #检测是否通过的标记

    if '-' in input:
        port_list = input.split('-')
    else:
        port_list = [input]

    if 0==len(port_list):
        error = True
    else:
        for port in port_list:
            if port.isdigit():
                if int(port) in range(1, 65535):
                    pass
                else:
                    error = True
                    break
            else:
                error = True
                break
    if error:
        print '端口号只能是1-65535的数字'
        exit()
    elif 1 == len(port_list):
        return range(int(port_list[0]), int(port_list[0])+1)
    elif 2 == len(port_list):
        return range(int(port_list[0]), int(port_list[1])+1)