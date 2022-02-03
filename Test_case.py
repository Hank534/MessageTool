import os
"""
This is a test case that will check for a file 
that was created by a client after making a 
connection to the socket.

The test is considered Passed if 1 is retunred.
If NONE is retunred the test is a fail.  

"""
#TODO build in pytest logic to assert if the test passed or failed
#TODO Make the script write a Test Report indicating Pass OR fail.  
expected_data = ['C:/Users/J91307/Desktop/Projects/.ipynb_checkpoints/MessageTool/Report.txt']
file_result = "Report.txt"


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return 1
        
            

print('If file was found, the system will report 1, if NO file the data will output as NONE')
print('='*80)
print(find(file_result,"C:/Users/J91307/Desktop/Projects/.ipynb_checkpoints/MessageTool"))
print('='*80)


