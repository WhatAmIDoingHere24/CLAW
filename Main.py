import customtkinter
from command import command,toolList
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
title_bar = customtkinter.CTkLabel(master=claw, text = "Encryption / Decryption", width=150, height=80, 
                                   text_color="black", fg_color="grey")

#Ceates the 4 colums that the different buttons are put into
columFrame= customtkinter.CTkScrollableFrame(claw, fg_color= "transparent", border_width= 0, corner_radius= 0)
colum1 = customtkinter.CTkFrame(columFrame, width= ((claw_size[0] / 3) -10), fg_color= "transparent", 
                                border_width= 0, corner_radius= 0)

colum2 = customtkinter.CTkFrame(columFrame, width= ((claw_size[0] / 3) -10), fg_color= "transparent", 
                                border_width= 0, corner_radius= 0)

colum3 = customtkinter.CTkFrame(columFrame, width= ((claw_size[0] / 3) -10), fg_color= "transparent", 
                                border_width= 0, corner_radius= 0)

#colum4 = customtkinter.CTkFrame(columFrame, width= ((claw_size[0] / 4) -10), fg_color= "transparent", 
#                                border_width= 0, corner_radius= 0)

colums = [colum1, colum2, colum3]

#Adds the title_bar and all 4 colum widgets onto the screen
title_bar.pack(anchor= "nw", padx= 5, pady = 5)
columFrame.pack(anchor= "nw", fill = customtkinter.BOTH, expand= True)
for colum in colums:
    #Setting pack_propagate to False makes the frames not expand to hold the widgets in it
    #colum.pack_propagate(False)
    colum.pack(anchor= "nw", fill= customtkinter.Y, side = customtkinter.LEFT, expand= True)

counter = 0 #Counter used to start new row of buttons once all four colums get one button
toolButtons = [] #Holds all the tool Buttons from toolList 

#Iterates through toolList to create buttons with pairing function from command file
"""
Somthing that you can change with the buttons that you aree adding that 
would make them easier to call back to would be assining them different names
so you can actually call back to them later (there is no real need for this that often but just better habbit)

(I just added it)
"""
invalidChar = [" ", ".", "(", ")", "/"]
for i in range(len(toolList)):
    #Creates a function with the argument included (you cant pass an argument into a button command without this)
    newCommand = partial(command,toolList[i])
    #Creates button with new name and command
    button_name = toolList[i]
    for j in range(len(button_name)):
        for charcter in invalidChar:
            if button_name[j] == charcter:
                button_name = button_name[:j] + "_" + button_name[j+1:]

    button_text = toolList[i]
    for n in range(len(button_text)):
        if button_text[n] == " ":
            button_text = button_text[:n] + "\n" + button_text[n+1:]
    print(button_name)
    toolButtons.append(exec("%s = None" % (button_name)))
    toolButtons[-1] = customtkinter.CTkButton(master= colums[counter], text=button_text, height= 80, 
                                              width= ((claw_size[0] / 3) - 30),fg_color="blue", command=newCommand)

    #Math to reset colum
    if (counter % 2 == 0) and (counter > 0):
        counter = 0
    else:
        counter = counter + 1
    toolButtons[i]._text_label.configure(wraplength=((claw_size[0] / 3)))
    toolButtons[i].pack(padx = 10, pady = 15, side= customtkinter.TOP)


#runs the window until it is closed by user
claw.mainloop()