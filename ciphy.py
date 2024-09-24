import sys
import os
import subprocess

"""
We should just make the user 
"""

x = "python3 -m pip install ciphey --upgrade"


def homeDir():
    subprocess.run(["powershell", x], shell=True)