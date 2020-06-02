# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry', 'Corinna Cortes']

# Concatenate both the strings
new_class=class_1+class_2
print('new_class', new_class)

# Append the list
new_class.append('Peter Warden')
# Print updated list
print('new_class', new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print('new_class', new_class)


# Create the Dictionary
courses={"Math":[65], "English":[70], "History":[80], "French":[70], "Science":[60]}
print('courses',courses)

# Slice the dict and stores  the all subjects marks in variable
values=list(courses.values())
print('values',values)

# Store the all the subject in one variable `Total
total=65+70+80+70+60
# Print the total
print('total',total)


# Insert percentage formula
percentage=total/500*100
#print the percentage
print('percentage',percentage)













# Create the Dictionary 
mathematics={"Geoffrey Hinton":[78], "Andrew Ng":[95], "Sebastian Raschka":[65], "Yoshua Benjio":[50], "Hilary Mason":[70], "Corinna Cortes":[66], "Peter Warden":[75]}
# print the dictionary
print('mathematics',mathematics)
# topper in mathematics
topper=max(mathematics,key=mathematics.get)
print('topper',topper)

#split topper
first_name, last_name= topper.split()
print('first_name:', first_name, 'last_name:', last_name)

# Concatenate the string
full_name= last_name+ ' ' +first_name
# print the full_name
print('full_name:' , full_name)
# print the name in upper case
certificate_name= full_name.upper()
print('certificate_name:', "'{}'" .format(certificate_name))

# Code ends here


