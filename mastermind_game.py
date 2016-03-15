import random
class MastermindGame:

    solution = [0]
    guesses = [[0]]

    def __init__(self, numPeople, numTents):
        self.numPeople = numPeople
        self.numTents = numTents
        MastermindGame.solution = [numTents]
        MastermindGame.solution = [i for i in range(0, numPeople)]
        random.shuffle(MastermindGame.solution)
        MastermindGame.solution = MastermindGame.solution[:numTents]
        
    def solution(self):
        return MastermindGame.solution
        
def main():
    x = MastermindGame(6, 4)
    print x.solution
    
main()