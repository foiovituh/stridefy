# 🧭 Stridefy
![GitHub License](https://img.shields.io/github/license/foiovituh/stridefy)

> CLI tool for organizing attack surface targets using STRIDE.

![Image](https://github.com/user-attachments/assets/db43f9ed-7488-4f24-ad96-dfe07b55da20)

## 🔎 About

Stridefy categorizes URLs, endpoints, and API targets using the STRIDE threat model.

STRIDE groups threats into six categories:
- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

Stridefy uses keyword-based heuristics to suggest relevant STRIDE categories for each target.

## 📦 Installation

### Requirements

- Python 3.12+
- pipx

If pipx is not installed:

```bash
sudo apt install pipx
pipx ensurepath
```

After running `pipx ensurepath`, open a new terminal.

### From GitHub

Install Stridefy using pipx:

```bash
pipx install git+https://github.com/foiovituh/stridefy.git
```

### Development environment

Clone and install for development:

```bash
git clone https://github.com/foiovituh/stridefy.git
cd stridefy

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -e ".[dev]"
```

## 🚀 Usage

### Help

```bash
stridefy --help
```

### STRIDE Analysis

Provide one or more text files containing URLs, endpoints, or API targets:

```bash
stridefy <file> [<file> ...]
```

Example:

```bash
stridefy targets.txt endpoints.txt
```

Stridefy analyzes the targets from all provided files and categorizes them according to the STRIDE threat model:

```text
(S)poofing:
https://example.com/login

(I)nformation Disclosure:
https://example.com/download?id=1

(E)levation of Privilege:
https://example.com/admin
```

Only categories with matching targets are displayed.

If no STRIDE categories match:

```text
NO_STRIDE_CATEGORIES_MATCHED
```

## 🧪 Development

Run the test suite:

```bash
pytest
```

Generate a coverage report:

```bash
pytest --cov=stridefy --cov-report=term-missing
```

Run Ruff:

```bash
ruff check . --fix
ruff format .
```

## ⭐ Support the Project

If you like this project or find it useful, please give it a star! It helps increase its visibility and supports future development.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
