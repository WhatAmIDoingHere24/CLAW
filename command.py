from crypto import encodeBase64, decodeBase64, encodeBase32, decodeBase32
from windowScriptManager import scriptManager
from CIA import cia
#from CipherID import torchTest
from CodeRed import CDRD

#List of tools to be assinged to buttons
toolList = ["encodeBase64","decodeBase64", "encodeBase32", "decodeBase32", "windowScripts", "C.I.A (Cipher Index Analysis)", "Cipher Recognition"," Code Red", "Shift Cipher"]

def command(commandName):
    match commandName:
        case "encodeBase64":
            print("this is base64")
            encodeBase64()
        case "decodeBase64":
            decodeBase64()
        case "bash":
            print("this is bash")
        case "md5":
            print("this is md5")
        case "windowScripts":
            print("this is windows script manager")
            scriptManager()
        case "encodeBase32":
            encodeBase32()
        case "decodeBase32":
            decodeBase32()
        case "C.I.A (Cipher Index Analysis)":
            cia()
        case "ciper recognition":
            print("this is supposed to be pytorch")#pyTorch()
        case "Code Red":
            CDRD()
        
    
            

