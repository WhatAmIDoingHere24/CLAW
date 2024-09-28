import subprocess
import os
import customtkinter
import threading
from functools import partial
import shutil
import time
present_working_directory = os.getcwd()

# maybe add OS check so peolple dont run windows scripts on ubnutu and vice versa

     
def userManagerInterface():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    umi = customtkinter.CTk()
    umi.title("UMI")
    umi.geometry('500x500')
    umi.resizable(False, False)

    
    selectedUsers = []
    running = True
    groups = []
    users = []
    loading = True
    totalTime = 0
    timeIncreament = 0
    loadIncrement = False
    def current_users():
        tu = []
        for user in users:
            tu.append(user.user_name)
        return tu

    def selected():
        for i in range(len(users)):
            if users != None:
                if users[i].button.get() == 1:
                    there = False
                    for user in selectedUsers:
                        if(user == users[i].button.cget("text")):
                            there = True
                    if not there:
                        selectedUsers.append(users[i].button.cget("text"))
                elif users[i].button.get() == 0:
                    for user in selectedUsers:
                        if(user == users[i].button.cget("text")):
                            del selectedUsers[selectedUsers.index(user)]
    
    class User():
        def __init__(self, user_name, users_groups, master):
            self.user_name = user_name
            self.users_groups = users_groups
            self.button = customtkinter.CTkCheckBox(master = master, text= self.user_name, text_color= ("black", "grey10"), command= selected)
        

        def find_groups(self):
            for group in groups:
                check = group.user_check(self.user_name)
                if check != None:
                    self.users_groups.append(check)


    class Group():
        def __init__(self, group_name, users):
            self.group_name = group_name
            self.users = users

        def user_check(self, user):
            if user in self.users:
                return self.group_name
            


    def deleteSelectedUsers():
        if len(selectedUsers) > 0:
            formatedUsers = ".".join(selectedUsers)
            formatedUsers += "."
            deleteUThreading(formatedUsers)

    def handleUserEntry(event):
        users = entry.get()
        entry.delete(0, customtkinter.END)
        if users.replace(" ", "") != "":
            if users[(len(users) -1 )] == " ":
                users = users[:-1]
            formatedUsers = ""
            if len(users) > 0:
                while " " in users:
                    index = users.index(" ")
                    while users[index] == " ":
                        users = users[:index] + users[index + 1:]
                    formatedUsers = formatedUsers + users[:index] + "."
                    users = users[index:]
                formatedUsers = formatedUsers + users + "."

                addUThreading(formatedUsers)

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
        nonlocal selectedUsers
        while running:
            currentUsers = sorted(current_users())
            updatedUsers = sorted(getUsers())
            if updatedUsers != currentUsers:
                while currentUsers != updatedUsers:
                    currentUsers = sorted(current_users())
                    if len(currentUsers) < len(updatedUsers):
                        for i in range(len(updatedUsers)):
                            if updatedUsers[i] not in current_users():
                                try:
                                    users.append(exec("%s = None" % (updatedUsers[i])))
                                except SyntaxError:
                                    users.append(exec("%s = None" % ("_" +updatedUsers[i] )))
                                users[-1] = User(updatedUsers[i], [], allUsersFrame)
                    elif len(currentUsers) > len(updatedUsers):
                        i = 0
                        while i < len(currentUsers):
                            if currentUsers[i] not in updatedUsers:
                                users[i].button.pack_forget()
                                users[i].button.destroy()
                                del users[i]
                                currentUsers = current_users()
                                i -= 1
                            else:
                                i += 1
                    else:
                        for i in range(len(updatedUsers)):
                            if updatedUsers[i] not in currentUsers:
                                users.append(exec("%s = None" % (updatedUsers[i])))
                                users[i] = User(updatedUsers[i], [], allUsersFrame)
                                currentUsers = current_users()
                        i = 0
                        while i < len(currentUsers):
                            if currentUsers[i] not in updatedUsers:
                                users[i].button.pack_forget()
                                users[i].button.destroy()
                                del users[i]
                                currentUsers = current_users()
                                i -= 1
                            else:
                                i += 1
                selectedUsers = []
                addUserButtons()

    def updateThreading():
        updateThread = threading.Thread(target= update)
        updateThread.start()

    def addUserButtons():
        for i in range(len(users)):    
            users[i].button.pack(anchor= "nw", pady = 10)

    def handleClose():
        nonlocal running
        nonlocal loading
        loading = False
        running = False
        umi.withdraw()
        umi.destroy()
    
    
    showUserFrame = customtkinter.CTkFrame(umi, width= 250, height= 250, fg_color= "transparent", border_width= 0, corner_radius= 0)
    showUserFrame.propagate(False)
    allUsersFrame = customtkinter.CTkScrollableFrame(showUserFrame, width= 200, fg_color= "transparent", border_width= 1, border_color= "light grey", corner_radius= 0)
    entry = customtkinter.CTkEntry(showUserFrame, fg_color= "light grey", placeholder_text= "Enter users here", 
                                placeholder_text_color= "dark grey", border_width= 0, corner_radius= 0)

    deleteUserButton = customtkinter.CTkButton(umi, text= "delete users", text_color= ("black", "dark grey"), 
                                            fg_color= ("slate grey", "dark slate grey" ) , command= deleteSelectedUsers)
    
    

    loadingScreenFrame = customtkinter.CTkFrame(umi, fg_color= "lightSkyBlue1", border_width= 0, corner_radius= 0)
    loadingText = customtkinter.CTkLabel(loadingScreenFrame, width = 250, height= 50, fg_color= "transparent", text= "Loading UMI")
    loadingBar = customtkinter.CTkProgressBar(loadingScreenFrame, width = 250)
    loadingBar.set(0)
    loadingScreenFrame.pack(anchor = "nw", fill = customtkinter.BOTH, expand = True)
    loadingText.pack()
    loadingBar.pack(padx = 50)

    def loadingScreen():
        nonlocal loadIncrement
        while True:
            if loadIncrement:
                loadingBar.set(timeIncreament / totalTime)
                loadIncrement = False
            if loading == False:
                break
            time.sleep(0.00001)
        time.sleep(0.5)
        loadingScreenFrame.pack_forget()
        loadingText.pack_forget()
        loadingBar.pack_forget()
        deleteUserButton.pack(anchor = "nw", side = customtkinter.LEFT, padx = 10, pady = 10)
        entry.pack(anchor= "sw", fill= customtkinter.X, side = customtkinter.BOTTOM)
        allUsersFrame.pack(anchor= "nw", fill= customtkinter.BOTH, expand = True)
        showUserFrame.pack(anchor = "ne", side = customtkinter.LEFT, expand = True, fill = customtkinter.BOTH)
        addUserButtons()
        updateThreading()

    def loadingThreading():
        loadingThread = threading.Thread(target = loadingScreen)
        loadingThread.start()

    def creating_users_and_groups():
        nonlocal loading
        nonlocal groups
        nonlocal users
        nonlocal timeIncreament
        nonlocal totalTime
        nonlocal loadIncrement
        totalGroups = getGroups()
        totalUsers = getUsers()
        totalTime = len(getGroups()) + len(getUsers())

        for i in range(len(totalGroups)):
            groups.append(exec("%s = None" % (totalGroups[i])))
            groups[i] = Group(totalGroups[i], find_users_in_group(totalGroups[i]))
            timeIncreament += 1
            loadIncrement = True


        for i in range(len(totalUsers)):
            try:
                users.append(exec("%s = None" % (totalUsers[i])))
            except SyntaxError:
                users.append(exec("%s = None" % ("_" +totalUsers[i])))
            users[i] = User(totalUsers[i], [], allUsersFrame)
            timeIncreament += 1
            loadIncrement = True
        loading = False

    def creating_users_and_groups_Threading():
        creating_users_and_groups_Thread = threading.Thread(target = creating_users_and_groups)
        creating_users_and_groups_Thread.start()
    
    creating_users_and_groups_Threading()
    loadingThreading()
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

