import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Entry

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


# Sign in frame
signin = ttk.Frame(root)
signin.pack(ipadx=10, ipady=10)


# email
email_label = ttk.Label(signin, text="Beacon ID")
email_label.pack(ipadx=5, ipady=5)

email_entry: Entry = ttk.Entry(signin, textvariable=bid)
email_entry.pack()
email_entry.focus()




# password
password_label = ttk.Label(signin, text="Day")
password_label.pack(ipadx=5,ipady=5, expand=True)


password_entry = ttk.Entry(signin, textvariable=date)
password_entry.pack( expand=True)

# password
password_label = ttk.Label(signin, text="Example June 15th, enter 15. "
                                        "The tool will use current month" )
password_label.pack(ipadx=5,ipady=5, expand=True)
# login button
login_button = ttk.Button(signin, text="Check Audit Log", command=login_clicked)
login_button.pack(expand=True, pady=20)




root.mainloop()