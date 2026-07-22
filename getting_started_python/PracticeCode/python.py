'''Round of lift'''

'''n = int(input("Enter total number of people:"))
c = int(input("Enter capacity of lift: "))

rounds = n // c
if n % c != 0:
    rounds += 1

print("Total rounds required:", rounds)'''

'''Sum of List Elements'''

'''list = []
n = int(input("Enter total no. of elements:"))
for i in range (n):
    ele = int(input("Enter element: "))
    list.append(ele)
sum = 0
for i in range (n):
    sum += list[i]
print("Sum of list elements:", sum)'''

'''Largest Element in List'''

'''list = []
n = int(input("Enter total no. of elements: "))
for i in range (n):
    ele = int(input("Enter element: "))
    list.append(ele)
largest = list[0]
for i in range (1, n):
    if list[i] > largest:
        largest = list[i]
print("Largest number is : ", largest)'''


'''Remove duplicates from list'''

'''list = []
n = int(input("Enter total no. of elements: "))
for i in range (n):
    ele = int(input("Enter element: "))
    list.append(ele)

unique = []
for i in list:
    if i not in unique:
        unique.append(i)

print("List after removing duplicates:", unique)'''


'''Check if all elements in list are unique'''

'''list = []
n = int(input("Enter total no. of elements: "))
for i in range(n):
    ele = int(input("Enter element: "))
    list.append(ele)
is_unique = True
for i in range(n):
    for j in range(i+1,n):
        if list[i] == list[j]:
            is_unique = False
            break
if is_unique:
    print("Unique elements")
else:
    print("Not unique")'''


'''Class and Object'''


'''class Employee:
    company = "ABC Ltd"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name
emp1 = Employee("John", 50000)
emp1.show_details()
Employee.change_company("XYZ Ltd")
emp2 = Employee("Alice", 60000)
emp2.show_details() '''


'''class MathHelper:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
num = int(input("Enter the number: "))
print(MathHelper.is_even(num))'''

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print("Current balance is: ", self.__balance)
user = BankAccount("Prachi", 90000)
user.deposit(10000)
user.show_balance()
user.withdraw(80000)
user.show_balance()