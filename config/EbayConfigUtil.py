"""
Functionality intentionally not put in a class in order to create a "singleton" type instance
"""
#Module Global Variables
from ConfigParser import SafeConfigParser
import os

"""
FILE VARIABLES
"""
parser = SafeConfigParser()
credentials_section_name = "Ebay User Credentials"
config_file_path = "config/config.ini"




"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CALLED WHENEVER ANY FUNCTION IN THE FILE IS CALLED
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
#Ensure that the config file exists whenever calling any methods in this file
def run():
    if not os.path.isfile(config_file_path):
        createConfigFile()




"""
FILE METHODS
"""
def getUsername():
    parser.read(config_file_path)
    return parser.get(credentials_section_name, "username")



def getPassword():
    parser.read(config_file_path)
    return parser.get(credentials_section_name, "password")



def createConfigFile():
    with open(config_file_path, "w") as f_config:
        """
        Add all config sections to file
        """
        #Ebay User Credentials
        parser.add_section(credentials_section_name)
        username = raw_input("\nEnter Ebay username: ")
        password = raw_input("\nEnter Ebay password: ")
        parser.set(credentials_section_name, "username", username)
        parser.set(credentials_section_name, "password", password)
        console.log("Config file can be viewed or modified at " + config_file_path)
        

        """
        Finally, write all sections and options to file
        """
        parser.write(f_config)








"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CALLED WHENEVER ANY FUNCTION IN THE FILE IS CALLED
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
run()        








def main():
    pass

if __name__ == "__main__":
    main()