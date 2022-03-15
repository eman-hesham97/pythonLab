from Person import Person
import re
from Car import Car

def emailValidation(email):
    rgx = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(rgx, email)):
        return True
    else:
        return False

class Employee(Person):

    moods = ["Happy" , "Tired" , "Lazy"]
    def __init__(self, id, car, email, salary, distanceToWork, name, money, healthRate):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        super().__init__(name, money, healthRate)
        mail_is_valid = emailValidation(self.email)
        if self.salary < 1000:
            print("The minimum value of salary is 1000")
        if mail_is_valid!=True:
            print("Invalid email! please enter a valid one.")
        if self.healthRate<0 and self.healthRate>100:
            print("Health Rate is a value between 0 and 100")

    def work(self, hours):
        if hours == 8:
            return self.moods[0]
        elif hours > 8:
            return self.moods[1]
        elif hours < 8:
            return self.moods[2]
        else:
            print("Invalid Input!")

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = self.car.fuelRate + gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        send_mail_valid = emailValidation(self.to)
        if send_mail_valid!=True:
            print("Invalid email! please enter a valid one.")
        with open(f"{subject} to {to}.txt", 'w') as email:
            message = f"From: {self.email}\n" \
                      f"To: {to}\n\n" \
                      f"Hi, {receiver_name}\n" \
