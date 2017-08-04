#! /bin/bash

clear				# clear terminal window

echo "The script starts now."

echo "Hi, $USER!"		# dollar sign is used to get content of variable
echo

echo "I will now fetch you a list of connected users:"
echo							
w				# show who is logged on and
echo			# what they are doing

echo "Please Wait...+"
echo

cd /Users/Allen/Desktop/Current\ Work/CODE/projectInventory_working
osascript SpreadsheetExportToCSV.scpt parts.numbers /Users/Allen/Desktop/Current\ Work/CODE/projectInventory_working/results

echo
echo
echo "Okay, you have the controls again"
echo "Have a nice day!"
echo
echo "Press any key to exit:"
read -n 1 -s