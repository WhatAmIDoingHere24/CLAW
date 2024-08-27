#List of tools to be assinged to buttons
toolList = ["base64","base32","bash","md5"]

def command(commandName):
    match commandName:
        case "base64":
            print("this is base64")
        case "base32":
            print("this is base32")
        case "bash":
            print("this is bash")
        case "md5":
            print("this is md5")

