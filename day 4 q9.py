def get_season(month, day):
   
    month_dict = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    
    
    month_num = month_dict.get(month)
    
    
    if (month_num == 3 and day >= 20) or (month_num == 4) or (month_num == 5) or (month_num == 6 and day < 21):
        season = "Spring"
    elif (month_num == 6 and day >= 21) or (month_num == 7) or (month_num == 8) or (month_num == 9 and day < 22):
        season = "Summer"
    elif (month_num == 9 and day >= 22) or (month_num == 10) or (month_num == 11) or (month_num == 12 and day < 21):
        season = "Fall"
    else:
        season = "Winter"
    
    return season

month = input("Enter the month (First three letters, e.g., Jan for January): ")
day = int(input("Enter the day: "))


season = get_season(month, day)


print("The season associated with the date {} {} is {}.".format(month, day, season))
