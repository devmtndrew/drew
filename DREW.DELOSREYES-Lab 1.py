ID Number: 205637
Surname: de los Reyes
Year and Course: 2 BS ITE

def dollars_to_pesos():
    dollars_to_pesos = int(input('Enter the amount in US Dollars: '))
    amount = dollars_to_pesos * 50
    return amount, 'Philippine Pesos'  

def perform_operations():
    first_input = int(input('x: '))
    second_input = int(input('y: '))
    print (first_input + second_input)
    print (first_input - second_input)
    print (first_input * second_input)
    print (first_input // second_input)
    print (first_input % second_input)

def bmi():
    first_input = int(input('kg: '))
    second_input = int(input('cm: '))
    meters = second_input / 100
    convertion = (first_input / meters**(2))
    return convertion