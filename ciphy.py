#theres two ways we can use ciphey
#either ass a library which is kinda weird
#or as CLI which is much easier
"""
import ciphey
from ciphey import decrypt
from ciphey.iface import Config

res = decrypt(
        Config().library_default().complete_config(),
        "SGVsbG8gbXkgbmFtZSBpcyBiZWUgYW5kIEkgbGlrZSBkb2cgYW5kIGFwcGxlIGFuZCB0cmVl",
    )

"""
    
"""
import sys
import os
import subprocess


x = "python3 -m pip install ciphey --upgrade"


def homeDir():
    subprocess.run(["powershell", x], shell=True)

""""