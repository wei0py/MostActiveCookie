from utils import *

class CookieProcessor:
    def __init__(self):
        self.cookie_dict = {}

    def read_data(self, log_file):
        self.cookie_dict = read_csv_log(log_file)
    
    '''
    Find the most active cookie
    date: the date given by user
    '''
    def find_most_active_cookie(self, date):
        if valid_date(date):
            if date in self.cookie_dict:
                cookie_max = self.cookie_dict[date]
                result = self.find_max_items(cookie_max)
                return result
            else:
                return []
        else:
            raise ValueError("Wrong date input")

    def find_max_items(self, cookie_max):
        max_value = max(cookie_max.values())
        result = [key for key,val in cookie_max.items() if val == max_value]
        return result


