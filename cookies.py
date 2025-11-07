#initial user inputs
name = input('Please enter your name: ')
address = input('Enter street address: ')
city = input('Enter city: ')
state = input('Enter state: ')
zipcode = input('Enter Zipcode: ')
number = int(input('Enter telephone number: '))
major = input('Enter your major: ')
cookies = int(input('Enter the number of cookies wanted: ') )
print(' ')

#printing the user inputs given
print(name)
print(address)
print(city, end= ' ')
print(state, end= ' ')
print(zipcode)
print(number)
print(major)
print(' ')

#calculating the amount of ingredients for the cookies wanted
sugar = 0.3125 * cookies
butter = 0.0208 * cookies
flour = 0.0571 * cookies

#printing the amount of cookie ingredients given for the cookies wanted
print (f'To make {cookies} cookies you will need:')
print (f'- {sugar} cups of sugar')
print (f'- {butter} cups of butter')
print (f'- {flour} cups of flour')

                
