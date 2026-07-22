# ---------------- Person class ---------------- #

class Person:
    university_name = "Vignan_University"

    def __init__(self, name, age, gender, department):
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department

    def display_info(self):
        pass


# ---------------- Student Class ---------------- #

class Student(Person):
    student_count = 0

    def __init__(self, name, age, gender, department,
                 student_id, course, year, education_background):

        super().__init__(name, age, gender, department)

        self.__student_id = student_id
        self.course = course
        self.year = year
        self.education_background = education_background

        Student.student_count += 1

    def display_info(self):
        print("\n========== STUDENT DETAILS ==========")
        print("University           :", Person.university_name)
        print("Name                 :", self.name)
        print("Age                  :", self.age)
        print("Gender               :", self.gender)
        print("Department           :", self.department)
        print("Student ID           :", self.__student_id)
        print("Course               :", self.course)
        print("Year                 :", self.year)
        print("Education Background :", self.education_background)

    def get_student_id(self):
        return self.__student_id

    @classmethod
    def total_students(cls):
        print("\nTotal Students :", cls.student_count)


# ---------------- Faculty Class ---------------- #

class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, gender, department,
                 faculty_id, qualification):

        super().__init__(name, age, gender, department)

        self.__faculty_id = faculty_id
        self.qualification = qualification

        Faculty.faculty_count += 1

    def display_info(self):
        print("\n========== FACULTY DETAILS ==========")
        print("University   :", Person.university_name)
        print("Name         :", self.name)
        print("Age          :", self.age)
        print("Gender       :", self.gender)
        print("Department   :", self.department)
        print("Faculty ID   :", self.__faculty_id)
        print("Qualification:", self.qualification)

    @classmethod
    def total_faculty(cls):
        print("\nTotal Faculty :", cls.faculty_count)


# ---------------- Teaching Staff Class ---------------- #

class TeachingStaff(Person):
    staff_count = 0

    def __init__(self, name, age, gender, department,
                 staff_id, subject, experience):

        super().__init__(name, age, gender, department)

        self.__staff_id = staff_id
        self.subject = subject
        self.experience = experience

        TeachingStaff.staff_count += 1

    def display_info(self):
        print("\n====== TEACHING STAFF DETAILS ======")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Department :", self.department)
        print("Staff ID   :", self.__staff_id)
        print("Subject    :", self.subject)
        print("Experience :", self.experience, "Years")

    @classmethod
    def total_teaching_staff(cls):
        print("\nTotal Teaching Staff :", cls.staff_count)


# ---------------- Non-Teaching Staff Class ---------------- #

class NonTeachingStaff(Person):
    staff_count = 0

    def __init__(self, name, age, gender, department,
                 staff_id, role, experience):

        super().__init__(name, age, gender, department)

        self.__staff_id = staff_id
        self.role = role
        self.experience = experience

        NonTeachingStaff.staff_count += 1

    def display_info(self):
        print("\n====== NON-TEACHING STAFF DETAILS ======")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Department :", self.department)
        print("Staff ID   :", self.__staff_id)
        print("Role       :", self.role)
        print("Experience :", self.experience, "Years")

    @classmethod
    def total_non_teaching_staff(cls):
        print("\nTotal Non-Teaching Staff :", cls.staff_count)


# ---------------- Bus Staff Class ---------------- #

class BusStaff(Person):
    bus_staff_count = 0

    def __init__(self, name, age, gender, department,
                 staff_id, bus_number, route, shift):

        super().__init__(name, age, gender, department)

        self.__staff_id = staff_id
        self.bus_number = bus_number
        self.route = route
        self.shift = shift

        BusStaff.bus_staff_count += 1

    def display_info(self):
        print("\n========= BUS STAFF DETAILS =========")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Department :", self.department)
        print("Staff ID   :", self.__staff_id)
        print("Bus Number :", self.bus_number)
        print("Route      :", self.route)
        print("Shift      :", self.shift)

    @classmethod
    def total_bus_staff(cls):
        print("\nTotal Bus Staff :", cls.bus_staff_count)


# ---------------- Creating Objects ---------------- #

student1 = Student("Rahul Sharma", 21, "Male", "IT", "S101", "B.Tech CSE", 3, "Intermediate (MPC)")
student2 = Student("Ananya Reddy", 20, "Female", "AI & DS", "S102", "B.Tech AI", 2, "Intermediate (MPC)")
student3 = Student("NITHYA Reddy", 22, "Female", "AIML", "KA23", "B.Tech CSE_AIML", 4, "Intermediate (MPC)")
student4 = Student("Rudra Varma", 25, "male", "AI", "A123", "B.Tech AI", 3, "Intermediate (BIMPC)")

faculty1 = Faculty("Dr. Ravi Kumar", 45, "Male", "Computer Science", "F101", "PhD")
faculty2 = Faculty("Dr. Meera", 48, "Female", "AI & ML", "F102", "PhD")

teacher1 = TeachingStaff("Mr. Suresh", 35, "Male", "Computer Science", "T201", "Python Programming", 10)

non_teacher1 = NonTeachingStaff("Lakshmi", 32, "Female", "Admin", "NT301", "Clerk", 7)

busstaff1 = BusStaff("Ramesh", 40, "Male", "Transport", "B301", "Bus-12", "Gajuwaka - University", "Morning")


# ---------------- Output ---------------- #

student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()
print("\nStudent IDs:", student1.get_student_id(), student2.get_student_id(), student3.get_student_id(),student3.get_student_id())

faculty1.display_info()
faculty2.display_info()

teacher1.display_info()
non_teacher1.display_info()
busstaff1.display_info()

Student.total_students()
Faculty.total_faculty()
TeachingStaff.total_teaching_staff()
NonTeachingStaff.total_non_teaching_staff()
BusStaff.total_bus_staff()
