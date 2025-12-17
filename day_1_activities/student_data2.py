Fname = input("What is your first name?")
ID = int(input("What is your 8 digit ID?"))
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
    'HR': HR,
    "GL": GL,
    "Email":[EMAIL1, EMAIL2]
}]
x = int("37") + int("1")
print("Your information:", students)
print("There are now ",x,"students in the school system")
print("\n--- Student Information ---")
print("CPS ID:", students["CPSID"])
print("Last Name:", students["LName"])
print("First Name:", students["FName"])
print("Middle Name:", students["MName"])
print("Homeroom:", students["HR"])
print("Grade Level:", students["GL"])
print("Emails:")
print("  -", students["Email"][0])
print("  -", students["Email"][1])