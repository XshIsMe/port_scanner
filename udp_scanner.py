#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
import threading


RESULT_DICT = {}  #存放扫描结果


def icmp_receiver(host, port):
    '''接收icmp报文
    
    Args:
        host: 扫描的地址
        port: 扫描的端口
    '''
    HOST = '0.0.0.0'
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sniffer.bind((HOST, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sniffer.settimeout(3)
    try:
        for i in range(5):
            data, address = sniffer.recvfrom(64)
            return
    except:
        pass
    RESULT_DICT[host].append(port)

def udp_scanner(host, port):
    '''发送udp报文
    
    Args:
        host: 扫描的地址
        port: 扫描的端口
    '''
    t = threading.Thread(target=icmp_receiver, args=(host, port))
    t.start()
    try:
        sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in range(5):
            sock_udp.sendto(b'', (host, port))
        sock_udp.close()
    except:
        return
    time.sleep(3)
    t.join()

def scan_udp(host_list, port_list):
    '''扫描udp端口
    
    Args:
        host: 扫描的地址列表
        port: 扫描的端口列表
    '''
    for host in host_list:
        RESULT_DICT[str(host)] = []
        for port in port_list:
            udp_scanner(str(host), int(port))
    return RESULT_DICT

if __name__ == "__main__":
    host_list = ['192.168.1.1', '192.168.0.1']
    port_list = range(50, 60)
    print scan_udp(host_list, port_list)