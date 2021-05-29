import os.path, time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import config

monthly = "/var/www/internal/data/monthly"

def sendingmail(sub, tx):
	msg = MIMEText(tx)
	msg['Subject'] = sub
	msg['From'] = 'internalchecker@lsb.pl'
	msg['To'] = 'andrzej@lsb.com.pl'
	frm = "internalchecker@lsb.pl"
	t = "andrzej@lsb.com.pl"
	server = smtplib.SMTP('mx10.lsb.com.pl', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(config.username, config.password)
	text = msg.as_string()
	server.sendmail(frm, t, text)

def datechecker(path, what):
    if what == "monthly":
        for filename in os.listdir(path):
            if filename.endswith(".SOS"): 
                print(os.path.join(path, filename))
                file = os.path.join(path, filename)
                file_timestamp = os.path.getctime(file)
                file_month = datetime.fromtimestamp(file_timestamp).strftime('%m')
                file_month_int = int(file_month)
                print(int(file_month_int))
                if (dt_month_int == file_month_int):
                    sendingmail("SOS MONTHLY PLIK AKTUALNY - %s" %file, "Plik jest aktualny - %s" %file)
                    continue
                else:
                    sendingmail("!!!WARNING!!! - %s" %file, "NIE AKTUALNY PLIK %s" %file)
                    continue
                continue
            else:
                continue
"""
    if what == "weekly":
        for filename in os.listdir(path):
            if filename.endswith(".CSV") or filename.endswith(".TXT"):
                print(os.path.join(path, filename))
                file = os.path.join(path, filename)
                file_timestamp = os.path.getctime(file)
                file_week = datetime.fromtimestamp(file_timestamp).strftime('%m')
                file_week_int = int(file_week)
                print(int(file_week_int))
                if (dt_week_int == file_week_int):
                    print("good")
                    #sendingmail("OK - %s" %file, "Plik jest aktualny - %s" %file)
                    continue
                else:
                    #sendingmail("!!!WARNING!!! - %s" %file, "NIE AKTUALNY PLIK %s" %file)
                    continue
                continue
"""

dt = datetime.today()
dt_month = dt.month
dt_month_int = int(dt_month)

datechecker(monthly, "monthly")
