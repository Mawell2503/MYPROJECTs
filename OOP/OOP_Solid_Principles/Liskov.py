#  Liskov Substitution 
#  class(Noise) is the parent 

class Noise:
    def make_sound(self):
        pass

#  class(LoudNoise) & class(AnnoyingNoise) are children/subclass
class LoudNoise(Noise):
    #  method make_sound in this subclass respect the parent class method
    def make_sound(self):
        print("Yannnick is heading towards Arveen...get bezer")

    #  extra method
    def fatigue_zorreil(self):
        print("Yannick talked for 3hrs about ...")

class AnnoyingNoise(Noise):
    #  method make_sound in this subclass respect the parent class method
    def make_sound(self):
        print("Lucas.")

    #  extra method
    def fatigue_latet(self):
        print("lucassssssssssssssssssssssssssssssssssssssssss...")

#  ---------------------------------------------------------------------------------
class Noise:
    def make_sound(self):
        print("making sound")

#  class(LoudNoise) & class(AnnoyingNoise) are children/subclass
class LoudNoise(Noise):
    #  method make_sound in this subclass respect the parent class method
    def make_sound(self):
        print("Yannnick is heading towards Arveen...get bezer")

    #  extra method
    def fatigue_zorreil(self):
        print("Yannick talked for 3hrs about ...")

class AnnoyingNoise(Noise):
    #  method make_sound in this subclass does not respect the parent class method
    def make_sound(self):
        raise Exception("Lukas is not here today?")

    #  extra method
    def fatigue_latet(self):
        print("lucassssssssssssssssssssssssssssssssssssssssss...")