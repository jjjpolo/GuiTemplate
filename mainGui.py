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
    def __init__ (self, log):
        self.log = log
        #creating main frame:
        self.window = Tk()
        self.window.geometry('500x200') # x y 
        self.window.title("Gui Template")

        #menubar
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        tools = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Tools', menu=tools)
        tools.add_command(label='Delete known_hosts file', command=self.launchDeleteKnownHosts)

        self.tabControl = ttk.Notebook(self.window) 
        
        self.tab1 = ttk.Frame(self.tabControl)
          
        self.tabControl.add(self.tab1, text ='Demo Tab1') 
        
        self.tabControl.pack(expand = 1, fill ="both") 

        self.myLogsGui = demoTabGuiClass(self.tab1, log)
        
    
    def run(self):
        self.window.mainloop()        

    # TODO change this function to something else more useful
    def launchDeleteKnownHosts(self):
        self.log.info('(mainGuiClass::launchDeleteKnownhosts) Launching delete known_hosts file view')

    def __del__(self):
        self.log.info("(mainGuiClass::__del__ )Closing GUI - BYE BYE")