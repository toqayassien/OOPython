from Students import Students


def main():
    student1 = Students("Harry", 123, 70, 98)
    student1.accept()
    student2 = Students("Ron", 456, 96, 50)
    student2.accept()
    Students.delete(123)

if __name__ == "__main__":
    main()

    