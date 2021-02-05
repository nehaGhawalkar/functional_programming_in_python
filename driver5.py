#!/usr/bin/env
import filters1 
import calls1    
import utility
import config
import input_file




inp=input_file.user_file()
con=config.configuration_of_file()

f1=filters1.take_filter_input()
c1=calls1.call_nested_filter()  
"""
creating object for importing all the functions of module 
@inp  taking file from the user
@f1   taking different filters from the user
@c1   calling functions to display the output according to user entry
"""
file_from_user=con.data_setting()
people=(inp.take_file_from_user(file_from_user))


def if_general_filter():
    check=f1.validate_yes_no_for_username()
    """
    if user wants to view details on the basis of
    username ,the @check will accept yes or no.
    
    if he enters yes, he will be prompted to give
    particular Username
    
    @f1.user_input will prompt the user to enter
    further bifurcation of filters, i.e whether he
    wants item wise, progress wise details 
    """
        
    if(check.lower()=='yes'):        
        user,first_filter,second_filter=f1.user_input(people) 
        if(first_filter=='1'):
                c1.call_item(people,user,second_filter)
        if(first_filter=='2'):
                c1.call_category(people,user,second_filter)
        if(first_filter=='3'):
                c1.call_source(people,user,second_filter)
        if(first_filter=='4'):
                c1.call_destination(people,user,second_filter)
        if(first_filter=='5'):
                c1.call_progress(people,user,second_filter)
        if(first_filter=='6'):
                c1.call_location_status(people,user,second_filter)
        if(first_filter=='7'):
                c1.call_username_expected_dates(people,user,utility)
        #call_username_expected_dates
        if(first_filter=='8'):
                c1.call_username_all_details(people,user,second_filter) 
            
        
    else:
        """
        if @check is no this block will get executed,
        wherein a generic input is asked from the user
        he can view all details item wise, destination wise
        inspite of not entering a particular username
        """
        first_filter,second_filter=f1.input_general_filter(people)
        if(first_filter=='1'):
                c1.call_item_no_username(people,second_filter)    
        if(first_filter=='2'):
                c1.call_category_no_username(people,second_filter)
        if(first_filter=='3'):
                c1.call_source_no_username(people,second_filter)
        if(first_filter=='4'):
                c1.call_destination_no_username(people,second_filter)    
        if(first_filter=='5'):
                c1.call_progress_no_username(people,second_filter)    
        if(first_filter=='6'):
                c1.call_location_status_no_username(people,second_filter)
        if(first_filter=='7'):
                c1.call_expected_dates(people,utility)
                
    
if_general_filter()
