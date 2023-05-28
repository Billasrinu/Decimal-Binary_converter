try:
    menu= int(input('Chosee an option from below\n 1. Deciaml to binary converter\n Binary to Decimal converter\nEnter the option :'))
    if menu <1 or menu>2:
        raise ValueError
    elif menu == 1:
        print('Enter the decimal number :')
        num = int(input())  
        print(f'Decimal {num} in binary is {bin(num)[2:]} ')
    elif menu == 2:
        print('Enter the binary number :')
        num = input()
        print(f'{num} in binary is {int(num,2)} in decimal')
except ValueError:
    print('Invalid option')
finally:
    print('Thank you for using the converter')

