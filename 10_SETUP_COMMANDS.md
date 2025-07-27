# GuitarTrainer Project Setup Guide

## Prerequisites
- Python installed
- Git installed
- UV package manager installed ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))

## Quick Setup Commands

### 1. Create UV Environment
```bash
# Create virtual environment
uv venv

# Activate environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

```bash
#Install Requirements
uv pip install -r requirements.txt
```


### 2. Create New GitHub Repository
```bash
# Initialize local repository
git init
git add .
git commit -m "Initial commit: GuitarTrainer project setup"

# Create a new repository using GitHub CLI
gh repo create GuitarTrainer --description "AI-powered guitar training application with pose detection" --public --source=. --remote=origin --push
```



## Daily Development Workflow

### Start Development Session
```bash
cd GuitarTrainer
source .venv/bin/activate  # macOS/Linux
# or .venv\Scripts\activate on Windows
```

### Run Tests
```bash
pytest tests/
```

### End Development Session
```bash
deactivate
```

## Troubleshooting

### UV Not Found
```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or download from https://github.com/astral-sh/uv/releases for Windows
```

### OpenCV Import Error
```bash
# Reinstall with specific version
uv remove opencv-python
uv add opencv-python==4.8.1.78
```

### PyQt6 Display Issues
```bash
# Install system dependencies (Linux only)
sudo apt-get install python3-pyqt6
```

### Permission Issues
```bash
# Fix permissions (macOS/Linux)
chmod +x .venv/bin/activate
```