import subprocess
import os
import customtkinter
import time
import threading
import shutil
present_working_directory = os.getcwd()

# maybe add OS check so peolple dont run windows scripts on ubnutu and vice versa

def deleteUsers():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    dus = customtkinter.CTk()
    dus.title("deleteUsers")
    dus.geometry('300x50')
    dus.resizable(False, False)
    entry = customtkinter.CTkEntry(dus, placeholder_text= "Enter Users", placeholder_text_color= "grey", width=150,
                                   height=50, text_color="black", fg_color= "light grey", border_width= 0,
                                   corner_radius= 5)


    def deleteU(users):
        newPath = os.path.realpath("winScripts")
        os.chdir(newPath)
        scriptPath = os.path.realpath("deleteUsers.ps1")
        subprocess.run(["powershell.exe", "Start-Process powershell.exe -Verb RunAs -WindowStyle Hidden -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath + " -Users " + users + "\""])
        os.chdir(present_working_directory)

    def handleUserEntry(event):
        users = entry.get()
        if users[(len(users) -1 )] == " ":
            users = users[:-1]
        users = users + "."
        formatedUsers = ""
        if len(users) > 0:
            for i in range(len(users)):
                if ((i + 1) != len(users)) and (users[i:(i+1)] == " "):
                    formatedUsers = formatedUsers + "."
                else:
                    formatedUsers = formatedUsers + users[i:(i+1)]
            deleteU(formatedUsers)
        dus.destroy()
        pass

    entry.pack(anchor= "nw", fill= customtkinter.BOTH, expand= True)
    dus.bind('<Return>', handleUserEntry)
    dus.mainloop()

def addUsers():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    aus = customtkinter.CTk()
    aus.title("addUsers")
    aus.geometry('300x300')
    aus.resizable(False, False)

    ausEntry = customtkinter.CTkEntry(aus, placeholder_text= "Enter Users", placeholder_text_color= "grey", width=150,
                                   height=50, text_color="black", fg_color= "light grey", border_width= 0,
                                   corner_radius= 5)
    ausUserLabel = customtkinter.CTkTextbox(aus, text_color="black", border_width= 1, corner_radius= 5, border_color= "light grey")

    def addU(users):
        newPath = os.path.realpath("winScripts")
        os.chdir(newPath)
        scriptPath = os.path.realpath("addUsers.ps1")
        subprocess.run(["powershell.exe", "Start-Process powershell.exe -Verb RunAs -WindowStyle Hidden -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath + " -Users " + users + "\""])
        os.chdir(present_working_directory)

    def handleUserEntry(event):
        users = ausEntry.get()
        if users[(len(users) -1 )] == " ":
            users = users[:-1]
        users = users + "."
        formatedUsers = ""
        if len(users) > 0:
            for i in range(len(users)):
                if ((i + 1) != len(users)) and (users[i:(i+1)] == " "):
                    formatedUsers = formatedUsers + "."
                else:
                    formatedUsers = formatedUsers + users[i:(i+1)]
            addU(formatedUsers)
        aus.destroy()

    ausUserLabel.pack(anchor ="nw", padx= 10, pady = 10, fill = customtkinter.BOTH, expand= True)
    ausEntry.pack(anchor= "sw", fill= customtkinter.BOTH, expand= True, side= customtkinter.LEFT)
    aus.bind('<Return>', handleUserEntry)
    aus.mainloop()

def setDefaultRules():
    #Script go here
    newPath = os.path.realpath("winScripts")
    os.chdir(newPath)
    scriptPath = os.path.realpath("setDefaultRules.ps1")
    pass


def userManagerInterface():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    umi = customtkinter.CTk()
    umi.title("addUsers")
    umi.geometry('300x300')
    umi.resizable(False, False)

    allUsersFrame = customtkinter.CTkScrollableFrame(umi, width= 200, fg_color= "transparent", border_width= 1, border_color= "light grey", corner_radius= 0)
    entry = customtkinter.CTkEntry(umi, fg_color= "light grey", placeholder_text= "Enter users here",
                                   placeholder_text_color= "dark grey", border_width= 0, corner_radius= 0)

    allUsersFrame.pack(anchor= "ne", fill= customtkinter.Y, expand= True)
    entry.pack(anchor= "sw", fill= customtkinter.X)


    umi.mainloop()
import fileinput
def getUsers():
    newPath = os.path.realpath("winScripts")
    os.chdir(newPath)
    scriptPath = os.path.realpath("getAllUsers.ps1")
    newText = present_working_directory + "\\users.txt"
    subprocess.run(["powershell.exe", "Start-Process powershell.exe -WindowStyle Hidden -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath + " -Path " + newText + "\""])
    os.chdir(present_working_directory)
    while not os.path.exists("users.txt"):
        time.sleep(1)
    time.sleep(2)
    userFile = open("users.txt")
    stuff = userFile.readlines()
    for i in range(len(stuff)):
        print(stuff[i])


def startGetUsersThread():
    gettingUsers = threading.Thread(target= getUsers)
    gettingUsers.start()

def runLinuxUserScript():
    # I want this to open a new terminal window to run the script in, but that wouldn't be distro-agnostic
    # it also wont let me cd to the script directory to run it, so the gum executable has to be temporarily copied over for the script to run
    shutil.copy2("linxScripts/lucasuserscript/gum", "./")
    os.system("bash ./linxScripts/lucasuserscript/userscript.sh")
    os.remove("./gum")
    print("script has exited")
