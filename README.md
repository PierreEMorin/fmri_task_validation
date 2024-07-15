
# fmri_task_validator
Code originaly provided by Pierre-Emmanuel Morin  
Script used to validate de content of e-prime directories obtained during fMRI session (CIMA-Q).  This code verifies that all files are properly identified (CIMA-Q naming convention) and that files required for further analysis are present.

## Use
You should have one, unzipped, directory per participant containing the files created during one fMRI session for CIMA-Q  
The directories are from /loris/media_uploads and are expected to be named according to the following rule:  
&emsp;&emsp;&emsp;PSCID_VisitLabel_IRMF_task_suffix (example: 1234567_V01_IRMf_task)  
  
The validate the content by running the scipt:  
&emsp;&emsp;&emsp; python3 fmri_task_validator.py 1234567_V03_IRMf_task  
or (to send results to a file)  
&emsp;&emsp;&emsp; python3 fmri_task_validator.py 1234567_V01_IRMf_task >> validation.txt  
&emsp;&emsp;&emsp; python3 fmri_task_validator.py 2345678_V01_IRMf_task  >> validation.txt  

***Output example:***  
&emsp;9889496_V03_IRMf_task  
&emsp;&emsp;&emsp;PRATIQUE-9889496-V03.edat2  
&emsp;&emsp;&emsp;PRATIQUE-9889496-V03.txt   
&emsp;&emsp;&emsp;Output_Retrieval_9889496_V03.txt  
&emsp;&emsp;&emsp;Retrieval-9889496-V03.edat2  
&emsp;&emsp;&emsp;Encoding-scan_NewPad-9889496-V03.txt  
&emsp;&emsp;&emsp;Output-Responses-Encoding_9889496_847696_V03A.txt  
&emsp;&emsp;&emsp;Onset-Event-Encoding_9889496_847696_V03A.txt  
&emsp;&emsp;&emsp;Encoding-scan_NewPad-9889496-V03.edat2  
&emsp;&emsp;&emsp;Retrieval-9889496-V03.txt  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;All IDs are OK!  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Content is valid!  

## Ignored files
An array contains a list of files to ignore.  
Current list includes:  
&emsp;&emsp;&emsp;README.txt  
&emsp;&emsp;&emsp;*.pdf (debrifing files are sometimes included)  

## Required files
The following files must be present:  
&emsp;&emsp;&emsp;Onset-Event-Encoding*  
&emsp;&emsp;&emsp;Output-Responses-Encoding*  
&emsp;&emsp;&emsp;Output_Retrieval*  

## Future development
Add an alternate printing mode (single vs multiple) 
