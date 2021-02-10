from termcolor import colored

def add(a,b):
    print(colored((a,b,a+b), "yellow"))
    return a+b
