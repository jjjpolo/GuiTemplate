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
from mainGui import mainGuiClass


# ----------------------------------------------------------------------------------
# Name:            Main
# Purpose:         Starts the main function from the main file.
# Parameter:       None
def main():
    log = createLogger("testingApp", "test.log", logging.DEBUG)
    log.info("Hello logging world!")
    myGui = mainGuiClass(log)
    myGui.run()

main()