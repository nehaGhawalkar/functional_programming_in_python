class take_filter_input:
    def __init__(self):
        print("")
    
    def input_general_filter(self,people):
        """
        @input_general_filter a general filter  to show
        details without entering the username        
        """
        
        first_filter=input(" enter a:  1- ITEM, 2-CATEGORY,3-SOURCE,4-DESTINATION,5-PROGRESS,6-LOCATION STATUS ,7-expected date:  ")
        while(first_filter not  in ('1','2','3','4','5','6','7')):
            print("Please enter valid input ")
            first_filter=input(" a:1- ITEM, 2-CATEGORY,3-SOURCE,4-DESTINATION,5-PROGRESS,6-LOCATION STATUS 7-expected date:  ")
        
        if(first_filter=='1'):
            
            unique_list=[]
            for key, value in people.items():
                    """
                    @unique_list creating a list of unique items
                    so for the user to understand the available options he has
                    """
                    if(people[key]['item'] not in unique_list):
                        unique_list.append(people[key]['item'])
            print(("list of ITEMs :{} ".format(unique_list)))
                    
            second_filter=input('enter from above list : ')
            """
            @second_filter  a check to validate the user input
            whether his entered value is present in
            the printed list or not,he has to enter 
            correct value to proceed further
            """
            while(second_filter.lower() not in unique_list):
                 second_filter=input("Please give proper input ! : ")
                        
            return first_filter,second_filter
            
        if(first_filter=='2'):
            unique_list=[]
            for key, value in people.items():
                
                    if(people[key]['item type'] not in unique_list):
                        unique_list.append(people[key]['item type'])
            print(("list of category :{} ".format(unique_list)))
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return  first_filter,second_filter
            
        
        if(first_filter=='3'):
            unique_list=[]
            for key, value in people.items():
               
                    if(people[key]['source'].strip() not in unique_list): 
                        unique_list.append(people[key]['source'])
            print(("list of sources :{} ".format(unique_list)))
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return  first_filter,second_filter
        
        if(first_filter=='4'):
            unique_list=[]
            for key, value in people.items():
                
                    if(people[key]['destination'].strip() not in unique_list):  
                        unique_list.append(people[key]['destination'])
            print(("list of destinations :{} ".format(unique_list)))
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return  first_filter,second_filter
        
        if(first_filter=='5'):
            unique_list=[]
            for key, value in people.items():
                #if(people[key]['username']==user.upper()):
                    if(people[key]['progress'].strip() not in unique_list):  
                        unique_list.append(people[key]['progress'])
            print(("list of progress :{} ".format(unique_list))) 
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return  first_filter,second_filter
        
        if(first_filter=='6'):
            unique_list=[]
            for key, value in people.items():
                
                    if(people[key]['location status'].strip() not in unique_list):  #strip is used to eliminate  spaces between strings like "pune  "
                        unique_list.append(people[key]['location status'])
            print(("list of location status :{} ".format(unique_list))) # printing categories available for a particular username
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return  first_filter,second_filter
        
        if(first_filter=='7'):
            first_filter='7'
            second_filter='0'
            #print("hello")
            return first_filter,second_filter
            
    
        
    def user_input(self,people):   
        """
        @user_input user specific function
        will have to enter a specific username
        to get details on user level
        """
        
        user=input("enter user name :")
        """
        @user  username validation
        """
        while(user.upper() not in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','Z')):
            user=input("enter proper username please  :")
            
        first_filter=input(" enter a:  1- ITEM, 2-CATEGORY,3-SOURCE,4-DESTINATION,5-PROGRESS,6-LOCATION STATUS,7-EXPECTED DATE,8 - NO FILTER :  ")
        while(first_filter not  in ('1','2','3','4','5','6','7','8')):
            print("Please enter valid input ")
            first_filter=input(" a:1- ITEM, 2-CATEGORY,3-SOURCE,4-DESTINATION,5-PROGRESS,6-LOCATION STATUS,7-EXPECTED DATE,8 - NO FILTER :   ")
        
        if(first_filter=='1'):
            unique_list=[]
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['item'] not in unique_list):
                        unique_list.append(people[key]['item'])
            print(("list of ITEMs :{} ".format(unique_list)))
                    
            second_filter=input('enter from above list : ')
            while(second_filter.lower() not in unique_list):
                 second_filter=input("Please give proper input ! : ")
                        
            return user,first_filter,second_filter
            
        if(first_filter=='2'):
            unique_list=[]
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['item type'] not in unique_list):
                        unique_list.append(people[key]['item type'])
            print(("list of category :{} ".format(unique_list))) 
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return user,first_filter,second_filter
            
        
        if(first_filter=='3'):
            unique_list=[]
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['source'].strip() not in unique_list):  
                        unique_list.append(people[key]['source'])
            print(("list of sources :{} ".format(unique_list))) 
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return user,first_filter,second_filter
        
        if(first_filter=='4'):
            unique_list=[]
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['destination'].strip() not in unique_list):  
                        unique_list.append(people[key]['destination'])
            print(("list of destinations :{} ".format(unique_list))) 
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return user,first_filter,second_filter
        
        if(first_filter=='5'):
            unique_list=[]
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['progress'].strip() not in unique_list):  
                        unique_list.append(people[key]['progress'])
            print(("list of progress :{} ".format(unique_list))) 
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return user,first_filter,second_filter
        
        if(first_filter=='6'):
            unique_list=[]
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['location status'].strip() not in unique_list):  
                        unique_list.append(people[key]['location status'])
            print(("list of location status :{} ".format(unique_list))) 
            second_filter=input('enter from above list! : ')         
            while(second_filter.lower() not in unique_list):
                second_filter=input("Please give proper input !: ")
                        
            return user,first_filter,second_filter
        
        if(first_filter=='7'):
            
            first_filter='7'
            second_filter='hi'
            return user,first_filter,second_filter
        
        if(first_filter=='8'):
           
            first_filter='8'
            second_filter='0'
            print("hello")
            return user,first_filter,second_filter
                    
            
        
    def validate_yes_no_for_username(self):
        check=input("DO YOU TO FILTER ACCORDING TO USERNAME ? ")
        while(check not in ('yes','YES','Yes','NO','no','No')):
            check=input("DO YOU TO FILTER ACCORDING TO USERNAME ? yes or no :  ")
        return check