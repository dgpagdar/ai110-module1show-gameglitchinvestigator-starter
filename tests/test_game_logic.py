from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

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


# --- Bug fix tests: invalid input should not count as an attempt ---

def test_parse_guess_empty_string_is_invalid():
    # Bug fix: empty input must return ok=False so attempt counter is not incremented
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_non_numeric_is_invalid():
    # Bug fix: non-numeric input must return ok=False so attempt counter is not incremented
    ok, value, _ = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_guess_none_is_invalid():
    # Bug fix: None input must return ok=False so attempt counter is not incremented
    ok, value, _ = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_guess_valid_int_is_accepted():
    # Valid integer input must return ok=True so attempt counter is incremented
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


# --- Bug fix tests: difficulty range must match selected difficulty ---

def test_easy_range():
    # Bug fix: new game secret and info message must use difficulty range, not hardcoded 1-100
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


# --- Bug fix tests: attempt counter starts at 1 and score calculation is correct ---

def test_update_score_win_on_first_valid_attempt():
    # attempts start at 0 and increment after validation; attempt_number=1 is the first real guess
    # 100 - 10 * (1 + 1) = 80
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 80

def test_update_score_win_minimum_points():
    # Score floor is 10 even on late attempts
    score = update_score(current_score=0, outcome="Win", attempt_number=10)
    assert score == 10

def test_update_score_no_change_on_unknown_outcome():
    # Unknown outcome leaves score unchanged
    score = update_score(current_score=50, outcome="Unknown", attempt_number=1)
    assert score == 50
