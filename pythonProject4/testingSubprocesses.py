import subprocess
import time
from datetime import datetime

p = subprocess.Popen('sleep 60', shell=True)

while True:
    rc = p.poll()
    if rc is None:
        print(f"{datetime.now()} Process with PID: {p.pid()} is still running")
        time.sleep(60)
    else:
        print(f"{datetime} Process with PID: {p.pid} has terminated")
        break