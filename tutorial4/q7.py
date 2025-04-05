class StudentMarks:
    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def computeTotal(self):
        return self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll No: {self.rollno}, Mark1: {self.mark1}, Mark2: {self.mark2}, Total: {self.computeTotal()}")


student = StudentMarks()
student.readData(201, 85, 90)
student.printDetails()
