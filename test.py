import subprocess
import os
import signal

# Simple command
proc = subprocess.Popen("sleep 500", shell=True)
os.kill(proc.pid, signal.SIGINT)
