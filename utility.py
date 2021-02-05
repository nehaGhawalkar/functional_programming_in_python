def check_date_format():
    import datetime
    good_value = False
    while(good_value == False):
        date = input("ENTER  DATE in  day/month/year format :")
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
            good_value = True
        except ValueError:
            print("Error: Date format invalid.")
    return date
        

"""
validation of the date
"""