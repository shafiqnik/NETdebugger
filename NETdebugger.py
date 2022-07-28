#https://www.pythontutorial.net/tkinter/tkinter-grid/
'''
Building the exe file
pyinstaller -F --hidden-import "babel.numbers" NETdebugger.py

or use this command to do the exe build
pyinstaller --hidden-import=babel.numbers NETdebugger.py


babel.numbers genreates error if above command is not used for building exe

'''

import tkinter as tk
from random import random
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from AuditLog import Audit
from tinydb import TinyDB, Query
import webbrowser

import sys
import os


# root window
root = tk.Tk()
root.geometry("940x500")
root.title('NETdebugger V2.0')
root.resizable(0, 0)

#store bid andd date info
bid = tk.StringVar()
date = tk.StringVar()
fromSelect = tk.StringVar()
toSelect = tk.StringVar()

audit = Audit()



# configure the grid
#root.columnconfigure(1, weight=1)
root.columnconfigure(10, weight=10)







def dbStore(beaconID, fromdate,todate,response):

    path = "X://BEACON//net//NET-Support-Tools//NETdebggerDB//"
    now = datetime.now()
    now1 = str(now.strftime(("%m%d%H%M")))
    print('now1...',now1)


    try:
        db = TinyDB(path+now1+'.json')
        db.insert({'dateTime':str(datetime.now()), 'beaconID':beaconID, 'FromDate': str(fromdate), 'ToDate':str(todate), 'Message':str(response)})
    except (FileNotFoundError or OSError):
        print('DB Location not accessible')



def checkAuditLog_clicked():


    print('get Audit data button is clicked')
    beaconID = bid.get()
    #daterange = date.get()

    print('entered data is ', bid.get())

    fromDate = datetime.strptime(fromSelect.get(),'%m/%d/%y')
    toDate = datetime.strptime(toSelect.get(),'%m/%d/%y')


    print('day is  ',fromDate.day)
    print('month is  ',toDate.month)

    text = audit.inputs(beaconID, fromDate,toDate)
    curlyBracket = audit.CurlyBrackets(text)
    startEvents = audit.StartEvents(text)
    ble_tag = audit.bleTag(text)
    powerIssue = audit.powerIssue(text)

    message = str(curlyBracket),',',str(startEvents),',',str(ble_tag),', ',str(powerIssue)


    dbStore(bid.get(),fromDate,toDate,message)    #storing the messages in a local db

    vcStartCheck = ttk.Label(root, text=str(startEvents),  foreground="green",font=("Arial",11))
    vcStartCheck.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

    vcCurlyBracket = ttk.Label(root, text=str(curlyBracket), foreground="green", font=("Arial",11))
    vcCurlyBracket.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

    bleEvents = ttk.Label(root, text=str(ble_tag), foreground="green", font=("Arial",11))
    bleEvents.grid(column=1, row=10, sticky=tk.W, padx=5, pady=5)

    power = ttk.Label(root, text=str(powerIssue), foreground="green",font=("Arial",11) )
    power.grid(column=1, row=11, sticky=tk.W, padx=5, pady=5)


# username
bid_label = ttk.Label(root, text="Beacon ID:")
bid_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)


bid_entry = ttk.Entry(root,textvariable=bid)
bid_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)



#calendar
# selecting from date

cal_label = ttk.Label(root,text=" From ")
cal_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

try:
    cal = DateEntry(root, selectmode='day', textvariable=fromSelect)
    cal.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
except (ModuleNotFoundError):
    print(' babel related error1..')

# selecting to date
cal_label2 = ttk.Label(root,text="To ")
cal_label2.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

try:
    cal2 = DateEntry(root, selectmode='day', textvariable=toSelect)
    cal2.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)

except (ModuleNotFoundError):
    print(' babel related error2..')
print('selected dates are from ',fromSelect.get(),' to  ',toSelect.get())



#tkc = Calendar(root,selectmode='day', year=2022, month=1, date=1)
#tkc.grid(column=1, row=5)

# check audit log button
checkLog_button = ttk.Button(root, text=" Check Audit Log ",command=checkAuditLog_clicked)
checkLog_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


def callback(url):
    webbrowser.open_new(url)

link1 = ttk.Label(root,text="V3.1 Debugging Instructions ",foreground ="blue", cursor="hand2")
#link1.grid(column=0, row=8, sticky=tk.SW, padx=5, pady=5)
link1.place(relx =0.1, rely=0.5, anchor ='sw')
link1.bind("<Button-1>", lambda e: callback("http://confluence.contigo.lan/display/MA/V3.1+Diagnostics+instructions"))


link2 = ttk.Label(root,text="V3.1 Testing Steps ",foreground ="blue", cursor="hand2")

link2.place(relx =0.1, rely=0.6, anchor ='sw')
link2.bind("<Button-1>", lambda e: callback("http://confluence.contigo.lan/display/CE/Vehicle+Collector+Testing+Steps"))

link3 = ttk.Label(root,text="V3.1 Installation & Documenations ",foreground ="blue", cursor="hand2")

link3.place(relx =0.1, rely=0.7, anchor ='sw')
link3.bind("<Button-1>", lambda e: callback("http://confluence.contigo.lan/pages/viewpage.action?pageId=31818229"))

root.mainloop()