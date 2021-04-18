#opening the files

f=open("input.txt", 'r')
new_file = open("output.txt", 'a')

#reading data from input line by line and storing as a list in a variable
data = f.readlines()

#adding the name of library or file for which you are creating request or response
library_name = "datasource_"

#an empty list to be used later
file_data=[]
 
def format_variable(var_name):
    '''  this method formats the name of each getter and setter '''

    for chars in var_name:
        if chars.isupper():
            var_name = var_name.replace(chars, f"_{chars.lower()}")
    return var_name
 
def setter_getter(none_line):
    ''' this method creates getters and setters for variables'''
    for lines in none_line:
        variable = lines.split('=')[0].strip(' ')
        variable_name = variable.split(':')[0]
        variable_type = variable.split(':')[1].strip(' ')
        formatted_name = format_variable(variable_name)
 
        str_append = f"@property\ndef {library_name}{formatted_name}(self):\n\treturn self.{variable_name}\n"
        str_append2 = f"\n@{library_name}{formatted_name}.setter\ndef {library_name}{formatted_name}(self,{library_name}{formatted_name}:{variable_type}):"
        str_append3 = f"\n\tself.{variable_name}={library_name}{formatted_name}\n\n"
 
        new_file.write(str_append + str_append2 + str_append3)
 
def add_none():
    ''' this method assigns none to each variable '''
    for lines in data:
        lines=lines.strip()
        lines=f"{lines} = None\n"
        file_data.append(lines)
        new_file.write(lines)
    new_file.write("\n\n")
    return file_data
 
# assigning none to each variable
none_lines_data=add_none()
#creating getters and setters
setter_getter(none_lines_data)

#closing files
f.close()
new_file.close()