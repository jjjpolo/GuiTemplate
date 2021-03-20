# ==================================================================================
# File Name: main.py
# ==================================================================================
# Purpose:         Prepares almost all the basics to start creating a GUI such as:
#                      * Logging
#                      * Config parser (to save and load data in .ini files)
#                      * Basic Tkinter GUI
#                      * Pinger (to test connection with a host, server, etc...)
#
#
# Author:          Jose Juan Jaramillo Polo
# Notes:             
# ==================================================================================

from loggingWrapper import createLogger, logging    #importing only the function to instantiate a logger
                                                    # and the logging class to set the logging level.
from jpUtilities import jpUtilitiesClass
from mainGui import mainGuiClass

# ----------------------------------------------------------------------------------
# Name:            Main
# Purpose:         Starts the main function from the main file.
# Parameter:       None
def main():
    #Creating a log object that we can use everywhere passing it as reference
    log = createLogger("testingApp", "test.log", logging.DEBUG)
    log.info("Hello logging world!")
    
    #Creating a utilities object that we can use everywhere passing it as reference
    utilities = jpUtilitiesClass(log)
    log.info("Ping to www.google.com: " + str(utilities.ping("www.google.com")))
    
    myGui = mainGuiClass(log, utilities)
    #log.info(utilities.browseLocation_GUI())  # In case you need to use utilities having a TK() instance
                                            # use it after creating the main GUI
    myGui.run()

main()