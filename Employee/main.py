from Person import Person
from Employee import Employee

p1 = Person("eman", 1000, "happy", 1)
print(p1)
p2 = p1.sleep(5)
print(p2)
p3 = p1.eat(1)
print(p3)

e1 = Employee(1, "audi", "e@gmail.com", 1000, 100, "eman", 1000, 1)
print(e1)
e2 = Employee(1, "audi", "emanhesham@gmail.com", 1000, 100, "eman", 1000, 1)
print(e2)
e3 = e2.work(12)
print(e3)
e4 = Employee(1, "audi", "emanhesham@gmail.com", 800, 100, "eman", 1000, 1)
print(e4)