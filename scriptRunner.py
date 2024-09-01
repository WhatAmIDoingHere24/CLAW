import subprocess
import os
import customtkinter

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
        subprocess.run(["powershell.exe", "Start-Process powershell.exe -Verb RunAs -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath + " -Users " + users + "\""])
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
    def test():
        print("test")
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
        subprocess.run(["powershell.exe", "Start-Process powershell.exe -Verb RunAs -ArgumentList \"-ExecutionPolicy Unrestricted -File " + scriptPath + " -Users " + users + "\""])
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