# System Developer Python and AI – Training Exercises

## Advanced Training Program: System Developer Python and AI

This repository contains practical Python exercises completed as part of an **Advanced Training Program in System Developer Python and AI**.

The supplied training material focuses on building a strong Python foundation through hands-on exercises, progressing from basic syntax and data types to strings, collections, conditions, loops, and applied console programs. fileciteturn2file2L2-L4

## 📚 Topics Covered

### Python Fundamentals
- Variables and data types
- `str`, `int`, `float` and `bool`
- Arithmetic operators
- `/`, `//`, `%` and `**`
- Type conversion
- User input with `input()`
- f-strings

### Strings
- `len()`
- Uppercase/lowercase
- `.strip()`
- Indexing and slicing
- String reversal
- `.split()`
- `.replace()`
- `in` membership
- String immutability

Example:
```python
text = "Python Programming"

print(len(text))
print(text.upper())
print(text.lower())
print(text.strip())
print(text[::-1])
```

### Collections
The training covers lists, tuples, sets, dictionaries and nested collections, including indexing, slicing, updating, copying, membership and collection methods. fileciteturn2file0L2-L4

Examples include:
- Lists: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `sorted()`
- Tuples and unpacking
- Sets and uniqueness
- Dictionaries and key/value access
- Nested lists and dictionaries

### Conditions and Boolean Logic
- `if`, `elif`, `else`
- `==`, `!=`, `>`, `<`, `>=`, `<=`
- `and`, `or`, `not`
- Truthy/falsy values
- Membership testing

### Loops
- `for` loops
- `while` loops
- `range()`
- `enumerate()`
- Nested loops
- `break`
- `continue`

Example:
```python
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

## 🧩 Applied Projects

The exercises include several small projects that combine the concepts above.

### Registration Summary
A console program that collects a person's first name, last name, city, year of birth and favourite programming language, then generates a user ID and displays derived information. fileciteturn2file2L3-L4

### Personal Media Catalogue
A catalogue using lists, dictionaries, sets and tuples to represent movies, games or books, including nested indexing and manual retrieval/update operations. fileciteturn2file0L3-L4

### Console Study Tracker
A study-tracking application based on a list of dictionaries. It calculates total study time, time per subject, identifies the longest session, filters sessions and provides a repeated menu. fileciteturn2file1L3-L4

## 🚀 Stretch Challenges

The training also includes progressively harder exercises such as:

- FizzBuzz
- Counting vowels
- Finding duplicate values
- Text histograms
- Number and string manipulation
- Nested collections
- Comparing lists, tuples, sets and dictionaries

The source material explicitly includes these challenges as the final progression of the Python foundation work. fileciteturn2file1L4-L4

## 🛠️ Technologies

- **Python**
- **Visual Studio Code**
- **Git**
- **GitHub**

## 🎯 Learning Objectives

Through these exercises, I am developing practical skills in:

- Writing Python programs from scratch
- Processing user input
- Working with data types and collections
- Manipulating strings
- Implementing conditional logic
- Building programs with loops
- Choosing appropriate data structures
- Combining multiple Python concepts into small applications
- Solving programming problems step by step

## 📂 Suggested Repository Structure

```text
.
├── lesson1_exercises.py
├── collections/
│   ├── lists.py
│   ├── tuples.py
│   ├── sets.py
│   ├── dictionaries.py
│   └── nested_collections.py
├── conditions/
│   ├── conditions.py
│   └── truthy_membership.py
├── loops/
│   ├── for_loops.py
│   ├── range_enumerate.py
│   ├── while_loops.py
│   └── break_continue.py
├── projects/
│   ├── registration_summary.py
│   ├── media_catalogue.py
│   └── study_tracker.py
└── README.md
```

## 📈 Next Steps

This repository documents the Python foundation part of my **Advanced Training Program – System Developer Python and AI**.

The supplied PDFs cover the Python foundation portion; they do not provide specific AI/ML exercises, so this README does not claim AI/ML projects that are not demonstrated in the material.

As the training progresses, this repository can be expanded with more advanced Python development and AI/ML projects.

## 👨‍💻 About

This repository documents my practical learning journey while developing my Python and software development skills through the **Advanced Training Program: System Developer Python and AI**.
