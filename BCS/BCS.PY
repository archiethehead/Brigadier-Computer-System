import time
import os
import random
import winsound
import keyboard
import sys
import sqlite3
import maskpass
import textwrap
import termtables as tt

class System():

    def __init__(self):
        self.filepath = os.getcwd()
        self.fullscreen = True
        self.driveOne = True
        self.logo = ["BBBBBBBBBBBBBBBBB           CCCCCCCCCCCCC   SSSSSSSSSSSSSSS ",
                    "B::::::::::::::::B       CCC::::::::::::C SS:::::::::::::::S",
                    "B::::::BBBBBB:::::B    CC:::::::::::::::CS:::::SSSSSS::::::S",
                    "BB:::::B     B:::::B  C:::::CCCCCCCC::::CS:::::S     SSSSSSS",
                    "  B::::B     B:::::B C:::::C       CCCCCCS:::::S            ",
                    "  B::::B     B:::::BC:::::C              S:::::S            ",
                    "  B::::BBBBBB:::::B C:::::C               S::::SSSS         ",
                    "  B:::::::::::::BB  C:::::C                SS::::::SSSSS    ",
                    "  B::::BBBBBB:::::B C:::::C                  SSS::::::::SS  ",
                    "  B::::B     B:::::BC:::::C                     SSSSSS::::S ",
                    "  B::::B     B:::::BC:::::C                          S:::::S",
                    "  B::::B     B:::::B C:::::C       CCCCCC            S:::::S",
                    "BB:::::BBBBBB::::::B  C:::::CCCCCCCC::::CSSSSSSS     S:::::S",
                    "B:::::::::::::::::B    CC:::::::::::::::CS::::::SSSSSS:::::S",
                    "B::::::::::::::::B       CCC::::::::::::CS:::::::::::::::SS ",
                    "BBBBBBBBBBBBBBBBB           CCCCCCCCCCCCC SSSSSSSSSSSSSSS   "]
        self.currentUser = ""
        self.currentPassword = ""

    def getFilepath(self):
        return self.filepath
    def getFullscreen(self):
        return self.fullscreen
    def getDriveOne(self):
        return self.driveOne
    def getSystemLogo(self):
        return self.logo
    def getCurrentUsername(self):
        return self.currentUser
    def getCurrentPassword(self):
        return self.currentPassword

    
    def setDriveOne(self, var):
        self.driveOne = var
    def setUsernamePassword(self, username, password):
        self.currentUser = username
        self.currentPassword = password

    def bootup(self):
        os.system('color 17')
        if system.getFullscreen():
            keyboard.press('f11')
        Database.checkDatabase()
        Main.POST()

