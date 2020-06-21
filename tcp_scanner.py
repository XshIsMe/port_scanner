#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
import threading
import multiprocessing


RESULT_DICT = {}  #存放扫描结果
SEM = threading.Semaphore(value=multiprocessing.cpu_count())  #线程池，大小等于CPU核心数


def tcp_scanner(host, port):
    '''扫描tcp端口

    Args:
        host：扫描的地址
        port：扫描的端口
    '''
    SEM.acquire()  #加入线程池
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.settimeout(3)
    try:
        sock_tcp.connect((host, port))
        RESULT_DICT[host].append(port)
    except:
        pass
    sock_tcp.close()
    SEM.release()  #退出线程池

def scan_tcp(host_list, port_list):
    '''扫描udp端口
    
    Args:
        host: 扫描的地址列表
        port: 扫描的端口列表
    '''
    threads = []  #线程列表
    for host in host_list:
        RESULT_DICT[str(host)] = []
        for port in port_list:
            t = threading.Thread(target=tcp_scanner, args=(str(host), int(port)))
            threads.append(t)
    for t in threads:
        t.setDaemon(True)  #设置为守护线程
        t.start()
        time.sleep(0.1)
    for t in threads:
        t.join()
    return RESULT_DICT

if __name__ == "__main__":
    host_list = ['192.168.1.1', 'www.baidu.com']
    port_list = range(1, 30)
    print scan_tcp(host_list, port_list)