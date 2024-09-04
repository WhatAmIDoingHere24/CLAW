import customtkinter
from command import command, titleCardCommand, toolList, titleList
from functools import partial
import os

"""
welcome to CLAW!
-----------------------
The following code is brought to you by the cybears of tvhs

"""


#Sets default apperence to your systems default, and sets color theme to blue
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
#Intiilizing the window
claw = customtkinter.CTk()

claw_size = [600, 500]
claw.geometry((str(claw_size[0]) + "x" + str(claw_size[1])))
claw.resizable(False, False)
claw.title("CLAW")



#Creates label (1 for now)
title_bar_frame = customtkinter.CTkScrollableFrame(claw, height= 90, fg_color= "transparent",corner_radius= 0, border_width= 0)
title_bar_frame._scrollbar.configure(height=0)

rectLabel = customtkinter.CTkLabel(claw, text= "", fg_color= ("light grey", "grey20"), corner_radius= 10, height= 2)
#Ceates the 3 buttonColums that the different buttons are put into
columFrame= customtkinter.CTkScrollableFrame(claw, fg_color= "transparent", border_width= 0, corner_radius= 0)

buttonColums = []
for i in range(3):
    colum_name = "buttonColum" + str(i)
    buttonColums.append(exec("%s = None" % (colum_name)))
    buttonColums[i] = customtkinter.CTkFrame(columFrame, width= ((claw_size[0] / 3) -10), fg_color= "transparent", 
                                            border_width= 0, corner_radius= 0)
    
titleColum = []
for i in range(4):
    colum_name = "titleColum" + str(i)
    titleColum.append(exec("%s = None" % (colum_name)))
    titleColum[i] = customtkinter.CTkFrame(title_bar_frame, height= 90, width= ((claw_size[0] / 4) -10), 
                                           fg_color= "transparent", border_width= 0, corner_radius= 0)


#Adds the title_bar and all 3 colum widgets onto the screen
#title_bar.pack(anchor= "nw", padx= 5, pady = 5)
title_bar_frame.pack(anchor= "nw", fill= customtkinter.X)
rectLabel.pack(anchor= "nw", padx= 10, pady= 5, fill= customtkinter.X)
columFrame.pack(anchor= "nw", fill = customtkinter.BOTH, expand= True, side= customtkinter.TOP)

for colum in buttonColums:
    colum.pack(anchor= "nw", fill= customtkinter.Y, side = customtkinter.LEFT, expand= True)

for colum in titleColum:
    colum.pack(anchor= "nw", pady= 5, fill= customtkinter.Y, side = customtkinter.LEFT, expand= True)

#Holds all the tool Buttons from toolList 
toolButtons = []
titleCards = []
invalidChar = [" ", ".", "(", ")", "/"]

#Iterates through toolList to create buttons with pairing function from command file
for i in range(len(toolList)):
    toolButtons.append([])
    counter = 0 #Counter used to start new row of buttons once all three buttonColums get one button
    for j in range(len(toolList[i])):
        #Creates a function with the argument included (you cant pass an argument into a button command without this)
        newCommand = partial(command,toolList[i][j])
        #Creates button with new name and command

        button_name = toolList[i][j]

        for l in range(len(button_name)):
            for charcter in invalidChar:
                if button_name[l] == charcter:
                    button_name = button_name[:l] + "_" + button_name[l+1:]

        button_text = toolList[i][j]
        button_text_list = []

        for n in range(len(button_text)):
            if button_text[n].isupper() and (n != 0 and (button_text[n+1] != "." and button_text[n-1] != ".") and (button_text[n+1] != ")" and button_text[n-1] != "(")):
                button_text_list.append("\n")
            button_text_list.append(button_text[n])
        button_text = "".join(button_text_list)


        toolButtons[i].append(exec("%s = None" % (button_name)))
        toolButtons[i][j] = customtkinter.CTkButton(master= buttonColums[counter], text=button_text, text_color= ("white", "dark grey"), height= 80, 
                                                width= ((claw_size[0] / 3) - 30), fg_color= ("slate grey", "dark slate grey" ) , command=newCommand)

        if(counter % 2 == 0) and (counter > 0):
            counter = 0
        else:
            counter = counter + 1



#Iterates through TitleList to create a radio button for each title with a function from command
counter = 0
for i in range(len(titleList)):

    titleText = titleList[i]
    titleName= titleList[i]
    newCommand = partial(titleCardCommand, toolButtons, i, titleCards)

    for n in range(len(titleText)):
        if titleText[n] == " ":
            titleText = titleText[:n] + "\n" + titleText[n+1:]

    for j in range(len(titleName)):
        for charcter in invalidChar:
            if titleName[j] == charcter:
                titleName = titleName[:j] + "_" + titleName[j+1:]

    titleCards.append(exec("%s = None" % (titleName)))
    titleCards[i] = customtkinter.CTkButton(titleColum[counter], text= titleText, text_color= ("white", "grey10"), height= 60, width=((claw_size[0] / 4) - 50), 
                                            fg_color="goldenrod", hover= False, command=newCommand)
    titleCards[i].pack_propagate(False)
    titleCards[i].pack(padx = 20, pady = 10)
    if i == 0:
        newCommand()
    if(counter % 3 == 0) and (counter > 0):
        counter = 0
    else:
        counter = counter + 1
#runs the window until it is closed by user
def reset():
    if os.path.exists("users.txt"):  
        os.remove("users.txt")
    claw.destroy()


claw.protocol("WM_DELETE_WINDOW", reset)
claw.mainloop()