class Database():
    def checkDatabase():
        global BCSDatabase
        global BCSDatabaseSQL
        BCSDatabaseExists = os.path.isfile("BCS.db")
        BCSDatabase = sqlite3.connect("BCS.db")
        BCSDatabaseSQL = BCSDatabase.cursor()
        if BCSDatabaseExists == False:
            Database.createDatabase()
    def createDatabase():
        BCSDatabaseSQL.execute(""" 
        CREATE TABLE userTable
        (
        username TEXT,
        userPassword TEXT
        )""")
        BCSDatabaseSQL.execute("""
        CREATE TABLE userLogTable
        (
        logNumber INTEGER,
        logName TEXT,
        logText TEXT,
        logCreator TEXT
        )""")
        BCSDatabaseSQL.execute("""
        CREATE TABLE codexTable
        (
        entryName TEXT,
        entryCatagory TEXT,
        entryInformation TEXT,
        entryText TEXT
        )""")
        BCSDatabaseSQL.execute("""
        CREATE TABLE catagoryTable
        (
        catagoryName TEXT,
        catagoryInformation TEXT
        )""")
        BCSDatabase.commit()

    def createUser(username, password):
        newData = [username, password]
        BCSDatabaseSQL.execute("""INSERT INTO userTable
                                Values(?,?)""",newData)
        BCSDatabase.commit()
    def deleteUser(username):
        BCSDatabaseSQL.execute("""DELETE FROM usertable WHERE """
         + "username" + "='" + username + "'")
        BCSDatabaseSQL.execute("""DELETE FROM userLogTable WHERE
                                logCreator = '""" + username + "'")
        BCSDatabase.commit()
    
    def createLog(logNumber, logName, logText, logCreator):
        newData = [logNumber, logName, logText, logCreator]
        BCSDatabaseSQL.execute("""INSERT INTO userLogTable
                                Values(?,?,?,?)""",newData)
        BCSDatabase.commit()
    def deleteLog(logNumber):
        BCSDatabaseSQL.execute("""DELETE FROM userLogTable
                                where logNumber = '""" + str(logNumber) + "'")
        BCSDatabase.commit()
    def updateLogNumber():
        logData = Database.getUserLogs()
        oldLogNumberList = []
        logNumberList = []
        for x in range(len(logData)):
            logNumberList.append(logData[x][0])
            oldLogNumberList.append(logData[x][0])
            if logNumberList[0] != 0:
                logNumberList[0] = 0
            if x > 0:
                if logNumberList[x] != (logNumberList[x - 1] + 1):
                    logNumberList[x] = (logNumberList[x - 1] + 1)
        for x in range(len(logNumberList)):
            BCSDatabaseSQL.execute("""UPDATE userLogTable SET
                                   logNumber = '""" + str(logNumberList[x]) + """
                                    ' WHERE logNumber = '""" + str(oldLogNumberList[x])
                                    + """' AND logCreator = '""" + system.getCurrentUsername() + "'")
            BCSDatabase.commit()
    def editLog(editedValue, newValue):
        BCSDatabaseSQL.execute("""UPDATE userLogTable SET '""" + editedValue + "' = '" + newValue + "'")
        BCSDatabase.commit()
    def getUserData():
        BCSDatabaseSQL.execute("SELECT * FROM userTable")
        userData = BCSDatabaseSQL.fetchall()
        return userData
    def getUserLogs():
        BCSDatabaseSQL.execute("""SELECT * FROM userLogTable 
                               WHERE logCreator ='""" + system.getCurrentUsername() + "'")
        logData = BCSDatabaseSQL.fetchall()
        return logData

    def getSpecificCatagoryData(catName):
        BCSDatabaseSQL.execute("""SELECT * FROM catagoryTable
                                WHERE catagoryName = '""" + catName + "'")
        catagoryData = BCSDatabaseSQL.fetchall()
        return catagoryData
    def getCatagoryData():
        BCSDatabaseSQL.execute("""SELECT * FROM catagoryTable""")
        catagoryData = BCSDatabaseSQL.fetchall()
        return catagoryData
    def getCodexData():
        BCSDatabaseSQL.execute("""SELECT * FROM codexTable""")
        codexData = BCSDatabaseSQL.fetchall()
        return codexData
    def createCodexEntry(newData):
        BCSDatabaseSQL.execute("""INSERT INTO codexTable
                               values(?,?,?,?)""",newData)
        BCSDatabase.commit()
    def createCatagory(newData):
        BCSDatabaseSQL.execute("""INSERT INTO catagoryTable Values(?,?)""",newData)
        BCSDatabase.commit()

