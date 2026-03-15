# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
-> The game is to guess the secret number, we have to put an number in the guess field and the hint will tell if we have to go Higher or Lower.

- List at least two concrete bugs you noticed at the start  
  1) The given hints were wrong
    expected: if num < secret num then it should say "Go Higher" and if num > secret num it sould say "Go Lower"
    current: if num < secret it says "Go Lower" and if num > secret num it say "Go Higher" 

  2) Invalid input in guess was counting as an attempt
   expected: Invalid input should not decrement the attempts left.
   current: Invalid input is decrementing the attempts left.

  3) Clicking on new game button dosen't reset the stats.
  expected: clicking on new game button should reset the stats and we should be able to play the game again.
  current: clicking on new game button dosen't reset the stats and not able to play the game again.

  4) Changing game difficulty dosen't change the range to guess number and the attemps left.
  expected: changing difficulty should change the range according to the difficulty
  current: changingn difficulty keeps the range same and also attempts left. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
-> I used Claude Code (Anthropic) throughout the project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
-> Claude correctly identified that the hint messages in `check_guess` were swapped — returning "Go LOWER" when the guess was too low and "Go HIGHER" when too high. I verified it by running the pytest tests which confirmed the correct message was returned for each case.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
-> Claude initially reset `attempts` to `1` to "match initialization," which kept the off-by-one bug. I caught it because the wrong count persisted, and the real fix was changing both initialization and resets to `0`.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
-> I manually ran the app and reproduced the original bug, then applied the fix and confirmed the expected behavior. I also ran pytest to make sure the logic held up.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
-> I ran `test_parse_guess_empty_string_is_invalid` and `test_parse_guess_non_numeric_is_invalid` using pytest. They confirmed that invalid input returns `ok=False`, meaning the attempt counter would never be incremented for bad guesses.

- Did AI help you design or understand any tests? How?
-> Yes, Claude suggested writing tests grouped by each bug fix one group for `parse_guess`, one for difficulty ranges, and one for score logic. This made it easy to see exactly which fix each test was covering.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
-> Every button click reruns the whole script top to bottom, wiping all variables. `session_state` is a persistent store that survives reruns that's where you keep things like attempts and history. If you update state mid-script, call `st.rerun()` so the UI re-renders with the new values.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
-> Writing a test for each bug fix right after fixing it — it keeps me honest about whether the fix actually works.

- What is one thing you would do differently next time you work with AI on a coding task?
-> Verify each AI fix immediately instead of stacking multiple fixes, so I can catch when one fix reintroduces a bug.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
-> AI can spot bugs fast but doesn't always get the full context right. You still need to understand the code yourself to catch when a suggestion is wrong.
