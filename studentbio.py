

#Collecting student bio-data
bio_data = {}

#Get user input

bio_data['name'] = input("Enter your name: ")
bio_data['age'] = input("Enter your age: ")
bio_data['gender'] = input("Enter your gender: ")

#Get courses as a comma-separated list and convert to list

courses = input("Enter your courses (separated by commas): ")
bio_data['courses'] = courses.split(',')

#Display bio-data using escape sequences
print("\n\t--- Student Bio Data ---")
print(f"\tName:bio_data['name']")
print(f"\tAge:bio_data['age']")
print(f"\tGender:bio_data['gender']")
print("\tCourses:")

for course in bio_data['courses']:
    print(f"\t\t- {course.strip()}")
