# learning-projectsMy first Project
Setting up VS Code

# Hello World

A Python hello world app built with enterprise standards.

## Project Structure
```
hello-world/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── logger.py
├── tests/
│   ├── unit/
│   │   └── test_main.py
│   └── integration/
│       └── test_integration.py
├── logs/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

## Run
```bash
python -m src.main
```

## Test
```bash
pytest tests/ -v
```

## Lint
```bash
flake8 src/ tests/
```

## Security Scan
```bash
bandit -r src/
```

## Full CI/CD Check
```bash
flake8 src/ tests/ && pytest tests/ -v && bandit -r src/
```