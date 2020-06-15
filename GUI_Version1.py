# Python script that reads in csv file data from vulnerability reports,
# separates out the important data, and saves it to a new csv file.
#
# Copyright Noah Former, June 2020

import csv
import sys

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
from tkinter import *

goodRows = []
check = False

i = 0
n = 0

sevCount1 = 0
sevCount2 = 0
sevCount3 = 0
sevCount4 = 0
sevCount5 = 0

vulnCount1 = 0
vulnCount2 = 0


print("Copyright Noah Former, 2020")
print("For use on Qualys csv file reports only.\n")
print("On Standby...\n")

# this is the function called when the button is clicked
def btnOpenFile():
    
    global i
    global n
    global labelText

    global check

    global writeProgressBar
    global readProgressBar

    global sevCount1
    global sevCount2
    global sevCount3
    global sevCount4
    global sevCount5

    global vulnCount1
    global vulnCount2

    global sevText1
    global sevText2
    global sevText3
    global sevText4
    global sevText5

    global vulnText1
    global vulnText2

    global severityBox
    global vulnerabilityCount

    global goodRows
    check = False

    i = 0
    n = 0

    sevCount1 = 0
    sevCount2 = 0
    sevCount3 = 0
    sevCount4 = 0
    sevCount5 = 0

    vulnCount1 = 0
    vulnCount2 = 0
    
    print("Opening file...")
    read_path = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("CSV","*.csv"),("All Files","*.*")))
    print("\nStarting filtering process...")

    with open(read_path) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            try:
                if(row[0] == "IP" and row[1] == "Network" and row[2] == "DNS"):
                    check = True
                    print("\nFound a break in the data! Collecting desired rows now...\n")
                    readProgressBar["value"] = 0

                if(check == True and len(row) != 0):
                    goodRows.append(row)
                    n = n + 1
                    sys.stdout.write(str(n) + " Rows Collected\r")
                    labelText.set(n)
                    #progressLabel = Label(root, text=str(labelText.get()), bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=133, y=421)
                    makeReadProgress()

                    #writeProgressBar=ttk.Progressbar(root, style='writeProgressBar.Horizontal.TProgressbar', orient='horizontal', length=360, mode='determinate', maximum=len(goodRows), value=0)
                    writeProgressBar.update()

                    if(row[13] == "1"):
                        sevCount1 = sevCount1 + 1

                    if(row[13] == "2"):
                        sevCount2 = sevCount2 + 1

                    if(row[13] == "3"):
                        sevCount3 = sevCount3 + 1

                    if(row[13] == "4"):
                        sevCount4 = sevCount4 + 1

                    if(row[13] == "5"):
                        sevCount5 = sevCount5 + 1


                        

                    if(row[12] == "Vuln"):
                        vulnCount1 = vulnCount1 + 1

                    if(row[36] == "yes"):
                        vulnCount2 = vulnCount2 + 1
                    

            except:
                print("\nAn Error was thrown. Most likely the row trying to be read in is blank.\n")


        readProgressBar["value"] = 0

        sevTotal = sevCount1+sevCount2+sevCount3+sevCount4+sevCount5


        sevText1.set(sevCount1)
        sevText2.set(sevCount2)
        sevText3.set(sevCount3)
        sevText4.set(sevCount4)
        sevText5.set(sevCount5)
        vulnText1.set(vulnCount1)
        vulnText2.set(vulnCount2)

        severityBox.delete('1', '5')
        severityBox.insert('1', '1: ' + str(sevCount1) + " (" + str(round(100*(sevText1.get()/sevTotal), 2)) + "%)")
        severityBox.insert('2', '2: ' + str(sevCount2) + " (" + str(round(100*(sevText2.get()/sevTotal), 2)) + "%)")
        severityBox.insert('3', '3: ' + str(sevCount3) + " (" + str(round(100*(sevText3.get()/sevTotal), 2)) + "%)")
        severityBox.insert('4', '4: ' + str(sevCount4) + " (" + str(round(100*(sevText4.get()/sevTotal), 2)) + "%)")
        severityBox.insert('5', '5: ' + str(sevCount5) + " (" + str(round(100*(sevText5.get()/sevTotal), 2)) + "%)")

        vulnerabilityCount.delete('0', '1')
        vulnerabilityCount.insert('0', '# of Vulnerabilities: ' + str(vulnText1.get()))
        vulnerabilityCount.insert('1', '# of PCI Vulnerabilities: ' + str(vulnText2.get()))


