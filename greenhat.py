# Copyright (c) 2015 Angus H. (4148)
# Distributed under the GNU General Public License v3.0 (GPLv3).
'''define utf-8 encoding'''

from datetime import date, timedelta, datetime
from random import randint
from time import sleep
import sys
import subprocess
from argparse import ArgumentParser



def get_date_string(n, startdate):
    '''# returns a date string for the date that is N days before STARTDATE'''
    d = startdate - timedelta(days=n)
    rtn = d.strftime("%a %b %d %X %Y %z -0400")
    return rtn

# main app
def main():
    '''Main function'''
    parser = ArgumentParser(description="Quick hack for making real work happen.")
    parser.add_argument("-dy", "--days", help="Number of days before to generate commits", type=int)
    parser.add_argument("-da", "--date", help="Specify a date(Default: Today)", type=str)

    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    n = args.days
    if args.date:
        startdate = datetime.strptime(str(args.date), "%Y-%m-%d").date()
    else:
        startdate = date.today()
    i = 0
    while i <= n:
        curdate = get_date_string(i, startdate)
        num_commits = randint(1, 10)
        for commit in range(0, num_commits):
            subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +"' > realwork.txt; git add realwork.txt; GIT_AUTHOR_DATE='" + curdate + "' GIT_COMMITTER_DATE='" + curdate + "' git commit -m 'update'; git push;", shell=True)
            sleep(.5)
        i += 1
    subprocess.call("git rm realwork.txt; git commit -m 'delete'; git push;", shell=True)

if __name__ == "__main__":
    main()
