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
