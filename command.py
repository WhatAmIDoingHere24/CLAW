from crypto import encodeBase64,decodeBase64,encodeBase32,decodeBase32

#List of tools to be assinged to buttons
toolList = ["encodeBase64","decodeBase64","encodeBase32","decodeBase32","Shift Cipher","Script1","Script2","Script 3"]

def command(commandName):
    match commandName:
        case "encodeBase64":
            print("this is base64")
            encodeBase64()
        case "decodeBase64":
            decodeBase64()
        case "encodeBase32":
            encodeBase32()
        case "decodeBase32":
            decodeBase32()

