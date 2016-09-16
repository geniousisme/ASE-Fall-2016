# HW1 - Practice with Static Analysis
### Chia-Hao Hsu (ch3141)

In this HW, I used a course project as the test target to run the static analysis. </br>
This project is the last project for CSEE 4119. I implemented the Distributed Bellman-Ford algorithm </br>
and also run some test cases. I ran two analyzers: pychecker & prospector. 

From the result of pychecker, </br>
I surprisingly find out that there are several module not existed in my local system anymore.</br>
For example, there are several ssl modules alreadu missing in the local system.</br>
Also, some locale module I used are missing too. </br>
Last but not the least, I didn't have a good habit to clean up the attribtes or variables in the code I didn't use anymore.</br>
For instance, in beclient.py I didn't use kwargs anymore but I didn't clean it up.

From the result of prospector, there are more same cases found in the program. For example, </br>
I imported several unused modules like time & datetime but I have never used them again. </br>
In prospector, I found that it will also check my complexity and give the corresponding warning.</br>
This is the part surprising me, since it is the part I didn't notice before when I developed this kind of school project.</br>
According to testing results, I will pay more attention on them in the future.

## Appendix 1: Result of pychecker
    Processing module Timer (Timer.py)...
    Processing module Utils (Utils.py)...
    warning: couldn't find real module for class <class 'ssl.SSLEOFError'> (module name: ssl)
    warning: couldn't find real module for class <class 'ssl.SSLError'> (module name: ssl)
    warning: couldn't find real module for class <class 'ssl.SSLSyscallError'> (module name: ssl)
    warning: couldn't find real module for class <class 'ssl.SSLWantReadError'> (module name: ssl)
    warning: couldn't find real module for class <class 'ssl.SSLWantWriteError'> (module name: ssl)
    warning: couldn't find real module for class <class 'ssl.SSLZeroReturnError'> (module name: ssl)
    warning: couldn't find real module for class <class 'ssl.SSLError'> (module name: ssl)
    Processing module bfclient (bfclient.py)...
    warning: couldn't find real module for class <class 'locale.Error'> (module name: locale)
    
    Warnings...
    
    [system path]/threading.py:66: (format) shadows builtin
    [system path]/threading.py:74: (format) shadows builtin
    
    Utils.py:50: No module attribute (err) found
    
    bfclient.py:57: Parameter (kwargs) not used
    bfclient.py:68: Parameter (kwargs) not used
    bfclient.py:242: (SystemExit) shadows builtin
    bfclient.py:242: Local variable (SystemExit) not used
## Appendix 2: Result of prospector
    Messages
    ========
    
    bfclient.py
      Line: 7
        pyflakes: F401 / 'time' imported but unused (col 1)
      Line: 10
        pyflakes: F401 / 'datetime.datetime' imported but unused (col 1)
      Line: 242
        pyflakes: F841 / local variable 'SystemExit' is assigned to but never used (col 39)
    
    bfclient_copy.py
      Line: 20
        pyflakes: F401 / 'time' imported but unused (col 1)
      Line: 24
        pyflakes: F401 / 'datetime.datetime' imported but unused (col 1)
    
    reference/michellevalente-CSEEW4119/PA1/protocol.py
      Line: 2
        pyflakes: F401 / 'copy' imported but unused (col 1)
    
    reference/michellevalente-CSEEW4119/PA1/server.py
      Line: 174
        mccabe: MC0001 / messageCenter is too complex (30)
    
    reference/michellevalente-CSEEW4119/PA2/bfclient.py
      Line: 327
        pyflakes: F841 / local variable 'distanceVector' is assigned to but never used (col 2)
    
    reference/morrisyoung-CSEE4119-PA2/bfclient.py
      Line: 10
        pyflakes: F811 / redefinition of unused 'time' from line 8 (col 1)
      Line: 221
        mccabe: MC0001 / listener is too complex (89)
      Line: 891
        mccabe: MC0001 / sender is too complex (27)
      Line: 1200
        mccabe: MC0001 / getfile is too complex (34)
      Line: 1496
        mccabe: MC0001 / If 1496 is too complex (40)
    
    reference/morrisyoung-CSEE4119-PA2/set.py
      Line: 3
        pyflakes: F401 / 'sys' imported but unused (col 1)
    
    
    
    Check Information
    =================
             Started: 2016-09-15 22:10:15.154215
            Finished: 2016-09-15 22:10:23.199089
          Time Taken: 8.04 seconds
           Formatter: grouped
            Profiles: default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings
          Strictness: None
      Libraries Used:
           Tools Run: dodgy, mccabe, pep8, profile-validator, pyflakes, pylint
      Messages Found: 14
