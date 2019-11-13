import os
import json

def FilePath(file_index,file_type = 'input'):
    
    if file_type == 'input':
        file_name = InputFileBaseName
    else:
        file_name = OutputFileBaseName
        
    file_name += str(file_index) + '.json'
    file_path = os.path.join(FolderPath,file_name)
    return file_path

def MergeDict(data1,data2):
    for key,val in data1.items():
        if key in data2:
            if type(val) == list:
                data2[key].extend(val)
            elif type(val) == dict:
                MergeJSON(val,data2[key])
            else:
                data2[key] = val
        else:
            data2[key] = val


def MergeJSON(): 
    
    input_index = 1
    output_index = 1
    temp_path = os.path.join(FolderPath,'temp')
    merged_data = {}


    while(os.path.exists(FilePath(input_index))):

        with open(FilePath(input_index),'r') as input_file:
            new_data = json.load(input_file)

        MergeDict(new_data,merged_data)

        with open(temp_path,'w') as temp:
            json.dump(merged_data,temp,ensure_ascii=False,indent=0)

        if os.stat(temp_path).st_size > MaxFileSize:
            output_index += 1
            merged_data = new_data

        with open(FilePath(output_index,'output'),'w') as output_file:
            json.dump(merged_data,output_file,ensure_ascii=False,indent=0)

        input_index += 1

    if os.path.exists(temp_path):
        os.remove(temp_path)
    
    if input_index == 1:
        return 0,0
    return input_index-1,output_index
    
    
        
FolderPath = input('Folder Path: ')
InputFileBaseName = input('Input File Base Name: ')
OutputFileBaseName = input('Output File Base Name: ')
MaxFileSize = int(input('MaxFileSize: '))

input_number, output_number = MergeJSON()
print('No. of Input Files : {}'.format(input_number))
print('No. of Output Files : {}'.format(output_number))