import subprocess
import os

present_working_directory = os.getcwd()

winScriptList = ["users", "testing_1", "testing_2", "testing_3", "testing_4"]

def script(commandName):
    match commandName:
        case "users":
            print("tried 1")
            deleteUsers()
        case "testing_1":
            print("tried 2")
        case "testing_2":
            print("tried 3")
        case "testing_3":
            print("tried 4")
        case "testing_4":
            print("tried 5")

def deleteUsers():
    path = os.path.realpath("deleteUsers.ps1")
    print(path)
    print(os.getlogin())
    runDeleteUserScript = ["PowerShell", "-ExecutionPolicy", "Unrestricted", "-File", path, "-Users", "Testing", "Testing2", "Testing3"]  
    subprocess.call(runDeleteUserScript)
