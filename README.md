# Wordle (Python CLI Version)

A terminal-based clone of the classic **Wordle** game written in Python.  
This program selects a daily word from a file and lets you guess it in up to **6 tries**, showing colored feedback (green, yellow, gray) just like the official game.

---

## Features
- 🎮 Play Wordle directly in your terminal.  
- 📅 Daily word selection based on date (starting **09/30/2025**).  
- ✅ Accepts only valid five-letter words (from `wordacceptablewords.txt`).  
- 🎨 Colored output:
  - 🟩 Green: Correct letter, correct position.  
  - 🟨 Yellow: Correct letter, wrong position.  
  - ⬛ Gray: Letter not in the word.  
- 📝 Saves guess history (`guess.txt`) and emoji-square results (`square.txt`) for each playthrough.  

---

## Requirements
- Python 3.x  
- Terminal/Command Prompt that supports ANSI colors and Unicode (emojis).  
  - Works on **Linux/macOS terminals**  
  - Works on **Windows PowerShell/Windows Terminal**  

---

## File Setup
Before running, make sure these files exist in the same folder as the script:

- **`wordoftheday.txt`**  
  Contains the daily words, one per line (in order).  

- **`wordacceptablewords.txt`**  
  Contains the dictionary of valid guessable words, one per line.  

- **`guess.txt`** *(auto-created)*  
  Stores guess history for the current game.  

- **`square.txt`** *(auto-created)*  
  Stores emoji-square results for the current game.  

---

## How to Run
```bash
python3 wordle.py   # macOS/Linux
python wordle.py    # Windows