class Functions():
    global printf
    global printfn
    global printfr
    global printfp
    global printft
    global userin
    global playAudio
    global beep
    global clearScreen
    global slashLoading
    global dotLoading
    global percentLoading
    global keyCreator
    global spaceGenerator
    global encrypt
    global decrypt

    def printf(text):
        print("    " + text)
        beep()
    
    def printfn(lines, text):
        gap = ""
        if lines > 1:
            for x in range(lines - 1):
                gap += "\n"
        print(gap)
        print("    " + text)
        beep()
    
    def printfr(text):
        print("\r", "   " + text, end = "")
    
    def printfp(paragraphLength, text):
        text = (textwrap.wrap(text, paragraphLength))
        for x in range(len(text)):
            printf(text[x])
    
    def printft(printedData, headers):
        table = tt.to_string(
            printedData,
            header= headers,
            style=tt.styles.ascii_thin_double,
            )
        print(textwrap.indent(table, "    "))
            
    def userin(text):
        userin = input("    " + text)
        return userin

    def playAudio(fileName):
        winsound.PlaySound(system.getFilepath() + 
        "\Assets\Sound\\" + fileName, winsound.SND_FILENAME)

    def beep():
        winsound.Beep(1200, 100)
        time.sleep(0.02)
    
    def clearScreen():
        os.system("cls")
    
    def dotLoading(text):
        for x in range(5):
            time.sleep(0.2)
            printfr(text + "      ")
            time.sleep(0.2)
            printfr(text + " .    ")
            time.sleep(0.2)
            printfr(text + " . .  ")
            time.sleep(0.2)
            printfr(text + " . . .")
        print("")
        time.sleep(0.2)
    
    def slashLoading(text):
        for x in range(5):
            time.sleep(0.2)
            printfr(text + " /")
            time.sleep(0.2)
            printfr(text + " —")
            time.sleep(0.2)
            printfr(text + " \\")
            time.sleep(0.2)
            printfr(text + " |")
        print("")
        time.sleep(0.2)
    
    def percentLoading(text):
        percent = 0
        for x in range(101):
            printfr(text + ": " + str(percent) + "%  ")
            percent += 1
            time.sleep(0.02)
        print("")
        time.sleep(0.2)
    
    def keyCreator(encryptOrDecrypt, plainText, currentKey):
        key = []
        if encryptOrDecrypt == False:
            hexCounter = 0
            for x in range(len(plainText)):
                if plainText[x] == "x":
                    hexCounter += 1
            length = hexCounter
        if encryptOrDecrypt == True:
            length = len(plainText)
        if length > len(currentKey):
            for x in range(length - len(currentKey)):
                currentKey += currentKey[x]
        for x in range(length):
            key.append(ord(currentKey[x]))
        return key

    def encrypt(plainText, username):
        key = keyCreator(True, plainText, username)
        encryptedString = ""
        for x in range(len(plainText)):
            encryptedString += (hex(ord(plainText[x]) * key[x]))
        return encryptedString

    def decrypt(encryptedString, username):
        key = keyCreator(False, encryptedString, username)
        decryptedString = ""
        encryptedList = encryptedString.split("0x")
        encryptedList.remove("")
        for x in range(len(encryptedList)):
            decryptedString += chr(int(int(encryptedList[x], 16) / int(key[x])))
        return decryptedString
            
