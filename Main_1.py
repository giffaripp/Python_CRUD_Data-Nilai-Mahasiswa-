# ===================================
# [ Student Grades Data - Basic Accounting Course ]
# ===================================
# Developed by: Muhammad Giffari Putra Pradana
# JCDSBSDAM - [29]

# /************************************/

from tabulate import tabulate

# Students data : List of Dictionary 

students_data = {
    "205030200111001": {"name": "Adli", "score": 78, "absent": 2, "midterm": True, "final": False},
    "205030200111002": {"name": "Bagas", "score": 68, "absent": 1, "midterm": True, "final": True},
    "205030200111003": {"name": "Caca", "score": 92, "absent": 4, "midterm": True, "final": True},
    "205030200111004": {"name": "Dea", "score": 81, "absent": 0, "midterm": True, "final": True},
    "205030200111005": {"name": "Evan", "score": 56, "absent": 5, "midterm": False, "final": False},
    "205030200111006": {"name": "Fino", "score": 86, "absent": 1, "midterm": True, "final": True},
    "205030200111007": {"name": "Giffari", "score": 98, "absent": 1, "midterm": True, "final": True},
    "205030200111008": {"name": "Hafizh", "score": 87, "absent": 4, "midterm": True, "final": True},
    "205030200111009": {"name": "Imam", "score": 94, "absent": 0, "midterm": False, "final": True},
    "205030200111010": {"name": "Jasmine", "score": 82, "absent": 0, "midterm": True, "final": True}
}

# Function for Menu 1 (Students Report) : Checking all student status.

def check_student_status(score, absent, attended_midterm, attended_final):
    reasons = []
    if not attended_midterm and not attended_final:
        reasons.append("did not attend Midterm & Final Exam")
    else:    
        if not attended_midterm:
            reasons.append("did not attend Midterm")
        if not attended_final:
            reasons.append("did not attend Final Exam")
    if score < 60:
        reasons.append("overall score below 60")
    if absent > 3:
        reasons.append("absences more than 3 times")
    
    if reasons:
        return "Not Passed: " + ", ".join(reasons)
    else:
        return "Passed"

# Function for Menu 1 (Students Report): Grade conversion from score to character (From A - E) 

def convert_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "E"

# Function for Menu 1 (Students Report) : Checking all student status displayed with a table.

def students_table():
    table = []
    for nim, info in students_data.items():
        grade = convert_grade(info['score'])
        status = check_student_status(info['score'], info['absent'], info['midterm'], info['final'])
        table.append([
            nim, info['name'], info['score'], grade, f"{info['absent']}/16",
            "Yes" if info['midterm'] else "No",
            "Yes" if info['final'] else "No",
            status
        ])

    print("\n" + "=" * 129)
    print("STUDENT GRADES TABLE".center(129))
    print("=" *129)
    print(tabulate(
        table,
        headers=["Student ID", "Name", "Score", "Grade", "Absence", "Midterm", "Final Exam", "Status"],
        tablefmt="fancy_grid",
        maxcolwidths=[None, None, None, None, None, None, None, 40]
    ))

# Function for Menu 1 (Students Report) : Checking all student status statistic displayed with a table.

def class_statistics():
    if not students_data:
        print("\nNo student data yet!\n")
        return
    passed, failed, total_score, max_absent = 0, 0, 0, 0
    attended_midterm, attended_final, attended_both = 0, 0, 0

    for nim, info in students_data.items():
        status = check_student_status(info["score"], info["absent"], info["midterm"], info["final"])
        total_score += info['score']
        if status == "Passed":
            passed += 1
        else:
            failed += 1
        if info["absent"] > max_absent:
            max_absent = info["absent"]

        if info["midterm"]:
            attended_midterm +=1
        if info["final"]:
            attended_final +=1
        if info["midterm"] and info["final"]:
            attended_both +=1

    average = total_score / len(students_data)
    table = [
    ["Total Students",  len(students_data)],
    ["Total Passed",  passed],
    ["Total Failed", failed],
    ["Average Score", f"{average:.2f}"],
    ["Highest Absence", max_absent],
    ["Students Attended Midterm", attended_midterm],
    ["Students Attended Final", attended_final],
    ["Students Attended Midterm & Final", attended_both]
    ]

    print("\n" + "=" * 45)
    print("BASIC ACCOUNTING CLASS STATISTICS".center(45))
    print("=" *45)
    print(tabulate(table, headers=["Category", "Value"], tablefmt="fancy_grid"))

