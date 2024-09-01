from scriptRunner import deleteUsers, addUsers

winScriptList = ["deleteUsers", "addUsers"]

def script(commandName):
    match commandName:
        case "deleteUsers":
            print("tried 1")
            deleteUsers()
        case "addUsers":
            print("tried 2")
            addUsers()