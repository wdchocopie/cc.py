import os
import time
os.system('chmod +x multiproc.sh')
print("xong bước 1")
os.system('python3 cc.py -down -f proxy.txt -v 5 -check')
while True:
    os.system('bash multiproc.sh')
    time.sleep(290)
    os.system('python3 cc.py -down -f proxy.txt -v 5 -check')
    print("xong vòng lặp")