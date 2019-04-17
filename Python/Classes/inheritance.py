class Parent():
    def __init__(self, last_name, eye_color):
        #print ("Parent Contstructor called")
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_stuff(self):
        #print("Hello")
        print("Parent Show Stuff. LN:" + self.last_name + ", EC:" + self.eye_color)
        #arg2 = arg1
        
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        #print ("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_stuff(self):
        Parent.show_stuff(self)
        print("Child. NoT:" + str(self.number_of_toys))
        
billy_cyrus = Parent("Cyrus", "blue")
#print (billy_cyrus.last_name);

miley_cyrus = Child("Cyrus", "Blue", 5)
billy_cyrus.show_stuff()
miley_cyrus.show_stuff()
#print(miley_cyrus.number_of_toys)

    
