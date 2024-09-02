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
        case "windowScripts":
            print("this is windows script manager")
            scriptManager()
        case "encodeBase32":
            encodeBase32()
        case "decodeBase32":
            decodeBase32()
        case "C.I.A (Cipher Index Analysis)":
            cia()
        case "Cipher Recognition":
            torchTest()
        case "Code Red":
            CDRD()
        
    
            

