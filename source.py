from datetime import datetime

students = {}

student_count = int(input("How many students do you want to add? "))

for _ in range(student_count):
    registrationnumber = input("Enter registration number: ")
    name = input("Enter student name: ")
    room_no = input("Enter room number: ")

    students[registrationnumber] = [name, room_no]

records = []
complaints = []
visitors = []

while True:

    print("\n===== HOSTEL MANAGEMENT =====")
    print("1. Student Entry")
    print("2. Student Exit")
    print("3. Search Student")
    print("4. View Records")
    print("5. Emergency Help")
    print("6. Hostel Information")
    print("7. Complaint")
    print("8. Mess Menu")
    print("9. Visitor Entry")
    print("10. Change Room")
    print("11. Student Count")
    print("12. All Students")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter Student ID: ")

        if id in students:
            name = students[id][0]
            room = students[id][1]
            time = datetime.now()

            print("\nStudent Name:", name)
            print("Room Number:", room)
            print("Entry Allowed")
            print("Time:", time)

            records.append([id, "Entry", time])

        else:
            print("Student Not Found")

    elif choice == "2":
        id = input("Enter Student ID: ")

        if id in students:
            name = students[id][0]
            time = datetime.now()

            print("\nStudent Name:", name)
            print("Exit Allowed")
            print("Time:", time)

            records.append([id, "Exit", time])

        else:
            print("Student Not Found")

    elif choice == "3":
        id = input("Enter Student ID: ")

        if id in students:
            print("\nName:", students[id][0])
            print("Room:", students[id][1])

        else:
            print("Student Not Found")

    elif choice == "4":
        print("\n===== RECORDS =====")

        if not records:
            print("No records found")

        else:
            for record in records:
                print("ID:", record[0])
                print("Type:", record[1])
                print("Time:", record[2])
                print()

    elif choice == "5":
        print("\n===== EMERGENCY HELP =====")
        print("1. Warden")
        print("2. Security")
        print("3. Medical Help")

        x = input("Choose an option: ")

        if x == "1":
            print("Warden Phone: 100")

        elif x == "2":
            print("Security Phone: 107")

        elif x == "3":
            print("Medical Help Phone: 108")

        else:
            print("Invalid choice")

    elif choice == "6":
        print("\n===== HOSTEL INFORMATION =====")
        print("Hostel: VIT Bhopal, Kotri Kalan")
        print("Contact the warden for any problem.")
        print("Use Emergency Help for urgent problems.")

    elif choice == "7":
        id = input("Enter Student ID: ")

        if id in students:
            complaint = input("Enter your complaint: ")
            complaints.append([id, complaint])
            print("Complaint have been registered successfully,we will solve your problem as soon as possible.")

        else:
            print("Student Not Found")

    elif choice == "8":
        print("\n===== MESS MENU =====")
        print("Breakfast: Idli / Dosa")
        print("Lunch: Rice / Dal")
        print("Snacks: Tea / Biscuits")
        print("Dinner: Roti / Rice")

    elif choice == "9":
        visitor = input("Enter visitor name: ")
        id = input("Enter Student ID: ")

        if id in students:
            visitors.append([visitor, id])
            print("Visitor entry recorded.")

        else:
            print("Student Not Found")

    elif choice == "10":
        id = input("Enter Student ID: ")

        if id in students:
            room = input("Enter new room number: ")
            students[id][1] = room
            print("Room changed successfully.")

        else:
            print("Student Not Found")

    elif choice == "11":
        print("Total Students:", len(students))

    elif choice == "12":
        print("\n===== ALL STUDENTS =====")

        for id in students:
            print("ID:", id)
            print("Name:", students[id][0])
            print("Room:", students[id][1])
            print()

    elif choice == "13":
        print("Thank you for using Hostel Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
