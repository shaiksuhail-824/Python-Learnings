print('^^^^Welcome to the general knowledge  Mock Test^^^^')
print("NOTE: Each question carried one mark,wrong answer will remove one fourth mark")
            
qa_pairs = {
    "What is the capital of India?": "Delhi",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the national bird of India?": "Peacock",
    "Who wrote the play 'Hamlet'?": "Shakespeare",
    "Which gas do plants absorb from the atmosphere?": "Carbon"
    "dioxide",
    "Which is the largest ocean on Earth?": "Pacific",
    "What is the currency of Japan?": "Yen",
    "Who is known as the Father of Computers?": "Babbage",
    "What is the chemical symbol of water?": "H2O",
    "Which animal is known as the Ship of the Desert?": "Camel"
}
score=0
neg_score=0
for question,answer in qa_pairs.items():
        answer_input=input(question+" ").strip()
        if answer==answer_input.capitalize():
                score+=1
        else :
                 neg_score+=1
print(f"your correct questions {score} and wrong questions {neg_score} ")
Total_score=score-neg_score*1/4
Percentage=(Total_score/10)*100 
print(f"Total_score :{Total_score}\npercentage :{Percentage} %")