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

import nodes
from nodes import orderlists


    

#####################################################################
# Numbers Spreadsheet Table Names,                                  #
# To add tables to the program, add the name of the export CSV      #
#   here into the variable name "export_file"                       #
# EX:                                                               #
#       export_file = ["my-file1.csv","my-file2.csv","NULL"]        #                                                                    #
#####################################################################

export_file = ["iPhone Parts-Table 1.csv", "iPhone Repair Tools-Table 1.csv", "NULL"]

######################################################################################

######################################################################################



def one():
    orderlists(export_file)
    raw_input("Press any key to continue...\n")
    main()
 
def two():
    os.system("clear")
    print "THIS FEATURE IS NOT YET ENABLED\n"
    raw_input("Press any key to continue...\n")
    main()
 
def exit():
    print "EXITING THE PROGRAM\n"

def error():
    raw_input("error. try again.")
    main()



options =   {   "1" : one,
                "2" : two,
                "exit": exit,
                "EXIT": exit,
            }


######################################################################################


def main():
    os.system("clear")
    print("Program initialized successfully\n\nSelect an option from the following or type \"EXIT\" to end:\n1) Send order list e-mail\n2) Receive parts\n\n")
    inputVar = raw_input(":: ")
    val = options.get(inputVar)
    if val is None:
        error()
    else:
        val()

main()
