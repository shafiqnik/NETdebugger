import re
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Audit:

    x = int

    def __init__(self):
        print('this is from the main audit class')
        self.url = 'http://gam-ra-production.contigo.lan:8013/developer/misc/audit_log/gprs_extract.php'
        self.page = urlopen(self.url)
        self.htmlsource = self.page.read()

    def status(self,state):
        self.state = state
        print('state of the VC is ....case',state)
        return state


    def inputs(self, bid, tday):

        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        print('current month is .......', currentYear)
        self.bid = bid
        self.tday = tday
        fday = int(tday)
        print('fday......is ', fday)
        print('inputs data..', bid, fday, tday)
        payload = {'bid': bid,
                   'esn': '',
                   'serial_no': '',
                   'fyr': str(currentYear),
                   'fmth': str(currentMonth),
                   'fday': fday,
                   'fhr': '00',
                   'fmin': '00',
                   'tyr': str(currentYear),
                   'tmth': str(currentMonth),
                   'tday': tday,
                   'thr': '23',
                   'tmin': '59'
                   }
        r = requests.post(self.url, data=payload)
        audit = r.text
        return audit

    def bleTag(self, audit):

        bleTag = audit.count('ble_tag')
        if bleTag != 0:
            message = ''
            print(message)
        else:
            message = 'Audit log does not have ble_tag messages'
            print(message)

        return message

    def CurlyBrackets(self, audit):
        self.audit = audit

        number_of_curly_bracket = audit.count('} }')
        print('number of curly brackets..........', number_of_curly_bracket)
        if number_of_curly_bracket > 1:
            message = 'The wirings could have some issues, there are', number_of_curly_bracket, ' curly brackets ~} } }'
            print(message)
        elif number_of_curly_bracket == 0:
            message = 'No symptoms of loose connection'
            print(message)
        else:
            message = 'everything seems to be working with this test...'
            print(message)

        return message


    def powerIssue(self, audit):

        self.audit = audit
        NumberOfpower_ups = audit.count('power_up')
        NumberOfpower_off = audit.count('power_off')
        if (NumberOfpower_ups or NumberOfpower_off > 1):
            message = 'multiple Power_up or Power_off events'
        else:
            message =''

        return message



    def StartEvents(self, audit):
        self.audit = audit

        soup = BeautifulSoup(audit, "html.parser")
        results = soup.findAll(class_="form_input")

        # print(results)

        ESN = results[1][
            'value']  # getting the value of ESN from <input class="form_input" maxlength="30" name="esn" size="35" type="text" value="354721091332018"/>

        ign_on = ESN + ',3,'
        ignOn = soup.get_text(ign_on)
        # print('the ign On type is ....',ignOn)
        # IgnOnCount = soup.findAll(ignOn)
        # print('number of ign On is ',IgnOnCount)

        # print('get text', soup.get_text(ign_on))

        Ign_On_Number = int(audit.count(ign_on))
        print('number of ign ON , ', Ign_On_Number)
        Number_of_VC_Starts = int(audit.count('~}-}*START}-}*'))
        print('number of START events  line 70  ', Number_of_VC_Starts)
        case1 = Number_of_VC_Starts > Ign_On_Number
        case2 = Number_of_VC_Starts < 1 & Ign_On_Number >1
        case3 = Number_of_VC_Starts and Ign_On_Number ==0
        case4 = Number_of_VC_Starts >= 1 and Ign_On_Number <0
        case5 = Number_of_VC_Starts ==0 and Ign_On_Number > 0
        case6 = Number_of_VC_Starts !=0 and Ign_On_Number !=0

        if case1:

            message = 'VC generated ', Number_of_VC_Starts, 'START' \
                       ' events. It should be ', Ign_On_Number, ', same as # of Ign On events. Please check wirings'
            print('case 1 ', message)
            x = 0
            self.status(x)  #value of x is used to calculate score number to determine if VC has issue
        elif case2:
            message = 'VC has not generated START event, Vehicle was used. Check VC'
            print('case 2 ', message)
            x = 0
            self.status(x)
        elif case3:
            message = 'No ign On or VC Start Events'
            print('case 3 ', message)
            x = 0
            self.status(x)
        elif case4:
            message = "Vehicle Collector has generated START events without Ign On, Wiring has issue "
            print('case 4 ', message)
            x= 0
            self.status(x)
        elif case5:
            message = 'VC has not generated any Start event after ignition On. VC or wiring has problem'
            x=0
        elif case6:
            message = 'Start and Ign On events are same, VC is OK'
            x=0
            self.status(x)
        else:
            message = "Not enough data, there are ", Number_of_VC_Starts, "Start events" \
                                                                               " and ", Ign_On_Number, "Ign events"
            x = 1
            self.status(x)

        return message

# a = Audit()
# a.inputs(123,11,22)