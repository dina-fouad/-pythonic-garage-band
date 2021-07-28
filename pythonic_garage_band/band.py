
from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod

class Band:
    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)



    def play_solos(self):
      solos = []
      for item in self.members:
            solos.append(item.play_solo())
      return solos



    def __str__(self):
      return(f"i am  {self.name} and I {self.members}" )
    def __repr__(self):
      return f"Band instance. name={self.name}"

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician():

   def __init__(self,name):
    self.name=name


   def __str__(self):
      return f"My name is {self.name} and I play {self.get_instrument()}"
   

   def __repr__(self):
       return f"{self.__class__.__name__} instance. Name = {self.name}"

   @abstractmethod
   def get_instrument(self):
     pass

   @staticmethod
   def play_solos(self):
      pass


      
class Guitarist(Musician):
      def __init__(self,name):
       super().__init__(name)


      def __str__(self):
        return f"My name is {self.name} and I play guitar"

      def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

      def get_instrument(self):
       return "guitar"

      def play_solo(self):
       return "face melting guitar solo"


class Bassist(Musician):

     def __init__(self,name):
      super().__init__(name)

     def __str__(self):
        return f"My name is {self.name} and I play bass"

     def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

     def get_instrument(self):
      return "bass"

     def play_solo(self):
      return "bom bom buh bom"



class Drummer(Musician):

     def __init__(self,name):
      super().__init__(name)

     def __str__(self):
        return f"My name is {self.name} and I play drums"

     def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

     def get_instrument(self):
      return "drums"

     def play_solo(self):
      return "rattle boom crash" 





