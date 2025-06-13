
# Pomodoro Timer ⏳🍅

This is a simple desktop Pomodoro Timer app built using Python and the Tkinter library.

## What is the Pomodoro Technique?

The Pomodoro Technique is a time management method that helps you focus and work with the time you have. It breaks work into 25-minute sessions (called "Pomodoros"), separated by short breaks. After a few sessions, you take a longer break.

In this version, for testing and demonstration purposes, the times are set to **1 minute** for work and short breaks. The long break is **20 minutes**.

---

## Features

- Start a work timer  
- Take short and long breaks automatically  
- Reset the timer anytime  
- Checkmarks are displayed for completed work sessions  

---

## How to Use

1. Make sure you have **Python** installed on your computer.  
2. Save the files in a folder:
   - `main.py` (the code file)  
   - `tomato.png` (an image file used in the interface)  
3. Open the terminal or command prompt.  
4. Run the app:
   ```bash
   python main.py
   ```
5. A simple window will appear. Click **Start** to begin your work session.  
6. After each work session, a short or long break will follow automatically.  

---

## File Structure

```
your-folder/
│
├── main.py         # The main Python script that runs the timer  
├── tomato.png      # Image of a tomato used as a visual for the timer  
└── README.md       # This instruction file  
```

---

## Dependencies

- Python 3  
- Tkinter (comes pre-installed with Python)  

---

## Customization

You can change the timer durations by modifying these constants in `main.py`:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

---

## Author

Made by aryl-shamir — inspired by the Pomodoro productivity method from Angela course on 100 days code.

---

## License

This project is open source and free to use.
