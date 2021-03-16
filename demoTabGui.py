import platform                         #let the script identifies the current platform (OS)
from tkinter import *
import datetime                         # for get current date time
from tkinter.ttk import Progressbar     # allows to use progressbar
import tkinter as tk                    # needed to declare boolean and double vars por gui elements
import platform                         #let the script identifies the current platform (OS)
import os                               # for file management and os command execution
import subprocess                       # run os commands in the background
from tkinter import filedialog          # for browsing files

class demoTabGuiClass:
    def __init__ (self, window,log):
        self.window = window
        self.log = log 
        #TODO add the name of the function to all the selg.log calls eg. (demoTabGui::example)
        
        # variables to set the position in this window
        currentRow = 0
        currentColumn = 0
                
        # TODO 1 move the content of frame to a new class file so I can create the frame as an object 
        # self.settings_labelframe and then pass it as an argument to the constructor of the frame 
        # class as I did with the tab element
        self.settings_labelframe = LabelFrame(self.window, text = "Group",width=100,height=100)
        self.settings_labelframe.grid(row=currentRow, column=currentColumn, columnspan = 2, padx=10,pady=3, ipadx=3)
        #*****************************************************FRAME SEPARATOR
        # variables to set the position in this widow(frame)
        currentRow_frame= 0
        currentColumn_frame = 0
        #----------------------------------------row separator
        currentRow_frame = currentRow_frame + 1
        currentColumn_frame = 0
        self.userComment_lbl = Label(self.settings_labelframe, text="Name folder comment: ", font=("Arial Bold", 10))
        self.userComment_lbl.grid (column = currentColumn_frame, row = currentRow_frame)
        #||||||||||||||||||||column separator
        currentColumn_frame = currentColumn_frame + 1
        self.userComment_txt = Entry(self.settings_labelframe,width=50, justify = CENTER)
        self.userComment_txt.delete(0,END)
        self.userComment_txt.insert(0,"")
        self.userComment_txt.grid(column = currentColumn_frame, row = currentRow_frame)
         #||||||||||||||||||||column separator
        currentColumn_frame = currentColumn_frame + 1
        self.browse_btn = Button(self.settings_labelframe, text="...", command = lambda: self.browseFile(self.userComment_txt))
        self.browse_btn.grid(column=currentColumn_frame, row=currentRow_frame, pady= 10)
        #TODO add a checkBox element her to demonstrate how to use it with boolean variables.
        #*****************************************************FRAME SEPARATOR - END

        #----------------------------------------row separator
        currentRow = currentRow + 1
        currentColumn = 0
        self.start_btn = Button(self.window, text="Show MSGBox", command = self.startFunc)
        self.start_btn.grid(column=currentColumn, row=currentRow, pady= 10)
        #||||||||||||||||||||column separator
        currentColumn =currentColumn+1
        self.reset_btn = Button(self.window, text="Exit", command = self.dummyFunction)
        self.reset_btn.grid(column=currentColumn, row=currentRow, pady= 10)

    def dummyFunction(self):
        self.log.info("(demoTabGui::dummy) function")

    #TODO move to a new utilities class since I always need this everywhere
    def browseFile(self, response_txt, event=None ):
        filePath = filedialog.askopenfilename()
        if filePath != '':
            response_txt.delete('0','end')
            response_txt.insert('0',str(filePath))
        self.log.info("(browseFile) Selected file: " + filePath)

    #TODO move to a new utilities class since I always need this everywhere
    def browseLocation(self, response_txt, event=None ):
        folderPath = filedialog.askdirectory()
        if folderPath != '':
            response_txt.delete('0','end')
            response_txt.insert('0',str(folderPath))
        self.log.info("(browseFile) Selected folder: " + folderPath)
   
    #TODO move to a new utilities class since I always need this everywhere
    def osCommandExecute(self,command, runInBackgroung=False):
        self.log.info("(osCommandExecute) " + command)
        # os.system(command)
        if runInBackgroung:
            if platform.system() == "Linux":
                os.system(command + " &")
            else:
                subprocess.Popen(command) # run this command in the background
        else:
            os.system(command)

    #TODO move to a new utilities class since I always need this everywhere
    def startFunc(self):
        self.log.info("(startFunc) ---------------------------------->>> Start button clicked")