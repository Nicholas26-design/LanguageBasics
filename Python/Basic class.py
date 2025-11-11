# A class in python is like a blueprint.
class Person:
    def __init__(self, name, age):
        """
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        Notes:
            the __init__() function assigns values to object properties
            instance variable/object property = parameter passed and used for value assignment
        """
        self.name = name
        self.age = age
        
    # Method
    def intro(self):
        """
        Get name of the person.

        Returns:
        str: A formatted string containing the person's name.
        """
        input_name = print("Hello my name is " + self.name)
        return input_name

# Creating an instance of the class and assigning it to a variable
person_instance = Person("Nicholas", 30)

# Accessing methods
person_instance.intro()

# Accessing the attribute 'name' of the created instance
print(person_instance.name)  # This will print "Nicholas"
