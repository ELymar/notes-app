#! C:\Python39\python.exe
from datetime import datetime
import os
import sys

# Generate path for current month's notes
basedir = r'C:\dev\notes'
date = datetime.now()
filename = f"notes-{date.strftime('%Y-%m')}.md"
fullpath = os.path.join(basedir, filename)

# Create root directory if doesn't exist
if not os.path.exists(basedir):
  print(f"Creating {basedir}")
  os.mkdir(basedir)
  
# Create this month's log if doesn't exist
if not os.path.exists(fullpath):
  print(f'{fullpath} does not exist, creating...')
  with open(fullpath, 'w') as f:
    pass

# Open a new VSCode window
os.system(f'code -n {fullpath}')
sys.exit() 



