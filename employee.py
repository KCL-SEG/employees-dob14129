"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryAmount, hourlyWage, hours, bonus, numContracts, commission, payType):
        self.name = name
        self.salaryAmount = salaryAmount
        self.hourlyWage = hourlyWage
        self.hours = hours
        self.bonus = bonus
        self.numContracts = numContracts
        self.commission = commission
        self.payType = payType

    def get_pay(self):
        return self.salaryAmount + (self.hourlyWage * self.hours) + self.bonus + (self.numContracts * self.commission)

    def __str__(self):
        if self.payType == 1:
            return f"{self.name} works on a monthly salary of {self.salaryAmount}.  Their total pay is {self.get_pay()}."
        elif self.payType == 2:
            return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour.  Their total pay is {self.get_pay()}."
        elif self.payType == 3:
            return f"{self.name} works on a monthly salary of {self.salaryAmount} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."
        elif self.payType == 4:
            return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."
        elif self.payType == 5:
            return f"{self.name} works on a monthly salary of {self.salaryAmount} and receives a commission for {self.numContracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour and receives a commission for {self.numContracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0, 1)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 100, 0, 0, 0, 2)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 0, 4, 200, 5)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 150, 0, 3, 220, 6)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 1500, 0, 0, 3)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 120, 600, 0, 0, 4)
