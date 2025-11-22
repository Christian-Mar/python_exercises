def evaluate_wordle_guess(target_word: str, guess_word: str) -> str:
    """
    Evaluates a 5-letter Wordle guess against the target word
    using only strings (no lists, tuples, dictionaries, or sets).

    The feedback is 'G' (Green), 'Y' (Yellow), or 'B' (Black/Grey).

    Parameters
    ----------
    target_word : str
        The secret 5-letter word (e.g., "CRANE").
    guess_word : str
        The player's 5-letter guess (e.g., "APPLE").

    Returns
    -------
    str
        A 5-character string representing the feedback (e.g., "BBYBG").

    Examples
    --------
    >>> evaluate_wordle_guess("APPLE", "CRANE")
    'BBYBG'
    >>> evaluate_wordle_guess("APPLE", "PUPPY")
    'YBGBB'
    >>> evaluate_wordle_guess("CRANE", "CRANE")
    'GGGGG'
    """
    # Convert to lowercase for case-insensitivity
    target_lower = target_word.lower()
    guess_lower = guess_word.lower()

    # Validate input length
    if len(target_lower) != 5 or len(guess_lower) != 5:
        return "Input must be 5 letters."

    # String to track unconsumed letters in the target
    target_tracker = target_lower

    # Pass 1: Identify GREEN (correct letter, correct position)
    feedback = "XXXXX"

    for i in range(5):
        if guess_lower[i] == target_lower[i]:
            # Mark as green
            feedback = feedback[:i] + 'G' + feedback[i+1:]
            # Consume the letter in the tracker
            target_tracker = target_tracker[:i] + '_' + target_tracker[i+1:]

    # Pass 2: Identify YELLOW (correct letter, wrong position) and BLACK
    for i in range(5):
        # Skip if already marked green
        if feedback[i] == 'G':
            continue

        char = guess_lower[i]

        # Check if the guess letter exists in the remaining target letters
        if char in target_tracker:
            # Mark as yellow
            feedback = feedback[:i] + 'Y' + feedback[i+1:]

            # Find and consume the first occurrence
            j = 0
            while j < 5:
                if target_tracker[j] == char:
                    target_tracker = target_tracker[:j] + '_' + target_tracker[j+1:]
                    break
                j += 1
        else:
            # Mark as black
            feedback = feedback[:i] + 'B' + feedback[i+1:]

    return feedback


def run_wordle_game_simulation(target_word: str) -> None:
    """
    Illustrative game loop for demonstration purposes.
    In a real game, this would use input() to get user guesses.
    """
    max_guesses = 6
    print(f"\nWordle Started! Find the 5-letter word '{target_word}'.")

    # Simulate 3 guesses without using a list
    for attempt in range(1, max_guesses + 1):
        # Determine the guess based on attempt number (avoiding list)
        if attempt == 1:
            guess = "CRANE"
        elif attempt == 2:
            guess = "ALERT"
        elif attempt == 3:
            guess = "APPLE"
        else:
            # In a real game, this would be: guess = input("Enter your guess: ").upper()
            print("End of simulation.")
            break

        feedback = evaluate_wordle_guess(target_word, guess)

        print(f"Guess {attempt}: {guess} -> Feedback: {feedback}")

        if feedback == "GGGGG":
            print(f"Congratulations! Word found in {attempt} attempts.")
            return

    print(f"The word was {target_word}.")


if __name__ == "__main__":
    import doctest
    print("Running doctests for the evaluation function...")
    doctest.testmod(verbose=False)
    print("Doctests finished. Result: G=Green, Y=Yellow, B=Black/Grey.")

    # run_wordle_game_simulation("APPLE")  # Uncomment to run the simulation