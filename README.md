# local-package-demo

Example scientific Python package demonstrating a clean architecture. In this project I show how to build a minimal python package from scratch following good standards in 2026

# Architechture

This is the current project architechture:

```bash
local-package-demo/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── CHANGELOG.md
│
├── src/
│   └── local_package_demo/
│       ├── __init__.py
│       ├── config.py
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   ├── algorithms.py
│       │   └── processing.py
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── math_utils.py
│       │   └── io_utils.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── data_model.py
│
├── tests/
│   ├── test_algorithms.py
│   └── test_utils.py
│
├── examples/
│   └── basic_example.py
│
└── docs/
    └── index.md
```

## Installation

```bash
pip install -e .
```

## Example

```bash
from local_package_demo import process_signal

data = [1,2,3,4]

print(process_signal(data))
```
