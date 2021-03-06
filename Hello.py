import datetime as dt

def main():
    #some datetime function is tested here
    today = dt.datetime.now()
    tomorrow = dt.datetime.now() +dt.timedelta(days =1)
    yesterday = dt.datetime.now() +dt.timedelta(days =-1)

    #put information together and make a string
    s = "Yesterday is " + yesterday.strftime("%Y-%m-%d")
    s = s + "\nToday is " + today.strftime("%Y-%m-%d")
    s = s + "\nTomorow is " + tomorrow.strftime("%Y-%m-%d")
    print(s)

if __name__ == '__main__':
    main()