class Main():

    def POST():
        clearScreen()
        from prompt_toolkit.shortcuts import message_dialog

        message_dialog(
        title='Example dialog window',
        text='Do you want to continue?\nPress ENTER to quit.').run()

        playAudio("bootup")
        time.sleep(0.2)
        printfn(1, "Brigadier Computer System BIOS v4.15PG, An Alliance Ally")
        printf("Copyright (C) SUY 2031-52, Brigadier Computer Systems, Inc.")
        printfn(1, "(55XWUQOE) BCS M170XL PCIset(TM)")
        printfn(1, "G5-BCS(A) CPU at 1200MHz")

        RAM = 640
        gap = "       "
        printfr("Memory Test :" + gap + str(RAM) + "K OK ")
        time.sleep(0.5)
        for x in range(2049):
            printfr("Memory Test :" + gap + str(RAM) + "K OK ")
            if RAM % 30 == 0:
                time.sleep(0.002)
            if RAM == 1000:
                gap = "      "
            RAM += 1
        time.sleep(0.5)

        printfn(2, "BCS Plug and Play BIOS Extension v1.0A")
        printf("Copyright (C) 2031, Brigadier Computer Software, Inc.")
        driveList = ["Primary Master    ", "Primary Slave     ",
                     "Secondary Master  ", "Secondary Slave   "]
        for x in range(4):
            mainText = "Detecting IDE " + driveList[x]
            endText = "PCemHD            "
            sys.stdout.write('\r      ' + mainText + " ... [Press F4 to skip]")
            for y in range(10):
                if keyboard.is_pressed('f4') or x == 2 or x == 3:
                    endText = "None              "
                    if x == 0:
                        system.setDriveOne(False)
                time.sleep(0.1)
            sys.stdout.write('\r      ' + mainText + " ... " + endText + "\n")
            if x == 0 and endText == "PCemHD            ":
                system.setDriveOne(True)
            beep()
        
        printfn(30, "Hold DEL to enter setup")
        for x in range(30):
            if keyboard.is_pressed('del'):
                Main.BIOS()
            time.sleep(0.1)
        Main.loadingBCS()

    def BIOS():
      clearScreen()
      os.system('color 17')
      time.sleep(3)
      printf("BIIIIIOOOOOOSSSS")
      time.sleep(3)
    
    def loadingBCS():
        clearScreen()
        print("\n")
        dotLoading("Searching for BCS Operating System")
        if system.getDriveOne() == False:
            printfn(1, "No bootables devices found")
            printf("Press F1 to retry boot")
            printf("Press F2 for setup")
            chosen = False
            while chosen == False:
                if keyboard.is_pressed('f1'):
                    Main.POST()
                if keyboard.is_pressed('f2'):
                    Main.BIOS()
        percentLoading("Loading BCS Operating System")
        time.sleep(1)
        Main.loginScreen()

    def BCSLogo():
        print("")
        os.system("cls")
        printfn(1, "")
        logo = system.getSystemLogo()
        for x in range(len(logo)):
            printf(logo[x])
        
    def loginScreen():
        print("")
        os.system("cls")
        loginScreenDone = False
        printfn(1, "User List")
        printf("---------")
        userData = Database.getUserData()
        for x in range(len(userData)):
            printf(userData[x][0])
        printfn(1, "Type /help for a list of commands")
        while loginScreenDone == False:
            menuInput = userin("")
            if menuInput == "/help":
                printfn(1, "NEW        Creates a new user")
                printf("DELETE     Deletes a user from the System")
                printf("SLEEP      Puts the System on a low power cycle")
                printf("RESTART    Restarts the System")
                printf("SHUTDOWN   Powers off the System\n")
                printfp(50, "To log into the System, enter the name of the user you wish to log as, and then enter the associated Password. While creating or deleting a user, simply type 'CANCLE' to exit the prompt.")
            if menuInput == "NEW":
                Main.newUser()
            if menuInput == "DELETE":
                Main.deleteUser()
            if menuInput == "SLEEP":
                powerOptions.sleep()
            if menuInput == "RESTART":
                powerOptions.restart()
            if menuInput == "SHUTDOWN":
                powerOptions.shutDown()
            else:
                loginSuccessful = Main.loginUser(menuInput)
                if loginSuccessful == True:
                    loginScreenDone = True
        Main.BCSLogo()
        playAudio("BCSIntro")
        printfn(1, "Welcome " + system.getCurrentUsername() + "!")
        Main.mainMenu()
      
    def newUser():
        username = userin("Enter the name of the new User: ")
        if username != 'CANCLE':
            passwordValid = True
            password = userin("Enter the Password of the new User: ")
            for x in range(len(password)):
                if password[x] == " ":
                    passwordValid = False
            if password != 'CANCLE' and passwordValid == True:
                Database.createUser(username, encrypt(password, username))
                clearScreen()
                Main.loginScreen()
            elif password != 'CANCLE' and passwordValid == False:
                printf("Invalid Password inputted.\n")
    
    def deleteUser():
        userSelected = False
        while userSelected == False:
            username = userin("Enter the name of the user you wish to delete: ")
            userData = Database.getUserData()
            if username == "CANCLE":
                break
            for x in range(len(userData)):
                if username == userData[x][0]:
                    incrament = x
                    userSelected = True
        if userSelected == True and username != 'CANCLE':
            passwordSelected = False
            while passwordSelected == False:
                password = userin("Enter the password of the user you wish to delete: ")
                if password == 'CANCLE':
                    break
                if encrypt(password, username) == userData[incrament][1]:
                    Database.deleteUser(username)
                    passwordSelected = True
        clearScreen()
        Main.loginScreen()

    def loginUser(menuInput):
        userData = Database.getUserData()
        for x in range(len(userData)):
            if menuInput == userData[x][0]:
                password = userData[x][1]
                inputPassword = maskpass.askpass(prompt="    Enter the Password of the chosen user: ", mask="*")
                if encrypt(inputPassword, menuInput) == password:
                    system.setUsernamePassword(menuInput, password)
                    printfn(1, "Correct Password inputted")
                    dotLoading("Loading into BCS as " + system.getCurrentUsername())
                    loginSuccessful = True
                    return loginSuccessful
                elif inputPassword == 'CANCLE':
                    pass
                else:
                    printf("Incorrect Password inputted")

        if menuInput == "ADMIN":
            password = "ADMIN"
            system.setUsernamePassword(menuInput, password)
            printfn(1, "Logging as Administrator")
            dotLoading("Loading into BCS")
            loginSuccessful = True
            return loginSuccessful

    def mainMenu():
        mainMenuDone = False
        printfn(1, "1: User Logs")
        printf("2: Codex")
        printf("3: Ship info")
        printf("4: Systsem Settings")
        printf("5: Remail")
        printf("6: Power Options")
        printf("----------------")
        while mainMenuDone == False:
            userChoice = userin("Enter your choice here: ")
            if userChoice == "1":
                clearScreen()
                userLogs.printUserLogs()
            if userChoice == "2":
                clearScreen()
                codex.loadingCodex()
            if userChoice == "6":
                clearScreen()
                powerOptions.printPowerOptions()
            
