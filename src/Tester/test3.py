# -*- coding: utf-8 -*-
import re
import sys

with open('/proc/net/tcp') as f:
    lineno = 0
    sockets = []
    for line in f:
        lineno += 1
        if lineno == 1:
            continue

        sockets.append(line.strip())

columns = ("seq", "uid", "inode", "local", "remote", "timeout")
title = dict()
for c in columns:
    title[c] = c

def split_every_n(data, n):
    return [data[i:i+n] for i in range(0, len(data), n)]

def convert_linux_netaddr(address):

    hex_addr, hex_port = address.split(':')

    addr_list = split_every_n(hex_addr, 2)
    addr_list.reverse()

    addr = ".".join(map(lambda x: str(int(x, 16)), addr_list))
    port = str(int(hex_port, 16))

    return "{0}:{1}".format(addr, port)

def format_line(data):
    return (("%(seq)-4s %(uid)5s %(local)25s %(remote)25s " +
             "%(timeout)8s %(inode)8s" % \
             data) + "\n")

rv = []
for info in sockets:
    _ = re.split(r'\s+', info)

    _tmp = {
        'seq': _[0],
        'local': convert_linux_netaddr(_[1]),
        'remote': convert_linux_netaddr(_[2]),
        'uid': _[7],
        'timeout': _[8],
        'inode': _[9],
    }
    rv.append(_tmp)

if len(rv) > 0:
    sys.stderr.write(format_line(title))

    for _ in rv:
        sys.stdout.write(format_line(_))