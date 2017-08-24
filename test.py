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
os.chdir(os.getcwd()+'/results')

#####################################################################
# For debugging purposes                                            #
# set True, all data will be shown and emailer will not execute;    #
# set False, program runs as expected                               #
#####################################################################
VERBOSE = True

#####################################################################
# Numbers Spreadsheet Table Names                                   #
# To add tables to the program, add the name of the export CSV      #
# here into the variable name                                       #
# EX: export_file = ["parts-1.csv","my-files.csv","NULL"]           #                                                                    #
#####################################################################

export_file = ["iPhone Parts-Table 1.csv", "iPhone Repair Tools-Table 1.csv", "NULL"]

######################################################################################

#############
# HTML Code #
#############



html = """\

<!DOCTYPE html>

<html>
            <head>
            <style>
            html,body{
                overflow-x: hidden;
            }

            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            h1 {
                font-family: helvetica, arial, sans-serif;
                color: white;
            }

            h2 {
                font-family: helvetica, arial, sans-serif;
                color: black;
                
            }

            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;

            }

            td.good, td.received {
                background-color: rgba(156,225,89, 0.7);
            }
            
            td.out, td.need {
                background-color: rgba(255,95,94, 0.7);
            }
            
            td.low, td.order {
                background-color: rgba(255,254,97, 0.7);
            }
            
            th.dark, tr.dark{
                background-color: rgb(40,40,40);
                border-bottom: 1px solid black;
                color: rgb(255,255,255);

            }

            th.red, tr.red{
                background-color: rgb(40,40,40);
                border-bottom: 1px solid black;
                color: rgb(255,255,255);

            }
            
            tr {
                background-color: rgb(255,255,255);
            }

            tr:nth-child(even) {
                background-color: #dddddd;
            }

            tr.bro {
                
                background-color: rgb(255,150,150);
            }

            tr.bro:nth-child(even) {
                background-color: rgb(255,190,150);
            }

            div.head {
                background: rgba(255,255,255,.6);
            }

            div.good {
                background: linear-gradient(to top right,rgba(100,178,223,.8),rgba(36,66,142,.7)); 
                padding:25px;
                margin: 20px 10px 10px 10px; 
                text-align: right;
                border-radius: 25px;
                box-shadow: -5px 5px 4px #aaa,
                             5px 4px 4px #aaa;
                min-width: 320px;

            }
            
            div.bad {
                background-color:rgb(255,190,190); 
                border: 1px solid rgb(255,150,150);
                padding-top: 1px;
                padding-bottom: 25px; 
                margin-top: 20px;
                margin: 20px 0px 0px 0px; 
                border-radius: 25px;

            }
            .fixed {
                min-width: 5em;
            }

            .special { 
                font-family: "Baskerville Old Face",Dingbats, Quivira, "Arial Unicode MS", Symbola, " Everson Mono";
                font-size: 50px;
                color: white;
                text-overflow: clip;
                overflow: hidden;
                width: 4em;    
            }

            .special1 { 
                font-family: "Dingbats", Quivira, "Arial Unicode MS", Symbola, " Everson Mono";
                font-size: 15px;
                color: rgb(200,0,0);
                text-shadow: 0.1em 0.1em black;
                
            }

            .special2 { 
                font-family: "Dingbats", Quivira, "Arial Unicode MS", Symbola, " Everson Mono";
                font-size: 25px;
                text-shadow: 0.05em 0.05em black;
                color: rgb(200,0,0);
            }

            .bro {
                color: rgb(200,0,0);
                text-shadow: 1px 1px black;
            }

            .shadow {
                box-shadow: 0px 5px 4px rgba(0,0,0, 0.1);
                padding: 20px;
                margin: 20px 0px 0px 0px;
                min-width: 40%;


            }
            .hidden {
            font-size: 0px;
            }
            .center {
                text-align: center;
                font-family: helvetica, arial, sans-serif;
                color: white;
            }
            
            .black {
                background-color: rgba(40,40,40,0.5);
                border-radius: 25px;

            }
            
            .white {
                background-color: rgba(255,255,255,0);
                padding-top: 10px;
                padding-bottom: 25px;
                padding-right: 10px;
                padding-left: 10px; 
                margin-top: 20px;

                border-radius: 25px;
                }

            </style>
            </head>
            <body>

"""
######################################################################################

# Globals #

a = "===null"
req = 1
stock = 3
parts = []
reqprint = "<===== INVALID REQUEST"


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

def error():
    raw_input("error. try again.")
    main()


