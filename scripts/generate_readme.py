#!/usr/bin/env python3
"""
Dynamic README Generator
Scans Python files in the repository and auto-generates README.md
"""

import os
import re
from pathlib import Path
from datetime import datetime


def extract_description(filepath):
    """Extract description from Python file docstring or comments"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Try to extract docstring
        docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if docstring_match:
            return docstring_match.group(1).strip().split('\n')[0]
        
        # Try to extract first comment
        comment_match = re.search(r'#\s*(.+?)(?:\n|$)', content)
        if comment_match:
            return comment_match.group(1).strip()
        
        return "Python learning script"
    except Exception as e:
        return "Python learning script"


def get_python_files():
    """Get all Python files in the root directory"""
    files = []
    for py_file in sorted(Path('.').glob('*.py')):
        if py_file.name != 'setup.py':
            size = py_file.stat().st_size
            description = extract_description(py_file)
            files.append({
                'name': py_file.name,
                'description': description,
                'size': size
            })
    return files


def generate_readme():
    """Generate dynamic README based on repository files"""
    
    python_files = get_python_files()
    
    # Build files section
    files_section = "## 📂 Files and Contents\n\n"
    
    if python_files:
        for file_info in python_files:
            files_section += f"- **{file_info['name']}** - {file_info['description']}\n"
    else:
        files_section += "No Python files found.\n"
    
    # Count of files
    file_count = len(python_files)
    
    # Build README content
    readme_content = f"""# Python Learning Repository 🐍

Welcome to this Python learning journey! This repository contains beginner-level Python scripts covering fundamental concepts and operations.

## 📚 Repository Overview

This is a learning-focused repository designed to help beginners understand core Python concepts from scratch. All files are written in Python and demonstrate basic programming principles through practical examples.

**Total Python Files:** {file_count}

## 📂 Files and Contents

{files_section}

## 🎯 Learning Concepts Covered

- Variables and Data Types
- Input and Output operations
- Arithmetic Operations
- String Operations and Manipulation
- Type Conversion
- Control Flow and Logic
- Functions and Modules

## 🚀 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/santhosh-hd-ctrl/python.git
   cd python
   ```

2. **Run any script**
   ```bash
   python3 filename.py
   ```

3. **Example**
   ```bash
   python3 demo.py
   ```

## 📝 Prerequisites

- Python 3.x installed on your system
- Basic understanding of command line/terminal
- Text editor for viewing/editing code

## 🔧 Installation

No external dependencies required! All scripts use only Python's built-in functions.

## 📖 Resources for Further Learning

- [Official Python Documentation](https://docs.python.org/3/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

## 👨‍💻 About

This repository is created for learning Python from zero. It showcases foundational concepts essential for any beginner Python developer.

**Author:** Santhosh HD Ctrl

## 📄 License

This repository is open for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and create pull requests with improvements or additional learning examples!

---

**Happy Learning! 🎓**

*README auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*
"""
    
    # Write README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ README.md generated successfully!")
    print(f"📊 Found and documented {file_count} Python files")


if __name__ == '__main__':
    generate_readme()
