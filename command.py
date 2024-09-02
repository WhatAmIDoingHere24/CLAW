from crypto import encodeBase64, decodeBase64, encodeBase32, decodeBase32
from windowScriptManager import scriptManager
import customtkinter
from CIA import cia
#from CipherID import torchTest
from CodeRed import CDRD

#List of tools to be assinged to buttons
titleList = ["Encryption / Decrption", "Window Scripts", "Linux Scripts", "Test"]
cryptoToolList = ["encodeBase64","decodeBase64", "encodeBase32", "decodeBase32", "C.I.A (Cipher Index Analysis)", "Cipher Recognition"," Code Red", "Shift Cipher"]
winScriptToolList = ["windowScripts"]
linScriptToolList = ["linuxScripts"]

toolList = [cryptoToolList, winScriptToolList, linScriptToolList]

def packButtons(buttonList, index, colums):
    counter = 0
    for i in range(len(buttonList)):
        if i == index:
            for j in range(len(buttonList[i])):
                #buttonList[i][j].configure(master= colums[counter])
                buttonList[i][j].pack(padx = 10, pady = 15, side= customtkinter.TOP)
        else:
            for n in range(len(buttonList[i])):
                buttonList[i][n].pack_forget()

def command(commandName, toolList, index, colums):
    match commandName:
        case "Encryption / Decrption":
            packButtons(toolList, index, colums)
        case "Window Scripts":
            packButtons(toolList, index, colums)
        case "Linux Scripts":
            packButtons(toolList, index, colums)
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
            #torchTest()
            pass
        case "Code Red":
            CDRD()
        
    
            

