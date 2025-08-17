
# Fixed subjects
subjects = ("Math", "English", "Science")

# Collecting student information
name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
gender = input("Enter student's gender: ")

# Collect scores for subjects
scores = []
for subject in subjects:
    score = float(input(f"Enter score for {subject}: "))
    scores.append(score)
scores = tuple(scores)  # store as tuple

# Guardian information
guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")

# Hobbies (comma-separated, stored as set → list)
hobbies_input = input("Enter hobbies (comma separated): ")
hobbies = list(set(h.strip() for h in hobbies_input.split(",")))

# Build student profile (nested dictionary)
student_profile = {
    "personal_details": {
        "name": name,
        "age": age,
        "gender": gender,
        "initials": "".join([word[0].upper() for word in name.split()])
    },
    "scores": {
        "subjects": subjects,
        "values": scores
    },
    "guardian": {
        "name": guardian_name,
        "phone": guardian_phone
    },
    "hobbies": hobbies
}

# Calculations
average_score = sum(scores) / len(scores)

# Output neatly
print("\n===== STUDENT PROFILE =====")
print(f"Name: {student_profile['personal_details']['name']} ({student_profile['personal_details']['initials']})")
print(f"Age: {student_profile['personal_details']['age']}, Gender: {student_profile['personal_details']['gender']}")
print(f"Guardian: {student_profile['guardian']['name']} ({student_profile['guardian']['phone']})")

print("\n--- Scores ---")
for sub, sc in zip(subjects, scores):
    print(f"{sub}: {sc}")
print(f"Average Score: {average_score:.2f}")

print("\n--- Hobbies ---")
print(", ".join(hobbies))
print(f"Total Hobbies: {len(hobbies)}")
