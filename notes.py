#! C:\Python39\python.exe
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
import sys

number = 0
# read command line argument and get the integer after the '-'
if len(sys.argv) > 1:
  number = int(sys.argv[1].split('-')[1])
  if number < 1:
    print("Please pass a positive integer for how many months back to get notes for.")
    sys.exit(-1)
    
# Generate path for current month's notes
basedir = r'C:\dev\notes'
date = datetime.now()
# adjust date to subtract number of months
date = date - relativedelta(months=number)
filename = f"notes-{date.strftime('%Y-%m')}.md"
fullpath = os.path.join(basedir, filename)

# Create root directory if doesn't exist
if not os.path.exists(basedir):
  print(f"Creating {basedir}")
  os.mkdir(basedir)
  
# Create this month's log if doesn't exist
if not os.path.exists(fullpath):
  if number != 0:
    print(f"A past log for {date.strftime('%Y-%m')} doesn't exist, exiting.")
    sys.exit(-1)
  print(f'{fullpath} does not exist, creating...')
  with open(fullpath, 'w') as f:
    pass

# Open a new VSCode window
os.system(f'code -n {fullpath}')
sys.exit() 



