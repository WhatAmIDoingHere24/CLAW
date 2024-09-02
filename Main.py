import customtkinter
from command import command, toolList, titleList
from functools import partial

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
claw_size = [500, 500]
claw.geometry((str(claw_size[0]) + "x" + str(claw_size[1])))
claw.resizable(False, False)
claw.title("CLAW")



#Creates label (1 for now)
title_bar_frame = customtkinter.CTkScrollableFrame(claw, height=100, fg_color= "transparent",corner_radius= 0, border_width= 0)
title_bar_frame._scrollbar.configure(height=0)


#Ceates the 3 colums that the different buttons are put into
columFrame= customtkinter.CTkScrollableFrame(claw, fg_color= "transparent", border_width= 0, corner_radius= 0)

colums = []
for i in range(3):
    colum_name = "colum" + str(i)
    colums.append(exec("%s = None" % (colum_name)))
    colums[i] = customtkinter.CTkFrame(columFrame, width= ((claw_size[0] / 3) -10), fg_color= "transparent", 
                                border_width= 0, corner_radius= 0)


#Adds the title_bar and all 3 colum widgets onto the screen
#title_bar.pack(anchor= "nw", padx= 5, pady = 5)
title_bar_frame.pack(anchor= "nw", fill= customtkinter.X)
columFrame.pack(anchor= "nw", fill = customtkinter.BOTH, expand= True)
for colum in colums:
    #Setting pack_propagate to False makes the frames not expand to hold the widgets in it
    colum.pack(anchor= "nw", fill= customtkinter.Y, side = customtkinter.LEFT, expand= True)

#Holds all the tool Buttons from toolList 
toolButtons = []
titleCards = []
invalidChar = [" ", ".", "(", ")", "/"]

#Iterates through toolList to create buttons with pairing function from command file
counter = 0 #Counter used to start new row of buttons once all four colums get one button
for i in range(len(toolList)):
    toolButtons.append([])
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
        toolButtons[i][j] = customtkinter.CTkButton(master= colums[counter], text=button_text, height= 80, 
                                                width= ((claw_size[0] / 3) - 30),fg_color="blue", command=newCommand)

        if(counter % 2 == 0) and (counter > 0):
            counter = 0
        else:
            counter = counter + 1

#Iterates through TitleList to create a radio button for each title with a function from command
radioVar = customtkinter.StringVar()
radioVar.set(None)
for i in range(len(titleList)):

    titleName= titleList[i]
    newCommand = partial(command,titleList[i], toolButtons, i, colums)

    for j in range(len(titleName)):
        for charcter in invalidChar:
            if titleName[j] == charcter:
                titleName = titleName[:j] + "_" + titleName[j+1:]

    titleCards.append(exec("%s = None" % (titleName)))
    titleCards[i] = customtkinter.CTkRadioButton(title_bar_frame, text= titleList[i], height= 80, variable= radioVar, 
                                            fg_color="blue", value= i,command=newCommand)
    titleCards[i].pack(padx = 20, pady = 5, side= customtkinter.LEFT)
    pass
#runs the window until it is closed by user
claw.mainloop()