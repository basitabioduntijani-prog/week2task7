# Collecting student information

name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
gender = input("Enter student's gender: ")

# Collect 3 subject scores

scores = {}
for subject in ["Math", "English", "Science"]:
    scores[subject] = float(input(f"Enter score for {subject}: "))

# Guardian information

guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")

# Hobbies (comma-separated, stored as set)

hobbies_input = input("Enter hobbies (comma separated): ")
hobbies = set(hobby.strip() for hobby in hobbies_input.split(","))

# Store everything in a nested dictionary

student = {
    "personal_details": {
        "name": name,
        "age": age,
        "gender": gender
    },
    "scores": scores,
    "guardian": {
        "name": guardian_name,
        "phone": guardian_phone
    },
    "hobbies": hobbies
}

# Calculations

average_score = sum(scores.values()) / len(scores)
initials = "".join([word[0].upper() for word in name.split()])

# Output neatly

print("\n===== STUDENT INFORMATION =====")
print(f"Name: {student['personal_details']['name']} ({initials})")
print(f"Age: {student['personal_details']['age']}")
print(f"Gender: {student['personal_details']['gender']}")
print(f"Guardian: {student['guardian']['name']} ({student['guardian']['phone']})")
print("Scores:", student["scores"])
print(f"Average Score: {average_score:.2f}")
print("Hobbies:", ", ".join(student["hobbies"]))
