# testpub1

[![Simple Python Test](https://github.com/intuitcode/testpub1/workflows/Simple%20Python%20Test/badge.svg)](https://github.com/intuitcode/testpub1/actions)

A test public repository demonstrating basic Python development with GitHub Actions CI/CD workflow.

## 📋 Overview

This repository contains a simple "Hello World" Python application with automated testing using GitHub Actions. It serves as a starting point for understanding GitHub workflows and continuous integration.

## 🚀 Features

- Simple Python "Hello World" script
- Automated CI/CD pipeline using GitHub Actions
- Runs tests on every push to main branch
- Clean project structure

## 📁 Project Structure

```
testpub1/
├── .github/
│   └── workflows/
│       └── python-test.yml    # GitHub Actions workflow configuration
├── hello_world.py              # Main Python script
└── README.md                   # Project documentation
```

## 🛠️ Installation

### Prerequisites

- Python 3.x
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/intuitcode/testpub1.git
cd testpub1
```

2. Run the script:
```bash
python hello_world.py
```

or

```bash
python3 hello_world.py
```

## 💻 Usage

Simply run the Python script to see the output:

```bash
python hello_world.py
```

**Expected Output:**
```
Hello, World!
```

## 🔄 GitHub Actions Workflow

This repository includes an automated workflow that:

1. Triggers on every push to the `main` branch
2. Sets up a Python environment
3. Checks out the code
4. Runs the `hello_world.py` script

The workflow configuration can be found in `.github/workflows/python-test.yml`.

### Viewing Workflow Runs

You can view the status of workflow runs in the [Actions tab](https://github.com/intuitcode/testpub1/actions) of this repository.

## 📊 Status

- **Latest Build:** ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/intuitcode/testpub1/python-test.yml?branch=main)
- **License:** Not specified

## 🤝 Contributing

This is a test repository, but feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is created for testing and educational purposes.

## 👤 Author

**intuitcode**
- GitHub: [@intuitcode](https://github.com/intuitcode)

## 🙏 Acknowledgments

- Created as a demonstration of GitHub Actions and CI/CD pipelines
- Simple Python example for learning purposes

---

**Created:** October 2025
