# ==================================================================================
# File Name: mainGui.py
# ==================================================================================
# Purpose:        * Here is the main assembling of the GUI. self.window = Tk() is 
#                   created here so this class does not receive a Tk() object
#                   because the main one is created from here.
#                 * Global elements such as: Tab, Menubar, Frames or any other 
#                   element that needs to be always available needs to be created here.
#                   In case you don't need special elements such as tabs just delete
#                   the menubar and tab demos and add whatever element you want
#                   in this file. 
#                 * This class receives as an argument: a logger object so if you 
#                   need to print something you should prefer:log.info(), log.debug, 
#                   and so on. (look at loggingWrepper.py). You should pass it as an
#                   argument to any other GUI object or class (like the self.demoTabGui)
#                   that migh need it.
#                 * It also includes a reference to a utilities object so ping, 
#                   browseFile, browseLocation and some others functionalities are
#                   always reachable throug this object. You should pass it as an
#                   argument to any other GUI object or class (like the self.demoTabGui)
#                   that migh need it.
#
#
# Author:           Jose Juan Jaramillo Polo
# Notes:             
# ==================================================================================
from tkinter import *
import tkinter as tk                    # Needed to use boolean and double vars for gui elements
from tkinter import ttk                 # To add tabs
from demoTabGui import demoTabGuiClass  # The content that the tab will contain in a class way.

#..............................................GUI CLASS
class mainGuiClass:
    def __init__ (self, log, utilities): 
        # Global variables that are reachable by whoever needs it. 
        self.log = log
        self.utilities = utilities

        #creating main frame:
        self.window = Tk()
        self.window.geometry('550x200') # width x height 
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