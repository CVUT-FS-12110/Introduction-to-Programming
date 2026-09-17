def create_player() -> dict:
    return {"score": 0, "correct_answers": 0, "total_questions": 0}


def answer_question(player: dict, is_correct: bool) -> None:
    player["total_questions"] += 1
    if is_correct:
        player["score"] += 10
        player["correct_answers"] += 1


def get_results(player: dict, name: str) -> str:
    return (
        f"{name}: score {player['score']}, "
        f"correct {player['correct_answers']}/{player['total_questions']}"
    )


if __name__ == "__main__":
    alice = create_player()
    bob = create_player()

    answer_question(alice, True)
    answer_question(alice, False)
    answer_question(alice, True)

    answer_question(bob, True)
    answer_question(bob, True)
    answer_question(bob, False)

    print(get_results(alice, "Alice"))
    print(get_results(bob, "Bob"))
