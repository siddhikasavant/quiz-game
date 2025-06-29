import json
# Load questions from JSON file
with open('questions.json', 'r') as f: #file handling
    questions = json.load(f)
score = 0
print("Welcome to quiz")
print("---------------")

for i,q in enumerate(questions , 1):
    print(f"\nQuestion{i}:{q['question']}")
    for idx, option in enumerate(q['options'], 1):
        print(f"{idx}.{option}")
    try:
        choice=int(input("your answer is (1-4)"))
        if q['options'][choice-1].lower()==q['answer'].lower():
            print("correct")
            score+=1
        else:
            print("wrong! try again")
    except:
        print("invalid option")
print("Quiz is over!")
print("thank you for participating!")  
print(f"Final score: {score}/{len(questions)}")