# Submenu Function 1 : To show students report table, class statistic, or both.

def report_students():
    while True:
        if not students_data:
            print("\nNo student data yet!\n")
            return
    
        print("\n" + "=" * 50)
        print("STUDENT REPORT SUBMENU".center(50))
        print("=" *50)
        print("1. Show students table")
        print("2. Show class statistics")
        print("3. Show both")
        print("0. Back to main menu")
        choice = input("Choose submenu: ")

        if choice == "1":
            students_table()
        elif choice == "2":
            class_statistics()
        elif choice == "3":
            students_table()
            class_statistics()
        elif choice == "0":
            break
        else:
            print("Invalid choice, please select 1-3")

# Menu Function 2: Adding or input new student data using all categories needed.

def add_student():
    while True:
        print("\n" + "=" * 60)
        print("ADD STUDENT DATA".center(60))
        print("=" *60)
        print("0. Back to main menu")
        nim = input("Enter Student ID: ")
        if nim == "0" : 
            break
        if not nim.isdigit () or len(nim) > 15 :
            print("Student ID must be digits with max 15 characters. Try again")
            continue
        elif nim in students_data:
            print("Student ID already exists. Please input correctly")
            continue
        
        name = input("Enter Student Name: ").capitalize()
    
        while True:
            try:
                score = int(input("Enter Final Score (0-100): "))
                if  0 <= score <= 100:
                    break
                else:
                    print("Score must be in range 0-100")
            except ValueError:
                print("Score must be a number!")
        while True:
            try:
                absent = int(input("Enter Number of Absences (0-16): "))
                if 0 <= absent <= 16:
                    break
                else:
                    print("Absence must be in range 0-16")
            except ValueError:
                print("Absence must be a number!")    

        midterm = input("Attended Midterm? (YES/NO): ").upper() == "YES"
        final = input("Attended Final Exam? (YES/NO): ").upper() == "YES"

        confirm_add = input("Are you sure want to add this student data? (YES/NO): ").upper()
        if confirm_add != "YES":
            print("Input cancelled")
            continue

        students_data[nim] = {"name": name, "score": score, "absent": absent, "midterm": midterm, "final": final}
        print("Data successfully added!")
        break

# Menu Function 3 : Modify or update current student report, based on categories selected.

