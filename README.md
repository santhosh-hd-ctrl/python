# Python Learning Repository 🐍

Welcome to this Python learning journey! This repository contains beginner-level Python scripts covering fundamental concepts and operations.

> **Status:** 📚 Learning in Progress | **Last Updated:** Auto-generated | **Files:** 9 Python Scripts

## 📊 Repository Overview

| Metric | Value |
|--------|-------|
| Language | 100% Python |
| Repository | [santhosh-hd-ctrl/python](https://github.com/santhosh-hd-ctrl/python) |
| Purpose | Learning Python from Zero |
| Total Files | 10 |
| Scripts | 9 |
| Beginner Level | ✅ Yes |

This is a learning-focused repository designed to help beginners understand core Python concepts from scratch. All files are written in Python and demonstrate basic programming principles through practical examples.

---

## 📂 Lesson Files & Contents

### 🎬 Demo & Introduction Files

#### **demo.py** - Introduction Script
- **Purpose:** Basic introduction with print statement
- **Concepts:** Simple output, string printing
- **Output:**
  ```
  Hii, i'am santhosh and i'am a python developer
  ```

#### **demo day 2.py** - Arithmetic Operations
- **Purpose:** Demonstrates all basic arithmetic operators
- **Key Operators:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Highlights:**
  - Operations: 10 + 3 = 13
  - Modulo: 10 % 3 = 1
  - Exponentiation: 10 ** 3 = 1000
  - Variable swapping using tuple unpacking
  - Before: a=10, b=3
  - After swap: a=3, b=10

---

### 📝 Input & String Manipulation

#### **3.py** - Basic Input Handling
- **Purpose:** Simple program to accept and display user input
- **Concepts:** `input()` function, string concatenation
- **Example Usage:**
  ```bash
  python3 3.py
  # Input: age 25
  # Output: age = 25
  ```

#### **3.1.py** - Relationship Age Difference Calculator
- **Purpose:** Calculates age difference between two people
- **Input:** Two names and their ages
- **Concepts:**
  - Multiple `input()` calls
  - `int()` type conversion
  - `abs()` function for absolute value
  - String concatenation methods
  - F-string formatting
- **Example:**
  ```bash
  python3 3.1.py
  # Output: John loves Jane. Age difference is 2 years
  ```

#### **3.2.py** - Personalized Greeting
- **Purpose:** Creates personalized greeting messages
- **Input:** Name and age
- **Concepts:**
  - String concatenation
  - F-string formatting (modern approach)
- **Output:**
  ```
  hello Alice you are 20 years old
  hello Alice you are 20 years old (f-string)
  ```

#### **3.3.py** - String Manipulation Operations
- **Purpose:** Demonstrates various string methods
- **String Methods Covered:**
  - `.upper()` - Convert to uppercase
  - `.lower()` - Convert to lowercase
  - `.strip()` - Remove excess whitespace
  - `.replace()` - Replace text within strings
  - `len()` - Get string length
- **Example Operations:**
  ```python
  "hello".upper()      # Output: HELLO
  "HELLO".lower()      # Output: hello
  " text ".strip()     # Output: text
  "Awesome".replace("Awesome", "Wonderful")  # Output: Wonderful
  len("Hello")         # Output: 5
  ```

#### **3.4.py** - Character Counter (Excluding Spaces)
- **Purpose:** Count characters in a string without spaces
- **Concepts:**
  - String `replace()` method
  - `len()` function
  - Method chaining
- **Example:**
  ```bash
  python3 3.4.py
  # Input: "Hello World"
  # Output: Number of characters (excluding spaces): 10
  ```

#### **3.5.py** - Special Characters & Escape Sequences
- **Purpose:** Demonstrates escape sequences in strings
- **Escape Sequences:**
  - `\n` - Newline
  - `\t` - Tab
  - `\\` - Backslash
- **Output Example:**
  ```
  Hello 
   	 World 
  This is a backslash: \ 
  ```

---

## 🎯 Learning Concepts Covered

### Core Programming Fundamentals
1. **Variables and Data Types**
   - Integer and string types
   - Variable assignment and manipulation
   - Type conversion (`int()`, `str()`)

2. **Input and Output**
   - `input()` function for user input
   - `print()` function for output
   - Dynamic output formatting

3. **Arithmetic Operations**
   - Basic operators: `+`, `-`, `*`, `/`
   - Integer division: `//`
   - Modulus: `%`
   - Exponentiation: `**`

4. **String Operations**
   - String concatenation
   - F-string formatting (modern approach)
   - String methods:
     - `upper()` - Uppercase conversion
     - `lower()` - Lowercase conversion
     - `strip()` - Whitespace removal
     - `replace()` - Text substitution
     - `len()` - String length
   - Escape sequences: `\n`, `\t`, `\\`

5. **Advanced Concepts**
   - Tuple unpacking for variable swapping
   - Absolute value calculation with `abs()`
   - Method chaining

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/santhosh-hd-ctrl/python.git
cd python
```

### 2. Run Any Script
```bash
python3 filename.py
```

### 3. Run Specific Examples

**Simple Output (No Input):**
```bash
python3 demo.py
python3 "demo day 2.py"
python3 3.5.py
```

**Interactive Scripts (Requires Input):**
```bash
# Age difference calculator
python3 3.1.py
# Enter boy name: John
# Enter boy age: 25
# Enter girl name: Jane
# Enter girl age: 23

# Character counter
python3 3.4.py
# Enter a string: Hello World

# String manipulation
python3 3.3.py
# Enter 4 inputs as prompted
```

---

## 💡 Recommended Learning Path

Follow this sequence to master the concepts:

| Order | File | Topic | Difficulty |
|-------|------|-------|------------|
| 1 | `demo.py` | Basic print statement | ⭐ Beginner |
| 2 | `3.py` | Simple input/output | ⭐ Beginner |
| 3 | `3.2.py` | Multiple inputs & greeting | ⭐ Beginner |
| 4 | `demo day 2.py` | Arithmetic operations | ⭐ Beginner |
| 5 | `3.1.py` | Complex input & string formatting | ⭐⭐ Beginner+ |
| 6 | `3.3.py` | String methods & manipulation | ⭐⭐ Beginner+ |
| 7 | `3.4.py` | Method chaining & logic | ⭐⭐ Beginner+ |
| 8 | `3.5.py` | Escape sequences | ⭐⭐ Beginner+ |

---

## 📋 Quick Reference

### Python Built-in Functions Used
| Function | Purpose | Example |
|----------|---------|---------|
| `print()` | Output text | `print("Hello")` |
| `input()` | Get user input | `name = input("Name: ")` |
| `int()` | Convert to integer | `age = int(input())` |
| `str()` | Convert to string | `str(123)` → `"123"` |
| `len()` | Get length | `len("Hello")` → `5` |
| `abs()` | Absolute value | `abs(-5)` → `5` |

### String Methods Reference
| Method | Purpose | Example |
|--------|---------|---------|
| `.upper()` | Uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | Lowercase | `"HELLO".lower()` → `"hello"` |
| `.strip()` | Remove spaces | `" hi ".strip()` → `"hi"` |
| `.replace()` | Replace text | `"hi".replace("h", "H")` → `"Hi"` |
| `.split()` | Split string | `"a,b".split(",")` → `["a", "b"]` |

---

## 📝 Prerequisites

- **Python 3.x** installed on your system
- Basic understanding of **command line/terminal**
- Text editor for viewing/editing code
- No external dependencies required! All scripts use built-in functions only.

### Check Python Installation
```bash
python3 --version
# Output: Python 3.x.x
```

---

## 🔗 External Resources

### Official Documentation
- [Official Python Documentation](https://docs.python.org/3/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Learning Resources
- [Real Python Tutorials](https://realpython.com/)
- [Python String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)
- [F-Strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

---

## 👨‍💻 Repository Info

**Author:** Santhosh HD Ctrl  
**Repository:** [santhosh-hd-ctrl/python](https://github.com/santhosh-hd-ctrl/python)  
**Created:** June 12, 2026  
**Purpose:** Learning Python from Zero - Beginner Level  
**License:** Open for Educational Purposes

### Key Features
- ✅ Beginner-friendly code
- ✅ Well-commented examples
- ✅ Step-by-step learning progression
- ✅ Interactive input examples
- ✅ Multiple string formatting approaches
- ✅ No external dependencies

---

## 🤝 Contributing

Feel free to:
- 🍴 Fork the repository
- ✏️ Modify and improve examples
- 🔄 Create pull requests with enhancements
- 💡 Suggest additional learning examples
- 🐛 Report any issues

---

## 📄 License

This repository is open for **educational purposes**. Free to use, modify, and distribute for learning.

---

<div align="center">

### 🎓 **Happy Learning!**

*Master Python one script at a time*

**[⬆ back to top](#python-learning-repository-)**

</div>
