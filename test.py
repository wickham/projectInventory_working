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
os.chdir(os.getcwd()+'/results')
# For debugging purposes
# set True, all data will be shown;
# set False, program runs as expected
#################

VERBOSE = False

#################




# Globals
a = "===null"
req = 1
stock = 3
parts = []
body = ("""\
        <html>
            <head></head>
            <body>
                <p>
        """)

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

options = { "1" : one,
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



# writes new .csv file with quotes instead of commas 	!! only good for testing purposes !!
#
#

def orderlist():

    ifile = open('iPhone Parts-Table 1.csv', "rb")
    reader = csv.reader(ifile)
    ofile  = open('ttest.csv', "wb")
    writer = csv.writer(ofile, delimiter="'", quotechar='"', quoting=csv.QUOTE_NONE)
    for row in reader:
        writer.writerow(row)
    ofile.close()



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
    
    # OBJECTIVE
    # scan csv for logic on slect fields
    #
    #               Received =/= Out of stock
    #               Received == Low
    #               Received ==

    ''' all cases
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
    body = str("""\
            <html>
            <head>
            <style>
            table   {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
                    }

            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }

            tr{
                background-color: rgb(255,255,255);
            }

            tr.bro {
                color: rgb(200,20,20);
                background-color: rgb(255,150,150);
            }
            
            tr:nth-child(even){
                background-color: #dddddd
            }
            td.bro{
                border: 1px solid rgb(255,150,150);
            }
            tr.bro:nth-child(even) {
                background-color: rgb(255,190,190);
            }
            div.good {background-color:#dddddd; padding:20px; margin: 20px 20px 20px 20px;}
            div.bad {background-color:rgb(255,190,190); padding:20px; margin: 20px 0px 0px 0px;}
            </style>
            </head>
            <body>
            """)
    body = body + str("""\
                    <div><h2><center><b>PLEASE ORDER</b></h2><br />
                    """)
    body = body + str("""\
                    <table>
                    <center><tr>
                            <th>PART #</th>
                            <th>STOCK</th>
                            <th>REQUEST</th>
                        </tr></center>
                    """)
    if VERBOSE is True:
        print("\n%32s \n" % ("+++ PLEASE ORDER +++"))
        print("================================================= ")
        print("| PART #     ||     STOCK     ||     REQUEST    |")
        print("================================================= ")
    while need != None:
        if((need.stock == "Out of stock" and (need.request =="Need to order" or need.request =="")) or (need.stock == "Low" and (need.request=="Need to order" or need.request==""))):
            body = body + str("""\
            <tr>
                <td> {} </td>
                <td> {} </td>
                <td> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())
            if VERBOSE is True:
                print ("%s      %s      %s      \n" % (need.getPart().ljust(12),need.getStock().upper().ljust(12),need.getRequest().upper().ljust(13) ))
            need = need.next
        elif need != None: need = need.next
    body = body + str("</table></div>")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n ")
    #
    #       NEEDING ATTENTION
    #

    need = head
    need = need.next
    body = body + str("""\
                <div class="bad"><h2><center><b>NEEDS INVESTIGATION</b></h2></div><br />
                                """)
    body = body + str("""\
                     <table>
                        <tr>
                            <th>PART #</th>
                            <th>STOCK</th>
                            <th>REQUEST</th>
                        </tr>
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
        if((need.request=="Need to order" and need.stock == "Good") or (need.request == "Order placed" and need.stock == "Good")):
            

            body = body + str("""\
            <tr class="bro">
                <td class="bro"> {} </td>
                <td class="bro"> {} </td>
                <td class="bro"> {} </td>
            </tr>
                """).format(need.getPart(),need.getStock(),need.getRequest())
            if VERBOSE is True:
                print (" {:<15} {:^15} {:>15} {:>25}\n".format(need.getPart(),need.getStock().upper(),need.getRequest().upper(), "<===== INVALID REQUEST" ))
            need = need.next
        elif need != None: need = need.next

    if VERBOSE is True:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n ")
    body = body + str("</table></body></html>")
    autoEmailer.send(body)



def main():
    os.system("clear")
    print("Program initialized successfully\n\nSelect on option from the following or type \"EXIT\" to end:\n1) Send order list e-mail\n2) Receive parts\n\n")
    inputVar = raw_input(":: ")
    val = options.get(inputVar)
    if val is None:
        error()
    else:
        val()

main()


html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""






