import pandas as pd
import scripts.endecrypt as edc
from io import StringIO
import time

path = __file__.replace("\\scripts\\csvmanip.py", "")
t = time.localtime()
current_time = time.strftime("%Y/%m/%d %H:%M:%S", t)

def generate():
    fp = open(f"{path}\\files\\passwords.csv", "w")
    headerstr = "~,Service,Username,Password,SecurityFactor,HackCount"
    fp.write(headerstr)
    fp.close()

def convertcsv():
    pwtext = edc.decrypt()
    iodata = StringIO(pwtext)
    pwdata = pd.read_csv(iodata)
    return pwdata

def insert(pwdata: pd.DataFrame, newrow: dict):
    pwdata.loc[len(pwdata)] = newrow
    return pwdata

def csvinsert(pwdata: pd.DataFrame):
    pwdata.to_csv(f"{path}\\files\\passwords.csv", index=False)
    edc.encrypt()
    

if __name__ == "__main__":
    test = convertcsv()
    print(test)