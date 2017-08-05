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

# For debugging purposes
# set True, all data will be shown;
# set False, program runs as expected
#################

VERBOSE = False

#################


os.chdir(os.getcwd()+'/results')
ifile = open('iPhone Parts-Table 1.csv', "rb")
reader = csv.reader(ifile)

# Globals
a = "===null"
req = 1
stock = 3
parts = []


def one():
    orderlist()
    raw_input("Press any key to continue...\n")
    main()
 
def two():
    os.system("clear")
    print "THIS FEATURE IS NOT YET ENABLED\n"
    raw_input("Press any key to continue...\n")
    main()
 
def exit():
    print "EXITING THE PROGRAM\n"

options = { "1" : one,
            "2" : two,
            "exit": exit,
}
 


#
# Data structure
#

class Node:
    def __init__(self,ppart, sstock, rrequest):
        self.part = ppart
        self.stock = sstock
        self.request =  rrequest
        self.next = None

    def getPart(self):
        return self.part

    def getStock(self):
    	return self.stock

    def getRequest(self):
    	return self.request

    def getNext(self):
        return self.next

    def setData(self,partdata, stockdata, requestdata):
        self.part = partdata
        self.stock = stockdata
        self.request = requestdata

    def setNext(self,newnext):
        self.next = newnext

#
# Print function for printing beautiful tables
#



##########################################



# writes new .csv file with quotes instead of commas 	!! only good for testing purposes !!
#
#

def orderlist():
    ofile  = open('ttest.csv', "wb")
    writer = csv.writer(ofile, delimiter="'", quotechar='"', quoting=csv.QUOTE_NONE)
    for row in reader:
        writer.writerow(row)
    ofile.close()



    # manipulate .csv file
    # prints out the lines and
    #
    #
    #
    head = Node(0,0,0)
    need = head
    with open('ttest.csv', 'rb') as csvfile:
        i = 0
        spamreader = csv.reader(csvfile, delimiter="'", quotechar='|')
        next(spamreader, None)
        for row in spamreader:
            #if ((row[req]=="Need to order") and (row[stock]=="Out of stock") or (row[req]=="Need to order" and row[stock]=="Low")):
            a = "ORDER"
            i += 1
            ppart = row[0]
            rrequest = row[req]
            sstock = row[stock]
            need.next = Node(ppart, sstock, rrequest)
            need = need.next


    	

    	while i >=1:
    		#print new.get_data()
    		#new.get_next()
    		
    		i-=1


    ifile.close()

    # OBJECTIVE
    # scan csv for logic on slect fields
    #
    #               Received =/= Out of stock
    #               Received == Low
    #               Received ==

    '''
        NONE            GOOD
        NONE            LOW
        NONE            OUT OF STOCK

        NEED TO ORDER   GOOD
        NEED TO ORDER   LOW
        NEED TO ORDER   OUT OF STOCK

        ORDER PLACED    GOOD
        ORDER PLACED    LOW
        ORDER PLACED    OUT OF STOCK

        RECEIVED        GOOD
        RECEIVED        LOW
        RECEIVED        OUT OF STOCK
    '''


    if VERBOSE is True:
        print ("\n==============")
        print ("||DEBUG MODE||")
        print ("==============\n")
        need = head
        need = need.next
        while need != None:
            print (need.getPart() + need.getStock() + need.getRequest())
            need = need.next
        print("\n +PROCESS COMPLETE+ \n")


    #
    #       NEEDS ORDERING
    #    

    need = head
    need = need.next
    print("\n%32s \n" % ("+++ PLEASE ORDER +++"))
    print("================================================= ")
    print("| PART #     ||     STOCK     ||     REQUEST    |")
    print("================================================= ")
    while need != None:
        if((need.stock == "Out of stock" and (need.request =="Need to order" or need.request =="")) or (need.stock == "Low" and (need.request=="Need to order" or need.request==""))):
            print ("%s      %s      %s      \n" % (need.getPart().ljust(12),need.getStock().upper().ljust(12),need.getRequest().upper().ljust(13) ))
            need = need.next
        elif need != None: need = need.next
    print("+++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n ")
    #
    #       NEEDING ATTENTION
    #

    need = head
    need = need.next
    print("\n         +++ NEEDS INVESTIGATION +++ \n")
    print("================================================= ")
    print("| PART #     ||     STOCK     ||     REQUEST    |")
    print("================================================= ")

    # If stock is GOOD and request is NEED TO ORDER ||
    #     GOOD and request is ORDER PLACED          ||
    #

    while need != None:
        if((need.request=="Need to order" and need.stock == "Good") or (need.request == "Order placed" and need.stock == "Good")):
            print ("%s      %s      %s      %s\n" % (need.getPart().ljust(12),need.getStock().upper().ljust(12),need.getRequest().upper().ljust(13), "<===== INVALID REQUEST".ljust(12) ))
            need = need.next
        elif need != None: need = need.next
    print("+++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n ")



def main():
    os.system("clear")
    print("Program initialized successfully\n\nSelect on option from the following or type \"EXIT\" to end:\n1) Send order list\n2) Receive parts\n\n")
    inputVar = raw_input(":: ")
    options.get(inputVar, lambda : None)()

main()








