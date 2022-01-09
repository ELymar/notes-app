from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
import sys
import json

def load_config():
    # load config file
    if not os.path.exists('./config.json'): 
        print("config.json not found")
        sys.exit(-1)

    # config file relative to running script
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as json_file:
        config = json.load(json_file)
    return config

# how many months back based on command line argument
def get_months_back():
    number = 0
    if len(sys.argv) > 1:
      number = int(sys.argv[1].split('-')[1])
      if number < 1:
        print("Please pass a positive integer for how many months back to get notes for.")
        sys.exit(-1)
    return number

# Get full path depending on months back and config's base dir
def get_full_path_of_notes_file(config, number):
    # Generate path for current month's notes
    basedir = config['baseDir']
    if not basedir:
      basedir = "./"

    if not os.path.exists(basedir):
      print(f"Creating {basedir}")
      os.mkdir(basedir)
      
    date = datetime.now()
    # adjust date to subtract number of months
    date = date - relativedelta(months=number)
    filename = f"notes-{date.strftime('%Y-%m')}.md"
    fullpath = os.path.join(basedir, filename)
    return fullpath

# Create this month's log if doesn't exist
def create_log_file_if_doesnt_exist(number, fullpath):
    if not os.path.exists(fullpath):
      if number != 0:
        print(f"A past log at {fullpath} doesn't exist, exiting.")
        sys.exit(-1)
      print(f'{fullpath} does not exist, creating...')
      with open(fullpath, 'w') as f:
        pass

def main():
  config = load_config()
  number = get_months_back()
  fullpath = get_full_path_of_notes_file(config, number)
  create_log_file_if_doesnt_exist(number, fullpath)
  os.system(f'code -n {fullpath}')

if __name__ == "__main__":
    main()