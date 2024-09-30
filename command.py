from crypto import encodeBase64, decodeBase64, encodeBase32, decodeBase32, openDCodeLink
from scriptRunner import userManagerInterface, runPurgeEvilScript, runSecureUFWScript, setDefaultRules, runLinuxUserScript
import customtkinter
from codeRed import CDRD
import platform
#from cipheymodule import cipheyDecryptManager
#from ciphy import homeDir

#List of tools to be assinged to buttons
cryptoToolList = ["encodeBase64","decodeBase64", "encodeBase32", "decodeBase32", "Ciphey", "Open dcode.fr in browser"]
winScriptToolList = ["userManagerInterface","setDefaultRules"]
linScriptToolList = ["Lucas User Script", "Purge Unwanted Apps", "Secure UFW"]
ctfToolList = ["codeRed", "osint", "metaDataGrabber", "www"]

#Must match index of titleList and toolList if you want said title to show said tool buttons
titleList = ["Crypto Tools", "Window Scripts", "Linux Scripts", "CTF Tools"]
toolList = [cryptoToolList, winScriptToolList, linScriptToolList,ctfToolList]


def popup():
    popup = customtkinter.CTk()
    popup.geometry("250x100")
    popup.resizable(False, False)
    popup.title("Error: Wrong OS")

    def handleClose():
        popup.withdraw()
        popup.quit()
        #exit()

    textLabel = customtkinter.CTkLabel(popup, text = ("This feature doesn't work on " + platform.system() + "."))
    okay_Button = customtkinter.CTkButton(popup, text= "Okay", command= handleClose)
    textLabel.pack(pady = 10, expand=True)
    okay_Button.pack(pady = 10)

    popup.protocol("WM_DELETE_WINDOW", handleClose)
    popup.mainloop()



def command(commandName):
    match commandName:
        case "encodeBase64":
            print("this is base64")
            encodeBase64()
        case "decodeBase64":
            decodeBase64()
        case "encodeBase32":
            encodeBase32()
        case "decodeBase32":
            decodeBase32()
        case "CodeRed":
            CDRD()
        case "Ciphey":
            #cipheyDecryptManager()
            pass
        case "Open dcode.fr in browser":
            openDCodeLink()
        case "userManagerInterface":
            if platform.system() == "Windows":
                userManagerInterface()
            else:
                popup()
        case "setDefaultRules":
            if platform.system() == "Windows":
                setDefaultRules()
            else:
                popup()
        case "Lucas User Script":
            if platform.system() == "Linux":
                runLinuxUserScript()
            else:
                popup()
        case "Purge Unwanted Apps":
            if platform.system() == "Linux":
                runPurgeEvilScript()
            else:
                popup()
        case "Secure UFW":
            if platform.system() == "Linux":
                runSecureUFWScript()
            else:
                popup()


def packButtons(buttonList, index, titleList):
    for i in range(len(titleList)):
        if i == index:
            titleList[i].configure(fg_color=  "DarkGoldenrod4")
        else:
            titleList[i].configure(fg_color=  "goldenrod")
    for i in range(len(buttonList)):
        if i == index:
            for j in range(len(buttonList[i])):
                buttonList[i][j].pack(padx = 10, pady = 15, side= customtkinter.TOP)
        else:
            for n in range(len(buttonList[i])):
                buttonList[i][n].pack_forget()


def titleCardCommand(toolList, index, titleList):
    packButtons(toolList, index, titleList)
