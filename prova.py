moves = {"3": ["LR"],
         "5": ["DR"],
         "6": ["LD"],
         "7": ["LR", "LD", "DR"],
         "9": ["UR"],
         "96": ["LD", "UR"],
         "A": ["LU"],
         "B": ["LR", "LU", "UR"],
         "C": ["UD"],
         "C3": ["LR", "UD"],
         "D": ["UD", "UR", "DR"],
         "E": ["LU", "LD", "UD"],
         "F": ["LR", "LD", "LU", "UD", "DR", "UR"]}

class Tyle:
    def __init__(self, id, cost, available):
        self.id = id
        self.cost = cost
        self.available = available

    def __str__(self):
        return f"Tyle - Cost: {self.cost}, Available: {self.available}"

    def use(self):
        if self.disponibili > 0:
            self.disponibili -= 1
        else:
            raise Exception("Not available")
    def can_move(self, f, t):
        return (f+t in moves[self.id] or t+f in moves[self.id])
    
t = Tyle("3", 4, 10)
print(t.can_move("R", "U"))
