#!/usr/bin/env python
# coding=utf-8

import os
import re
import socket
import time
import json
import threading


def get_ip():
    hostname = socket.getfqdn(socket.gethostname())
    ipaddr = socket.gethostbyname(hostname)
    print ipaddr
    return ipaddr

get_ip()
