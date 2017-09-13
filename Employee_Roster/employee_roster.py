class Employee(object):
    num_of_empl = 0
    raise_amount = .04
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@company.com"

        Employee.num_of_empl += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def employee_raise(self):
        self.salary = int(self.salary * self.raise_amount)

class Developer(Employee):

    raise_amount = .06

    def __init__(self,first,last,salary,prog_lang):
        #super().__init__(first,last,salary)
        Employee.__init__(self,first,last,salary)
        self.prog_lang = prog_lang

class Manager(Employee):

    raise_amount = .08

    def __init__(self,first,last,salary,employees=None):
        #super().__init__(first,last,salary)
        Employee.__init__(self,first,last,salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

def add_empl(self, empl):
    if empl not in employees:
        self.employees.append(empl)

def remove_empl(self, empl):
    if empl in self.employees:
        self.employees.remove(empl)

def print_empl(self):
    for empl in self.employees:
        print "--->", empl.fullname

    

dev1 = Developer("Jesus", "Franco", 65000,"Python")
emp2 = Employee("Ruben", "Vences", 55000)
print emp2.raise_amount
print emp2.salary
print emp2.email
mgr_1 = Manager("Brian", "Palowski", "95000", [emp2])
print Employee.num_of_empl
mgr_1.print_empl.fullname()