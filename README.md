# CLAW
Cyber Logic Analyzer Workspace

This is a Workspace/Toolkit made by the Cybears / TVHS CyberPatriots for the CyberPatriot competition / CTFs. Includes encryption/decryption for most common ciphers, metadata for images / files, and modular automated scripts for both Linux and Windows VMs. Pull requests are welcome.

This project is a final send off for Cybears 2025. To be able to work with all the amazing people in the club has been an honor and we all wish to pass tools and tricks down to the next genration. HACK ON!

Pull Requests are welcome just dont push broken code. That's cringe.

# Compiling a Binary

To Compile:
- The pyinstaller package has to be installed through pip or as a package
- For every OS you target, pyinstaller has to be run on that OS
- The `ciphey` module does not work with pyinstaller, since it depends on `pywhat`

On Linux:
  `pyinstaller main.py --clean -F -n CLAW --add-binary "linxScripts/lucasuserscript/gum:./linxScripts/lucasuserscript"`
