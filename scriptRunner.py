import subprocess
import os
import customtkinter
import threading
from functools import partial
import shutil
present_working_directory = os.getcwd()

# maybe add OS check so peolple dont run windows scripts on ubnutu and vice versa

     
def userManagerInterface():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    umi = customtkinter.CTk()
    umi.title("addUsers")
    umi.geometry('500x500')
    umi.resizable(False, False)

    currentUsers = []
    currentUsers.extend(getUsers())
    userRadioButtons = []
    selectedUsers = []
    running = True

    def addUThreading(theUsers):
        addUThread = threading.Thread(target= partial(addU, theUsers))
        addUThread.start()

    def addU(theUsers):
        newPath = os.path.realpath("winScripts")
        os.chdir(newPath)
        scriptPath = os.path.realpath("addUsers.ps1")
        subprocess.run(["powershell.exe", "Start-Process powershell.exe -Verb RunAs -WindowStyle Hidden -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath + " -Users " + theUsers + "\""])
        os.chdir(present_working_directory)

    def deleteUThreading(theUsers):
        deleteUThread = threading.Thread(target= partial(deleteU, theUsers))
        deleteUThread.start()

    def deleteU(theUsers):
        newPath = os.path.realpath("winScripts")
        os.chdir(newPath)
        scriptPath = os.path.realpath("deleteUsers.ps1")
        subprocess.run(["powershell.exe", "Start-Process powershell.exe -Verb RunAs -WindowStyle Hidden -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath + " -Users " + theUsers + "\""])
        os.chdir(present_working_directory)

    def update():
        nonlocal currentUsers
        nonlocal selectedUsers
        while running:
            if getUsers() != currentUsers:
                while currentUsers != getUsers():
                    if len(currentUsers) < len(getUsers()):
                        for i in range(len(getUsers())):
                            if getUsers()[i] not in currentUsers:
                                currentUsers.insert(i, getUsers()[i])
                    elif len(currentUsers) > len(getUsers()):
                        i = 0
                        while i < len(currentUsers):
                            if currentUsers[i] not in getUsers():
                                userRadioButtons[i].destroy()
                                userRadioButtons.pop(i)
                                currentUsers.pop(i)
                                i -= 1
                            else:
                                i += 1
                    else:
                        for i in range(len(getUsers())):
                            if getUsers()[i] not in currentUsers:
                                currentUsers.insert(i, getUsers()[i])
                        i = 0
                        while i < len(currentUsers):
                            if currentUsers[i] not in getUsers():
                                userRadioButtons[i].destroy()
                                userRadioButtons.pop(i)
                                currentUsers.pop(i)
                                i -= 1
                            else:
                                i += 1
                selectedUsers = []
                addRadioButtons()

    def updateThreading():
        updateThread = threading.Thread(target= update)
        updateThread.start()

    def handleUserEntry(event):
        users = entry.get()
        entry.delete(0, customtkinter.END)
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
            addUThreading(formatedUsers)

    userFrame = customtkinter.CTkFrame(umi, width= 250, height= 250, fg_color= "transparent", border_width= 0, corner_radius= 0)
    userFrame.propagate(False)
    allUsersFrame = customtkinter.CTkScrollableFrame(userFrame, width= 200, fg_color= "transparent", border_width= 1, border_color= "light grey", corner_radius= 0)
    entry = customtkinter.CTkEntry(userFrame, fg_color= "light grey", placeholder_text= "Enter users here", 
                                   placeholder_text_color= "dark grey", border_width= 0, corner_radius= 0)

    def deleteSelectedUsers():
        print(selectedUsers)
        if len(selectedUsers) > 0:
            formatedUsers = ".".join(selectedUsers)
            formatedUsers += "."
            deleteUThreading(formatedUsers)
    
    deleteUserButton = customtkinter.CTkButton(umi, text= "delete users", text_color= ("black", "dark grey"), 
                                            fg_color= ("slate grey", "dark slate grey" ) , command= deleteSelectedUsers)
    deleteUserButton.pack(anchor = "nw", side = customtkinter.LEFT, padx = 10, pady = 10)
    entry.pack(anchor= "sw", fill= customtkinter.X, side = customtkinter.BOTTOM)
    allUsersFrame.pack(anchor= "nw", fill= customtkinter.BOTH, expand = True)
    userFrame.pack(anchor = "ne", side = customtkinter.LEFT, expand = True, fill = customtkinter.BOTH)


    def selected():
        for i in range(len(userRadioButtons)):
            print(userRadioButtons[i])
            if userRadioButtons != None:
                if userRadioButtons[i].get() == 1:
                    there = False
                    for user in selectedUsers:
                        if(user == userRadioButtons[i].cget("text")):
                            there = True
                    if not there:
                        selectedUsers.append(userRadioButtons[i].cget("text"))
                elif userRadioButtons[i].get() == 0:
                    for user in selectedUsers:
                        if(user == userRadioButtons[i].cget("text")):
                            del selectedUsers[selectedUsers.index(user)]
        print(selectedUsers)

    def addRadioButtons():
        radioButtonNames = []
        for button in userRadioButtons:
            radioButtonNames.append(button.cget("text"))
        for i in range(len(currentUsers)):
            if currentUsers[i] not in radioButtonNames:
                userName = currentUsers[i]
                userRadioButtons.insert(i, exec("%s = None" % (userName)))
                userRadioButtons[i] = customtkinter.CTkCheckBox(allUsersFrame, text= userName, text_color= ("black", "grey10"), command= selected)
                userRadioButtons[i].pack(anchor= "nw", pady = 10)
    
    def handleClose():
        nonlocal running
        running = False
        umi.destroy()
    
    addRadioButtons()
    updateThreading()
    umi.bind('<Return>', handleUserEntry)
    umi.protocol("WM_DELETE_WINDOW", handleClose)
    umi.mainloop()



