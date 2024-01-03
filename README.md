# How to use PFUZZER

Environment : python

1. Download the folder.
2. In the CMD, enter the command.

--------------------------------------------------------

# Command Options
**Required Options**
  - `python PFUZZER.py` : Specifies the URL for purging, where the string "PFUZZ" is replaced by a purging value.
  - `-u [TargetUrl]` : Enter the target url for fuzzing.
  - `-type [num | txtFile]` : Select the type you want to fuzzy.

**If the type is a number**
  - `-start [value]` : Start number for num fuzzing.
  - `-step [value]` : Step for num fuzzing.
  - `-end [value]` : End number for num fuzzing.

**Examples of Commands**
  - `python PFUZZER.py -u http://example.com/PFUZZ -type num -start 1 -step 1 -end 100`
  - `python PFUZZER.py -u http://example.com/PFUZZ -type words.txt`
    