def update_student():
    print("\n" + "=" * 60)
    print("UPDATE STUDENT DATA".center(60))
    print("=" *60)
    print("0. Back to main menu")
    nim = input("Enter Student ID: ")
    if nim not in students_data:
        print("Student not found. Please input a valid Student ID.")
        return

    while True:
        print(f"\nUpdate data for ID {nim} - {students_data[nim]['name']}")
        print("1. Update Score")
        print("2. Update Absences")
        print("3. Update Midterm Attendance")
        print("4. Update Final Exam Attendance")
        print("5. Update All Data")
        print("0. Back to previous menu")
        choice = input("Choose option 1-5 to update: ")
        
        if choice == "0":
            print("Back to main menu")
            break
    
        if choice == "1":
            try:
                score = int(input("Enter new score (0-100): "))
                if 0 <= score <= 100:
                    confirm_update = input("Are you sure want to update this student data? (YES/NO): ").upper()
                    if confirm_update != "YES":
                        print("Update cancelled")
                        continue
                    students_data[nim]["score"] = score
                    print("Score successfully updated")
                    break
                else:
                    print("Score must be in range 0-100.")
            except ValueError:
                print("Invalid input, score must be a number.")

        elif choice == "2":
            try:
                absent = int(input("Enter new number of absences: "))
                if 0 <= absent <= 16:
                    confirm_update = input("Are you sure want to update this student data? (YES/NO): ").upper()
                    if confirm_update != "YES":
                        print("Update cancelled")
                        continue
                    students_data[nim]["absent"] = absent
                    print("Absences successfully updated")
                    break
                else:
                    print("Absences must be in range 0-16.")
            except ValueError:
                print("Invalid input, absences must be a number.")

        elif choice == "3":
            midterm = input("Did the student attend Midterm? (YES/NO): ").upper()
            confirm_update = input("Are you sure want to update this student data? (YES/NO): ").upper()
            if confirm_update != "YES":
                print("Update cancelled")
                continue
            students_data[nim]["midterm"] = (midterm == "YES")
            print("Midterm attendance successfully updated!")

        elif choice == "4":
            final = input("Did the student attend Final Exam? (YES/NO): ").upper()
            confirm_update = input("Are you sure want to update this student data? (YES/NO): ").upper()
            if confirm_update != "YES":
                print("Update cancelled")
                continue
            students_data[nim]["final"] = (final == "YES")
            print("Final exam attendance successfully updated")

        elif choice == "5":
            try:
                score = int(input("Enter new score (0-100): "))
                if 0 <= score <= 100:
                    students_data[nim]["score"] = score
            except ValueError:
                print("Invalid score")

            try:
                absent = int(input("Enter new number of absences: "))
                if 0 <= absent <= 16:
                    students_data[nim]["absent"] = absent
            except ValueError:
                print("Invalid absence value")

            midterm = input("Did the student attend Midterm? (YES/NO): ").upper()
            students_data[nim]["midterm"] = (midterm == "YES")

            final = input("Did the student attend Final Exam? (YES/NO): ").upper()
            students_data[nim]["final"] = (final == "YES")

            confirm_update = input("Are you sure want to update this student data? (YES/NO): ").upper()
            if confirm_update != "YES":
                print("Update cancelled")
                continue

            print("Data successfully updated. Thank you.")
        else:
            print("Invalid choice. Please select 1-5")

# Menu Function 4 : Find current student report listed on student grades table using student ID.

def find_student():
    if not students_data:
        print("\nNo student data yet!\n")
        return
    
    nim = input("Enter Student ID to search: ")
    if nim in students_data:
        info = students_data[nim]
        grade = convert_grade(info['score'])
        status = check_student_status(info['score'], info['absent'], info['midterm'], info['final'])
        table = [[
            nim, info['name'], info['score'], grade, f"{info['absent']}/16",
            "Yes" if info['midterm'] else "No",
            "Yes" if info['final'] else "No",
            status
        ]]
        print("\n" + "=" * 117)
        print("STUDENT DETAILS".center(117))
        print("=" *117)
        print(tabulate(
            table,
            headers=["Student ID", "Name", "Score", "Grade", "Absence", "Midterm", "Final Exam", "Status"],
            tablefmt="fancy_grid",
            maxcolwidths=[None, None, None, None, None, None, None, 40]
        ))
    else:
        print(f"Student with ID {nim} not found.")

# Menu Function 5 : Delete or remove student and their data from the program.

def delete_student():
    while True:
        print("\n" + "=" * 60)
        print("DELETE STUDENT DATA".center(60))
        print("=" *60)
        print("0. Back to main menu")
        nim = input("Enter Student ID to delete: ")
        if nim == "0":
            break
        if nim not in students_data:
            print("Data not found!")
            continue
        confirm_delete = input(f"Are you sure to delete {students_data[nim]['name']}? (YES/NO): ").upper()
        if confirm_delete == "YES":
            del students_data[nim]
            print("Data successfully deleted!")
        else:
            print("Delete cancelled.")
        break

# Main Menu

def main():
    while True:
        print("\n" + "=" * 50)
        print("BASIC ACCOUNTING COURSE GRADE MANAGEMENT SYSTEM".center(50))
        print("=" *50)
        print("1. Student Report")
        print("2. Add Student Data")
        print("3. Update Student Data")
        print("4. Search Student Data")
        print("5. Delete Student Data")
        print("6. Exit")
        choose = input("Choose menu: ")

        if choose == "1": report_students()
        elif choose == "2": add_student()
        elif choose == "3": update_student()
        elif choose == "4": find_student()
        elif choose == "5": delete_student()
        elif choose == "6":
            print("Thank you for using the Student Grade Management System.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