class userLogs():
    def printUserLogs():
        printfn(2, "")
        logData = Database.getUserLogs()
        userLogDone = False
        printedLogData = []
        for x in range(len(logData)):
            printedLogData.append([str(logData[x][0]), logData[x][1], logData[x][3]])
        try:
            printft(printedLogData, ["Log-Number", "Log-Name", "Log-Creator"])
        except:
            printf("No log data available! Enter 'NEW' to change that.")
        printfn(1, "Type /help for a list of commands")
        while userLogDone == False:
            logChoice = userin("")
            if logChoice == "NEW":
                userLogs.createLog()
            if logChoice == "DELETE":
                userLogs.deleteLog()
            if logChoice == "EDIT":
                userLogs.editLogData()
            if logChoice == "MENU":
                userLogDone = True
            if logChoice == "/help":
                printfn(1, "NEW        Create a new log under your name.")
                printf("DELETE     Delete a log attributed to your account.")
                printf("EDIT       Edit the details of a log on the record.")
                printf("MENU       Return to the BCS main menu.\n")
                printfp(50, "Enter the log number of the log you wish to view, and the content within will be printed on screen.")
            else:
                for x in range(len(logData)):
                    if logChoice == str(logData[x][0]):
                        userLogs.printLogData(logChoice)
        clearScreen()
        Main.BCSLogo()
        Main.mainMenu()
    
    def createLog():
        logData = Database.getUserLogs()
        clearScreen()
        print("\n")
        newLogName = userin("Enter the name of the log here: ")
        if newLogName != "CANCLE":
            newLogTextDone = False
            newLogText = ""
            printf("Press ENTER to move the text to a new line, and enter FIN on a new line when the log is complete.")
            newText = userin("Enter text here: ")
            while newText != "FIN":
                if newText != "FIN":
                    newLogText += newText + " "
                newText = userin("")
            if newLogText != "CANCLE":
                Database.createLog(len(logData), newLogName, newLogText, system.getCurrentUsername())
        userLogs.printUserLogs()
    
    def deleteLog():
        logValid = False
        logData = Database.getUserLogs()
        logNumber = userin("Enter the number of the log you would like to delete: ")
        for x in range(len(logData)):
            if logData[x][0] == int(logNumber):
                logValid = True
        if logValid == True:
            Database.deleteLog(logNumber)
            Database.updateLogNumber()
            clearScreen()
            userLogs.printUserLogs()
        if logNumber != "CANCLE":
            printf("Invalid log number entered.")
    
    def printLogData(logNumber):
        logData = Database.getUserLogs()
        print("")
        printfp(50, logData[int(logNumber)][2])

    def editLogData():
        logData = Database.getUserLogs()
        logFound = False
        logNumber = userin("Enter the Log Number here: ")
        for x in range(len(logData)):
            if str(logData[x][0]) == logNumber:
                logFound = True
        if logFound == True:
            nameOrText = userin("Enter TEXT to edit the content of the log, and NAME to change it's name: ")
            if nameOrText == "TEXT" or nameOrText == "NAME":
                newValue = userin("Enter the new " + nameOrText.lower() + " for log " + str(logNumber) + ": ")
                if nameOrText == "TEXT":
                    nameOrText = "logText"
                if nameOrText == "NAME":
                    nameOrText = "logName"
                Database.editLog(nameOrText, newValue)
            if nameOrText != "logName" and nameOrText != "logText" and nameOrText != "CACNLE":
                printf("Invalid data type entered.\n")
        if logFound != True and logNumber != "CANCLE":
            printf("Invalid log number entered.\n")
        clearScreen()
        userLogs.printUserLogs()

