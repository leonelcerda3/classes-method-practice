BOLD = "\033[1m"
END = "\033[0m"

class Dog:

    def __init__(self, name, age):
        
        self.name = name
        self.age = age 

    
    def get_name(self):
        return self.name
    
    def set_name(self, newname):
        self.name = newname
    

        
    
    

buddy = Dog("Buddy", 3)

print(buddy.name)
print(buddy.age)

newname = input("What should the new dog name be: ")

buddy.set_name(newname)

#buddy.name = newname "does the same just for simpler getters and setters"

print(f"New dog name is now {BOLD}{buddy.get_name().upper()}{END}")



