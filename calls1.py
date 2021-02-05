import datetime
from datetime import timedelta

class call_nested_filter:
    def __init__(self):
        print("")
        
    def call_item(self,people,user,second_filter):
            count_of_items=0
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['item']==second_filter.lower()):
                        """
                        validation of second_filter is already done in filters module
                        where the user has to enter value from specific set of results
                        """
                        """
                        printing details according to different item calls
                        """
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
      
                
    def call_category(self,people,user,second_filter):
            count_of_items=0
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['item type']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
                   
                        
    def call_source(self,people,user,second_filter):
            count_of_items=0
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['source']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
                 
                        
                        
    def call_destination(self,people,user,second_filter):            
            count_of_items=0
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['destination']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['source']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
                    
            
    def call_progress(self,people,user,second_filter):           
            count_of_items=0
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['progress']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
                        
    def call_location_status(self,people,user,second_filter):
            count_of_items=0
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    if(people[key]['location status']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
            
    
    def call_username_all_details(self,people,user,second_filter):
            count_of_items=0
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    #if(people[key]['location status']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        
                        
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
    #user,first_filter,second_filter_date1,second_filter_date2      
              
    def call_username_expected_dates(self,people,user,utility):
        """
        validation to enter date in specified format
        """
        
        first_date=utility.check_date_format()
        second_date=utility.check_date_format()
        
        while(first_date>second_date):
                first_date=input("Please enter first date less than second date : ")
                while(second_date<first_date):
                    second_date=input("Please give second date : ") 
        """
        first_date=second_filter[1]
        second_date=second_filter[2]
        
        """
        """
        converting string to date time format
        """
        
        first_date = datetime.datetime.strptime(first_date, '%d/%m/%Y')
        second_date = datetime.datetime.strptime(second_date, '%d/%m/%Y')
        """
        display details between 2 expected dates
        """
        counter_for_deliveries=0
        while first_date <= second_date:        
            for key, value in people.items():
                if(people[key]['username']==user.upper()):
                    expected_date=datetime.datetime.strptime(people[key]['expecteddate'] , '%d/%m/%Y')
                
                    if(expected_date==first_date):
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['source']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        counter_for_deliveries=counter_for_deliveries+1
            first_date = first_date + timedelta(days=1)   
        if(counter_for_deliveries==0):
            print("you do not have deliveries between thes date range !")                 
                        
                        
    ##---- functions which does not require username!!!
                        
    def call_item_no_username(self,people,second_filter):
            count_of_items=0
            for key, value in people.items():
                    if(people[key]['item']==second_filter.lower()):
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))     
                
    def call_category_no_username(self,people,second_filter):
            count_of_items=0
            for key, value in people.items():
                if(people[key]['item type']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
   
                        
    def call_source_no_username(self,people,second_filter):
           
            count_of_items=0
            for key, value in people.items():
                if(people[key]['source']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
                        
                        
    def call_destination_no_username(self,people,second_filter):
            
            count_of_items=0
            for key, value in people.items():              
                    if(people[key]['destination']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
              
            
    def call_progress_no_username(self,people,b):
           
            count_of_items=0
            for key, value in people.items():
                    if(people[key]['progress']==b.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))     
                        
    def call_location_status_no_username(self,people,second_filter):
           
            count_of_items=0
            for key, value in people.items():
              
                    if(people[key]['location status']==second_filter.lower()):  
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
                        count_of_items=count_of_items+1
                        print("\n")
            print("TOTAL NUMBER OF DELIVERIES : {}".format(count_of_items))
     
    ###dates
    def call_expected_dates(self,people,utility):
        """
        validation to enter date in specified format
        """
        first_date=utility.check_date_format()
        second_date=utility.check_date_format()
        
        first_date = datetime.datetime.strptime(first_date, '%d/%m/%Y')
        second_date = datetime.datetime.strptime(second_date, '%d/%m/%Y')
        """
        display details between 2 expected dates
        """
        
        while first_date < second_date:        
            for key, value in people.items():
                a=datetime.datetime.strptime(people[key]['expecteddate'] , '%d/%m/%Y')
                
                if(a==first_date):
                        print("\n")
                        print("uid :{} ".format(people[key]['uid']))
                        print("ITEM :{} ".format(people[key]['item']))
                        print("CATEGORY :{} ".format(people[key]['item type']))
                        print("progress :{} ".format(people[key]['progress']))
                        print("SOURCE :{} ".format(people[key]['source']))
                        print("DESTINATION :{} ".format(people[key]['destination']))
                        print("location status :{} ".format(people[key]['source']))
                        print("location status :{} ".format(people[key]['location status']))
                        print("expected delivery date :{} ".format(people[key]['expecteddate']))
            first_date = first_date + timedelta(days=1)    
        
                     

                