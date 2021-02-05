import csv


class user_file:
    def __init__(self):
        print("")
    
    def take_file_from_user(self,filepath):
        """
        taking csv file from the config file and converting it 
        into a dictionary of values
        """
        people={}                                   
        while(len(people)==0):                      
            with open(filepath) as input_file:                           
                    reader = csv.reader(input_file)
                    for row in reader:
                        people[row[0]]={'uid':row[0],'username':row[1],'item type':row[2],'item':row[3],
                              'startdate':row[4],'expecteddate':row[5],'progress':row[6],'source':row[7],
                              'destination':row[8],'location status':row[9]}
        
                        
        """
        mapping  items to  correct item type
        """        
        list_of_items=[]
        item_dictionary={'iphone':'electronics','apple iphone':'electronics','laptop':'electronics','apple':'fruit','mango':'fruit','cycle':'vehicle','phone':'electronics','truck':'vehicle','matress':'home','bike':'vehicle','pillows':'home','iphone':'electronics'}
        for key, value in people.items():
            list_of_items.append(people[key]['item']) 
        correct_item_mapping=list(map(item_dictionary.get,list_of_items))   
        i=0
        for key, value in people.items():
            if(people[key]['item type']!=correct_item_mapping[i]):
                people[key]['item type']=correct_item_mapping[i]
            i=i+1
        del people['uid']
        
        return people