class codex():
    def loadingCodex():
        print("\n")
        slashLoading("Checking Relnet for Codex Data")
        percentLoading("Downloading Codex Data")
        clearScreen()
        codex.printCodexCatagories()

    def printCodexCatagories():
        codexDone = False
        printfn(2, "###-CODEX-###\n")
        catagoryData = Database.getCatagoryData()
        codexCatagories = []
        for x in range(len(catagoryData)):
            codexCatagories.append([x + 1, catagoryData[x][0]])
        for x in range(len(codexCatagories)):
            printf(str(codexCatagories[x][0]) + ": " + codexCatagories[x][1])
        print("")
        printf("Type HELP for a list of commands")
        while codexDone == False:
            codexChoice = userin("")
            if system.getCurrentUsername() == "ADMIN":
                if codexChoice == "NEW":
                    clearScreen()
                    codex.addCodex()
                if codexChoice == "NEWCAT":
                    clearScreen()
                    codex.newCatagory()
            if codexChoice == "HELP":
                printfp(50, "Enter the number of the Catagory of the Codex you would like to view. When done, enter 'MENU' to return to the BCS menu.")
            if codexChoice == "MENU":
                codexDone = True
            for x in range(len(codexCatagories)):
                if str(codexCatagories[x][0]) == codexChoice:
                    codex.printCatagoryEntries(codexCatagories[x][1])
        clearScreen()
        Main.BCSLogo()
        Main.mainMenu()

    def addCodex():
        newName = userin("Enter the name of the new entry here: ")
        newCatagory = userin("Enter the entries catagory here: ")
        newInformation = userin("Enter the information here (type FIN when done): ")
        newInformationString = ""
        while newInformation != "FIN":
            if newInformation != "FIN":
                newInformationString += newInformation + "/"
            newInformation = userin("")
        newText = userin("Enter the text of the entry here: ")
        newData = [newName, newCatagory, newInformationString, newText]
        Database.createCodexEntry(newData)
        clearScreen()
        codex.printCodexCatagories()
    
    def newCatagory():
        newName = userin("Enter the name of the new entry here: ")
        newInformationString = ""
        newInformation = userin("Enter the infromation of the catagory here:\n ")
        while newInformation != "FIN":
            if newInformation != "FIN":
                newInformationString += newInformation + "/"
            newInformation = userin("")
        newData = [newName, newInformationString]
        Database.createCatagory(newData)
        clearScreen()
        codex.printCodexCatagories()
    
    def printCatagoryEntries(catagoryName):
        catagoryDone = False
        clearScreen()
        printfn(2,"")
        codexData = Database.getCodexData()
        catagoryData = Database.getCatagoryData()
        catagoryInformation = []
        for x in range(len(catagoryData)):
            if catagoryData[x][0] == catagoryName:
                catagoryInformation = codex.decodeCatagoryData(catagoryData[x][1])
        codexEntries = []
        entryInformation = []
        for x in range(len(codexData)):
            if codexData[x][1] == catagoryName:
               codexEntries.append(codexData[x])
        printedCodexData = []
        for x in range(len(codexEntries)):
            newData = []
            newData.append(codexEntries[x][0])
            newInformation = codex.decodeCatagoryData(codexEntries[x][2])
            for y in range(len(newInformation)):
                newData.append(newInformation[y])
            printedCodexData.append(newData)
        catagoryInformation.insert(0, "Name")
        printft(printedCodexData, catagoryInformation)

        printf("Type HELP for a list of commands")
        while catagoryDone == False:
            catagoryDecision = userin("")
            if catagoryDecision == "MENU":
                catagoryDone = True
                clearScreen()
                codex.printCodexCatagories()
            if catagoryDecision == "HELP":
                printfp(50, "Enter the name of the " + catagoryName + " you'd like to learn more about, or type 'MENU' to reutrn to the Codex menu.")
            else:
                for x in range(len(codexData)):
                    if catagoryDecision == codexData[x][0]:
                        codex.printCodexData(codexData[x][3])

    def printCodexData(codexText):
        printfp(50, codexText)

    def decodeCatagoryData(data):
        data = data.split("/")
        return data

