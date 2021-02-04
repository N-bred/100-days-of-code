from random import choice

questions = [
    "Insert the name of the city you grew on: ",
    "Insert the name of your pet: ",
    "Insert the name your favorite food: ",
    "Insert the name your favorite youtuber: ",
    "Insert the name of your favorite game: ",
]

n_of_questions = 2

questions_to_ask = [choice(questions) for n in range(0, n_of_questions)]

print("Hey, welcome to the generator\n")

band_name = ""
for n in range(0, n_of_questions):
    question = choice(questions_to_ask)
    questions_to_ask.remove(question)
    band_name += input(question)


print(f"Your band name is {band_name} congrats.")
