# Immutable

## Overview

This library provides decorators and base classes to create immutable data classes
in Python. By enforcing immutability and keyword-only arguments, it enhances the
robustness and clarity of your data structures.

## 📋 Requirements

- Python 3.9 or later.
- No external dependencies are required.

## 📦 Installation

### Pip

```bash
pip install python-immutable
```

### uv

```bash
uv add python-immutable
```

### Poetry

```bash
poetry add python-immutable
```

## 🛠 Usage

### Using `immutable` Decorator

Apply `immutable` to a class to make it immutable and enforce keyword-only arguments.

```python
from immutable import immutable

@immutable
class MyClass:
    # Fields here
```

### Extending `Immutable` Base Class

Inherit from `Immutable` for similar functionality.

```python
from immutable import Immutable

class MyClass(Immutable):
    # Fields here
```

## 🤝 Contributing

Contributions are welcome. Please submit pull requests or issues on the GitHub repository.

### ⚠️ Important Note

Ensure compatibility with Python 3.9 or newer when contributing.

## 🔒 License

This project is released under the Apache-2.0 License. See the [LICENSE](./LICENSE)
file for more details.
