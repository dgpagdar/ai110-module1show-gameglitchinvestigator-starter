import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0  # Fixed: start at 0 (no attempts used), was 1 causing off-by-one in display

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "last_hint" not in st.session_state:
    st.session_state.last_hint = None

# Fixed: game_id tracks game resets so text input key changes, clearing old value
if "game_id" not in st.session_state:
    st.session_state.game_id = 0

if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty

# Fixed: detect difficulty change and reset all game state so new difficulty takes effect
if st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.last_hint = None
    st.session_state.game_id += 1
    st.rerun()

st.subheader("Make a guess")

# Fixed: use low/high from difficulty instead of hardcoded "1 and 100"
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

# Fixed: hint stored in session state and shown here so it renders with updated state after rerun
if st.session_state.last_hint:
    st.warning(st.session_state.last_hint)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

# Fixed: include game_id in key so input clears on new game or difficulty change
raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}_{st.session_state.game_id}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# Fixed: reset all game state on new game (was only resetting attempts and secret)
if new_game:
    st.session_state.attempts = 0  # Fixed: reset to 0 to match initialization
    st.session_state.secret = random.randint(low, high)  # Fixed: was hardcoded randint(1,100), ignoring difficulty
    st.session_state.score = 0
    st.session_state.status = "playing"  # Fixed: was never reset, blocked play after win/loss
    st.session_state.history = []
    st.session_state.last_hint = None
    st.session_state.game_id += 1
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.balloons()
        st.success(
            f"You won! The secret was {st.session_state.secret}. "
            f"Final score: {st.session_state.score}. Start a new game to play again."
        )
    else:
        st.error(
            f"Out of attempts! The secret was {st.session_state.secret}. "
            f"Score: {st.session_state.score}. Start a new game to try again."
        )
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.attempts += 1  # Fixed: moved here so invalid input doesn't consume an attempt
        st.session_state.history.append(guess_int)

        secret = st.session_state.secret  # Fixed: always int, was conditionally cast to str on even attempts

        outcome, message = check_guess(guess_int, secret)

        # Fixed: store hint in session state so it renders correctly after rerun
        st.session_state.last_hint = message if show_hint else None

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.status = "won"
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"

        st.session_state.game_id += 1  # Fixed: increment on every submit so input key changes and field clears
        # Fixed: rerun so attempts left, history, and hint all render with updated state
        st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
