"""" PayRoll processor
 """

class Employee:
    def __init__(self, name):
        self.name = name

    def Pay_calculate(self, salary=0, hourlyrate=0, hoursworked=0):
        if hourlyrate and hoursworked:
            print("Salary for", self.name, ": ", hourlyrate * hoursworked)
        else:
            print("Salary for", self.name, ": ", salary)


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class HourlyWorker(Employee):
    def __init__(self, name, hourlyRate, hoursWorked):
        super().__init__(name)
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked


salariedEmployee = SalariedEmployee("nithish", 100000)
hourlyWorker = HourlyWorker("cr7", 360, 24)
salariedEmployee.Pay_calculate(10000)
hourlyWorker.Pay_calculate(hourlyrate=360, hoursworked=24)
