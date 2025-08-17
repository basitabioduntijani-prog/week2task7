#Understanding the task

class Student:
    def __init__(self, name, age, gender, guardian):
        self.name = name
        self.age = age
        self.gender = gender
        self.guardian = guardian
        self.scores = {}
        self.hobbies = set()

    def add_score(self, subject, score):
        self.scores[subject] = score

    def add_hobby(self, hobby):
        self.hobbies.add(hobby)

    def average_score(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        return 0

    def initials(self):
        return "".join([word[0].upper() for word in self.name.split()])

    def display_info(self):
        print(f"Name: {self.name} ({self.initials()})")
        print(f"Age: {self.age}, Gender: {self.gender}")
        print(f"Guardian: {self.guardian}")
        print(f"Scores: {self.scores}")
        print(f"Average Score: {self.average_score():.2f}")
        print(f"Hobbies: {', '.join(self.hobbies)}")


# Example usage:

student = Student("John Doe", 15, "Male", "Mr. Doe")
student.add_score("Math", 85)
student.add_score("English", 90)
student.add_score("Science", 78)
student.add_hobby("Reading")
student.add_hobby("Football")
student.add_hobby("Reading")  

# won't duplicate

student.display_info()
