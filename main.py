from modules.hostel import Hostel


def main():
    hostel = Hostel()

    while True:

        print("\n")
        print("======================================")
        print("       HOSTEL MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Allocate Room")
        print("5. Vacate Room")
        print("6. View Available Rooms")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        # Add Student
        if choice == "1":

            print("\n========== ADD STUDENT ==========")

            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")

            hostel.add_student(
                student_id,
                name,
                department
            )

        # View Students
        elif choice == "2":

            hostel.view_students()

        # Search Student
        elif choice == "3":

            print("\n========== SEARCH STUDENT ==========")

            student_id = input("Enter Student ID: ")

            hostel.search_student(student_id)

        # Allocate Room
        elif choice == "4":

            print("\n========== ALLOCATE ROOM ==========")

            student_id = input("Enter Student ID: ")

            print("\nAvailable Rooms:")

            for room_number, room in hostel.rooms.items():

                if room.is_available():

                    available = room.capacity - len(room.students)

                    print(
                        room_number,
                        "-",
                        available,
                        "space(s) available"
                    )

            room_number = input("\nEnter Room Number: ")

            hostel.allocate_room(
                student_id,
                room_number
            )

        # Vacate Room
        elif choice == "5":

            print("\n========== VACATE ROOM ==========")

            student_id = input("Enter Student ID: ")

            hostel.vacate_room(student_id)

        # View Rooms
        elif choice == "6":

            hostel.view_rooms()

        # Exit
        elif choice == "7":

            print("\nThank you for using Hostel Management System!")
            break

        else:

            print(
                "\nInvalid choice! "
                "Please enter a number from 1 to 7."
            )


if __name__ == "__main__":
    main()