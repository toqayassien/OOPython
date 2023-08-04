class Students:
    students = []

    def __init__(self, name, id, grade1, grade2):
        self.name = name
        self.id = id
        self.grade1 = grade1
        self.grade2 = grade2

    def accept(self):
        Students.students.append(
            {
                "name": self.name,
                "id": self.id,
                "grade1": self.grade1,
                "grade2": self.grade2,
            }
        )

    def display(self):  # works fine
        for student in Students.students:
            if student["id"] == self.id:
                print(f"Name: {self.name}")
                print(f"ID: {self.id}")
                print(f"GRADE1: {self.grade1}")
                print(f"GRADE2: {self.grade2}")
                print()

    @classmethod
    def search(cls, id):  # so far so great, works fine
        for student in Students.students:
            if student["id"] == id:
                for key, value in student.items():
                    print(f"{key.upper()}: {value}")

    @classmethod
    def delete(cls, id):
        for student in Students.students:
            if student["id"] == id:
                Students.students.remove(student)

    def update(self, id, new):  # works now
        for student in Students.students:
            if student["id"] == self.id:
                student["id"] = new
                self.id = new