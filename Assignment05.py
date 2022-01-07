import random

#function to calculate multiplication of two random numbers
def randomNumber():
    randNum1 = random.randint(0, 9)
    randNum2 = random.randint(0, 9)
    print("Hey! How much is " + str(randNum1) + " * " + str(randNum2) + " ?")
    return randNum1 * randNum2

realAnswer = randomNumber()

#Array of String for correct answer
ifCorrect = ["Very Good!", "Excellent", "Nice Work!", "Keep up the good work!"]

#Array of String for incorrect answer
ifNotCorrect = ["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. keep trying."]


userAnswer = 0
#loop to check if the answer is matched or not
while str(realAnswer) != userAnswer:
    userAnswer = input("Enter your answer : ")
    if str(realAnswer) != userAnswer:
        print(random.choice(ifNotCorrect))
    elif str(realAnswer) == userAnswer:
        print(random.choice(ifCorrect))
        realAnswer = randomNumber()