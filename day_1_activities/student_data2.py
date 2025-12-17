Fname = input("what is your first name")
ID = input("What is your 8 digit ID?")
LNAME = input("what is your Last Name?")
MNAME = input("What is your middle name?")
HR = input("what is your homeroom?")
GL = input("What is your grade level?")
EMAIL1 = input("What is your first email?")
EMAIL2 = input("What is your second email?")
students = [{
    "CPSID": ID,
    "LName": LNAME,
    "FName": Fname,
    "MName": MNAME,
    "HR": HR,
    "GL": GL,
    "Email":[EMAIL1, EMAIL2]
}]

print(students)
