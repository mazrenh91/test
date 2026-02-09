# # basic class definition
# class Person:
#     # class attribute (shared by all instances)
#     species = "homo sapiens"

#     # constructor method
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # instance method
#     def introduce(self):
#         return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
#     # method with parameters
#     def have_birthday(self):
#         self.age += 1
#         return f"Happy birthday! {self.name} is now {self.age}."

# # creating objects (instances)
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)

# # accessing attributes
# print(person1.name)     # "Alice"
# print(person1.age)      # 25

# # calling methods
# print(person1.introduce())
# print(person1.have_birthday())

# # class attributes
# print(Person.species)   # "homo sapiens"
# print(person1.species)  # "homo sapiens"

# # # ----------------------------------------------------------------- # # #

# class BankAccount:
#     def __init__(self, account_number, owner, balance=0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = balance
#         self.transaction_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transaction_history.append(f"Deposited ${amount}")
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount"
        
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             self.transaction_history.append(f"Withdrew ${amount}")
#             return f"Withdrew ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid withdrawal amount or insufficient funds"
    
#     def get_balance(self):
#         return f"Current balance: ${self.balance}"
    
#     def get_transaction_history(self):
#         return self.transaction_history
    
#     # using the BankAccount class
# account = BankAccount("123456789", "Azren", 100000)
# print(account.deposit(500))  # Deposited $500. New balance: $100500
# print(account.withdraw(200)) # Withdrew $200. New balance: $100300
# print(account.get_balance())  # Current balance: $100300
# print(account.get_transaction_history())  # ['Deposited $500', 'Withdrew $200']

# # # ----------------------------------------------------------------- # # #

# create a simple game character class with health, attack and heal methods
class GameCharacter:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"{self.name} attacked and took {damage} damage. Health is now {self.health}."

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        return f"{self.name} healed by {amount}. Health is now {self.health}."
    
# using the GameCharacter class
character = GameCharacter("Hero")
print(character.attack(30))  # Hero attacked and took 30 damage. Health is now 70.
print(character.heal(20))    # Hero healed by 20. Health is now 90.
print(character.attack(100)) # Hero attacked and took 100 damage. Health is now 0.
print(character.heal(150))   # Hero healed by 150. Health is now 100.

