"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, bonus, numContracts, commission, payType):
        self.name = name
        self.bonus = bonus
        self.numContracts = numContracts
        self.commission = commission
        self.payType = payType
        self.pay = 0

    def get_pay(self):
        return self.pay

    def __str__(self):
        if payType = 1:
            return f"{self.name} works on a monthly salary of {self.getSalary()}. Their total pay is {get_pay()}"


class SalaryWorker(Employee):

    def __init__(name, salaryAmount, bonus, numContracts, commission, payType):
        super().__init__(name, bouns, numContracts, commission, payType)
        self.salaryAmount = salaryAmount
        setPay()

    def setPay(self):
        self.pay = self.salaryAmount + self.bonus + (self.numContracts * self.commission)

    def getSalary(self):
        return self.salaryAmount


class ContractWorker(Employee):

    def __init__(name, hourlyWage, hours, bonus, numContracts, commission, payType):
        super().__init__(name, bonus, numContracts, commission, payType)
        self.hourlyWage = hourlyWage
        self.hours = hours
        setPay()

    def setPay(self):
        self.pay = (self.hourlyWage * self.hours) + self.bonus + (self.numContracts * self.commission)

    def getHourlyWage(self):
        return self.hourlyWage

    def getHours(self):
        return self.hours

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryWorker('Billie', 4000, 0, 0, 0, 1)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0, 0, 2)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
