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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
