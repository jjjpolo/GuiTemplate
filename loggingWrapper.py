# ==================================================================================
# File Name: loggingWrapper.py
# ==================================================================================
# Purpose:         This is a wrapper (just a function) that creates and returns a 
#                  logging object and configures it in a easier way by receiving 
#                  some parameters.
#
# Author:          Jose Juan Jaramillo Polo
# Notes:             
# ==================================================================================

from logging.handlers import RotatingFileHandler #for better file logs management| RotatingFileHandler instead of FileHandler
import logging, os # os is needed to check if a log files was already creted before

logger = logging.getLogger("default")   # Making this variable as global lets you get the reference once the 
                                        # object has been created. 


# ----------------------------------------------------------------------------------
# Name:            Main
# Purpose:         Starts the main function from the main file.
# Parameter:       appName:     Used to set/get a readable name reference
#                  logFileName: Set the logging file name e.g. myApp.log
#                  logLevel:    Sets the logging leve (debug, info, warning, ...).
#                  maxFileSize: Sets the max size of log files, once a log file
#                               is greater than this value, it will create a new one.
#                               If it is not set default will be 5*1024*1024 (5 MB).
#                  maxFiles:    Sets the max num of log files that will remain in the HDD
#                               if a new one is needed the older will be deleted. 
#                               If it is not set default value is 5                   
def createLogger (appName, logFileName, logLevel, maxFileSize=5*1024*1024, maxFiles=5):
    #Redefining a loggin object (the Main object called logger)
    logger = logging.getLogger(appName) #assinging it a name (reference)
    logger.setLevel(logLevel)   # Despite the config (setLevel) of handlers, 
                                # this controls the general-log-level to be showed 
                                # All lower levels will be included.

    #Creating a log file handler
    logsToInsertInFile = logLevel #all lower levels will be included 
    should_roll_over = os.path.isfile(logFileName)  # Checks if there is a log file (logFileName) already crated, 
                                                    # if so it doRollover() method will rotates the files, this
                                                    # we will have a new file on every run and the oldest one will
                                                    # be deleted.
    logsToInsertInFile_handler = RotatingFileHandler(logFileName, mode='a', maxBytes=maxFileSize, 
                                backupCount=maxFiles, encoding=None, delay=0)
    if should_roll_over:  # log already exists, roll over!
        logsToInsertInFile_handler.doRollover()
    logsToInsertInFile_handler.setLevel(logsToInsertInFile)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logsToInsertInFile_handler.setFormatter(file_format)
    logger.addHandler(logsToInsertInFile_handler)
    
    #Creating a printer (in cmd) log handler
    logsToShowInaShell = logLevel #all lower levels will be included 
    logsToShowInaShell_handler = logging.StreamHandler()
    logsToShowInaShell_handler.setLevel(logsToShowInaShell)
    shell_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logsToShowInaShell_handler.setFormatter(shell_format)
    logger.addHandler(logsToShowInaShell_handler)   

    #Use this as an example to use the logger
    logger.debug('Logger is ready to go')

    return logger