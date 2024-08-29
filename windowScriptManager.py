import customtkinter
from functools import partial
from windowScipts import winScriptList,script


def scriptManager():
    scriptButtons = []  
    #Sets default apperence to your systems default, and sets color theme to blue
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    #Initilizes the application screen 
    #sciptManagerWindow =  smw
    smw = customtkinter.CTk()
    smw.title("windowsScriptManager")
    smw.geometry('300x300')
    smw.resizable(False, False)


    scriptFrame = customtkinter.CTkScrollableFrame(smw, orientation= "vertical", fg_color= "transparent")

    scriptFrame.pack(fill= customtkinter.BOTH, side= customtkinter.TOP, expand= True)



    for i in range(len(winScriptList)):
        #Creates a function with the argument included (you cant pass an argument into a button command without this)
        newCommand = partial(script,  winScriptList[i])
        #Creates button with new name and command
        scriptButtons.append(exec("%s = None" % (winScriptList[i])))
        scriptButtons[-1] = customtkinter.CTkButton(scriptFrame, text=winScriptList[i], height= 80, fg_color="blue", command=newCommand)

        #Add widget to screen in scriptFrame
        scriptButtons[i].pack(padx = 10, pady = 25, side= customtkinter.TOP)


    smw.mainloop()

