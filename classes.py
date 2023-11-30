# classes are the blue print that help us build any thing in code.
# classes are made up of properties and behaviors
# objects are the product built out of classed


class Person:
    def __init__(self, name, age):  # inistatiating the function
        self.name = name  # defining name property
        self.age = age  # defining age property


wang = Person('wang', 23)  # declaring object
joyce = Person('joyce', 36)  # declaring object

print('Hello, my name is ' + wang.name +
      ',I am ' + str(wang.age) + ' years old')
# printing object name and concatenating it with age
print('Hello, my name is ' + joyce.name +
      ',I am ' + str(joyce.age) + ' years old')
