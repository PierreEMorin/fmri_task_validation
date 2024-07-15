#!/usr/bin/env python
#encoding: utf-8

import os
import argparse

def get_argument():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="",
        epilog="""    Validate the content of fmri_task directories (task files not actual fMRI)
    Make sure that fmri_task directories are unziped beforehand.
        """)

    parser.add_argument("filesToCheck", help="Directory with fmri_task files (i.e. 1234567_fmri_task/)")

    return parser
    
#get fileS to check from arguments
parser = get_argument()
args   = parser.parse_args()
directory_content = os.listdir(args.filesToCheck)

#print all files in directory 
#print('\nValidating content of:', args.filesToCheck,)
print('\n',args.filesToCheck,)
#print('\n',args.filesToCheck,)
#for val in directory_content:
    #print(' '.ljust(4),val)

#remove files to ignore from directory_content
filesToIgnore = ['README.txt',
                 '*.pdf']
for file in filesToIgnore:
    if file in directory_content:
        directory_content.remove(file)
        
#check if all files have the proper id
pscid = args.filesToCheck[0:7]
fileIDErrorCount = 0
#print(' '.ljust(4),'Validating participant ID')
for file in directory_content:
    if pscid not in file:
        fileIDErrorCount += 1
        #print(' '.ljust(8),file,' Error: Wrong ID!')
        directory_content.remove(file)

#check for extra number at the begining or end of the PSCID
salt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for extra in salt:
    pscidx = pscid + extra
    xpscid = extra + pscid
    for file in directory_content:
        if pscidx in file:
            fileIDErrorCount += 1
            #print(' '.ljust(8),file,' Error: Wrong ID!', pscidx)
            directory_content.remove(file)
    for file in directory_content:
        if xpscid in file:
            fileIDErrorCount += 1
            #print(' '.ljust(8),file,' Error: Wrong ID!', xpscid)
            directory_content.remove(file)

if fileIDErrorCount == 0:
    print(' '.ljust(8),'All IDs are OK!')
else:
    print(' '.ljust(8),'Error: Wrong ID!')

#check if all necessary files are present
#print(' '.ljust(4),'Validating content')
content = {"Onset-Event-Encoding": 0,
           "Output-Responses-Encoding": 0,
           "Output_Retrieval": 0}
for key in content:
    for file in directory_content:
        if key in file:
            content[key] = 1

if all(value > 0 for value in content.values()):
    print(' '.ljust(8),'Content is valid!')
else:
    print(' '.ljust(8),'Error: Files are missing!')
