class Dog:
 def __init__ (self, name, age):
   self.name = name
   self.age = age
 
 def bark(self):
   print("woof! woof! arf arf daddy")
   
 def celebrateBirthday(self):
  self.age += 1
  print(f"happy birthday {self.name}, you are now {self.age} years old! tiguwang na kayka<3")

 def getInfo(self):
  return f"Dog name: {self.name},  Age: {self.age}"
 
troy = Dog("Troy", 21)
troy.bark()
troy.celebrateBirthday()
print(troy.getInfo())