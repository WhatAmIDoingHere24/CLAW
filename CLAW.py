#import pytorch
#import time
#import math
#import matplotlib
#import scapy
#import PyCrypto
#import BeautifulSoup
#import Paramiko
#import nmap
#import scikitlearn
#import socket
#import ploty
#import pandas
#import Pygal
#import numpy
import customtkinter
import tkinter
#import pillow
#import subprocess
#import threading
#import socket
#holy carp this is a lot of libraries lets hope threading helps at all

"""
welcome to CLAW!
-----------------------
The following code is brought to you bby the cybears of tvhs

TO DO:
Plan application use cases
Sketch out GUI ideas
Create GUI
Decryption
Encryption
Image Proccesing
Making it not run like a fish out of water
find files
execute bash scripts
script builder
!WIP! custom encryption

[etc...add other stuff to do :3]

"""
#setting up start window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#intiilizing the window
claw = customtkinter.CTk()
claw.geometry("500x500")

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
    
    button.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    
    tool1Window.mainloop()


#main window
#interactive action's
def tool1_Press():
    tool1_window()

def tool2_Press():
    print("button2pressed")

def tool3_Press():
    print("button3pressed")


#settign up elements
title_bar = customtkinter.CTkLabel(master=claw,
                                   text = "Welcome to CLAW you'r CyberPatriot ToolKit",
                                   width=80,
                                   height=50,
                                   text_color="black",
                                   fg_color="red",
                                   )


tool1 = customtkinter.CTkButton(master=claw,
                                command=tool1_Press,
                                text="button1",
                                width=100,
                                height=80,
                                fg_color="blue",
                                )


tool2 = customtkinter.CTkButton(master=claw,
                                command=tool2_Press,
                                text="button2",
                                width=100,
                                height=80,
                                fg_color="blue")


tool3 = customtkinter.CTkButton(master=claw,
                                command=tool3_Press,
                                text="button3",
                                width=100,
                                height=80,
                                fg_color="blue")

#intilizing elemnts
title_bar.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)
tool1.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)
tool2.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
tool3.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)




#idk what to call this just dont touch it
claw.mainloop()



















