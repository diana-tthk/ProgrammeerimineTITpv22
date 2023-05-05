class KgToPounds:
    
    def __init__(self, kg):
        self.__kg = kg
    
    def to_pounds(self):
        return self.__kg * 2.205
    
    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами!')

    def get_kg(self):
        return self.__kg

weight = KgToPounds(12)
print(weight.to_pounds())
weight.set_kg(15)
print(weight.to_pounds())
print(weight.get_kg())
input()