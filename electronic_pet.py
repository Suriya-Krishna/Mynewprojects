import random

class Pet():

    print("You can feed, teach and interact with your pet now.")
    th_bore = 150
    th_hun = 100
    boredom_decrem = 15
    hunger_decrem = 20
    def __init__(self,pet_name, hunger=10, boredom = 10, sounds = []):
        self.hunger = hunger
        self.boredom = boredom
        self.sounds = sounds
        self.pet_name = pet_name

    def clock_tick(self):
            self.hunger = self.hunger + 10
            self.boredom = self.boredom + 10


    def __str__(self):
        if self.hunger >= Pet.th_hun:
            return f"I'm {self.pet_name}, i'm hungry!"
        if self.boredom >= Pet.th_bore:
            return f"I'm {self.pet_name}, i'm bored!"
        else:
            return f"I'm {self.pet_name}, i'm okay!"



    def reduce_boredom(self):
        if self.boredom>0:
            self.boredom = self.boredom - Pet.boredom_decrem

    def reduce_hunger(self):
        if self.hunger>0:
            self.hunger = self.hunger - Pet.hunger_decrem


    def teach(self, new_word):
        Pet.reduce_boredom(self)
        self.sounds.append(new_word)


    def hi(self):
        if len(self.sounds)!=0:
           know_word = random.choice(self.sounds)
           print(f"I Know a word, {know_word}. It's cool!")
           Pet.reduce_boredom(self)
        else:
            print("I don't know anything")

    def feed(self):
        Pet.reduce_hunger(self)
pets_list = {}
pet1 = Pet("Boogie")
pet2 = Pet("Huskiee")
pet3 = Pet("Grug")
pets_list[1]=pet1
pets_list[2]=pet2
pets_list[3]=pet3
c = 'y'
n = 3
while c=='y':
    option = int(input("Select your activity :1.Adopt a new pet ,2.Interact with an existing one."))
    if option == 1:
        name = input("Enter the pet name you want")
        pet_new = Pet(name)
        pets_list[n+1]= pet_new
        print("You can teach your pet new words")
        word = input("Give a word")
        pet_new.teach(word)
    elif option == 2:
        print(pets_list)
        fav_pet = int(input("select your favourite pet: "))
        for key in pets_list:
            if key == fav_pet:
                obj = pets_list[key]

        print("You have three ways to interact, g: Greet, t: Teach, f:Feed")
        opt = input("What do you wanna do?")
        if opt == 'g':
              obj.hi()
        elif opt == 't':
            word1 = input("give the word you want to teach")
            obj.teach(word1)
            obj.hi()
        elif opt == 'f':
            obj.feed()

    c = input("do you want to contnue? y/n")
for key in pets_list:
    mn = pets_list[key]
    mn.clock_tick()
status = int(input("Enter the state of pet you want to know"))
print(pets_list[status])

