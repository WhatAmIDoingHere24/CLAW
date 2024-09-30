#!/usr/bin/env python3

from tkinter import Tk
import tkinter
import customtkinter
from customtkinter.windows.ctk_input_dialog import CTkButton
from customtkinter.windows.widgets.core_widget_classes.ctk_base_class import Any
from command import command, titleCardCommand, toolList, titleList
from functools import partial
import os

"""
welcome to CLAW!
-----------------------
The following code is brought to you by the cybears of tvhs

"""


#Sets default apperence to your systems default, and sets color theme to blue
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
#Intiilizing the window
claw = customtkinter.CTk()

claw_size = [600, 500]
claw.geometry((str(claw_size[0]) + "x" + str(claw_size[1])))
claw.resizable(True, True)
claw.title("CLAW")



# Create Frame for the Tabs
tabsFrame = customtkinter.CTkFrame(
    claw,
    height= 90,
    fg_color= "transparent",
    corner_radius= 0,
    border_width= 0,
    #scrollbar_button_color= ("gray87", "grey18")
)
#title_bar_frame._scrollbar.configure(width=0)

# Create a spacer between tabs and content
rectLabel = customtkinter.CTkLabel(
    claw,
    text= "",
    fg_color= ("light grey", "grey20"),
    corner_radius= 10,
    height= 2,
    #scrollbar_button_color= ("gray87", "grey18")
)

# Creates frame for content buttons
contentFrame= customtkinter.CTkFrame(
    claw,
    fg_color= "transparent",
    border_width= 0,
    corner_radius= 0,
    #scrollbar_button_color= ("gray87", "grey18")
)

# Make all columns to put inside of contentFrame
buttonColums = []
for i in range(3):
    colum_name = "buttonColum" + str(i)
    buttonColums.append(exec("%s = None" % (colum_name)))
    buttonColums[i] = customtkinter.CTkFrame(
        contentFrame,
        width= ((claw_size[0] / 3) -10),
        fg_color= "transparent",
        border_width= 0,
        corner_radius= 0
    )

# Adds all 3 frames to the screen
tabsFrame.pack(
    anchor= "nw",
    fill= customtkinter.X
)
rectLabel.pack(
    anchor= "nw",
    padx= 10,
    pady= 5,
    fill= customtkinter.X
)
contentFrame.pack(
    anchor= "nw",
    fill = customtkinter.BOTH,
    expand= True,
    side= customtkinter.TOP
)

# Display each column frame inside of contentFrame
for colum in buttonColums:
    colum.pack(anchor= "nw", fill= customtkinter.Y, side = customtkinter.LEFT, expand= True)

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
            if n == len(button_text):
                button_text_list.append("\n")
            button_text_list.append(button_text[n])
        button_text = "".join(button_text_list)


        toolButtons[i].append(exec("%s = None" % (button_name)))
        toolButtons[i][j] = customtkinter.CTkButton(
            master= buttonColums[counter],
            text=button_text,
            text_color= ("white", "dark grey"),
            height= 80,
            width= ((claw_size[0] / 3) - 20),
            fg_color= ("slate grey", "dark slate grey" ),
            command=newCommand)

        if(counter % 2 == 0) and (counter > 0):
            counter = 0
        else:
            counter = counter + 1



#Iterates through TitleList to create a radio button for each title with a function from command
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

    #titleCards.append(exec("%s = None" % (titleName)))

    newButton: CTkButton = customtkinter.CTkButton(
        tabsFrame,
        text= titleText,
        text_color= ("white", "grey10"),
        height= 60,
        width=((claw_size[0] / 4)-40),
        fg_color="goldenrod",
        hover= False,
        command=newCommand
    )

    # this is using grid, not pack, cus its easier
    #newButton.pack_propagate(False)
    #newButton.pack(padx = 20, pady = 10)
    newButton.grid(padx=20,pady = 10, row=0,column=i, sticky = "N")

    titleCards.append(newButton)

    # to auto select the first tab
    if i == 0:
        newCommand()

def handleClose():
        claw.withdraw()
        claw.quit()
        exit()


claw.protocol("WM_DELETE_WINDOW", handleClose)
claw.mainloop()
