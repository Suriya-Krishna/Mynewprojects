class Pet():
    def __init__(self, species=None, name=""):
        self.name = name
        self.species = species
    def __str__(self):
        if self.name != "":
            return f"Species of : {self.species}, named : {self.name}"
        else:
            return f"Species of : {self.species}, unnamed"


class Dog(Pet):
    def __init__(self, name="", chases="Cats"):
        super().__init__("Dog", name)
        self.chases = chases

    def __str__(self):
        if self.name != "":
            return f"Species of Dog, named:{self.name},chases : {self.chases}"
        else:
            return f"Species of Dog,unnamed,chases : {self.chases}"


class Cat(Pet):
    def __init__(self, name="", hates="Dogs"):
        super().__init__("Cats", name)
        self.hates = hates

    def __str__(self):
        if self.name != "":
            return f"Species of Cat, named:{self.name},hates : {self.hates}"
        else:
            return f"Species of Dog,unnamed,hates : {self.hates}"
dict1={}
dict1[1]=Dog("Bruno")
dict1[2]=Dog()
dict1[3]=Dog("Sammy")
dict1[4]= Dog("Huskie")
dict1[5]= Dog()
you_option=input("Enter y if you want to create dogs")
if you_option =='y':
      num1 = int(input("number of cats you want to create"))
      for i in range(6, 7+num1):
        opt_name = input(f"Enter the {i} dog name")
        dict1[i] = Dog(opt_name)


dict2={}
dict2[1]=Cat("Diva")
dict2[2]=Cat("Lilly")
dict2[3]=Cat("silly")

you_option1=input("Enter y if you want to create cats")
if you_option1 =='y':
    num = int(input("number of cats you want to create"))
    for i in range(4, 5+num):
        opt_name1 = input(f"Enter the {i} cat name")
        dict2[i] = Cat(opt_name1)

pet_dict = {'Dog': dict1, 'Cat': dict2}
print("Let's befriend the pets")
opt = input("Enter your favourite pet(Dog/Cat)")
if opt == 'Dog':
    for key in dict1:
       print(dict1[key])
       if dict1[key].name=="":
           na1 = input("your dog is not named,give a name")
           dict1[key].name = na1
           print(dict1[key])
if opt == 'Cat':
    for key in dict2:
       print(dict2[key])
       if dict2[key].name =="":
          na =  input("your cat is not named,give a name")
          dict2[key].name=na
          print(dict2[key])

