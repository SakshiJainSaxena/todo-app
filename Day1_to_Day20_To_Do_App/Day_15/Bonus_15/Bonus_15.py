import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)

    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"Q{index + 1}. {result} - Correct Answer: {question['correct_answer']}," \
              f" Your Answer: {question['user_choice']}"
    print(message)

print(f"Your score is {score} / {len(data)}")