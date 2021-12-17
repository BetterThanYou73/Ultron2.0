import json
import os
from datetime import date
today = date.today()
today = today.strftime('%B %d')

os.system('python operations/is_lib_installed.py')

try:
    with open("details_service.txt",'r+') as file:
        if ("USERNAME" or "PASSWORD" or "from_addr" or "to_addr") not in json.loads(file.read()):
            file1 = open("details_service.txt",'w')
            file1.write("""{
"USERNAME"  : "",
"PASSWORD"  : "",
"from_addr" : "",
"to_addr"   : ""
}
                   """)
            file1.close()


except FileNotFoundError:
    file1 = open("details_service.txt",'w')
    file1.write("""{
"USERNAME"  : "",
"PASSWORD"  : "",
"from_addr" : "",
"to_addr"   : ""
}
                   """)
    file1.close()
    

try:    
    with open("program_list.txt",'r+') as file2:
        if file2.read() == "":
            file2.write("""THIS IS AN EXAMPLE OF ADDING YOUR SELECTED PROGRAMS 

###Please add in the following format###

{
"file_name1" : "File_address(absolute)",                    
"file_name2" : "File_address(absolute)",
"file_name3" : "File_address(absolute)",
.........so on
}

and so on as many programs you want to add do make sure have the name in small.                   
                    """)


except FileNotFoundError:
    file3 = open("program_list.txt",'w')
    file3.write("""THIS IS AN EXAMPLE OF ADDING YOUR SELECTED PROGRAMS 

###Please add in the following format###
{}
"File_name1" : "File_address(absolute)",                    
"File_name2" : "File_address(absolute)",
"File_name3" : "File_address(absolute)",
.........so on
}
and so on as many programs you want to add do make sure to remove the comma after the last program in the list.                   
                    """)
    file3.close()

try:
    with open("log_last_created.txt",'r+') as file:
        pass
except FileNotFoundError:
    file3 = open("log_last_created.txt",'w')
    file3.write(today)
    file3.close()

try:
    with open("operations_list.txt",'r+') as file:
        if file.read() == "":
            file.write("""THIS IS AN EXAMPLE OF ADDING YOUR SELECTED OPERATIONS 

###Please add in the following format###

{
"operation1" : "<name_of_the_file>.py",                    
"operation2" : "<name_of_the_file>.py",
"operation3" : "<name_of_the_file>.py",
.........so on
}

and so on as many operations you want to add.                   
                    """)
except FileNotFoundError:
    file4 = open("operations_list.txt",'w')
    file4.write("""THIS IS AN EXAMPLE OF ADDING YOUR SELECTED OPERATIONS 

###Please add in the following format###

{
"operation1" : "<name_of_the_file>.py",                    
"operation2" : "<name_of_the_file>.py",
"operation3" : "<name_of_the_file>.py",
.........so on
}

and so on as many operations you want to add.                   
                    """)
    file4.close()

try:
    with open("operations_list_help.txt",'r+') as file:
        if file.read() == "":
            file.write("""THIS IS AN EXAMPLE OF ADDING YOUR SELECTED OPERATIONS 

###Please add in the following format###

{
"operation1" : "File_address(Relative)",                    
"operation2" : "File_address(Relative)",
"operation3" : "File_address(Relative)",
.........so on
}

and so on as many operations you want to add.                   
                    """)
except FileNotFoundError:
    file5 = open("operations_list_help.txt",'w')
    file5.write("""THIS IS AN EXAMPLE OF ADDING YOUR SELECTED OPERATIONS 

###Please add in the following format###

{
"operation1" : "File_address(Relative)",                    
"operation2" : "File_address(Relative)",
"operation3" : "File_address(Relative)",
.........so on
}

and so on as many operations you want to add.                   
                    """)
    file5.close()