import pandas as pd
import endecrypt as edc
from io import StringIO
import time

path = __file__.replace("\\scripts\\csvmanip.py", "")
t = time.localtime()
current_time = time.strftime("%Y/%m/%d %H:%M:%S", t)

def convertcsv():
    pwtext = edc.decrypt()
    iodata = StringIO(pwtext)
    pwdata = pd.read_csv(iodata)
    return pwdata

def insert(pwdata: pd.DataFrame, newrow: dict):
    pwdata.loc[len(pwdata)] = newrow
    return pwdata
    

if __name__ == "__main__":
    test = convertcsv()
    test2 = {'~': current_time, "Service":"TestService", 'Username': "test1", 'Password': "test2", "SecurityFactor":53,"HackCount":15}
    newpd = insert(test, test2)
    print(newpd)