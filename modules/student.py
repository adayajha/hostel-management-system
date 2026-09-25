class Student:
    def __init__(self, student_id, name, department, room=None):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.room = room

    def display(self):
        print("--------------------------------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Department :", self.department)

        if self.room is None:
            print("Room       : Not Allocated")
        else:
            print("Room       :", self.room)