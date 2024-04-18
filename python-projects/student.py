class student:
    def __init__(self, fname, lname, id, level=10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.level = level
    def __str__(self):
        return f"last name is: {self.lname}, id: {self.id}"
    def greeting(self):
        return f"hello, i am: {self.fname} {self.lname}"
    def take_exam(self):
        self.level = self.level -1
    def get_level(self):
        return self.level
        
    
        





















    """
    def __init__(self, fname, lname, id, energy_level):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
       return  f"{self.lname}: {self.id}"
    
    def fname(self, fname):
        self.fname = fname

    def lname(self, lname):
        self.lname = lname

    def id(self, id):
        self.id = id

    def energy_level(self, energy_level):
        self.energy_level = energy_level

    def greeting(self):
        return f"Hi, my name is {self.fname} {self.lname}"
    
    def take_exam(self, energy_level):
        self.energy_level -= energy_level
    
    def get_energy_level(self):
        return self.energy_level   
        """