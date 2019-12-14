from random import randrange

class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds  = ['Mrrp']

    def __init__(self,name="kitty",pet_type = 'dog'):
        
        ## this variable is introduces in side the 
        ## def __init__ so this four is the instance variabe
        ## and in the inherired class has no other 
        ## constructor
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.pet_type = pet_type
        
        
        
        # this is the clas variable
        self.sounds = self.sounds[:]
        

    def clock_tick(self):
        self.boredom += 1
        self.hunger +=1 

    def mood(self):
        if self.hunger <=self.hunger_threshold and self.boredom <=self.boredom_threshold:
            if self.pet_type=='dog':
                return "happy"
            elif self.pet_type == 'cat':
                return "happy probably"
            else:
                return "happy"
        elif self.hunger>self.hunger_threshold:
            if self.pet_type== 'dog':
                return "hungry ,arf"
            elif self.pet_type == 'cat':
                return "hungry meeeow"
            else:
                return "hungry"
        else:
            return "bored"
    
    
    def reduce_hunger(self):
        self.hunger = max(0,self.hunger-self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0,self.boredom - self.boredom_decrement)

    def feed(self):
        print ("This is calling from the parent class")
        self.reduce_hunger()

    def hi(self):
        print (self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self,word):
        self.sounds.append(word)
        self.reduce_boredom()


    
    ## converting the class in to ste

    def __str__(self):
        state = "   i am "+self.name+" ."
        state+= "  i fell"+self.mood()+" ."
        return state 
    




## inherit the class

class Cat(Pet):
    sounds = ['Mewo']

    def chasing_rats(self):
        return "what are you doing"


# p1 = Pet("Fido")
# print(p1) # we've seen this stuff before!

# p1.feed()
# p1.hi()
# print(p1)

# cat1 = Cat("Fluffy")
# print(cat1) # this uses the same __str__ method as the Pets do

# cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
# cat1.hi()
# print(cat1)

# print(cat1.chasing_rats())


## lets inherit even more

class Cheshire(Cat):

    def smile(self):
        print (":D :D :D")



# new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
# new_cat.hi() # same as Cat!
# new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
# new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
# p1 = Pet("Teddy")
# p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.




## not only we can override the propertise
## we also can overwrite the method
## if we need we can chnge the method
## or overwrite them


class Dog(Pet):
    
    ## changing the sounds
    sounds = ['woof','ruff']


    ## chaing the method
    def mood(self):
        if(self.hunger > self.hunger_threshold and self.boredom>self.boredom_threshold):
            return "bored and happy"
        else:
            return "happy"

    ## making another custom method

    def feed(self):
        Pet.feed(self)
        print ("Arf thanks from the clild class")


#c1 = Cat("Fluffy")
#d1 = Dog("Astro")
# c1.boredom = 1
# print(c1.mood())
# c1.boredom = 10
# for i in range(10):
#     print(d1.mood())
# print(d1.mood())
## so now you are in the chind class 
## can you invooke the parent class method
## of course you can invoke the parent method
## but i am taking about invoking method inside your new method
#d1.feed()


## but there are other method to call the parent method
## from the clild method

class Bird(Pet):
    sounds = ['chrip']


    def __init__(self,name='kitty',chirp_number=2):
        ## you can init the name by your self by 
        ## writing
        # self.name = name
        # or you can ask the parent class to do that
        # because you already write this kind of statement
        Pet.__init__(self,name)
        ## it will call the parent constructor and assign this for you
        ## now adding a new instance variable inside the constructor
        self.chirp_number = chirp_number

    ## overwriting the function



b = Bird()

print(b)