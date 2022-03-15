import datetime
import csv
import os

def valid_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        if date != datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
            return False
        else:
            return True
    except:
        return False

def read_csv_log(log_file):
    try:
        f = open(log_file)
        data = csv.reader(f)
    except OSError:
        print('cannot open', log_file)
    else:
        dict_log = {}
        header = next(data)
        count = 0
        for line in data:
            count += 1
            try:
                cookie, timestamp = line[0], line[1]
                date, time = timestamp.split("T")
                if not valid_date(date):
                    raise OSError(log_file+" has wrong date format at line "+str(count))
                elif date in dict_log:
                    if cookie in dict_log[date]:
                        dict_log[date][cookie] += 1
                    else:
                        dict_log[date][cookie] = 1

                else:
                    dict_log[date] = {cookie:1}
            except:
                print(log_file+" has wrong format at line "+str(count))
        return dict_log

