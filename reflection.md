# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game had several bugs:

The secret number resets every time you submit a guess, making it impossible to win. This happens because the secret number is re-randomized on each rerun or when starting a new game, instead of persisting correctly in session state.
The hints for guesses are incorrect: when the guess is higher than the secret, it says "Go HIGHER!" instead of "Go LOWER!", and vice versa. This misleads the player and makes the game unplayable.
The "New Game" button always resets the secret number to a value between 1 and 100, ignoring the selected difficulty range.
What should happen: The secret number should remain the same throughout a game session, hints should accurately tell the player to guess higher or lower, and the new game should respect the selected difficulty range.

---

## 2. How did you use AI as a teammate?

I used Claude Code (via the Claude Code VS Code extension) as my primary AI tool throughout this project.

**Correct suggestion:** Claude correctly identified that the hint messages in `check_guess` were swapped — when `guess > secret` the code returned "Go HIGHER!" instead of "Go LOWER!". It also correctly flagged that the secret was being cast to a string on even-numbered attempts, which silently broke integer comparisons. I verified both by reading the logic carefully and then running the corresponding pytest tests (`test_too_high_message_is_go_lower` and `test_check_guess_secret_stays_int`), which passed after the fix.

**Incorrect/misleading suggestion:** When pytest first failed with a `ModuleNotFoundError` for `logic_utils`, Claude's first attempt used a chained shell command with `--import-mode=importlib` and `PYTHONPATH=.` flags piped together, which was confusing and hard to read. That command was not the right approach. The real fix was simply adding a `conftest.py` at the project root — a standard pytest convention. I verified this worked by running `pytest tests/test_game_logic.py -v` cleanly afterward with all 8 tests passing.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when both a manual check of the logic and a passing pytest test agreed. For the hint bug, I read the `if/else` in `check_guess` to confirm the messages matched the conditions, then ran `pytest -v` and watched `test_too_high_message_is_go_lower` and `test_too_low_message_is_go_higher` turn green. For the difficulty range bug, I checked that `get_range_for_difficulty("Easy")` returned `(1, 20)` and confirmed it via `test_difficulty_range_easy`. Claude helped design the tests by suggesting simple, focused cases — for example, "a guess of 60 against a secret of 50 should return Too High and a message containing LOWER" — which made each test target exactly one behavior and nothing more.

---

## 4. What did you learn about Streamlit and state?

Every time you interact with a Streamlit app, clicking a button, typing in a box, Streamlit reruns the entire Python script from top to bottom. Think of it like refreshing a webpage: all your variables reset to their default values unless you explicitly save them. That's where session state comes in: `st.session_state` is a dictionary that persists across reruns, so values stored there survive each refresh. In this game, the secret number had to live in `st.session_state.secret`; without that, it was re-randomized on every guess, making it impossible to win.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I learned that context is very important. The AI agent has to understand your codebase (if it is simple like this one), before asking it to do anything else it would be a very generalized solution instead of tailoring it to your use case. It is better to separate the chats based on a specific problem that way you have context for everything you are working on and not just dumping everything into one chat.

- What is one thing you would do differently next time you work with AI on a coding task?

  Create better prompts so the AI agent knows exactly what I want instead of writing vague prompts and assuming it will understand.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI is a very powerful tool in terms of helping understand a new codebase to be caught up to speed and as a helper on the side whenever I am stuck on something.
