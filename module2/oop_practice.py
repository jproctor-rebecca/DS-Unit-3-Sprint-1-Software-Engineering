'''
building an exotic pet class
'''
names = ['Roger', 'Stuart', 'Rossetta', 'Karla', 'Cep']
colors = ['red', 'yellow', 'green', 'blue', 'purple', 'rainbow']
species = ['fish', 'snake', 'bird', 'frog', 'whale', 'dog']



# create animal class
class ExoticAnimals:
    # instantiate class attributes
    '''
    height is an integer value
    weight is an integer value
    legs is an integer value
    mammals is a boolean value
    '''
    def __init__(self, height, weight, color, legs, species, mammal=True):
        self.height = int(height)
        self.weight = int(weight)
        self.color = color
        self.legs = int(legs)
        self.species = species
        self.mammal = bool(mammal)

    # create method
    def move(self, distance, direction):
        return f'{self.name} travels {distance} meters in {distance} direction!'

    # create method
    def eat(self, food):
        return f'Yum, Yum! I love {food}!'
    
# inheritance class
class Anaconda(ExoticAnimals):
    def __init__(self, height, weight, color, legs=0, species=snake, mammal=False):
        super().__init__(self, height, weight, color, legs, species, mammal)
    
    # create inherited method
    def move(self, distance, direction):
        return f'{self.name} slithers {distance} meters in {distance} direction!'

# note that the second parent method is available to the child class


# create an animal
def create_animal():
    print('Hello!  Please enter the following to create your animal: ')
    n = input("What is your animal's name?")
    h = input("What is your animal's height?")
    w = input("What is your animal's weight?")
    c = input("What is your animal's color?")
    l = input("What is your animal's number of legs?")
    s = input("What is your animal's species?")
    m = input("Is your animal a mammal? True or False")
    dist = input("How far will your animal travel?")
    dirc = input("In which direction will your animal travel?")
    user_animal = ExoticAnimal(name=n, weight=w, color=c, legs=l, species=s, mammal=m)
    
    print(user_animal.move(dist, dirc))

# create a function that creates lots of animals
def lots_of_animals(n):
    a_name = random.choice(names)
    a_height = random.randint(5, 501)
    a_weight = random.randint(2, 2001)
    a_color = random.choice(colors)
    a_legs = random.randint(0, 5)
    a_species =random.choice(species_names)
    if a_species == 'dog' or a_species == 'whale':
        a_mammal = True
    else:
        a_mammal = False
    a_animal = ExoticAnimals(a_name, a_height, a_weight, a_color, a_legs, a_legs, a_species)
    animals.append(a_animal)
    return animals
