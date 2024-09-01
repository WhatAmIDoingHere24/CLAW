#this is the main resean we devolped CLAW right here. it is 
#the ciper identification tool that make this whole project worth it

import torch
from CIA import cia
from crypto import encodeBase64, decodeBase64, encodeBase32, decodeBase32

"""
Jett's plans on how pytorch will work

Pre-Requisets
    -a seet of encrypted text paitred with matching unencrypted text
    -more CIA tools

1.user will enter the encrypted string into pytorch
2.pytorch will than do a few things at once
    -run that string char by char agiunast alll other strings to try and find a few tghat masy mathc
    -if a rough match is found run more test going char by char to de4duce how similar they are to erach other
3.pyutorch than runs the given encryptiont brough CIA and looks at what stats it gets
4.pytorch than matches those stats agoianst all other encryptions that may have those same stats
5.once a suitible match is found try the most proballble decryption algorythem
6. once done return what encryptio it is and tyhe given string

"""


def torchTest():
    #Sets default apperence to your systems default, and sets color theme to blue
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    #Initilizes the application screen 
    toolWindow = customtkinter.CTk()
    toolWindow.title("Cipher Identification")
    toolWindow.geometry('300x300')
    toolWindow.resizable(False, False)

    
    #Initilizes text box
    entry = customtkinter.CTkEntry(toolWindow, placeholder_text= "Enter text", placeholder_text_color= "grey", width=150, 
                                   height=50, text_color="black", fg_color= "light grey", border_width= 0, corner_radius= 5)
    #Initilizes result label
    resultLabel = customtkinter.CTkTextbox(toolWindow, width=150, height=50, text_color="black")
    resultLabel.configure(state= "disabled")

    #Adds all widgets to screen
    resultLabel.pack(anchor= "nw", padx = 10, pady = 10, fill= customtkinter.BOTH, expand= True)
    entry.pack(anchor= "nw", padx = 10, pady = 10, fill= customtkinter.X, side= customtkinter.BOTTOM)

