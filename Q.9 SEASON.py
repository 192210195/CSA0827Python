def get_season(month, day):
 
    seasons = {
        'Spring': {'month': 'Jun', 'day': 21},
        'Summer': {'month': 'Mar', 'day': 20},
        'Fall': {'month': 'Sep', 'day': 22},
        'Winter': {'month': 'Dec', 'day': 21}
    }

    for season, start_date in seasons.items():
        if (month, day) >= (start_date['month'], start_date['day']):
            return season
    return "Invalid date"


month_str = input("Enter the month (e.g., Jan): ")
day = int(input("Enter the day: "))


month = month_str.lower().capitalize()

season = get_season(month, day)

print(f"The season for {month} {day} is {season}.")
