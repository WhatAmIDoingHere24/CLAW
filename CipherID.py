#this is the main resean we devolped CLAW right here. it is 
#the ciper identification tool that make this whole project worth it

import torch
from CIA import cia
from crypto import encodeBase64, decodeBase64, encodeBase32, decodeBase32

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

