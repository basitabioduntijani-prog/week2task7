
#Step 1: Basic student info

name = input("Enter full name: ")
age = input("Enter age: ")
gender = input("Enter gender: ")

#Step 2: Subjects and scores

subjects = ("Math", "English", "Biology")
print(f"Subjects: {subjects}")

scores = tuple(int(input(f"Enter score for {subj}: ")) for subj in subjects)

#Step 3: Guardian details

guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")

#Step 4: Hobbies

hobbies_input = input("Enter hobbies (comma-separated): ")
hobbies = set(h.strip() for h in hobbies_input.split(","))

#Step 5: Build student_profile dictionary

student_profile = {
    "Basic Info": {
        "Name": name,
        "Age": age,
        "Gender": gender
    },
    "Guardian": {
        "Name": guardian_name,
        "Phone": guardian_phone
    },
    "Scores": {subj: score for subj, score in zip(subjects, scores)},
    "Hobbies": hobbies,
    "Calculated": {
        "Average Score": sum(scores) / len(scores),
        "Initials": ''.join([n[0].upper() for n in name.split()]),
        "Hobbies Count": len(hobbies)
    }
}

#Step 6: Display results neatly

print("\n--- Student Profile ---")
print(f"\n\tName:\tstudent_profile['Basic Info']['Name']")
print(f"\tAge:\tstudent_profile['Basic Info']['Age']")
print(f"\tGender:\tstudent_profile['Basic Info']['Gender']")
print(f"\tGuardian:student_profile['Guardian']['Name'] ({student_profile['Guardian']['Phone']})")
print("\n\tScores:")
for subj, score in student_profile["Scores"].items():
    print(f"\tsubj:score")
print(f"\n\tHobbies:', '.join(student_profile['Hobbies'])")
print(f"\tAverage Score:student_profile['Calculated']['Average Score']")
print(f"\tInitials:student_profile['Calculated']['Initials']")
print(f"\tHobbies Count:student_profile['Calculated']['Hobbies Count']")
