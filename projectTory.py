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

import nodes
from nodes import orderlists


    

#####################################################################
# Numbers Spreadsheet Table Names,                                  #
# To add tables to the program, add the name of the export CSV      #
#   here into the variable name "export_file"                       #
# EX:                                                               #
#       export_file = ["my-file1.csv","my-file2.csv","NULL"]        #                                                                    
#####################################################################
def config():
    export_file = ["iPhone Parts-Table 1.csv", "iPhone Repair Tools-Table 1.csv", "NULL"]
    diR = "/Users/Allen/Desktop/Current Work/CODE/projectInventory_working/results"
    return (export_file, diR)

def automator():
    #os.system("/Users/Allen/Desktop/Current\ Work/CODE/projectInventory_working/SpreadsheetExportToCSV.scpt")
    os.chdir("/Users/Allen/Desktop/Current Work/CODE/projectInventory_working")
    wkdir=os.getcwd()
    print(wkdir)
    subprocess.call(["cd","/Users/Allen/Desktop/Current Work/CODE/projectInventory_working"])
    subprocess.call(["osascript","SpreadsheetExportToCSV.scpt", "/Users/Allen/Desktop/Current Work/CODE/projectInventory_working/templates/parts.numbers","/Users/Allen/Desktop/Current Work/CODE/projectInventory_working/results"])

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
    print "THIS FEATURE IS NOT YET ENABLED\n"
    #raw_input("Press any key to continue...\n")
    #main()
 
def exit():
    print "EXITING THE PROGRAM\n"

def error():
    #raw_input("error. try again.")
    #main()
    print("error. try again.")



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