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


choice = start_screen()

if choice=='1':
    print("Startiing the quiz...")
    start_quiz()
elif choice=='2':
    print("Here are the rules...")
elif choice=='3':
    print("Thanks for playing!")
else:
    print("Invalid option. Please try again.")
    choice=start_screen()