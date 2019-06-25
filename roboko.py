import csv


class Roboko(object):
    def __init__(self):
        print("Hi! I'm Roboko. What's your name?")
        self.name = input()
    def ask_favorite_restaurant(self):
        print(self.name, 'which restaurant do you like？')

    def greetings(self):
        print(self.name, 'thank you. \nhave a good day!')
    def check_favorite_restaurant(self, restaurant_name):
        print(self.name, 'do you like',restaurant_name,'？[Yes/No]')


roboko = Roboko()
try:
    with open('restaurant.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['Name'], row['Count'])
            restaurant_name = row['Name']
            count = row['Count']

            roboko.check_favorite_restaurant(restaurant_name)
            if_you_like_or_not = input()
            if if_you_like_or_not not in ['yes', 'YES', 'Yes','no','NO','No']:
                roboko.check_favorite_restaurant(restaurant_name)
                if_you_like_or_not = input()


    roboko.ask_favorite_restaurant()
    favorite_resutaurant_name = input()
    # data.append(favorite_resutaurant_name)
    # data.append(1)
    with open('restaurant.csv', 'r+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow({'Name': favorite_resutaurant_name, 'Count': 1})


    roboko.greetings()

    # with open('restaurant.csv', 'r+') as csv_file:
    #     reader = csv.DictReader(csv_file)
    #     for row in reader:

except:
    roboko.ask_favorite_restaurant()
    favorite_resutaurant_name = input()

    with open('restaurant.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name': favorite_resutaurant_name, 'Count': 1})
    roboko.greetings()
