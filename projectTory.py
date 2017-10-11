'''
    This program is for open source use
    Designed by Allen Wickham
    Q3 2017
    Project info @
    www.allenwickham.me
    Contact:
    allenwickhamiii@gmail.com
'''

import csv
import os
import autoEmailer
import time
import sys
import subprocess
import shelve

import nodes
from nodes import orderlists


#####################################################################
#   Variables                                                       #
#   Database    =  "database"                                       #
#   Results     = config[i, diR]                                    #
#   CSV Files   = congig[export_file, j]                            #
#   Automator   = automator()                                       #
#####################################################################

#####################################################################
# Numbers Spreadsheet Table Names,                                  #
# To add tables to the program, add the name of the export CSV      #
#   here into the variable name "export_file"                       #
# EX:                                                               #
#       export_file = ["my-file1.csv","my-file2.csv","NULL"]        #                                                                    
#####################################################################
def cd(path):
    os.chdir(os.path.expanduser(path))

def config():
    cd("~/Desktop/projectInventory_working")
    wkdir=os.getcwd()
    export_file = shelve.open("mydata")

    export_file = ["iPhone Parts-Table 1.csv", "iPhone Repair Tools-Table 1.csv", "NULL"]
    diR = wkdir+"/results"
    return (export_file, diR)

def automator():
    #os.system("/Users/Allen/Desktop/Current\ Work/CODE/projectInventory_working/SpreadsheetExportToCSV.scpt")
    cd("~/Desktop/projectInventory_working")
    wkdir=os.getcwd()
    print(wkdir)
    subprocess.call(["cd",wkdir])
    subprocess.call(["osascript","SpreadsheetExportToCSV.scpt", wkdir+"/templates/parts.numbers",wkdir+"results"])

######################################################################################

######################################################################################



def one():
    export_file, results_dir = config()
    orderlists(export_file, results_dir)
    print(os.getcwd())
    #raw_input("Press any key to continue...\n")
    #main()
 
def two():
    os.system("clear")
    storedData = shelve.open("two")
    #path = "/Users/Allen/Desktop/Current Work/CODE/projectInventory_working"
    storedData["path"] = os.getcwd()
    #storedData["path"]=raw_input("Type the stuff:  ")
    print(storedData["path"])
    storedData.close()
    #print "THIS FEATURE IS NOT YET ENABLED\n"
    #raw_input("Press any key to continue...\n")
    #main()
 
def exit():
    print "EXITING THE PROGRAM\n"

def error():
    #raw_input("error. try again.")
    #main()
    print("error. try again.")


def setDatabase(diR, name):
    print(name)
    numbers = shelve.open(name)
    if (len(numbers) == 0):
        print("VARIABLE IS NOT INITIALIZED\nInitializing...")
        numbers["path"] = diR
    if (len(diR)<=0):
        print (numbers["path"] + "Cancel")
    elif (diR == numbers["path"]):
        print(numbers["path"] + "OLD")
    else:
        numbers["path"] = diR
        print(numbers["path"] + "NEW")
    numbers.close()
    return


class Folder:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set(self,diR, name):
        print("\n")
        storedData = shelve.open(name)
        if (len(storedData) == 0):
            print("VARIABLE IS NOT INITIALIZED\nInitializing...")
            storedData["path"] = diR
        if (len(diR)<=0):
            print (storedData["path"] + "    Cancel")
            

        elif (diR == storedData["path"]):
            print(storedData["path"] + "    OLD")
        else:
            storedData["path"] = diR
            print(storedData["path"] + "    NEW")
        storedData.close()
        return

    def get(self, name):
        print("\n")
        storedData = shelve.open(name)
        if (len(storedData) == 0):
            print("VARIABLE IS NOT INITIALIZED\n")
        else:
            print("{}".format(storedData["path"] + "    GET"))
        storedData.close()
        return storedData




options =   {   "1" : one,
                "2" : two,
                "exit": exit,
                "EXIT": exit,
            }


######################################################################################




'''def main():
    os.system("clear")
    print("Program initialized successfully\n\nSelect an option from the following or type \"EXIT\" to end:\n1) Send order list e-mail\n2) Receive parts\n\n")
    inputVar = raw_input(":: ")
    val = options.get(inputVar)
    if val is None:
        error()
    else:
        val()

main()
'''