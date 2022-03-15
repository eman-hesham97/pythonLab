class Office:
    employeesNum = 0

    def __init__(self, officeName, employees):
        self.officeName = officeName
        self.employees = employees
        Office.employeesNum += len(employees)

    def get_all_employees(self):
        employees = []
        for i in self.employees:
            employees.append(i.name)
        return employees

    def get_employee(self, empId):
        for i in self.employees:
            if i.id == empId:
                return i.name

    def hire(self, Employee):
        newEmployee = Employee(Employee)
        self.employees.append(newEmployee)
        Office.employeesNum += 1

    def fire(self, empId):
        len_of_Emp = len(self.employees)
        for i in range(len_of_Emp):
            if self.employees[i].id == empId:
                del self.employees[i]
                Office.employeesNum -= 1
                return

    def deduct(self, empId, deduction):
        len_of_Emp = len(self.employees)
        for i in range(len_of_Emp):
            if self.employees[i].id == empId:
                self.employees[i].money -= deduction
                return

    def reward(self, empId, reward):
        len_of_Emp = len(self.employees)
        for i in range(len_of_Emp):
            if self.employees[i].id == empId:
                self.employees[i].money += reward
                return

    def check_lateness(self, empId, moveHour):
        pass

    @staticmethod
    def calculate_lateness(self, targetHour, moveHour, distance, velocity):
        pass

    @classmethod
    def change_emps_num(num):
        employeesNum = num