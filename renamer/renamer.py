#!/usr/bin/python
import os
import datetime

count = 0
suffix = ""

tospace = [ '_', '   ', '  ' ]
toremove = [ 'Official Video', '(HD)', 'Original Version', 'Uncensored', 'Official Music Video', '-edited', '(HQ)', 'Subtitled', '(', ')']

filenames = os.listdir('.')

# function checking if filename already exists
def fexists(filename):
    if os.path.isfile(filename):
        return True
    else:
        return None

for filename in filenames:
    tmp_filename = filename

    # make sure underscore and double spaces become single spaces            
    for element in tospace:
        if element in tmp_filename:
            tmp_filename = tmp_filename.replace(element, " ")

    # transform double dash to single dash
    if "--" in tmp_filename:
        tmp_filename = tmp_filename.replace("--", "-")

    # remove specific words/letters
    for element in toremove:
        if element in tmp_filename:
            tmp_filename = tmp_filename.replace(element, "")    

    # does the file qualify for renaming ?
    if tmp_filename != filename:
        while True:
            # check if filename already exists
            if fexists(tmp_filename+suffix):
                count = count + 1
                print "Filename : '"+tmp_filename+suffix+"' Exists!"
                suffix = "-"+str(count) # retry with a suffix
            else:
                break

        # finally, rename the file
        now = datetime.datetime.now()
        os.rename(filename, tmp_filename+suffix)

        # append rename info to log file
        with open(".work.log", "a") as logfile:
            logfile.write(now.strftime("%Y-%m-%dT%H:%M:%S")+";"+str(filename)+";"+str(tmp_filename+suffix)+"\n")
