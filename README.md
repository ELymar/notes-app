# Notes App
## Overview
A note management tool. Creates monthly markdown files when launching the app and opens them in VSCode to edit.

## Usage
### Install
1. run `sh ./init.sh` to install prerequisites
2. Edit config.json with base directory
3. launch `notes.py` with Python3 
    - To view older notes add a -x argument where x is a positive integer indicating how many months back to go. Default is zero. E.g. `python notes.py -5` will go back 5 months from the current month. 



