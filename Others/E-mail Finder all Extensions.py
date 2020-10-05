import re

#String to determine if the file name is valid
file_pattern = r"([\w\s\_-]+)\.txt"

alt_file_pattern = r"([\w\s\_-]+)\.([\w]+)"

#String to determine how to identify an e-mail address
email_pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

#Variable to check the file name validation
name_valid = False

#Welcome text
welcome_str = """
\t\t***************************************
\t\t*                                     *
\t\t*   THIS PROGRAM IDENTIFIES E-MAILS   *
\t\t*            IN A DOCUMENT            *
\t\t*                                     *
\t\t***************************************
\t\t*      NOTE: Actually this works      *
\t\t*       with all file extensions      *
\t\t***************************************
"""

print(welcome_str)

#Function to validate the file name
def validate_name():
    file = input('Write the file name to inspect: ')
    if re.match(alt_file_pattern, file):
        print('\n\tFile name valid!\n')
        try:
            global text
            text = open(file)
            text = str(text.read())
            print('\tFile opened successfully!\n')
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
            return True
        except:
            print('\t¡¡ERROR!!\n\tFile not found\n')
            return False
    else:
        print('\n\tFile name or extension invalid!\n\tRemember to include the extension\n')
        return False

#Asking for the file name to the user and then validate it
while name_valid == False:
    name_valid = validate_name()

match = re.findall(email_pattern, text)

if match:
    print('These e-mails were found in the document:\n')
    for word in match:
        print('\t'+word[0]+'@'+word[1]+word[2])
else:
    print('No e-mails were found in the document')
    
input('\n\n\nPress ENTER to exit')
