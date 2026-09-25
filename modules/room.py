class Room:
    def __init__(self, room_number, capacity=2):
        self.room_number = room_number
        self.capacity = capacity
        self.students = []

    def is_available(self):
        return len(self.students) < self.capacity

    def allocate_student(self, student_id):
        if self.is_available():
            self.students.append(student_id)
            return True

        return False

    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)
            return True

        return False

    def display(self):
        print("--------------------------------")
        print("Room Number :", self.room_number)
        print("Occupied    :", len(self.students))
        print("Available   :", self.capacity - len(self.students))

        if len(self.students) == 0:
            print("Status      : Completely Empty")
        elif len(self.students) < self.capacity:
            print("Status      : Partially Occupied")
        else:
            print("Status      : Full")