def getUsers():
    p = subprocess.check_output(["powershell.exe", "Get-LocalUser"])
    mes = []
    add = True
    invalid = ['\r', '-']
    for i in range(len(p)):
            add = True
            for chra in invalid:
                if chr(p[i]) == chra:
                    add = False
            if chr(p[i]) == ' ' and chr(p[i- 1]) == ' ':
                add = False
            if add == True:
                mes.append(chr(p[i]))
    new = []

    for j in range(len(mes)):
        if j > 30:
            new.append(mes[j])
    

    while (" " in new):
        start = new.index(" ")
        while(new[start] != "\n"):
            del new[start]
        del new[start]
        new.insert(start, ".")
    
    news = ''.join(new)
    users = []
    while("." in news):
        users.append(news[0:news.index(".")])
        news = news[(news.index(".")+1):]

    removeUsers = ["WDAGUtilityAccount", "DefaultAccount", "Administrator"]
    for user in removeUsers:
        if user in users:
            del users[users.index(user)]

    return(users)

def setDefaultRules():
    #Script go here
    newPath = os.path.realpath("winScripts")
    os.chdir(newPath)
    scriptPath = os.path.realpath("setDefaultRules.ps1")
    pass

def runLinuxUserScript():
    # I want this to open a new terminal window to run the script in, but that wouldn't be distro-agnostic
    # it also wont let me cd to the script directory to run it, so the gum executable has to be temporarily copied over for the script to run
    shutil.copy2("linxScripts/lucasuserscript/gum", "./")
    os.system("bash ./linxScripts/lucasuserscript/userscript.sh")
    os.remove("./gum")
    print("script has exited")

def runPurgeEvilScript():
    os.system("sudo bash ./linxScripts/purgeEVIL.sh")

def runSecureUFWScript():
    os.system("sudo bash ./linxScripts/ufwSetup.sh")
