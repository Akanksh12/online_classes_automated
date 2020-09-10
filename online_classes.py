from webbrowser import open
import tkinter as tk
import time

drive_link = 'https://drive.google.com/u/1'
classroom_link = 'https://classroom.google.com/u/1'

open(classroom_link)
open(drive_link)


win = tk.Tk()
win.wm_title("Classes automated")
win.geometry('500x500')

welcome = tk.Label(text="Welcome to Online classes automated!")

class Class():
    def __init__(self,meet_link):
        self.meet_link = meet_link


eco = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=a63lcr6fgn')

eng = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=dtuu3fvz3p')

math = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=f64wxtbiz3')

phy = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=dipb37vrdq')

chem = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=begd3clsbo')

bio = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=hnyegm44h4')

comp = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=elsot7zabb')

french = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=ff2hnnsgv4')

act = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=ejb7enjvgi')

lib = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=b5oqv35ic7')

pt = Class('https://meet.google.com/_meet/whoops?authuser=1&hs=179&sc=256&alias=a2olworqyx')

mon = False
tue = False
wed = False
thu = False
fri = False

Periods = ['08 30 00', '09 30 00', '10 10 00 ', '11 05 00', '11 45 00', '12 25 00']
pn = 0

sl = tk.Label(text="option selected")

sl.pack()

def exemon():
    mon = True
    sl.pack()
    pn = 0
    while mon == True:
        ctime = time.strftime('%H %M %S')

        if ctime == Periods[pn]:
            open(phy.meet_link)
            pn += 1

        if ctime == Periods[pn]:
            open(comp.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(lang.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(bio.meet_link)
            pn += 1
        if ctime == Periods[pn]:
            open(math.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(chem.meet_link)
            pn += 1
        

def exetue():
    tue = True
    sl.pack()
    pn = 0
    while tue == True:
        ctime = time.strftime('%H %M %S')

        if ctime == Periods[pn]:
            open(act.meet_link)
            pn += 1

        if ctime == Periods[pn]:
            open(math.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(lib.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(eng.meet_link)
            pn += 1
        if ctime == Periods[pn]:
            open(eco.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(comp.meet_link)
            pn += 1

def exewed():
    wed = True
    sl.pack()
    pn = 0
    while wed == True:
        ctime = time.strftime('%H %M %S')

        if ctime == Periods[pn]:
            open(bio.meet_link)
            pn += 1

        if ctime == Periods[pn]:
            open(pt.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(eng.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(phy.meet_link)
            pn += 1
        if ctime == Periods[pn]:
            open(chem.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(eco.meet_link)
            pn += 1
        

def exethu():
    thu = True
    sl.pack()
    pn = 0
    while thu == True:
        ctime = time.strftime('%H %M %S')

        if ctime == Periods[pn]:
            open(math.meet_link)
            pn += 1

        if ctime == Periods[pn]:
            open(eng.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(eco.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(bio.meet_link)
            pn += 1
        if ctime == Periods[pn]:
            open(french.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(phy.meet_link)
            pn += 1

def exefri():
    fri = True
    sl.pack()
    pn = 0
    while fri == True:
        ctime = time.strftime('%H %M %S')

        if ctime == Periods[pn]:
            open(comp.meet_link)
            pn += 1

        if ctime == Periods[pn]:
            open(chem.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(eng.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(pt.meet_link)
            pn += 1
        if ctime == Periods[pn]:
            open(french.meet_link)
            pn += 1
        
        if ctime == Periods[pn]:
            open(math.meet_link)
            pn += 1

bmon = tk.Button(text="Monday", command=exemon).pack()
btue = tk.Button(text="Tuesday", command=exetue).pack()
bwed = tk.Button(text="Wednesday", command=exewed).pack()
bthu = tk.Button(text="Thursday", command=exethu).pack()
bfri = tk.Button(text="Friday", command=exefri).pack()


win.mainloop()







