import random


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Computer Science Quiz Game!")
        print("Answer multiple-choice or fill-in-the-blank questions to test your knowledge.")
        print("Let's get started!\n")

    def present_quiz_questions(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question['text']}")
            if 'choices' in question:
                for j, choice in enumerate(question['choices'], start=1):
                    print(f"{j}. {choice}")
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_user_answer(user_answer, question['answer'])
            print()

    def evaluate_user_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {correct_answer}")

    def display_final_results(self):
        print("\nQuiz Finished!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        return choice == 'yes'


# to play again same questions may ask but randomly choosing
def main():
    questions = [
        {
            'text': "What is the most popular programming language in 2022?",
            'choices': ["Python", "Java", "C++", "JavaScript"],
            'answer': "Python"
        },
        {
            'text': "What does HTML stand for?",
            'answer': "Hyper Text Markup Language"
        },
        {
            'text': "What is the main purpose of a firewall?",
            'answer': "To protect against unauthorized access"
        },
        # Add more questions here
    ]

    game = QuizGame(questions)
    game.display_welcome_message()

    play_again = True
    while play_again:
        game.present_quiz_questions()
        game.display_final_results()
        play_again = game.play_again()

        if play_again:
            new_questions = random.sample(questions, k=min(len(questions), 10))
            game = QuizGame(new_questions)
            game.display_welcome_message()


if __name__ == "__main__":
    main()