def btnSaveFile():

    global i
    global n

    global writeProgressBar

    global goodRows

    write_path = filedialog.asksaveasfilename(initialdir = "/", title = "Select File", filetypes = (("CSV files","*.csv"),("All Files","*.*")))

    writeProgressBar["maximum"] = len(goodRows)

    writeProgressBar["value"] = 0

    print("\nWriting to new file...\n")

    with open(write_path, "w+", newline='') as file:
        writer = csv.writer(file)
        
        for x in goodRows:
            i = i + 1
            writer.writerow(x)
            sys.stdout.write(str(int(i/len(goodRows)*100)) + " Percent Complete\r")
            makeProgress()
            writeProgressBar.update()

    print("\nComplete! Check " + write_path + ".csv for the new csv file.")

    #writeProgressBar.destroy()


# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
    global writeProgressBar
    
    writeProgressBar['value']=writeProgressBar['value'] + 1
    root.update_idletasks()

# Function that updates the read progress bar
def makeReadProgress():
    global readProgressBar

    readProgressBar["value"] = readProgressBar["value"] + 1
    root.update_idletasks()

# this is a function to get the selected list box value
def getListboxValue():
    itemSelected = vulnerabilityCount.curselection()
    return itemSelected

# this is a function to get the selected list box value
def getListboxValue():
    itemSelected = severityBox.curselection()
    return itemSelected

root = Tk()

labelText = IntVar(value=0)
labelText.set(n)

sevText1 = IntVar()
sevText2 = IntVar()
sevText3 = IntVar()
sevText4 = IntVar()
sevText5 = IntVar()
vulnText1 = IntVar()
vulnText2 = IntVar()

sevText1.set(sevCount1)
sevText2.set(sevCount2)
sevText3.set(sevCount3)
sevText4.set(sevCount4)
sevText5.set(sevCount5)
vulnText1.set(vulnCount1)
vulnText2.set(vulnCount2)

writeProgressBar=ttk.Progressbar(root, style='writeProgressBar.Horizontal.TProgressbar', orient='horizontal', length=360, mode='determinate', maximum=len(goodRows), value=0)


# This is the section of code which creates the main window
root.geometry('500x480')
root.minsize(500, 480)
root.maxsize(500, 480)
root.configure(background='#F0F8FF')
root.title('Qualys Filter')

# This is the section of code which creates the a label
Label(root, text='Qualys Filter', bg='#F0F8FF', font=('arial', 24, 'bold')).place(x=153, y=11)

# This is the section of code which creates a button
Button(root, text='Open File', bg='#C1CDCD', font=('arial', 12, 'normal'), command=btnOpenFile).place(x=13, y=11)
Button(root, text='Save File', bg='#C1CDCD', font=('arial', 12, 'normal'), command=btnSaveFile).place(x=400, y=11)

# This is the section of code which creates the a label
Label(root, text='Write Progress:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=13, y=451)

# This is the section of code which creates a progress bar
writeProgressBar=ttk.Progressbar(root, style='writeProgressBar.Horizontal.TProgressbar', orient='horizontal', length=360, mode='determinate', maximum=100, value=0)
writeProgressBar.place(x=130, y=453)

# Code for read progress bar
readProgressBar=ttk.Progressbar(root, style='writeProgressBar.Horizontal.TProgressbar', orient='horizontal', length=360, mode='indeterminate', maximum=500, value=0)
readProgressBar.place(x=130, y=424)

# This is the section of code which creates the a label
Label(root, text='Read Progress:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=13, y=421)

# This is the section of code which creates the a label
#Label(root, text=str(labelText.get()), bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=133, y=421)

# This is the section of code which creates a listbox
vulnerabilityCount=Listbox(root, bg='#F0F8FF', font=('arial', 20, 'normal'), width=0, height=0)
vulnerabilityCount.insert('0', '# of Vulnerabilities: ' + str(vulnText1.get()))
vulnerabilityCount.insert('1', '# of PCI Vulnerabilities: ' +str( vulnText2.get()))
vulnerabilityCount.place(x=13, y=101)

# This is the section of code which creates a listbox
severityBox=Listbox(root, bg='#F0F8FF', font=('arial', 15, 'normal'), width=0, height=0)
severityBox.insert('0', 'Severity Statistics:')
severityBox.insert('1', '1: ' + str(sevCount1) + " (" + str(sevText1.get()) + "%)")
severityBox.insert('2', '2: ' + str(sevCount2) + " (" + str(sevText2.get()) + "%)")
severityBox.insert('3', '3: ' + str(sevCount3) + " (" + str(sevText3.get()) + "%)")
severityBox.insert('4', '4: ' + str(sevCount4) + " (" + str(sevText4.get()) + "%)")
severityBox.insert('5', '5: ' + str(sevCount5) + " (" + str(sevText5.get()) + "%)")
severityBox.place(x=13, y=211)

root.mainloop()
