import sys

print(sys.version)
print(sys.executable)

def greet(person):
    greeting = 'Hello, {}'.format(person)
    return greeting

print(greet('Cocoa'))