

#Tuple of days
days = ("Monday", "Wednesday", "Friday")

#Collect activities for the days

activities = []
for day in days:
    activity = input(f"What activity do you have on {day}? ")
    activities.append(activity)

#Use dictionary comprehension with zip to pair days and activities

schedule = {day: activity for day, activity in zip(days, activities)}

#Print the dictionary

print("\n--- Weekly Activities ---")
for day, activity in schedule.items():
    print(f"{day}: {activity}")
