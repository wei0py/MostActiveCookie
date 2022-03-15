from cookie_processor import CookieProcessor
from utils import *
import sys

def runner():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("log_file")
    parser.add_argument("--date",'-d', type=str)
    args = parser.parse_args(sys.argv[1:])
    params = vars(args)
    Processor = CookieProcessor()
    Processor.read_data(params["log_file"])
    most_active_cookies = Processor.find_most_active_cookie(params["date"])
    for cookie in most_active_cookies:
        print(cookie)

if __name__ == "__main__":
    runner()

    
