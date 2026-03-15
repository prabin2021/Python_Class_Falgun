class Human:
    
    def __init__(self,species,features):
        self.species = species
        self.features = features
    
    def show_info(self):
        print(f"This show_info method is from Human class.")
        print(f"It's species is {self.species}.")
        print(f"It's feature is to {self.features}.")
    
human1 = Human("Human","walk")   
    
class Birds:
    
    def __init__(self,species,features):
        self.species = species
        self.features = features
    
    def show_info(self):
        print(f"This show_info method is from Birds class.")
        print(f"It's species is {self.species}.")
        print(f"It's feature is to {self.features}.")
   
bird1 = Birds("Bird","fly") 

class Reptiles:
    
    def __init__(self,species,features):
        self.species = species
        self.features = features
    
    def show_info(self):
        print(f"This show_info method is from Reptiles class.")
        print(f"It's species is {self.species}.")
        print(f"It's feature is to {self.features}.")
 
rep1 = Reptiles("Reptiles","crawl")   


for i in (human1,bird1,rep1):
    i.show_info()