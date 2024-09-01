import customtkinter
import base64
from functools import partial

def encodeBase64():

    #Does the decoding
    def convert2base64(str):
        try:
            newStr = str.encode('utf-8') #converts string to bytes
            newStr = base64.b64encode(newStr)
            newStr = newStr.decode('utf-8')
            return newStr
        #convert2base64 = partial(convert2base64,entry.get())
        except Exception as e:
            print("Invalid entry, enter ASCII")


    #Gets text from text entry and clears text entry, then runs decoder on entry text
    def handleEntryEnter(event):
        str = entry.get()
        entry.delete(0, customtkinter.END)
        #Filters out any enters with no input in the text entry
        if len(str) > 0:
            resultLabel.configure(state= "normal")
            resultLabel.insert('end', (str + (" --> " + convert2base64(str)))  + "\n\n")
            resultLabel.configure(state= "disabled")


    #Sets default apperence to your systems default, and sets color theme to blue
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    #Initilizes the application screen 
    toolWindow = customtkinter.CTk()
    toolWindow.title("encodeBase64")
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


    #Handels enter button being pressed to submit entry text to conversion
    #toolWindow.bind('<Return>', lambda event: convert2base64(event, entry.get()))
    toolWindow.bind('<Return>', handleEntryEnter)
    entry.focus_force()
    toolWindow.mainloop()


def decodeBase64():

    #does the actual encoding
    def convert2Ascii(str):
        try:
            newStr = str.encode('utf-8') #converts string to bytes
            newStr = base64.b64decode(newStr)
            newStr = newStr.decode('utf-8')
            return newStr
        #convert2base64 = partial(convert2base64,entry.get())
        except Exception as e:
            print("Invalid entry, enter base64")


    #Gets text from text entry and clears text entry, then runs decoder on entry text
    def handleEntryEnter(event):
        str = entry.get()
        entry.delete(0, customtkinter.END)
        #Filters out any enters with no input in the text entry
        if len(str) > 0:
            resultLabel.configure(state= "normal")
            resultLabel.insert('end', (str + (" --> " + convert2Ascii(str)))  + "\n\n")
            resultLabel.configure(state= "disabled")


    #Sets default apperence to your systems default, and sets color theme to blue
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    #Initilizes the application screen 
    toolWindow = customtkinter.CTk()
    toolWindow.title("decodeBase64")
    toolWindow.geometry('300x300')
    toolWindow.resizable(False, False)


    #initilizes text box
    entry = customtkinter.CTkEntry(toolWindow, placeholder_text= "Enter text", placeholder_text_color= "grey", width=150, 
                                   height=50, text_color="black", fg_color="light grey", border_width= 0, corner_radius= 5)
    #initilizes result Label
    resultLabel = customtkinter.CTkTextbox(toolWindow, width=150, height=50, text_color="black" )
    resultLabel.configure(state= "disabled")

    #Adds all widgets to screen
    resultLabel.pack(anchor= "nw", padx = 10, pady = 10, fill= customtkinter.BOTH, expand= True)
    entry.pack(anchor= "nw", padx = 10, pady = 10, fill= customtkinter.X, side= customtkinter.BOTTOM)
    
    
    #Handels enter button being pressed to submit entry text to conversion
    #toolWindow.bind('<Return>', lambda event: convert2Ascii(event, entry.get()))
    toolWindow.bind('<Return>', handleEntryEnter)
    toolWindow.mainloop()

def encodeBase32():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    toolWindow = customtkinter.CTk()
    toolWindow.title("encodeBase64")
    toolWindow.geometry('300x300')


    #initilizes / creates text box
    entry = customtkinter.CTkEntry(master=toolWindow,
                                    width=150,
                                    height=50,
                                    text_color="black",
                                    fg_color="gray"
                                    )
    entry.place(relx=0.5,rely=0.5,anchor='center')

    resultLabel = customtkinter.CTkTextbox(master=toolWindow,
                                    width=150,
                                    height=50,
                                    text_color="black",
                                    fg_color="gray"
                                    )
    resultLabel.place(relx=0.5,rely=0.7,anchor='center')
    #does the actual encoding
    def convert2base32(str):
        newStr = str.encode('utf-8') #converts string to bytes
        newStr = base64.b32encode(newStr)
        newStr = newStr.decode('utf-8')
        resultLabel.delete(0.0,'end')
        resultLabel.insert('end', newStr)
    #convert2base64 = partial(convert2base64,entry.get())

    #initilizes / creates enter button
    enterButton = customtkinter.CTkButton(master=toolWindow,
                                    text="Enter",
                                    width=50,
                                    height=50,
                                    text_color="black",
                                    fg_color="blue",
                                    command=lambda: convert2base32(entry.get())
                                    )
    enterButton.place(relx=0.7,rely=0.5,anchor='center')
    toolWindow.mainloop()

def decodeBase32():

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    toolWindow = customtkinter.CTk()
    toolWindow.title("decodeBase64")
    toolWindow.geometry('300x300')

    #initilizes / creates text box
    entry = customtkinter.CTkEntry(master=toolWindow,
                                    width=150,
                                    height=50,
                                    text_color="black",
                                    fg_color="gray"
                                    )
    entry.place(relx=0.5,rely=0.5,anchor='center')

    resultLabel = customtkinter.CTkTextbox(master=toolWindow,
                                    width=150,
                                    height=50,
                                    text_color="black",
                                    fg_color="gray"
                                    )
    resultLabel.place(relx=0.5,rely=0.7,anchor='center')
    #does the actual encoding
    def convert2Ascii(str):
        newStr = str.encode('utf-8') #converts string to bytes
        newStr = base64.b32decode(newStr)
        newStr = newStr.decode('utf-8')
        resultLabel.delete(0.0,'end')
        resultLabel.insert('end', newStr)
    #convert2base64 = partial(convert2base64,entry.get())

    #initilizes / creates enter button
    enterButton = customtkinter.CTkButton(master=toolWindow,
                                    text="Enter",
                                    width=50,
                                    height=50,
                                    text_color="black",
                                    fg_color="blue",
                                    command=lambda: convert2Ascii(entry.get())
                                    )
    enterButton.place(relx=0.7,rely=0.5,anchor='center')
    toolWindow.mainloop()