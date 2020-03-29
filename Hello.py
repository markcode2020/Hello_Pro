import pandas as pd
import datetime as dt

def main():
    today = dt.datetime.now()
    tomorrow = dt.datetime.now() +dt.timedelta(days =1)
    yesterday = dt.datetime.now() +dt.timedelta(days =-1)
    s = "Yesterday is " + yesterday.strftime("%Y-%m-%d")
    s = s + "\nToday is " + today.strftime("%Y-%m-%d")
    s = s + "\nTomorow is " + tomorrow.strftime("%Y-%m-%d")
    print(s)

if __name__ == '__main__':
    main()
