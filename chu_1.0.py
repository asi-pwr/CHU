#!/usr/bin/env python3
# Python2.7 should die already

import subprocess
import sys
import re
import datetime
if(len(sys.argv) > 1 and re.match('^\d{1,3}.\d{1,3}.\d{1,3}$', sys.argv[1])):
    print(sys.argv)
    amount = 0
    hostname = sys.argv[1]
    startValue = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    endValue = int(sys.argv[3]) if len(sys.argv) > 3 else 254
    path = sys.argv[4] if len(sys.argv) > 4 else "output.txt"
    if(startValue < endValue):

        for i in range(startValue,endValue):
            output = subprocess.Popen(["ping", "-c", "1", "-w", "2","{}.{}".format(hostname, str(i))], stdout = subprocess.PIPE).communicate()[0]
            output = str(output)
            if('100% packet loss' not in output):
                amount += 1

        with open(path, "w") as f:
            f.write("{} at {}".format(str(amount), datetime.datetime.utcnow()))
