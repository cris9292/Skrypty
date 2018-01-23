#!/bin/sh
ip address show dev enp0s3 | grep -w inet | awk '{print $2}' | cut -f1 -d/
