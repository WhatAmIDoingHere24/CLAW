import customtkinter
import base64
from functools import partial
def encodeBase64():
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
    def convert2base64(str):
        newStr = str.encode('utf-8') #converts string to bytes
        newStr = base64.b64encode(newStr)
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
                                    command=lambda: convert2base64(entry.get())
                                    )
    enterButton.place(relx=0.7,rely=0.5,anchor='center')
    toolWindow.mainloop()


def decodeBase64():
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
        newStr = base64.b64decode(newStr)
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