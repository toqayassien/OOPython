from Students import Students


def main():
    student1 = Students("Harry", 123, 70, 98)
    student1.accept()
    student2 = Students("Ron", 456, 96, 50)
    student2.accept()
    student1.update(123, 789)
    student1.display()
    Students.search(456)


if __name__ == "__main__":
    main()