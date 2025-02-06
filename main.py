# mad libs!
# The starting menu gives the user a choice of four stories to choose from.
# Depending on the story, cycle through the necessary prompts for the blanks.
# Print the new story with the user selected words.
# Use .isalpha() to ensure all the entries are only letters and .lower() for
# formatting.
# The above still needs work.
# Bonus round! Use choice() to generate random responses from the category 
# list if prompted.
# let's get into it!

# Choice from the random module for generating random stories
from random import choice 


# Category lists lists for the program generated mad libs.
# two lists for nouns and adjectives to ensure the generated mad libs don't 
# use the same word for both gaps

adjective_list = ['magnificent', 'serene', 'ethereal', 'vibrant', 'smelly', 'hungry']
adjective_two_list = ['mysterious', 'silly', 'cranky', 'cheeky', 'awkward', 'bizarre']
animal_list = ['lion', 'tiger', 'bear', 'penguin', 'unicorn', 'giraffe', 'whale', 'dolphin']
city_list = ['London', 'Tokyo', 'Nashville', 'Vilnius', 'Barcelona', 'Dubai']
color_list = ['chartreuse', 'magenta', 'blue', 'orange', 'dark green', 'gold', 'yellow']
noun_list = ['moon', 'phone', 'computer', 'door', 'window', 'song']
noun_two_list = ['tree', 'cloud', 'book', 'ball', 'water bottle', 'building']
number_list = ['5000', '1234', '4643', '2424', '1870', '3242']
occupation_list = ['nurse', 'bin man', 'teacher', 'dental hygienist', 'thief', 'fireman', 'pilot']
vegetable_list = ['beet', 'spinach', 'cucumber', 'potato', 'celery', 'broccoli', 'lettuce']


# the function will start with a while loop (my favourite) to keep the game running. 
def mad_lib():
    while True:
        print('\nChoose a story!')
        print('1. The Mysterious Island')
        print('2. The Fantasic Voyage')
        print('3. Time Traveling Train')
        print('4. Alien Invasion')
        print('5. Exit the game')

        story = input('Choose a story (1-4): ')
        # Error for choice
        if story not in ['1', '2', '3', '4', '5']:
            print(
                'Error: Please enter a number between 1 and 4 for a story. Enter 5 to exit.'
            )

        if story == '5':
            print('\nThanks for playing, bye bye now!')
            break

        # Give the user the option to fill in the mad lib themselves 
        # or get a program generated response
        elif story in ['1', '2', '3','4']:
        
            print('\nDo you want to...')
            print('1. Add your own responses')
            print('2. Generate responses')
            print('3. Back to menu')

            response = input('How would you like to proceed: ')
            # Error for response
            if response not in ['1', '2', '3']:
                print("Error: Invalid entry")
 
            # There's always at least one noun and adjective, 
            # placing this code here to reduce repeating code 
            if response == '1':
                print('\nPlease provide the following:')
                adjective = input('An adjective: ').lower()
                noun = input('A noun: ').lower()
                
                # Collects unique user inputs and displays the story
                if story == '1':
                    
                    adjective_two = input('Another adjective: ').lower()
                    color = input('A color: ').lower()
                    noun_two = input('Another noun: ').lower()

                    print(
                        f'''\n
                        The shipwrecked sailors washed ashore on a {adjective} island. 
                        They explored the island, discovering a hidden {noun}, 
                        a waterfall cascading into a {color} pool,
                        and a {noun_two} that spoke in a {adjective_two} voice.'''
                    )

                elif story == '2':

                    animal = input('An animal: ').lower()
                    color = input('A color: ').lower()
                    
                    print(
                        f'''\n
                        In a {color} submarine, the explorers journeyed to the 
                        deepest part of the ocean. They encountered {adjective} fish, 
                        a giant {animal}, and a lost city made of {noun}.'''
                    )

                elif story == '3':

                    city = input('A city: ').capitalize()
                    color = input('A color: ').lower()
                    number = input('A four digit number: ').lower()

                    # ensuring number is digits and the correct length
                    if number.isdigit() == False or len(number) != 4:
                        print("Error: the number must be four digits long. eg. '1234'")
                        number = input('Please enter a four digit number: ').lower()

                    print(
                        f'''\n
                        The {color}, rusty train chugged along the tracks, 
                        transporting passengers through {city}. One rainy night, 
                        the train mysteriously arrived in the year {number}, 
                        where they met a {noun} and learned about life in the 
                        {adjective} past.''' 
                    )
                
                elif story == '4':

                    animal = input('An animal: ').lower()
                    city = input('A city: ').capitalize()
                    noun_two = input('Another noun: ').lower()
                    occupation = input('An occupation: ').lower()
                    
                    print(
                        f'''\n
                        The citizens of {city} were startled by the arrival of {adjective} 
                        spaceships. The {noun} emerged, looking like a cross between a 
                        {animal} and a {vegetable}. Luckily, a brave {occupation} used their 
                        knowledge of {noun_two} to scare the aliens away.'''
                    )


            # choice() to generate random stories from category lists
            elif response == '2':
                adjective = choice(adjective_list)
                adjective_two = choice(adjective_two_list)
                animal = choice(animal_list)
                city = choice(city_list)
                color = choice(color_list)
                noun = choice(noun_list)
                noun_two = choice(noun_two_list)
                number = choice(number_list)
                occupation = choice(occupation_list)
                vegetable = choice(vegetable_list)

                # Store the mad lib in a variable to catch the choice() variables.
                mysterious_island =  f'''\n
                                The shipwrecked sailors washed ashore on a {adjective} island. 
                                They explored the island, discovering a hidden {noun}, 
                                a waterfall cascading into a {color} pool,
                                and a {noun_two} that spoke in a {adjective_two} voice.'''

                fantastic_voyage =  f'''\n
                                In a {color} submarine, the explorers journeyed to the 
                                deepest part of the ocean. They encountered {adjective} fish, 
                                a giant {animal}, and a lost city made of {noun}.'''

                time_traveling_train = f'''\n
                                The {color}, rusty train chugged along the tracks, 
                                transporting passengers through {city}. One rainy night, 
                                the train mysteriously arrived in the year {number}, 
                                where they met a {noun} and learned about life in the 
                                {adjective} past.'''

                alien_invasion = f'''\n
                                The citizens of {city} were startled by the arrival of {adjective} 
                                spaceships. The {noun} emerged, looking like a cross between 
                                a {animal} and a {vegetable}. Luckily, a brave {occupation} 
                                used their knowledge of {noun_two} to scare the aliens away.'''
                
                if story == '1':
                    print(mysterious_island)

                elif story == '2':
                    print(fantastic_voyage)

                elif story == '3':
                    print(time_traveling_train)

                elif story == '4':
                    print(alien_invasion)
            
            # Returns the user to main menu.
            elif response == '3':
                mad_lib()

# Function call to start the menu
mad_lib()