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

from tkinter import *
import tkinter as tk                    # needed to declare boolean and double vars por gui elements
from tkinter import messagebox
from demoLabelFrame import demoLableFrameClass

class demoTabGuiClass:
    def __init__ (self, window,log, utilities):
        # Global variables that are reachable by whoever needs it. 
        self.window = window
        self.log = log 
        self.utilities = utilities
                
        # variables to set the position in this window
        currentRow = 0
        currentColumn = 0

        #----------------------------------------row separator                
        # Inserting a Label Frame GUI in this window.
        self.settings_labelframe = LabelFrame(self.window, text = "LabelFrame - Group",width=100,height=100)
        self.settings_labelframe.grid(row=currentRow, column=currentColumn, columnspan = 2, padx=10,pady=3, ipadx=3)
        # Inserting content to LabelFrame by passing it as a reference to be the self.window in demoLableFrameClass (POO)
        self.demoUsingLabelFrame = demoLableFrameClass(self.settings_labelframe, self.log, self.utilities) 

        #----------------------------------------row separator
        currentRow = currentRow + 1
        currentColumn = 0
        self.start_btn = Button(self.window, text="Show MSGBox", command = self.startFunc)
        self.start_btn.grid(column=currentColumn, row=currentRow, pady= 10)
        #||||||||||||||||||||column separator
        currentColumn =currentColumn+1
        self.reset_btn = Button(self.window, text="Dummy", command = self.dummyFunction)
        self.reset_btn.grid(column=currentColumn, row=currentRow, pady= 10)

    def dummyFunction(self):
        self.log.info("(demoTabGuiClass::dummyFunction) Dummy function")

    def startFunc(self):
        self.log.info("(demoTabGuiClass::startFunc) ---------------------------------->>> Start button clicked")
        msg = "State of checkbox is: " + str(self.demoUsingLabelFrame.chk_state.get()) + '\n Selected file: ' + self.demoUsingLabelFrame.demo_txt.get()
        messagebox.showinfo(message=msg, title="Demo MsgBox")

    def __del__(self):
        self.log.debug("(demoTabGuiClass::__del__) Destroying window")