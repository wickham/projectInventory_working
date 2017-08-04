import csv
import os

os.chdir(os.getcwd()+'/results')
ifile = open('iPhone Parts-Table 1.csv', "rb")
reader = csv.reader(ifile)

# Globals
a = "===null"
req = 1
stock = 3
parts = []

# Data structure
#
#

class Node(object):

    def __init__(self, d, next_node=None):
        self.data = d
        self.next_node = next_node

    def get_data(self):
        return self.data
    
    def set_data(self, d):
    	self.data = d

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
    	return self.size

	def add(self, d):
		next_node = Node(d, self.root)
		self.root = new_node
		self.size += 1

	def remove(self, d):
		active_node = self.root
		prev_node = None
		while active_node:
			if active_node.get_data() == d:
				if prev_node:
					prev_node.set_next(active_node.get_next())
				else:
					self.root = active_node
				self.size -= 1
				return True					#remove complete
			else:
				prev_node = active_node
				active_node = active_node.get_next()
		return False						#remove incomplete

	def search(self,d):
		active_node = self.root
		while active_node:
			if active_node.get_data() == d:
				return d
			else:
				self.root = active_node.get_next
		return None




##########################################



# writes new .csv file with quotes instead of commas 	!! only good for testing purposes !!
#
#

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

with open('ttest.csv', 'rb') as csvfile:
	i = 0
	spamreader = csv.reader(csvfile, delimiter="'", quotechar='|')
	next(spamreader, None)
	for row in spamreader:
		
		if ((row[req]=="Need to order") and (row[stock]=="Out of stock") or (row[req]=="Need to order" and row[stock]=="Low")):
			a = "ORDER"
			i += 1
			part = row[0]
			print part
			request = ""
			index = i
			new = LinkedList()

			new.insert('part')
			print new

			print 
			#new.remove(new.search('part'))
			print
			#new.part = row[0]
			#new.request = "Need to order"
		


			
			
		
		print row[0]+", "+row[req]+", "+row[stock]+a
		a = "===null"
		#print '|'.join(row)

	print "\n"

	while i >=1:
		#print new.get_data()
		#new.get_next()
		
		i-=1




# OBJECTIVE
# scan csv for logic on slect fields
#
# 				Received =/= Out of stock
#				Received == Low
#				Received ==
ifile.close()

