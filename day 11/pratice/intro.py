class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def details_st(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)

s1 = Student("Vishwa", 90)
s1.details_st()
s2 = Student("l", 34)
s2.details_st()
s3 = Student("x", 85)
s3.details_st()
if s1.marks > 35:
    print("s1.passed")
else:
    print("s1.failed")
if s2.marks > 35:
    print("s2.passed")
else:
    print("s2.failed")
if s3.marks > 35:
    print("s3.passed")
else:
    print("s3.failed")
