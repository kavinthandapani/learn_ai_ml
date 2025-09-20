import random
import numpy as np

class Probability:
    def __init__(self, face, rolls, number_to_calucalte_probability_for):
        self.rolls = rolls
        self.face = face
        self.number_to_calucalte_probability_for = number_to_calucalte_probability_for
        self.dice_rolls = [random.randint(1, self.face) for _ in range(self.rolls)]
    
    def calculte_probability(self):
        dice_rolls = self.dice_rolls.copy()
        return dice_rolls.count(self.number_to_calucalte_probability_for) / len(dice_rolls)
    
    def calculate_probability_for_even_number(self):
        dice_rolls = self.dice_rolls.copy()
        even_count = sum(1 for _ in dice_rolls if _ % 2 == 0)
        return even_count / len(dice_rolls)
    
class ProbabilityNumPy():
    def __init__(self, face, rolls, number_to_calucalte_probability_for):
        self.rolls = rolls
        self.face = face
        self.number_to_calucalte_probability_for = number_to_calucalte_probability_for
        self.dice_rolls = np.random.randint(1, self.face + 1, size=self.rolls)
    
    def calculate_probability(self):
        dice_rolls = self.dice_rolls
        return np.sum(dice_rolls == self.number_to_calucalte_probability_for) / self.rolls
    
    def calculate_probability_for_even_number(self):
        dice_rolls = self.dice_rolls
        return np.sum(dice_rolls % 2 == 0) / self.rolls

########################################################################################

probability = Probability(6, 10000, 3)

print(f"Probability of rolling a 3: {probability.calculte_probability()}")
print(f"Probability of rolling an even number: {probability.calculate_probability_for_even_number()}")

########################################################################################

probability_numpy = ProbabilityNumPy(6, 10000, 3)

print(f"Probability of rolling a 3: {probability_numpy.calculate_probability()}")
print(f"Probability of rolling an even number: {probability_numpy.calculate_probability_for_even_number()}")
