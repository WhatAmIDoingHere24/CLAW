"""
from time import strftime
from ciphey import decrypt
import ciphey
from ciphey.iface import Config
import customtkinter

# INFO:
    # This is a copy of the base64 stuff, with ciphey integrated into the label system
    # The input box does not reset until ciphey has calculated it's answer, idk how to fix it
    # Ciphey can take potentially forever, so make sure that your cipher text is solvable
    # Currently, only the first result ciphey returns is sent to the label, it's python api isn't as good as the cli app
    # The tool also doesn't output what cipher the text is decoded with
    # - Lucas

def cipheyDecryptManager():
    #Gets text from text entry and clears text entry, then runs ciphey on entry text
    def handleEntryEnter(event):
        str = entry.get()
        entry.delete(0, customtkinter.END)
        #Filters out any enters with no input in the text entry
        if len(str) > 0:
            resultLabel.configure(state= "normal")
            result = ciphey.decrypt(
                    Config().library_default().complete_config(),
                    str
                )
            print(result)
            if str in result:
                result = str(result)
            resultLabel.insert('end', result + "\n\n")
            resultLabel.configure(state= "disabled")

    #Sets default apperence to your systems default, and sets color theme to blue
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    #Initilizes the application screen
    toolWindow = customtkinter.CTk()
    toolWindow.title("Ciphey Decoder")
    toolWindow.geometry('300x300')
    toolWindow.resizable(False, False)


    #Initilizes text box
    entry = customtkinter.CTkEntry(toolWindow, placeholder_text= "Enter text to decode", placeholder_text_color= "grey", width=150,
    height=50, text_color="black", fg_color= "light grey", border_width= 0, corner_radius= 5)
    #Initilizes result label
    resultLabel = customtkinter.CTkTextbox(toolWindow, width=150, height=50)
    resultLabel.configure(state= "disabled")

    #Adds all widgets to screen
    resultLabel.pack(anchor= "nw", padx = 10, pady = 10, fill= customtkinter.BOTH, expand= True)
    entry.pack(anchor= "nw", padx = 10, pady = 10, fill= customtkinter.X, side= customtkinter.BOTTOM)

    #Handels enter button being pressed to submit entry text to conversion
    toolWindow.bind('<Return>', handleEntryEnter)
    entry.focus_force()
    toolWindow.mainloop()
"""
