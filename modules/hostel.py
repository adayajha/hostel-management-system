import json
import os

from .student import Student
from .room import Room


class Hostel:

    def __init__(self):
        self.students = []
        self.rooms = {}

        # Create rooms
        room_numbers = [
            "101", "102", "103", "104", "105",
            "201", "202", "203", "204", "205"
        ]

        for room_number in room_numbers:
            self.rooms[room_number] = Room(room_number)

        # Load saved data
        self.load_data()

    # -----------------------------------------
    # ADD STUDENT
    # -----------------------------------------

    def add_student(self, student_id, name, department):

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return False

        student = Student(
            student_id,
            name,
            department
        )

        self.students.append(student)

        self.save_data()

        print("Student added successfully!")

        return True

    # -----------------------------------------
    # VIEW STUDENTS
    # -----------------------------------------

    def view_students(self):

        if len(self.students) == 0:
            print("No students registered.")
            return

        print("\n========== ALL STUDENTS ==========")

        for student in self.students:
            student.display()

    # -----------------------------------------
    # SEARCH STUDENT
    # -----------------------------------------

    def search_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent Found!")

                student.display()

                return

        print("Student not found.")

    # -----------------------------------------
    # ALLOCATE ROOM
    # -----------------------------------------

    def allocate_room(self, student_id, room_number):

        student_found = None

        # Find student
        for student in self.students:

            if student.student_id == student_id:
                student_found = student
                break

        if student_found is None:
            print("Student not found.")
            return

        # Check if student already has room
        if student_found.room is not None:

            print(
                "Student already has Room:",
                student_found.room
            )

            return

        # Check if room exists
        if room_number not in self.rooms:

            print("Invalid room number.")

            return

        room = self.rooms[room_number]

        # Check room availability
        if not room.is_available():

            print("Room is already full.")

            return

        # Allocate room
        room.allocate_student(student_id)

        student_found.room = room_number

        self.save_data()

        print("Room allocated successfully!")

        print("Student:", student_found.name)

        print("Room:", room_number)

    # -----------------------------------------
    # VACATE ROOM
    # -----------------------------------------

    def vacate_room(self, student_id):

        student_found = None

        # Find student
        for student in self.students:

            if student.student_id == student_id:
                student_found = student
                break

        if student_found is None:

            print("Student not found.")

            return

        # Check if student has room
        if student_found.room is None:

            print("Student does not have a room.")

            return

        room_number = student_found.room

        # Remove student from room
        self.rooms[room_number].remove_student(student_id)

        # Remove room from student
        student_found.room = None

        self.save_data()

        print("Room vacated successfully!")

        print("Student:", student_found.name)

        print("Vacated Room:", room_number)

    # -----------------------------------------
    # VIEW ROOMS
    # -----------------------------------------

    def view_rooms(self):

        print("\n========== ROOM STATUS ==========")

        for room in self.rooms.values():

            room.display()

    # -----------------------------------------
    # SAVE DATA TO JSON
    # -----------------------------------------

    def save_data(self):

        data = []

        for student in self.students:

            student_data = {
                "id": student.student_id,
                "name": student.name,
                "department": student.department,
                "room": student.room
            }

            data.append(student_data)

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data.json"
        )

        with open(file_path, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # -----------------------------------------
    # LOAD DATA FROM JSON
    # -----------------------------------------

    def load_data(self):

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data.json"
        )

        # If file doesn't exist
        if not os.path.exists(file_path):
            return

        try:

            with open(file_path, "r") as file:

                data = json.load(file)

            for student_data in data:

                student = Student(
                    student_data["id"],
                    student_data["name"],
                    student_data["department"],
                    student_data.get("room")
                )

                self.students.append(student)

                # Restore room allocation
                room_number = student.room

                if room_number in self.rooms:

                    self.rooms[room_number].allocate_student(
                        student.student_id
                    )

        except (json.JSONDecodeError, KeyError):

            print("Warning: Could not load data.json")