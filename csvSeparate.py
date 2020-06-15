# Python script that reads in csv file data from vulnerability reports,
# separates out the important data, and saves it to a new csv file.
#
# Copyright Noah Former, June 2020

import csv
import sys

import tkinter as tk
from tkinter import filedialog

goodRows = []
check = False

i = 0
n = 0


print("Copyright Noah Former, 2020")
print("For use on Qualys csv file reports only.\n")


print("Opening file...")

root = tk.Tk()
root.withdraw()

read_path = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("CSV","*.csv"),("All Files","*.*")))

print("\nStarting filtering process...")

with open(read_path) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            try:
                if(row[0] == "IP" and row[1] == "Network" and row[2] == "DNS"):
                    check = True
                    print("\nFound a break in the data! Collecting desired rows now...\n")

                if(check == True and len(row) != 0):
                    goodRows.append(row)
                    n = n + 1
                    sys.stdout.write(str(n) + " Rows Collected\r")

            except:
                print("\nAn Error was thrown. Most likely the row trying to be read in is blank.\n")

write_path = filedialog.asksaveasfilename(initialdir = "/", title = "Select File", filetypes = (("CSV files","*.csv"),("All Files","*.*")))

print("\nDone collecting rows. Writing to new file...\n")

with open(write_path, "w+", newline='') as file:
    writer = csv.writer(file)
        
    for x in goodRows:
        i = i + 1
        writer.writerow(x)
        sys.stdout.write(str(int(i/len(goodRows)*100)) + " Percent Complete\r")

print("\nComplete! Check " + write_path + ".csv for the new csv file.")
