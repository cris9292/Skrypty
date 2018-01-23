#!/usr/bin/python
import os
cpu= os.popen("cat /proc/cpuinfo | grep processor").read()
ip= os.popen("ip address show dev enp0s3 | grep -w inet | awk '{print $2}' | cut -f1 -d/").read()
cpu= cpu.split('\n')
print(len(cpu)-1)
print(ip)