options =   {   "1" : one,
                "2" : two,
                "exit": exit,
                "EXIT": exit,
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



# writes new .csv file with quotes instead of commas 	!! my testing purposes !!
#
#

def orderlist():
    j = 0
    while export_file[j] != "NULL":
        ifile = open(export_file[j], "rb")
        reader = csv.reader(ifile)
        ofile  = open('ttest.csv', "wb")
        writer = csv.writer(ofile, delimiter="'", quotechar='"', quoting=csv.QUOTE_NONE)
        for row in reader:
            writer.writerow(row)
        ofile.close()
        j+=1


        # manipulate .csv file
        # prints out the lines and
        #
        #
        

    head = Node(0,0,0)
    need = head
    with open('ttest.csv', 'rb') as csvfile:
        i = 0
        spamreader = csv.reader(csvfile, delimiter="'", quotechar='|')
        next(spamreader, None)
        for row in spamreader:
            a = "ORDER"
            i += 1
            ppart = row[0]
            rrequest = row[req]
            sstock = row[stock]
            need.next = Node(ppart, sstock, rrequest)
            need = need.next


        
      
    ifile.close()
    ''' OBJECTIVE
      scan csv for logic on slect fields
    
                   Received =/= Out of stock
                   Received == Low
                   Received ==

        all cases
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
    body = html
    body = body + str("""\
            <div class="good">
                <span class="hidden">APPLE CONFIDENTIAL --- Order Request --- Please proceed with ordering the following below. 
                Needs Investigation should be inspected an validate correct status.</span>
                <span class="special">&#xF000</span><div class="center"></div>
                <div class="black">
                <div class="white head"><h2><center><b>PLEASE ORDER</b></h2>
                    """)
    body = body + str("""\
                    <table class="shadow">
                    <center>
                        <tr class="dark">
                            <th class"fixed">PART #</th>
                            <th class"fixed">STOCK</th>
                            <th class"fixed">REQUEST</th>
                        </tr>
                    </center>
                    """)
    if VERBOSE is True:
        print("\n%32s \n" % ("+++ PLEASE ORDER +++"))
        print("================================================= ")
        print("| PART #     ||     STOCK     ||     REQUEST    |")
        print("================================================= ")
    while need != None:
        if(need.stock == "Out of stock" and need.request =="Need to order"):
            body = body + str("""\
            <tr>
                <td> {} </td>
                <td class="out"> {} </td>
                <td class="need"> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())
            if VERBOSE is True:
                print ("%s      %s      %s      \n" % (need.getPart().ljust(12),need.getStock().upper().ljust(12),need.getRequest().upper().ljust(13) ))
            need = need.next
        elif(need.stock == "Out of stock" and need.request ==""):
            body = body + str("""\
            <tr>
                <td> {} </td>
                <td class="out"> {} </td>
                <td class="blank"> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())
            if VERBOSE is True:
                print ("%s      %s      %s      \n" % (need.getPart().ljust(12),need.getStock().upper().ljust(12),need.getRequest().upper().ljust(13) ))
            need = need.next
        elif(need.stock == "Low" and need.request=="Need to order"):
            body = body + str("""\
            <tr>
                <td> {} </td>
                <td class="low"> {} </td>
                <td class="need"> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())
            if VERBOSE is True:
                print ("%s      %s      %s      \n" % (need.getPart().ljust(12),need.getStock().upper().ljust(12),need.getRequest().upper().ljust(13) ))
            need = need.next 
        elif(need.stock == "Low" and need.request==""):
            body = body + str("""\
            <tr>
                <td> {} </td>
                <td class="low"> {} </td>
                <td class="blank"> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())
            if VERBOSE is True:
                print ("%s      %s      %s      \n" % (need.getPart().ljust(12),need.getStock().upper().ljust(12),need.getRequest().upper().ljust(13) ))
            need = need.next
        elif need != None: need = need.next
    body = body + str("</table></div></div>")
    if VERBOSE is True:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n ")

    #
    #       NEEDING ATTENTION
    #

    need = head
    need = need.next
    body = body + str("""\
                <div class="black">
                <div class="white head"><h2><center><b><span class="special2">&#10071</span><span>NEEDS INVESTIGATION</span><span class="special2">&#10071</span></b></h2>
                                """)
    body = body + str("""\
                     <table class="shadow">
                        <center>
                        <tr class="dark">
                            <th class="red fixed">PART #</th>
                            <th class="red fixed">STOCK</th>
                            <th class="red fixed">REQUEST</th>
                        </tr>
                        </center>
                    """)
    if VERBOSE is True:
        print("{:^50}\n".format("+++ NEEDS INVESTIGATION +++"))
        print("=================================================")
        print("| {:^14}||{:^14}||{:^14}|".format("PART #","STOCK","REQUEST"))
        print("=================================================\n")

    # If stock is GOOD and request is NEED TO ORDER ||
    #     GOOD and request is ORDER PLACED          ||
    #

    while need != None:
        if(need.request=="Need to order" and need.stock == "Good"):
            body = body + str("""\
            <tr>
                <td><span class="special1">&#10071</span>{}</td>
                <td class="good"> {} </td>
                <td class="need"> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())
            if VERBOSE is True:
                print (" {:<15} {:^15} {:>15} {:>25}\n".format(need.getPart(),need.getStock().upper(),need.getRequest().upper(), "<===== INVALID REQUEST" ))
            need = need.next
        elif(need.request == "Order placed" and need.stock == "Good"):
            body = body + str("""\
            <tr>
                <td><span class="special1">&#10071</span> {} </td>
                <td class="good"> {} </td>
                <td class="order"> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())

            
            if VERBOSE is True:
                print (" {:<15} {:^15} {:>15} {:>25}\n".format(need.getPart(),need.getStock().upper(),need.getRequest().upper(), "<===== INVALID REQUEST" ))
            need = need.next
        elif need != None: need = need.next

    if VERBOSE is True:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n ")
        body = body + str("</table></div></div></div></body></html>")
    else:
        body = body + str("</table></div></div></div></body></html>")
        autoEmailer.send(body)



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
