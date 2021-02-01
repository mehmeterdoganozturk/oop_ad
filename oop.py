class Employee:
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

print(Employee.num_of_emp)
emp1 = Employee('erdogan', 'ozturk', 50000)
emp2 = Employee('guler', 'ozturk', 100000)
emp1.fullname()
Employee.fullname(emp1)
print(Employee.num_of_emp)

#print(emp1.first, emp1.last, emp1.pay, emp1.email)
#print(emp1.fullname())
#print(emp2.fullname() + ' ' + emp2.email)
print(Employee.fullname(emp1))
print(emp2.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp1.__dict__)
print(Employee.__dict__)


