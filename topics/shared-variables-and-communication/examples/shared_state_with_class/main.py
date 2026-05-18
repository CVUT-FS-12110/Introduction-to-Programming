class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self._score = 0
        self._correct_answers = 0
        self._total_questions = 0

    def answer_question(self, is_correct: bool) -> None:
        self._total_questions += 1
        if is_correct:
            self._score += 10
            self._correct_answers += 1

    def results(self) -> str:
        return (
            f"{self.name}: score {self._score}, "
            f"correct {self._correct_answers}/{self._total_questions}"
        )


if __name__ == "__main__":
    alice = Player("Alice")
    bob = Player("Bob")

    alice.answer_question(True)
    alice.answer_question(False)
    alice.answer_question(True)

    bob.answer_question(True)
    bob.answer_question(True)
    bob.answer_question(False)

    print(alice.results())
    print(bob.results())
