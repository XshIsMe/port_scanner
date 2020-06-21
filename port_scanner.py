#! /usr/bin/env python
# -*- coding: utf-8 -*-

import get_args
import tcp_scanner
import udp_scanner


def main():
    host_list, port_list = get_args.get_args()

    print '正在进行 tcp 端口扫描...'
    result_tcp = tcp_scanner.scan_tcp(host_list, port_list)
    print '正在进行 udp 端口扫描...'
    result_udp = udp_scanner.scan_udp(host_list, port_list)

    print 'tcp 端口扫描结果：', result_tcp
    print 'udp 端口扫描结果：', result_udp

if __name__ == "__main__":
    main()