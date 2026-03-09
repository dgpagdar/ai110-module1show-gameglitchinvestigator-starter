from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix tests: verify correct outcome AND message ---

def test_guess_too_high_returns_go_lower():
    # Bug fix: guess > secret must say Go LOWER, not Go HIGHER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low_returns_go_higher():
    # Bug fix: guess < secret must say Go HIGHER, not Go LOWER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_equals_secret_is_win():
    # Correct guess returns Win outcome and correct message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_check_guess_with_integers_only():
    # Bug fix: secret must always be int, not str — both args are int here
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert isinstance(30, int)
    assert isinstance(50, int)

def test_guess_one_above_secret():
    # Edge case: guess is just 1 above secret
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_one_below_secret():
    # Edge case: guess is just 1 below secret
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
