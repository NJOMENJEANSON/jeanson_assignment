import time

# Quiz data structure
quiz_data = {
    "Science": {
        "easy": [
            {
                "question": "What is the chemical symbol for water?",
                "options": ["H2O", "CO2", "NaCl", "O2"],
                "answer": 0
            },
            {
                "question": "Which planet is closest to the sun?",
                "options": ["Venus", "Mars", "Mercury", "Earth"],
                "answer": 2
            }
        ],
        "hard": [
            {
                "question": "What is the atomic number of Carbon?",
                "options": ["4", "6", "8", "12"],
                "answer": 1
            }
        ]
    },
    "History": {
        "easy": [
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"],
                "answer": 1
            }
        ],
        "hard": [
            {
                "question": "When was the Declaration of Independence signed?",
                "options": ["1774", "1776", "1778", "1780"],
                "answer": 1
            }
        ]
    }
}


def initialize_high_scores():
    """Initialize high scores dictionary without using lambda"""
    high_scores = {}
    for category in quiz_data:
        high_scores[category] = {"easy": 0, "hard": 0}
    return high_scores

def display_progress(current, total):
    """Show progress bar"""
    progress = int((current / total) * 10)
    print(f"[{'█' * progress}{'░' * (10 - progress)}] {current/total*100:.0f}% Complete\n")

def show_categories():
    """Display available categories"""
    print("\n=== QUIZ MASTER ===")
    print("Categories:", ", ".join(quiz_data.keys()))
    print()

def select_category_difficulty():
    """Get user selection for category and difficulty"""
    while True:
        category = input("Choose a category: ").title()
        if category in quiz_data:
            break
        print("Invalid category. Please choose from:", ", ".join(quiz_data.keys()))
    
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").lower()
        if difficulty in ["easy", "hard"]:
            break
        print("Please enter either 'easy' or 'hard'")
    
    return category, difficulty

def run_quiz(category, difficulty, high_scores):
    """Run the quiz and track scores"""
    questions = quiz_data[category][difficulty]
    score = 0
    wrong_answers = []
    
    print(f"\nSelected: {category} ({difficulty.capitalize()})")
    
    for i, question in enumerate(questions, 1):
        display_progress(i, len(questions))
        print(f"Question {i}/{len(questions)}: {question['question']}")
        
        for j, option in enumerate(question['options']):
            print(f"{chr(65 + j)}) {option}")
        
        start_time = time.time()
        while True:
            user_answer = input("Your answer: ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Please enter A, B, C, or D")
        
        answer_time = time.time() - start_time
        user_index = ord(user_answer) - 65
        
        if user_index == question['answer']:
            print(f"\n✅ Correct! (+{10} points)")
            score += 10
        else:
            correct_option = chr(65 + question['answer'])
            print(f"\n❌ Incorrect! The correct answer was {correct_option}")
            wrong_answers.append({
                'question': question['question'],
                'your_answer': user_answer,
                'correct_answer': correct_option,
                'options': question['options']
            })
        
        print(f"Time: {answer_time:.1f} seconds\n")
    
    # Calculate final score
    total_possible = len(questions) * 10
    final_score = min(score, total_possible)
    
    # Check if new high score
    if final_score > high_scores[category][difficulty]:
        print(f"🎉 New personal best in {category}!")
        high_scores[category][difficulty] = final_score
    
    # Display results
    print("\nFINAL SCORE:")
    print(f"{final_score}/{total_possible} ({score//10}/{len(questions)} correct)")
    
    if wrong_answers:
        print("\nREVIEW WRONG ANSWERS:")
        for i, wrong in enumerate(wrong_answers, 1):
            print(f"\n{i}. {wrong['question']}")
            print(f"Your answer: {wrong['your_answer']}) {wrong['options'][ord(wrong['your_answer']) - 65]}")
            print(f"Correct answer: {wrong['correct_answer']}) {wrong['options'][ord(wrong['correct_answer']) - 65]}")

def main():
    """Main program loop"""
    high_scores = initialize_high_scores()
    
    show_categories()
    while True:
        category, difficulty = select_category_difficulty()
        run_quiz(category, difficulty, high_scores)
        
        if input("\nTake another quiz? (y/n): ").lower() != 'y':
            print("\nSession high scores:")
            for category, scores in high_scores.items():
                print(f"{category}: Easy - {scores['easy']}, Hard - {scores['hard']}")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()