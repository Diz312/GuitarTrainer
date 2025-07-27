# Pytest Commands Reference - GuitarTrainer

## 🎯 **Quick Reference Commands**

### **Basic Test Execution**
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/10_project_components/test_video_utils.py

# Run with verbose output
pytest tests/10_project_components/test_video_utils.py -v
```

### **Coverage Commands** 
```bash
# Basic coverage report (terminal)
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input

# Coverage with missing lines shown
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=term-missing

# Generate HTML coverage report
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=html

# Combined terminal + HTML reports
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=term-missing --cov-report=html
```

---

## 📊 **Coverage Reports Explained**

### **Terminal Report (`--cov-report=term`)**
```
Name                             Stmts   Miss  Cover
----------------------------------------------------
src\video_input\__init__.py          2      0   100%
src\video_input\video_utils.py      44      8    82%
----------------------------------------------------
TOTAL                               46      8    83%
```

### **Terminal with Missing Lines (`--cov-report=term-missing`)**
```
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src\video_input\video_utils.py      44      8    82%   45-52, 89
```
Shows exactly which line numbers weren't covered.

### **HTML Report (`--cov-report=html`)**
- Creates `htmlcov/index.html` file
- Open in browser for detailed line-by-line analysis
- Color-coded: Green = covered, Red = missed, Yellow = partial

---

## 🔧 **Recommended Commands for Development**

### **During Development (Quick Check)**
```bash
# Fast feedback - just run the tests
pytest tests/10_project_components/test_video_utils.py -v
```

### **Before Committing (Coverage Check)**
```bash
# Comprehensive coverage report
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=term-missing --cov-report=html
```

### **Deep Analysis (HTML Investigation)**
```bash
# Generate detailed HTML report
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=html

# Then open: htmlcov/index.html in your browser
```

---

## 📁 **Directory Structure for Commands**

### **Run from Project Root:**
```
E:\Python\GitHub\GuitarTrainer\
├── .coveragerc                    # Coverage configuration (auto-loaded)
├── tests/
│   └── 10_project_components/
│       └── test_video_utils.py    # Test file target
├── src/
│   └── video_input/              # Source code target (--cov=src/video_input)
└── htmlcov/                      # Generated HTML reports
    └── index.html                # Main coverage report
```

### **Always Run Commands From:**
```bash
cd E:\Python\GitHub\GuitarTrainer
# Then run pytest commands
```

---

## 🎛️ **Advanced Options**

### **Test Selection**
```bash
# Run specific test function
pytest tests/10_project_components/test_video_utils.py::test_check_file_exists_valid -v

# Run tests matching pattern
pytest tests/10_project_components/test_video_utils.py -k "file_exists" -v

# Run parametrized test with specific parameter
pytest tests/10_project_components/test_video_utils.py::test_validate_video_format_case_insensitive[.mp4] -v
```

### **Output Options**
```bash
# Quiet output (minimal)
pytest tests/10_project_components/test_video_utils.py -q

# Show local variables on failure
pytest tests/10_project_components/test_video_utils.py -l

# Stop on first failure
pytest tests/10_project_components/test_video_utils.py -x

# Show full diff on assertion failures
pytest tests/10_project_components/test_video_utils.py -vv
```

### **Coverage Options**
```bash
# Coverage for multiple modules
pytest tests/ --cov=src --cov-report=html

# Coverage with branch analysis
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-branch --cov-report=html

# Fail if coverage below threshold
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-fail-under=80
```

---

## 📈 **Coverage Configuration**

### **Using .coveragerc File**
The project includes `.coveragerc` which automatically:
- ✅ Excludes `__main__` sections from coverage
- ✅ Focuses coverage on `src/` directory only
- ✅ Ignores test files and virtual environments
- ✅ Shows missing line numbers
- ✅ Sets HTML output directory to `htmlcov/`

### **What Gets Excluded (Automatic)**
```python
# These are automatically excluded from coverage:
if __name__ == "__main__":
    # Demonstration code not counted

def __repr__(self):
    # Representation methods not counted

# pragma: no cover
# Lines with this comment not counted
```

---

## 🔍 **Reading Coverage Reports**

### **Terminal Report Columns:**
- **Stmts**: Total executable statements in file
- **Miss**: Statements not executed during tests  
- **Cover**: Percentage coverage (Stmts - Miss) / Stmts * 100
- **Missing**: Line numbers that weren't executed

### **HTML Report Navigation:**
1. **Open `htmlcov/index.html`** in browser
2. **Click on file names** to see line-by-line coverage
3. **Red lines** = not covered, **Green lines** = covered
4. **Yellow lines** = partially covered (branches)

### **Good Coverage Targets:**
- **80%+** = Excellent coverage
- **60-79%** = Good coverage  
- **40-59%** = Acceptable for development
- **<40%** = Consider adding more tests

---

## ⚡ **Quick Commands Summary**

```bash
# Most common development commands:

# Quick test run
pytest tests/10_project_components/test_video_utils.py -v

# Coverage check  
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=term-missing

# Full analysis
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=html
```

---

## 🚨 **Troubleshooting**

### **Common Issues:**

**1. "ModuleNotFoundError"**
```bash
# Solution: Run from project root
cd E:\Python\GitHub\GuitarTrainer
pytest tests/10_project_components/test_video_utils.py
```

**2. "No coverage data to report"**
```bash
# Solution: Ensure source path is correct
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input
```

**3. "HTML report not generated"**
```bash
# Solution: Check for htmlcov/ directory after command
pytest tests/10_project_components/test_video_utils.py --cov=src/video_input --cov-report=html
ls htmlcov/  # Should show index.html
```

**4. "Tests not found"**
```bash
# Solution: Check file path exists
ls tests/10_project_components/test_video_utils.py
```

---

**💡 Pro Tip**: Bookmark this file for quick reference during development!
