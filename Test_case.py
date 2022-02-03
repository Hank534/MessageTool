import os

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


