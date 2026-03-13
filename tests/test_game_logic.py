from logic_utils import check_guess, get_range_for_difficulty

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

# --- Tests targeting the three bugs fixed in Phase 2 ---

def test_too_high_message_is_go_lower():
    # Bug fix: guess higher than secret should say Go LOWER!, not Go HIGHER!
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_is_go_higher():
    # Bug fix: guess lower than secret should say Go HIGHER!, not Go LOWER!
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_difficulty_range_easy():
    # Bug fix: Easy difficulty should return range 1-20, not 1-100
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_difficulty_range_hard():
    # Bug fix: Hard difficulty should return range 1-50, not 1-100
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_check_guess_secret_stays_int():
    # Bug fix: secret should not be cast to string; int comparison must work correctly
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
