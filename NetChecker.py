#https://www.pythontutorial.net/tkinter/

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Entry
from tkcalendar import DateEntry

from AuditLog import Audit

# root window
root = tk.Tk()
root.geometry("900x900")
root.resizable(True, True)
root.title('NET issue ')

# store email address and password
bid = tk.StringVar()
date = tk.StringVar()
audit = Audit()


def login_clicked():
    """ callback when the login button clicked

    """
    beaconID = bid.get()
    daterange = date.get()
    text = audit.inputs(beaconID, daterange)
    print('login_clicked, NETchecker.py line 25 ',daterange, beaconID)
   # print('text.....',text)
    text2 = audit.CurlyBrackets(text)

    result = audit.StartEvents(text)
    ble_tag = audit.bleTag(text)
    powerIssue = audit.powerIssue(text)
   # print('result.......',result)
    displayMessage = str(result) +'\n'+ str(text2)+' \n'+str(ble_tag)+'\n'+str(powerIssue)

    feedback = ttk.Label(signin, text=displayMessage)
    feedback.pack(ipadx=50, ipady=50)


    '''
    msg = f'You entered email: {bid.get()} and password: {date.get()}'
    showinfo(
        title='Information',
        message=msg
    )
    '''



# Create gui frame
signin = ttk.Frame(root)
signin.pack(ipadx=10, ipady=10)


'''
#calendar  https://www.plus2net.com/python/tkinter-DateEntry.php
sel=tk.StringVar() # declaring string variable
cal=DateEntry(root,selectmode='day',textvariable=sel)
cal.pack()
'''


# Enter beaconID
beaconID = ttk.Label(signin, text="Beacon ID")
beaconID.pack(ipadx=5, ipady=5)
beaconID_entry: Entry = ttk.Entry(signin, textvariable=bid)
beaconID_entry.pack()
beaconID_entry.focus()





# Enter day
day = ttk.Label(signin, text="Day")
day.pack(ipadx=5,ipady=5, expand=True)
day_entry = ttk.Entry(signin, textvariable=date)
day_entry.pack( expand=True)
#label
day_label = ttk.Label(signin, text="Example June 15th, enter 15. "
                                        "The tool will use current month" )
day_label.pack(ipadx=5,ipady=5, expand=True)

# login button
login_button = ttk.Button(signin, text="Check Audit Log", command=login_clicked)
login_button.pack(expand=True, pady=20)




root.mainloop()