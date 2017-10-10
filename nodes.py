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
import time
import autoEmailer
import style
import sys



#####################################################################
# For debugging purposes                                            #
# set True, all data will be shown and emailer will not execute;    #
# set False, program runs as expected                               #
#####################################################################

VERBOSE = True

#############
# HTML Code #
#############

html = style.html()

#############################
#                           #
# TEST IF ALL HEADERS EXIST #
#                           #
#############################

def headerTest(header):
    i=0
    while i < len(header):    
        if(header[i].lower()==("part number")):
            part = i
            if VERBOSE is True:print("{} --- {}".format(header[i],i))
        elif(header[i].lower()==("order request")):
            request = i
            if VERBOSE is True:print("{} --- {}".format(header[i], i))
        elif(header[i].lower()==("current stock")):
            stock = i
            if VERBOSE is True:print("{} --- {}".format(header[i], i))
        i+=1

    try: part
    except NameError: 
        sys.exit("ERROR READING TABLE HEADERS\n\nPlease make sure the headers are formatted correctly and try again...\nEXITING")   
    try: request
    except NameError: 
        sys.exit("ERROR READING TABLE HEADERS\n\nPlease make sure the headers are formatted correctly and try again...\nEXITING")    
    try: stock
    except NameError: 
        sys.exit("ERROR READING TABLE HEADERS\n\nPlease make sure the headers are formatted correctly and try again...\nEXITING")

    if VERBOSE is True: print("HEADERS EXSIST\n")
    return part, request, stock

##############################
#                            #
#       Data structure       #
#                            #
##############################

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

 


######################################################
#                                                    #
# writes new .csv file with quotes instead of commas #	
# !! my testing purposes !!                          #
#                                                    #
######################################################

def orderlists(export_file,dir):
    #############################
    #   CSV Result Directory    #
    #############################
    old_dir = os.getcwd()
    os.chdir(dir)


    a = "===null"
    reqprint = "<===== INVALID REQUEST"
    tab =['']
    j = 0
    head = Node(0,0,0)
    need = head
    ofile  = open('ttest.csv', "wb")
    while export_file[j] != "NULL":
        tab[0] = str(export_file[j])
        ifile = open(export_file[j], "rb")
        reader = csv.reader(ifile)
        writer = csv.writer(ofile, delimiter="'", quotechar='"', quoting=csv.QUOTE_NONE)
        header = next(reader)

        writer.writerow(tab)
        writer.writerow(header)
        for row in reader:
            writer.writerow(row)
        j+=1
        end = ["NULL"]
        end.append(j)
        writer.writerow(end)
      
    
    ofile.close()  


    ############################
    # manipulate .csv file     #
    # prints out the lines and #
    ############################

    with open('ttest.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter="'", quotechar='|')
        if VERBOSE is True:
            print ("\n==============")
            print ("||DEBUG MODE||")
            print ("==============\n")
        tab = next(spamreader)
        header = next(spamreader)
        if VERBOSE is True:print("TAB --- {}\nHEADER --- {}".format(tab, header))

        ###################
        # GATHER NODE POS #
        ###################

        part, request, stock = headerTest(header)
        for row in spamreader:

            
            #################
            # TEST NULL ROW #
            #################

            if(row[0] == "NULL"):
                tab = next(spamreader, None)
                if(tab== None):
                    if VERBOSE is True:print("NODES:")
                    break

                header = next(spamreader)
                if VERBOSE is True:print("TAB --- {}\nHEADER --- {}".format(tab, header))
                part, request, stock = headerTest(header)
                row=next(spamreader)
           
            ppart = row[part]
            rrequest = row[request]
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

################################################
#                                              #
# Print function for printing beautiful tables #
#                                              #
################################################ 
    if VERBOSE is True:
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

    os.chdir(old_dir)

