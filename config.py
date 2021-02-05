#import csv
import os.path
from configparser import ConfigParser
from shutil import copyfile

class configuration_of_file:
    def __init__(self):
        print("")    
    
    def data_setting(self):
    
        source=input("enter file : ")
        while( not os.path.exists(source)):
            print("The File does not exists! ")
            source=input("enter proper file : ")

        copyfile(source,'E:/fedex/FEDEX USECASE/11sept/experiment/FINAL_12SEPT/files/file.csv')
             
        configur=ConfigParser()
        configur.read('configuration_file.ini')

        filepath= configur.get('input','fileinput')
        return filepath
"""
     taking file from the user and copying
     the file into working directory 
     
     the file "configuration_file.ini"
     contains the path of the csv file
     where the user entered file is copied
"""