def getGroups():
    p = subprocess.check_output(["powershell.exe", "Get-LocalGroup"])
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
        if j > 21:
            new.append(mes[j])
    

    while (" " in new):
        start = new.index(" ")
        while(new[start] != "\n"):
            del new[start]
        del new[start]
        new.insert(start, ".")
    
    news = ''.join(new)
    groups = []
    while("." in news):
        groups.append(news[0:news.index(".")])
        news = news[(news.index(".")+1):]
    
    removeGroups = ["__vmware__", "Device", "Distributed", "Event", "HyperV", "IIS_IUSRS", "Performance", "System", "Remote"]
    for group in removeGroups:
        while group in groups:
            del groups[groups.index(group)]

    return(groups)

def find_users_in_group(group):
    p = subprocess.check_output(["powershell.exe", "Get-LocalGroupMember -Group \"" + group + "\""])
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
        if j > 36:
            new.append(mes[j])

    while ("\\" in new):
        if "." in new:
            start = new.index(".")
        else:
            start  = 0
        while(new[start] != "\\"):
            del new[start]
        del new[start]
        if start != 0:
            new.insert(start, "_")
        start = new.index(" ")
        while(new[start] != "\n"):
            del new[start]
        del new[start]
        if start == len(new) -2:
            new.insert(start, "_")
        else:
            new.insert(start, ".")
    
    
    news = ''.join(new)
    groups = []
    while("_" in news):
        groups.append(news[0:news.index("_")])
        news = news[(news.index("_")+1):]

    remove = ["INTERACTIVE", "Authenticated", "Administrator"]
    for group in remove:
        while group in groups:
            del groups[groups.index(group)]

    return(groups)



def setDefaultRules():
    newPath = os.path.realpath("winScripts")
    os.chdir(newPath)
    scriptPath = os.path.realpath("setDefaultRules.ps1")
    subprocess.run(["powershell.exe", "Start-Process powershell.exe -Verb RunAs -WindowStyle Hidden -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath  + "\""])
    os.chdir(present_working_directory)

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
