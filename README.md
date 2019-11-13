# JSON-Merge-using-python
The main goal is to Merge n-json files into a single file or multiple size of specified size.

#### User Input:
    1.Folder Path
    2. Input Files Base Name
    3. Output Files Base Name
    4. Max File Size
   
   
#### Output form
    1. No. of Input Files
    2. No. of Output Files
    
    
####Functional Description:
     1. File Path(): Used to return the path of File.
     2. MergeDict(): Merging of key-value pairs based on different datatypes.
     3. MergeJSON(): This Function is used to actually merge the JSON Files.
     

#### TestCases
    1. Testcase1:
                1. Inputs:
                      1. Input1: {  "strikers": [
                                                  { "name": "Alexis Sanchez", "club": "Manchester United" },
                                                  { "name": "Robin van Persie", "club": "Feyenoord" }
                                              ] 
                                 }
                      2. Input2: {  "strikers": [
                                                  { "name": "Nicolas Pepe", "club": "Arsenal" }
                                                  ] 
                                 }
                      
                      3. Input3: {"strikers": [
                                                  { "name": "Gonzalo Higuain", "club": "Napoli" },
                                                  { "name": "Sunil Chettri", "club": "Bengaluru FC" }
                                              ]
                                 }
                       4. Max File Size: 1000
                       
                  2. Output:
                                 {
                                    "strikers": [
                                                    {
                                                    "name": "Alexis Sanchez",
                                                    "club": "Manchester United"
                                                    },
                                                    {
                                                    "name": "Robin van Persie",
                                                    "club": "Feyenoord"
                                                    },
                                                    {
                                                    "name": "Nicolas Pepe",
                                                    "club": "Arsenal"
                                                    },
                                                    {
                                                    "name": "Gonzalo Higuain",
                                                    "club": "Napoli"
                                                    },
                                                    {
                                                    "name": "Sunil Chettri",
                                                    "club": "Bengaluru FC"
                                                    }
                                    ]
                                  }

#### Language Used:
        1. Python
 
     
#### Execution Commands
    1. cd to the directory where python file is
    2. Input the file path.
    3. Base Name of the file.
    4. Output name of file
    5. Size of output file in bytes.
