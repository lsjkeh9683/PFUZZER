# How to use PFUZZER

Environment : python

1. Download the folder.
2. In the CMD, enter the command.

--------------------------------------------------------

# Command Options
**Required Options**
  - `python PFUZZER.py` : Run a script in command line
  - `-u [TargetUrl]` : Enter the target url for fuzzing.
  - `-type [num | txtFile]` : Select the type you want to fuzzy.

**If the type is a number**
  - `-start [value]` : Enter a number to start with.

**Examples of Commands**
  - `PortScanner.exe -targetIp 127.0.0.1 -port 1 5000 -save check.txt`
    
