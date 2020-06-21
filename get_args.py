#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
import analyzer


def show_help():
    '''显示帮助信息'''
    help_text = '''
    参数：
        -h,--help：显示帮助文档
        -t,--target <IP/网络号>：要扫描的目标主机
        -p,--port <端口/端口范围>：要扫描的端口
    示例：
        python port_scanner.py -t 192.168.1.1 -p 80
        python port_scanner.py -t 192.168.0.0/16 -p 1-100
    '''
    print help_text
    exit()

def get_args():
    '''获取参数'''
    try:
        opts, args = getopt.getopt(sys.argv[1:], '-h-t:-p:', ['help', 'target=', 'port='])
    except:
        show_help()
    if 0==len(opts) or 0!=len(args):
        show_help()

    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            show_help()
        if opt_name in ('-t', '--target'):
            host_list = analyzer.ip_analyzer(opt_value)
        if opt_name in ('-p', '--port'):
            port_list = analyzer.port_analyzer(opt_value)

    return host_list, port_list

if __name__ == "__main__":
    get_args()