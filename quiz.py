import json

def get_questions():
    with open('questions.json', 'r') as file:
        questions = json.load(file)
    return questions

def start_screen():
    print("╔══════════════════════════════════════╗")
    print("║                                      ║")
    print("║             QUIZ                     ║")
    print("║                                      ║")
    print("║        Test your knowledge!          ║")
    print("║                                      ║")
    print("║              1. PLAY                 ║")
    print("║              2. RULES                ║")
    print("║              3. EXIT                 ║")
    print("║                                      ║")
    print("╚══════════════════════════════════════╝")
    choice=input('Enter your desired option: ')
    return choice

def choose_topic(questions):
    print('Choose a topic:')
    topics=[]
    for i in questions:
        if i['topic'] not in topics:
            topics.append(i['topic'])
    for i in  range (len(topics)):
        print(topics[i])
    a=input('Enter your desired topic: ')
    topic_choice=a.capitalize()
    return topic_choice

def quiz(questions, topic_choice):
    score=0
    for i in questions:
        if i['topic']==topic_choice:
            print(i['question'])
            options=i['options']
            for j in range(len(options)):
                print(j+1," ",options[j])
            answer=int(input('Enter your answer: '))
            if answer==i['options'].index(i['answer'])+1:
                score+=1
                print('Correct!')
            else:
                print('Incorrect!')
    print('Your score is: ',score)



while True:
    choice = start_screen()
    if choice == '1':
        print("Starting the quiz...")
        questions = get_questions()
        topic_choice = choose_topic(questions)
        quiz(questions, topic_choice)
        break
    elif choice == '2':
        print("Here are the rules")
        print("Answer before the timer runs out")
        print("Each correct answer gives you 1 point")
    elif choice == '3':
        print("Thanks for playing!")
        break
    else:
        print("Invalid option. Please try again")