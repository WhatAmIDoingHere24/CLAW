import sys
import os
import subprocess


x = "python3 -m pip install ciphey --upgrade"


def homeDir():
    subprocess.run(["powershell", x], shell=True)