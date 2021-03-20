# ==================================================================================
# File Name: demoTabGui.py
# ==================================================================================
# Purpose:         This file contains a demo (proposal) of how to place content 
#                  in a tab. As you can see, the idea is to create an object
#                  (instance) of a tab (ttk.Frame) and pass it to this class (through 
#                  the constructor) so this class (demoTabGuiClass) will use it as if 
#                  we were creating a new tkinter window: 
#
#                  self.window = window # self.window would be the new tkinter window
#                                       # window is the tab received as an argument
#
#                  So once we set the self.window instance to be the tab (ttk.Frame)
#                  we can add element to it as we do in a normal tkinter window (Tk())
#
# Author:          Jose Juan Jaramillo Polo
# Notes:             
# ==================================================================================

import platform                         #let the script identifies the current platform (OS)
from tkinter import *
#from tkinter.ttk import Progressbar     # allows to use progressbar
import tkinter as tk                    # needed to declare boolean and double vars por gui elements
import platform                         # let the script identifies the current platform (OS)

class demoTabGuiClass:
    def __init__ (self, window,log, utilities):
        # Global variables that are reachable by whoever needs it. 
        self.window = window
        self.log = log 
        self.utilities = utilities
                
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
        self.browse_btn = Button(self.settings_labelframe, text="...", command = lambda: self.utilities.browseFile(self.userComment_txt))
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
        self.log.info("(demoTabGuiClass::dummy) function")

    def startFunc(self):
        self.log.info("(demoTabGuiClass::startFunc) ---------------------------------->>> Start button clicked")