class shipInfo():
    def temp():
        print("")

class systemSettings():
    def temp():
        print("")

class Remail():
    def temp():
        print("PLACEHOLDER")

class powerOptions():

    def printPowerOptions():
        printfn(2, "1: Sleep")
        printf("2: Shut Down")
        printf("3: Restart")
        printf("4: Sign Out")
        printf("5: Main Menu")
        printf("------------")

        powerOptionsDone = False
        while powerOptionsDone == False:
            powerOption = userin("Enter your choice here: ")
            if powerOption == "1":
                powerOptions.sleep()
                Main.BCSLogo()
                printfn(1, "Rise and shine " + system.getCurrentUsername() + "!\n")
                powerOptionsDone = True
            if powerOption == "2":
                powerOptions.shutDown()
            if powerOption == "3":
                powerOptions.restart()
            if powerOption == "4":
                powerOptions.signOut()
            if powerOption == "5":
                powerOptionsDone = True
        clearScreen()
        Main.BCSLogo()           
        Main.mainMenu()
    
    def sleep():
        clearScreen()
        sleepDone = False
        counter = 0
        sleepList = ["            ", ".           ", ". .         ", ". . .       "
        ,". . . Z    ", ". . . Z Z  ", ". . . Z Z Z"]

        printfn(2, "Sleeping (Press ESC to wake up) . . .")
        while sleepDone == False:
            printfr("(U.U) " + sleepList[counter])
            sleepDone = powerOptions.cancleSleep(sleepDone)
            counter += 1
            if counter == 7:
                counter = 0
        clearScreen()
        
    def cancleSleep(sleepDone):
        for x in range(5):
            if keyboard.is_pressed("esc"):
                sleepDone = True
            else:
                time.sleep(0.2)
            return sleepDone
    
    def shutDown():
        clearScreen()
        print("\n")
        slashLoading("Saving user data")
        print("")
        slashLoading("Shutting down")
        print("")
        clearScreen()
        printfn(20, "\t\t\t\t\t\t\t\t\t    Bye!")
        time.sleep(0.5)
        winsound.Beep(975, 350)
        winsound.Beep(850, 350)
        time.sleep(1.5)
        BCSDatabase.close()
        os._exit(0)
    
    def restart():
        clearScreen()
        print("\n")
        slashLoading("Saving user data")
        print("")
        slashLoading("Restarting BCS")
        print("")
        clearScreen()
        time.sleep(2)
        Main.POST()
    
    def signOut():
        clearScreen()
        print("\n")
        slashLoading("Saving user data")
        print("")
        slashLoading("Signing out of BCS")
        printfn(1,"Bye " + system.getCurrentUsername() + "!")
        time.sleep(2)
        Main.loginScreen()

system = System()
system.__init__()
system.bootup()