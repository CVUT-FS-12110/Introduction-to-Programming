score = 0
correct_answers = 0
total_questions = 0


def answer_question(is_correct: bool) -> None:
    global score, correct_answers, total_questions
    total_questions += 1
    if is_correct:
        score += 10
        correct_answers += 1


def reset() -> None:
    global score, correct_answers, total_questions
    score = 0
    correct_answers = 0
    total_questions = 0


def get_results() -> str:
    return f"Score: {score}, Correct: {correct_answers}/{total_questions}"


if __name__ == "__main__":
    # Round 1 - Alice
    answer_question(True)
    answer_question(False)
    answer_question(True)
    print("Alice:", get_results())

    reset()

    # Round 2 - Bob
    answer_question(True)
    answer_question(True)
    answer_question(False)
    print("Bob:", get_results())

    # Try running Alice and Bob at the same time — not possible with global state!
