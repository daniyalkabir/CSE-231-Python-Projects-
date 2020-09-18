##
## Class PetError -- complete
##
 
class PetError( ValueError ):
   
    pass
 
##
## Class Pet -- not complete
##
 
class Pet( object ):
   
    def __init__( self, species=None, name="" ):
       
        if species and (species.lower() in ['dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']):
            self.species = species.title()
            self.name = name.title()
        else:
            raise PetError()
    def __str__( self ):
        result = "Species of {:s}".format(self.species)
        if self.name:
            result += ", named {:s}".format(self.name)
        else:
            result += ", unnamed"
        return result
 
class Dog( Pet ):
    def __init__( self, name="", chases="Cats" ):
        super(Dog, self).__init__("Dog", name)
        self.chases = chases
    def __str__( self ):
        result = super(Dog, self).__str__()
        result += ", chases {:s}".format(self.chases)
        return result
 
class Cat( Pet ):
    def __init__( self, name="", hates="Dogs" ):
        super(Cat, self).__init__("Cat", name)
        self.hates = hates
    def __str__( self ):
        result = super(Cat, self).__str__()
        result += ", hates {:s}".format(self.hates)
        return result