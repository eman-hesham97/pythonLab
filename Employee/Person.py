class Person:

    def __init__(self,name, money, mood, healthRate=1):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
            return self.mood
        elif hours<7:
            self.mood = "Tired"
            return self.mood
        else:
            self.mood = "Lazy"
            return self.mood

    def eat(self, meals):
        if meals == 3:
            self.healthRate = "health rate is 100%"
            return self.healthRate
        elif meals == 2:
            self.healthRate = "health rate is 75%"
            return self.healthRate
        elif meals == 1:
            self.healthRate = "health rate is 50%"
            return self.healthRate
        else:
            print("Health rate is a value between 1 and 3")

    def buy(self, items):
        if items != 0:
            self.money = self.money - 10