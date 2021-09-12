person = {

    "f_name": "Markel",
    "l_name": "Samuel",
    "age": "19",
    "hometown": "Columbia, SC",
    "current city": "Anderson",
    "username": "msamuel117",
}
print(person)
print(person["f_name"])
print(person["l_name"])
print(person["age"])
print(person["hometown"])
print(person["current city"])
print(person["username"])
print(f"Hello my name is {person['f_name' ]} {person['l_name']}, I'm {person['age']} years old. I'm from {person['hometown']}, but I currently live in {person['current city']}. My username is {person['username']}.")

definitions = {
    "python": "Python is a high-level general-purpose programming language.",
    "variable": "Variable is a element, feature, or factor that is liable to vary or change.",
    "list": "List is a number of connected items or names written or printed consecutively, typically one below the other.",
    "method": "A method is a function that is available for a given object because of the object's type.",
    "if statement": "If statement is a programming conditional statement that, if proved true, performs a function or displays information.",
    "dictionary": "Dictionary is a set of words or other text strings made for use in applications such as spelling checkers.",
    "function": "Function is a relationship or expression involving one or more variables.",

}
print('\n')
print(definitions["python"])
print('\n')
print(definitions['variable'])
print('\n')
print(definitions["list"])
print('\n')
print(definitions["method"])
print('\n')
print(definitions["if statement"])
print('\n')
print(definitions["dictionary"])
print('\n')
print(definitions["function"])


#Create a dictionary that contains 6 South Carolina county names with their respective county capital/seat (link (Links to an external site.)).
sccounties = {
    "Abbeville": "Abbevile County",
    "Aiken": "Aiken County",
    "Allendale": "Allendale County",
    "Anderson": "Anderson County",
    "Bamberg": "Bamberg County",
    "Barnwell": "Barnwell County",

}
print('\n')
#Create a list of 10 South Carolina counties.
sccounties2 = [
    'Abbeville County', 'Aiken County','Allendale County', 'Andesron County', 'Bamberg County', 'Barnwell County', 'Beaufort County', 'Berkeley County', 'Calhoun County', 'Charleston County'
               ]
for counties in sccounties2:
    print(counties)

for counties in sccounties:
    print(f"County Name is in our dictionary, and the capital is {counties}.")

else:
    print("If your county name isn't list its not in our dictionary. We will add this county shortly. Thanks!")

print('\n')

#Create a list of 5 cities that are within a county of your choice (1 must be the capital, 4 can be any other city/town within the county).
andersoncounty = [
    'Anderson', 'Pendleton', 'Piedmont', 'Powdersville', 'Williamston',
]

for capital in andersoncounty:
    print(capital)

x = sccounties.keys()
print(x)

for capital in x:
    print('City Name is not a capital of any South Carolina county')

else:
    print('Anderson is a capital of any South Carolina county')

print('\n')
#Nesting. Create 5 dictionaries, each a SC county. Within each dictionary, have 5 cities (key) and the value is population number. Create a new list, each item being a South Carolina county dictionary.
berkleycounty = {'Alvin': 7337, 'Moncks Corner': 10743, 'Hannahan': 24353, 'Huger': 3590, 'Goose Creek': 41978}
richlandcounty = {'Columbia': 133273, "Hopkins": 2719, "Eastover": 749, "Forest Acres": 10412, "Dentsville": 15153}
greenvillecounty = {'Greenville': 67737, 'Mauldin': 25217, "Taylors": 22230, "Wade Hampton": 20906, "Parker":12227}
lexingtoncounty = {'Lexington': 21334, 'Pelion': 695, 'West Columbia':17641, 'Chapin': 1940,'Seven Oaks': 15484}
collentoncounty = {'Walterboro': 5477, 'Cottageville': 885, 'Edisto': 2301, 'Williams': 193, 'Smoaks': 109,}

countiestest = [berkleycounty, richlandcounty, greenvillecounty, lexingtoncounty, collentoncounty]

# Using the list, loop through each dictionary and print a statement that says "In CityName, CountyName, the current population is Population".
for key,value in berkleycounty.items():
    print("{}, Berkley County, the current population is {}".format(key, value))
print('\n')
for key,value in richlandcounty.items():
    print("{}, Richland County, the current population is {}".format(key, value))
print('\n')
for key,value in greenvillecounty.items():
    print("{}, Greenville County, the current population is {}".format(key, value))
print('\n')
for key,value in lexingtoncounty.items():
    print("{}, Lexington County, the current population is {}".format(key, value))
print('\n')
for key,value in collentoncounty.items():
    print("{}, Collenton County, the current population is {}".format(key, value))
print('\n')

# Create 1 dictionary titled sc_counties. This dictionary should have 5 keys. Each key should have a list as the value. This list should have the three largest cities in that county.
sc_counties ={
    "Richland county": ['Columbia', 'Forest Acres', 'Arcadia Lakes'],
    "Charleston county": ['Mount Pleasant', 'Isle of Palms', 'Folly Beach'],
    "Greenville county": ['Greenville', 'Simpsonville', 'Mauldin'],
    "Horry county": ['Conway', 'Myrtle Beach', 'North Myrtle Beach'],
    "Aiken county": ['Aiken', 'Graniteville', 'North Augusta'],
}
for key,value in sc_counties.items():
    print("In {} the largest cities are {}".format(key, value))

print('\n')

#Write a program that asks a user/student for their name, and welcomes them to Anderson University
name = input("Enter your name: ")
print("Hello " + name + " welcome to Anderson University.")

#Write a program that asks how much money they have. Create some type of if-elif-else, or multiple if statements (however you see fit) that prints off which processor they can afford to buy (i3, i5, i7, and/or i9).
i3 = 120
i5 = 220
i7 = 600
i9 = 1200

pocket = int(input("What does your budget look like: "))

if pocket >= i9:
    print('You can afford our i3, i5, i7, and i9 processor option. ')
elif pocket >= i7:
    print('You can afford our i3, i5, and i7 processor option. ')
elif pocket >= i5:
    print('You can afford our i3 and i5 processor option. ')
elif pocket >= i3:
    print('You can afford our i3 processor option. ')
else:
    print("You can't afford any processor options today. Whenever your ready to exit type out. ")

active = True
while active:
    if pocket == 'out':
        active = False
    else:
        print('Thank for stopping by come and see us again. ')
        active = False
