<div align="center">

# Smart Student Utility System

</div>
A Python-based utility program designed to help students perform simple tasks, such as integer input validation, basic calculations, text analysis, and file management. This project covers fundamental Python concepts including functions, type hints, docstrings, list and dictionary comprehensions, sets, file I/O, *args/**kwargs, and testing with pytest.

---

## Features

- Safe integer input using error handling
- Basic calculator with addition, subtraction, multiplication, and division
- Text analysis (total characters, words, and unique words)
- Save and load data to/from JSON files
- Bonus function to practice *args and **kwargs
- Fully tested functions using pytest
- Simple command-line interface with menu options

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ZannatulRaian/smart-student-utility.git
cd smart-student-utility
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate    # Windows
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main program:

```bash
python project.py
```

You will see a menu with options:

1. Enter a safe integer  
2. Calculator  
3. Analyze a text  
4. Save data to file  
5. Load data from file  
6. Bonus features  
7. Exit  

Follow the prompts to interact with the program.

---

## Project Structure

```
smart-student-utility/
│
├── project.py          # Main program and custom functions
├── test_project.py     # Pytest unit tests
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

---

## Running Tests

This project uses pytest for testing. To run all tests:

```bash
pytest
```

Tests include validation of:

- Calculator operations  
- Text analysis function  
- Input handling functions  

---

## Dependencies

- Python 3.10+  
- pytest  
- Optional: cowsay and pyttsx3 if extending with sound output features

---

## License

This project is open-source and available under the MIT License.

---

## Future Improvements

- Add more text statistics (average word length, most common word)  
- Expand calculator to support more operations and error handling  
- Implement user login and data persistence  
- Add GUI using Tkinter or PyQt  
