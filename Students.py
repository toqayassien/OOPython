class Students:
    students = []  # empty list to store students' data in

    def __init__(self, name, id, grade1, grade2):
        self.name = name
        self.id = id
        self.grade1 = grade1
        self.grade2 = grade2

    def accept(
        self,
    ):  # accepting the students by appending info to the list for later access
        Students.students.append(
            {
                "name": self.name,
                "id": self.id,
                "grade1": self.grade1,
                "grade2": self.grade2,
            }
        )

    # instance method that loops through the list and prints out a formatted data
    def display(self):  # works fine
        for student in Students.students:
            if student["id"] == self.id:
                print(f"Name: {self.name}")
                print(f"ID: {self.id}")
                print(f"GRADE1: {self.grade1}")
                print(f"GRADE2: {self.grade2}")
                print()

    # class method that will search all instances of the class using a student id
    # then will loop the list using that id and printing out formatted data
    @classmethod
    def search(cls, id):  # so far so great, works fine
        for student in Students.students:
            if student["id"] == id:
                for key, value in student.items():
                    print(f"{key.upper()}: {value}")

    # class method that will search all instances of the class
    # then will us the given id to loop through the list until found
    # then remove the found student data from list
    @classmethod
    def delete(cls, id):
        for student in Students.students:
            if student["id"] == id:
                Students.students.remove(student)

    # instance method that allows students to change their given id with another given id
    # updates both the list and the id attribute
    def update(self, id, new):  # works now
        for student in Students.students:
            if student["id"] == self.id:
                student["id"] = new
                self.id = new
