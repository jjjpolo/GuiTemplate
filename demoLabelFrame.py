# ==================================================================================
# File Name: demoLableFrame.py
# ==================================================================================
# Purpose:          Following the porposed model of mine, this class provides a demo
#                   of how to add content to a label frame (known as group box in 
#                   some other languages). 
#                   The idea is to receives the label frame reference as an argument
#                   so that this class will use it as if we were creating a new:
#                   
#                   self.window = Tk()  #Tk() will by replaced by the labelFrame
#
# Author:          Jose Juan Jaramillo Polo
# Notes:             
# ==================================================================================
from tkinter import *

class demoLableFrameClass:

    def __init__ (self, window, log, utilities):
        # Global variables that are reachable by whoever needs it. 
        self.window = window
        self.log = log 
        self.utilities = utilities
        
        # variables to set the position in this widow(frame)
        currentRow= 0
        currentColumn = 0
        
        #----------------------------------------row separator
        currentRow = currentRow + 1
        currentColumn = 0
        self.userComment_lbl = Label(self.window, text="Name folder comment: ", font=("Arial Bold", 10))
        self.userComment_lbl.grid (column = currentColumn, row = currentRow)
        #||||||||||||||||||||column separator
        currentColumn = currentColumn + 1
        self.userComment_txt = Entry(self.window,width=50, justify = CENTER)
        self.userComment_txt.delete(0,END)
        self.userComment_txt.insert(0,"")
        self.userComment_txt.grid(column = currentColumn, row = currentRow)
         #||||||||||||||||||||column separator
        currentColumn = currentColumn + 1
        self.browse_btn = Button(self.window, text="...", command = lambda: self.utilities.browseFile(self.userComment_txt))
        self.browse_btn.grid(column=currentColumn, row=currentRow, pady= 10)
        #----------------------------------------row separator
        currentRow = currentRow + 1
        currentColumn = 0
        self.chk_state = BooleanVar()
        self.chk_state.set(False) #set check state
        self.chk = Checkbutton(self.window, text='Demo CheckBox', var=self.chk_state)
        self.chk.grid(column=currentColumn, row=currentRow)

    def __del__(self):
        self.log.debug("(demoLabelFrameClass::__del__) Destroying window")