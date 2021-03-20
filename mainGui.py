#TODO add header
import platform                         #let the script identifies the current platform (OS)
import os                               # for file management and os command execution
import subprocess                       # To run os commands in the background
import datetime                         # To get current date time
from tkinter import *
from tkinter.ttk import Progressbar     # To use progressbar
import tkinter as tk                    # Needed to use boolean and double vars for gui elements
from tkinter import ttk                 # for adding tabs

from demoTabGui import demoTabGuiClass

#..............................................GUI CLASS
class mainGuiClass:
    def __init__ (self, log, utilities): 
        # Global variables that are reachable by whoever needs it. 
        self.log = log
        self.utilities = utilities

        #creating main frame:
        self.window = Tk()
        self.window.geometry('500x200') # x y 
        self.window.title("Gui Template")

        #menubar
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)
        self.tools = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Tools', menu=self.tools)
        self.tools.add_command(label='Delete known_hosts file', command=self.launchDeleteKnownHosts)

        # Tab elements
        self.tabControl = ttk.Notebook(self.window) 
        self.tab1 = ttk.Frame(self.tabControl)          
        self.tabControl.add(self.tab1, text ='Demo Tab1')         
        self.tabControl.pack(expand = 1, fill ="both") 

        # Creating a new GUI where self.tab1 will be the self.window container similar to mainGui.py::self.window=TK()
        self.demoTabGui = demoTabGuiClass(self.tab1, self.log, self.utilities)
        
    # This method is only needed here because constructor will buil (add) all the neede GUI elements
    def run(self):
        self.window.mainloop()        

    # TODO change this function to something else more useful
    def launchDeleteKnownHosts(self):
        self.log.info('(mainGuiClass::launchDeleteKnownhosts) Launching delete known_hosts file view')

    def __del__(self):
        self.log.info("(mainGuiClass::__del__ )Closing GUI - BYE BYE")