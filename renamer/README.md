# renamer

This application will rename all files in working directory according to defined rules. 

## About

Rename rules are defined in these two variables:

```
tospace = [ '_', '   ', '  ' ]
toremove = [ 'Official Video', '(HD)', 'Original Version', 'Uncensored', 'Official Music Video', '-edited', '(HQ)', 'Subtitled', '(', ')']
```

* Values in "tospace" list will be changed to a single space.
* Values in "toremove" list will be removed.

Case where two (or more) renamed files would result in same final file name, are handled by appending a number to the end (1..n).
File changes are logged to ".work.log", along with original file name and a timestamp - each value separated with a colon.

Tested Python version, on Debian 8:
```
$ python -V
Python 2.7.9
```

## Example usage


First of all, make sure the correct python command location is specified in renamer.py and make executable:
```
$ which python
/usr/bin/python

$ head -1 renamer.py 
#!/usr/bin/python

$ chmod +x renamer.py
```

Running the application:
```
$ touch "abc(HQ).mp4" "abcd-edited.mp4" "abcd(HD).mp4"
$ ls -la
 abcd-edited.mp4
 abcd(HD).mp4
 abc(HQ).mp4
 renamer.py
 
$ ./renamer.py 
Filename : 'abcd.mp4' Exists!

$ ls -la
 abcd.mp4
 abcd.mp4-1
 abc.mp4
 renamer.py
 .work.log

$ cat .work.log 
2017-02-01T14:55:50;abc(HQ).mp4;abc.mp4
2017-02-01T14:55:50;abcd(HD).mp4;abcd.mp4
2017-02-01T14:55:50;abcd-edited.mp4;abcd.mp4-1
```
