#https://www.pythontutorial.net/tkinter/tkinter-grid/
'''
Building the exe file
pyinstaller -F --hidden-import "babel.numbers" NETdebugger.py

babel.numbers genreates error if above command is not used for building exe

'''

import tkinter as tk
from tkinter import ttk

from tkcalendar import DateEntry
from datetime import datetime
from AuditLog import Audit
from tinydb import TinyDB, Query

# root window
root = tk.Tk()
root.geometry("940x800")
root.title('NETChecker V2.0')
root.resizable(0, 0)

#store bid andd date info
bid = tk.StringVar()
date = tk.StringVar()
fromSelect = tk.StringVar()
toSelect = tk.StringVar()

audit = Audit()



# configure the grid
#root.columnconfigure(1, weight=1)
root.columnconfigure(5, weight=3)


db = TinyDB('X://BEACON//net//NET-Support-Tools//NETdebggerDB//db.json')

def dbStore(beaconID, fromdate,todate,response):

    db.insert({'dateTime':str(datetime.now()), 'beaconID':beaconID, 'FromDate': str(fromdate), 'ToDate':str(todate), 'Message':str(response)})



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

    vcStartCheck = ttk.Label(root, text=str(startEvents),  foreground="blue",)
    vcStartCheck.grid(column=4, row=8, sticky=tk.W, padx=5, pady=5)

    vcCurlyBracket = ttk.Label(root, text=str(curlyBracket), foreground="blue", )
    vcCurlyBracket.grid(column=4, row=9, sticky=tk.W, padx=5, pady=5)

    bleEvents = ttk.Label(root, text=str(ble_tag), foreground="blue", )
    bleEvents.grid(column=4, row=10, sticky=tk.W, padx=5, pady=5)

    power = ttk.Label(root, text=str(powerIssue), foreground="blue", )
    power.grid(column=4, row=11, sticky=tk.W, padx=5, pady=5)


# username
bid_label = ttk.Label(root, text="Beacon ID:")
bid_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)


bid_entry = ttk.Entry(root,textvariable=bid)
bid_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)



#calendar
# selecting from date

cal_label = ttk.Label(root,text=" From ")
cal_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
cal = DateEntry(root, selectmode='day', textvariable=fromSelect)
cal.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

# selecting to date
cal_label2 = ttk.Label(root,text="To ")
cal_label2.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)
cal2 = DateEntry(root, selectmode='day', textvariable=toSelect)
cal2.grid(column=3, row=2, sticky=tk.W, padx=5, pady=5)





# check audit log button
checkLog_button = ttk.Button(root, text=" Check Audit Log ",command=checkAuditLog_clicked)
checkLog_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


root.mainloop()