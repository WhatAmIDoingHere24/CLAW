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






#creates / places label (1 for now)
title_bar = customtkinter.CTkLabel(master=claw,
                                    text = "Encryption / Decryption",
                                    width=150,
                                    height=80,
                                    text_color="black",
                                    fg_color="gray"
                                    )

title_bar.place(x=10,y=10,)


xValue = 1
xSep = 130
yValue = 20
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



















