#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

address_to_server = ('localhost', 8686)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)

while True:
    client.send(bytes(input('Введите сообщение в следующем формате:\n'
                            'BBBBxNNxHH:MM:SS.zhqxGGCR\n>>>'), encoding='UTF-8'))

    data = client.recv(1024)
    print(str(data))
