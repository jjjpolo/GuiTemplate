# ==================================================================================
# File Name: loggingWrapper.py
# ==================================================================================
# Purpose:         Provides common utilities for GUI such as:
#                        * browse a file
#                        * browse a location
#                        * ping a host, server, etc...
#
#
# Author:          Jose Juan Jaramillo Polo
# Notes:     
#                 * As a recomendation you should create an object in the main.py
#                   after creating a logging object so you can pass that logging
#                   instance to the constructor of this class (jpUtilitiesClass)
#                   and ensure that logging will work properly using the same 
#                   reference everywhere (see the __init__).
#
#                       utilities = jpUtilitiesClass(log)
#
#                 * In case you need to use browsing methods out of a TK() instance
#                   such as a window, a tab or a frame you should consider:
#                   1.- Call it after creating the TK() instance because I got an 
#                       error calling it before creating that TK() instnace.
#
#                           utilities = jpUtilitiesClass(log)
#                           myGui = mainGuiClass(log, utilities)
#                           print(utilities.browseLocation_GUI())  # Look at this!
#                           myGui.run()
#
#                   2.- If a TK() instance (window, tab, etc) is not needed then 
#                       just use it without taking care of something else. 
#
#                           utilities = jpUtilitiesClass(log)
#                           print(utilities.browseLocation_GUI())  # Look at this!
# ==================================================================================

import platform                         # let the script identifies the current platform (OS)
import os                               # for file management and os command execution 
import subprocess                       # run os commands in the background
from tkinter import filedialog          # for browsing files 

class jpUtilitiesClass:

    def __init__(self, log):
        self.log = log
    
    # add a comment to explain how to use the response_txt and event arguments
    def browseFile_GUI(self, response_txt=None, event=None ):
        filePath = filedialog.askopenfilename()
        if response_txt is not None:
            if filePath != '':
                response_txt.delete('0','end')
                response_txt.insert('0',str(filePath))
        self.log.info("(jpUtilitiesClass::browseFile_GUI) Selected file: " + filePath)
        return filePath
      
    # add a comment to explain how to use the response_txt and event arguments
    def browseLocation_GUI(self, response_txt=None, event=None ):
        folderPath = filedialog.askdirectory()
        if response_txt is not None:
            if folderPath != '':
                response_txt.delete('0','end')
                response_txt.insert('0',str(folderPath))
        self.log.info("(jpUtilitiesClass::browseLocation) Selected folder: " + folderPath)
        return folderPath
   
    #TODO add comment
    def osCommandExecute(self,command, runInBackgroung=False):
        if runInBackgroung:
            self.log.info("(demoTabGuiClass::osCommandExecute) [running in back ground] " + command)
            if platform.system() == "Linux":
                os.system(command + " &")
            else:
                subprocess.Popen(command) # run this command in the background
        else:
            self.log.info("(demoTabGuiClass::osCommandExecute) " + command)
            os.system(command)

    # TODO-rev add pinger method
    def ping(self,host):
        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', host]

        return subprocess.call(command) == 0