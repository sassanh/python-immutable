# README.md for Immutable Library

## Overview

This library provides decorators and base classes to create immutable data classes in Python. By enforcing immutability and keyword-only arguments, it enhances the robustness and clarity of your data structures.

## ⚡️ Requirements

- Python 3.9 or later.
- No external dependencies are required.

## 📦 Installation

Include this library in your Python project by adding the provided file. Use the decorators and classes directly in your scripts.

## 🚀 Usage

### Using `immutable` Decorator

Apply `immutable` to a class to make it immutable and enforce keyword-only arguments.

```python
from your_library import immutable

@immutable
class MyClass:
    # Fields here
```

### Extending `Immutable` Base Class

Inherit from `Immutable` for similar functionality.

```python
from your_library import Immutable

class MyClass(Immutable):
    # Fields here
```

## ⚒️ Contribution

Contributions are welcome. Please submit pull requests or issues on the GitHub repository.

### ⚠️ Important Note

Ensure compatibility with Python 3.9 or newer when contributing.

## 📜 License

This project is released under the Apache-2.0 License. See the LICENSE file for more details.
