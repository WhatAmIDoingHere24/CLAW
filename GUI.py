import customtkinter
from command import command,toolList
from functools import partial

"""
welcome to CLAW!
-----------------------
The following code is brought to you by the cybears of tvhs

"""


#setting up start window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#intiilizing the window
claw = customtkinter.CTk()
claw.geometry("500x500")
claw.title("CLAW")

#tool1 window ()
def tool1_window():
    tool1Window = customtkinter.CTk()
    tool1Window.geometry('500x500')

    def buttonTouched():
        print('button been touched')

    button = customtkinter.CTkButton(master=tool1Window,
                                    command=buttonTouched,
                                    text='this is a second button',
                                    width=40,
                                    height=80,
                                    text_color='pink',
                                    fg_color='green'
                                    )
    
    button.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
    
    tool1Window.mainloop()


#main window
#interactive action's
def tool1_Press():
    tool1_window()

def tool2_Press():
    print("button2pressed")

def tool3_Press():
    print("button3pressed")




#creates / places label (1 for now)
title_bar = customtkinter.CTkLabel(master=claw,
                                    text = "Encryption / Decryption",
                                    width=110,
                                    height=50,
                                    text_color="black",
                                    fg_color="gray"
                                    )


xValue = 1
xSep = 130
yValue = 50
#iterates through toolList to create buttons with pairing function from command file
for i in range(len(toolList)):
    #createss a function with the argument included (you cant pass an argument into a button command without this)
    newCommand = partial(command,toolList[i])
    #creates button with new name and command
    tool = customtkinter.CTkButton(master=claw,
                                    command=newCommand,
                                    text=toolList[i],
                                    width=100,
                                    height=80,
                                    fg_color="blue",
                                    )
    #math to put buttons into four collumns
    if i % 4 == 0:
        yValue+=100
        xValue=0
    tool.place(x=(xValue*xSep),y=yValue)
    xValue+=1


#runs the window until it is closed by user
claw.mainloop()



















