#!/usr/bin/python
import sys, os, re
if not os.path.exists(sys.argv[1]):
    sys.exit()
print sys.argv[1]

gap=file(sys.argv[1])
y=gap.read()
y=y.split('\n')
print y[0]

for line in y:
    print len(line)

dlug=80
for line in y:
    if dlug == len(line):
        print line

for line in y:
    if re.search('[0-9]',line):
        print line
