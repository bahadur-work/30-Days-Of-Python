print()
print('1. Addition of 2+3 =', 2+3)  # addition(+)
print('2. Subtraction of 3-2=', 3-2)   # subtraction(-)
print('3. Multiplication of 3*2=', 3*2)   # multiplication(*)
print('4. Division of 3/2=', 3/2)  # division(/)
print('5. 3 to the power 2 =', 3**2) # exponential(**)
print('6. 3 mod 2 =', 3%2) # modulus(%)
print('7. 3 floor devided by 2 =', 3//2)# Floor division operator(//)
print()

print('Check all datatypes:')
print()
print('1. type(10) is ', type(10)) #int
print('2. type() is ', type(3.24)) # Float
print('3. type(2+3j) is ', type(2+3j))# Complex
print('4. type("string") is ', type('string'))# String
print('5. type([1,2,3]) is ', type([1,2,3])) # List is ordered and changeable. Alows duplicate items.
print('6. type({"name:bahadur"}) is ', type({'name':'bahadur'}))# Dictionary is a key value pair. Ordered and changeable but without dublicate pairs. 
print('7. type({9.8, "string", 10.2}) is', type({9.8, 'string', 10.2}))# Set is unordered, uncahnageable and unindexed. No duplicates.
print('8. type((9.8, "string", 10.2)) is', type((9.8, 'string', 10.2)))# Tuple is ordered, unchangeable, allows dublicates.

print(
    '\nList is a collection which is ordered and changeable. Allows duplicate members.\nTuple is a collection which is ordered and unchangeable. Allows duplicate members.\nSet is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.\nDictionary is a collection which is ordered** and changeable. No duplicate members.'
)

print()
print('1. List is ordered, changeable and allows duplicates: ',[1,2,3,1])
print('2. Touple is ordered, unchangeable and allows duplicates' ,(1,2,3,1))
print('3. Set is unordered, unchangeable, unindexed and does not allow duplicates', {1,2,3,1})
print('4. Dictionary is keyValue pair. Ordered, changeable, no duplicate pairs',{'Name':'Bahadur','Sex':'Male','Age':'30'})
print()
