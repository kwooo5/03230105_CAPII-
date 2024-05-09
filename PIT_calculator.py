# first we have to initilize the employee object with the following attributes 
#  calculates the tax owned bt the employees based on their incopme and other attributes
class Employee:
    def __init__ (self, name, income, income_source,num_children, employee_type,organization_type):
        self.name = name 
        self.income = income 
        self.income_source = income_source 
        self.num_children = num_children
        self.employee_type = employee_type
        self.organization_type = organization_type

    def calculate_deductions(self): # its an instance of the class to calculate the deductions for the employee
        deductions = 0 #this will be used to keep track of total deductions for the employee
        if self.income_source == 'salary':
            if  self.employee_type == 'Regular' or (self.employee_types == 'contract'and self.organization_type != 'Government'):
                deductions += min(self.income * 0.1, 300000) # NPPF contributions 
                deductions += self.income * 0.3  # 30% on gross other income
        educations += 350000 * min(self.num_children, 2)  # education allowance up to maximum of Nu. 350000 per child
        deductions += min(self.income, 350000)# the self education allowance up to maximum of Nu. 350000 per taxpayer
        return deductions

    def calculate_tax(self):# calculating taxable income by subtracting by the deductions from employee's income
        taxable_income = self.income - self.calculate_deductions()
        tax_rates = [             # it defines a list of tuples which contains taxable income corresponding to tax rates
            (300000, 0),
            (100000, 0.1),
            (250000, 0.15),
            (350000, 0.2),
            (350000, 0.25),
            (500000, 0.3),
        ]
        tax = 0 
        prev_limit = 0           # initializing tax variable to 0 and pervious limit to 0
        for limit, rate in tax_rates:
            if taxable_income > limit:      # iterate over the tax rate and if the taxable income is greater than the current limit 
                tax += (limit - prev_limit) * rate   # then calculate tax owned for the current tax rate range 
                prev_limit = limit
        if taxable_income > 1000000:            # if the taxable income is greater than 1000000 then we calculate the additional tax owned for the excess amount
            tax += (taxable_income - 1000000) * 0.1
        return max(tax, 0) # it return the maximum of the calculate tax or 0

# Input values
name = input('Enter your Name: ')
employee_type = input('Enter type of employee (Regular/Contract): ')
organization_type = input('Enter Organization type (Government/Corporate/Private): ')
income_source = input('Income source is salary(y/n): ')
income = float(input('Enter your Salary: ' )) * 12 # converts monthly salary to annual by myultiplying with 12
num_children = int(input('Enter Number of children: '))

# Creating an instance of the Employee class
emp = Employee(name, income, income_source, num_children, employee_type, organization_type)

# Calculating tax for the employee
tax = emp.calculate_tax()
print(f"The tax for {name} is: {tax:.2f}")