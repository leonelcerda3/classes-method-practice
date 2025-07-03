BOLD = "\033[1m"
END = "\033[0m"

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    
    def is_new_dog(self):
        return new_dog_name
        
    
    

buddy = Dog("Buddy", 3)

print(buddy.name)
print(buddy.age)

new_dog_name = input("What should the new dog name be: ")

print(f"New dog name is now {BOLD}{buddy.is_new_dog().upper()}{END}")


#print(f"New dog name is now", {BOLD}buddy.is_new_dog().upper(){END})