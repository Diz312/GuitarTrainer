# Developer Agent Behavioral Patterns & Standards

## 🔄 **CRITICAL BEHAVIORAL PATTERNS**

### **Authorization Protocol - MANDATORY**
**NEVER make file edits without explicit user approval**
- ❌ Do NOT use filesystem:edit_file without permission
- ❌ Do NOT update any project files automatically  
- ✅ ALWAYS ask "Should I make this change?" or "May I update this file?"
- ✅ Wait for explicit "yes", "proceed", or "approved" before editing
- ✅ Show proposed changes and request approval first

### **Content Review Protocol - CRITICAL**
**Always check existing content before making changes**
- ✅ **Read existing file content first** to identify redundancies/conflicts
- ✅ **Remove conflicting/outdated content** when adding new features
- ✅ **Clean up while adding** - don't just append
- ✅ **Avoid redundant information** in the same file
- ✅ **Update only relevant sections** - don't change what doesn't need changing

---

## 🧪 **TESTING METHODOLOGY STANDARDS**

### **Dual Testing Pattern - MANDATORY**
**Every module must have both automated testing AND manual demonstration**

**CORRECT Approach**:
```python
# module.py - Clean module with __main__ for demonstration
def some_function(): pass

if __name__ == "__main__":
    """Manual testing and demonstration only"""
    print("🎯 MODULE DEMONSTRATION")
    result = some_function()
    print(f"✅ Function result: {result}")

# tests/XX_category/test_module.py - Separate pytest file
def test_some_function():
    """Automated testing in separate file"""
    assert some_function() == expected
```

**WRONG Approach (Never Do)**:
- ❌ Mixed pytest functions inside module files
- ❌ Running pytest within `__main__` sections

### **Test Organization Standards**
- ✅ **Separate pytest files** in organized `tests/XX_category/` directories
- ✅ **Test organization** - Numbered directories (10_project_components/, 20_infrastructure/, 30_integration/)
- ✅ **Dynamic demonstrations** - Never hardcode values in `__main__` sections

### **Coverage Methodology**
**Standard Testing Workflow**:
```bash
# Quick development check
pytest tests/10_project_components/test_module.py -v

# Coverage analysis
pytest tests/10_project_components/test_module.py --cov=src/module --cov-report=term-missing

# Deep investigation
pytest tests/10_project_components/test_module.py --cov=src/module --cov-report=html
```

**Infrastructure Requirements**:
- `.coveragerc` with `__main__` exclusions
- `PYTEST_COMMANDS.md` reference documentation
- `.gitignore` updates for coverage files
- Numbered test directory organization

---

## 🔧 **DYNAMIC DATA STRUCTURE HANDLING**

### **CORE PRINCIPLE - Always Use Dynamic Patterns**
**Always:**
- ✅ Use recursive functions to traverse data structures
- ✅ Loop through available data dynamically
- ✅ Handle unknown structure sizes gracefully

**Never:**
- ❌ Hardcode specific print statements for known values
- ❌ Assume specific data structure contents
- ❌ Write separate code for each possible value

### **Correct Dynamic Pattern**:
```python
# ✅ CORRECT: Dynamic recursive printing
def print_structure_recursively(data, indent=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print(f"{'  ' * indent}{key}:")
            print_structure_recursively(value, indent + 1)
        else:
            print(f"{'  ' * indent}{key}: {value}")
```

### **Anti-Pattern (Never Use)**:
```python
# ❌ WRONG: Hardcoded specific values
print(f"Video formats: {config.video.core.supported_formats}")
print(f"GUI width: {config.gui.core.window.width}")
```

---

## 🏗️ **INFRASTRUCTURE INTEGRATION PATTERNS**

### **Configuration Usage Standard**
```python
# Standard pattern for all modules:
try:
    from config import get_project_config
    config = get_project_config()
    settings = config.component.core.setting_name
except ImportError:
    # Graceful fallback for standalone usage
    settings = fallback_value
```

### **Logging Usage Standard**
```python
# Standard pattern for all modules:
try:
    from utils.logger_factory import get_component_logger
    logger = get_component_logger('component_name')
except ImportError:
    logger = logging.getLogger(__name__)
```

---

## 📝 **CODE QUALITY STANDARDS**

### **Comment Placement Rules**
**ALL comments including Educational Notes MUST be inside function bodies**
- ❌ Never place Educational Notes outside functions
- ❌ Never place explanatory comments between functions
- ✅ All Educational Notes go inside the function docstring or body
- ✅ All explanatory comments go inside the function they explain

### **Function Scope Validation**
**Validate that function behavior matches stated purpose**
- ✅ **Single responsibility principle** - test what the function claims to do
- ✅ **Separate concerns** - don't test filesystem validation in format validation
- ✅ **Function name should match function scope** (e.g., validate_video_format = extension validation only)
- ✅ **When making design choices, explicitly state what function will/won't do**
- ✅ **Align all related components** (tests, docs, implementation) with design decisions

---

## 🔬 **TEST DESIGN VALIDATION**

### **Test Case Alignment Principles**
**Test cases must align with function design and scope**
- ✅ **Always verify test cases match actual function responsibility**
- ✅ **Question test assumptions before writing** - what should this function actually do?
- ✅ **Don't assume edge cases are failures** - validate against single responsibility principle
- ✅ **When tests fail, first ask: "Should this actually fail?"**
- ✅ **Distinguish between code bugs vs incorrect test expectations**
- ✅ **Test failures might indicate wrong test design, not wrong code**

---

## 🔄 **MICRO-INCREMENTAL DEVELOPMENT DISCIPLINE**

### **Development Rules**
**Always:**
- ✅ Build smallest possible piece first
- ✅ Test immediately after each piece
- ✅ Validate before proceeding to next increment
- ✅ Ask permission before major progression
- ✅ Document progress in appropriate files

**Never:**
- ❌ Combine multiple capabilities in one increment
- ❌ Skip testing/validation steps
- ❌ Assume previous work is correct without validation

---

## 📋 **REQUIREMENTS.TXT MANAGEMENT**

### **Mandatory Protocol for ALL Agents**

**1. Read Current File First**:
```python
# Always read existing requirements.txt from project root
with open('requirements.txt', 'r') as f:
    current_requirements = f.read()
```

**2. Show Proposed Changes Explicitly**:
```
"I need to update requirements.txt to add pytest dependencies.

**Current requirements.txt content:**
[current content]

**Proposed changes:**
+ [new dependencies]

**Updated requirements.txt would contain:**
[complete updated content]

May I proceed with this requirements.txt update?"
```

**3. Request Permission Before ANY Changes**:
- Never update requirements.txt without explicit user approval
- Show complete before/after comparison
- Explain why each dependency is needed
- Wait for confirmation before proceeding

**NEVER DO**:
❌ Update requirements.txt without reading current content  
❌ Make changes without showing proposed modifications  
❌ Update without explicit user permission  

**ALWAYS DO**:
✅ Read current file first  
✅ Show before/after comparison  
✅ Request permission explicitly  

---

## 📋 **CONTEXT UPDATE COMMANDS**

### **"Update Contexts" Command Protocol**
**Trigger**: User says "update contexts"  
**Action**: Systematic optimization across ALL three context file types  
**Approach**: Preserve essential knowledge, archive project-specific details  

**Process:**
1. **Architect Context Files** (`docs/architect_agent_context/`):
   - Optimize for future project bootstrapping
   - Keep essential methodology and infrastructure standards
   - Archive project-specific implementation details
   - Consolidate redundant information into specialized files

2. **Developer Context Files** (`docs/developer_agent_context/`):
   - Extract behavioral patterns for future developer agents
   - Archive project-specific implementation details
   - Create clean behavioral standards reference
   - Preserve critical development patterns and protocols

3. **Project Progress Context Files** (`docs/project_progress_context/`):
   - Consolidate current status from archived content and existing files
   - Update progress with latest implementation details
   - Integrate infrastructure and quality gate achievements
   - Optimize for current development continuation

**Goal**: Maintain lean, focused context files while preserving all critical knowledge for future projects and current development continuation.

### **Individual Update Commands**
**Commands:**
- **"update thinking"** - Update `docs/developer_agent_context/` files (general behavior patterns)
- **"update progress"** - Update `docs/PhaseN/` files (project-specific progress)

**Process:**
1. **Read existing files first** - Understand current state
2. **Assess if updates needed** - Based on actual new information
3. **Ask permission before changes** - NEVER update automatically
4. **Update only relevant sections** - Don't change what doesn't need changing

---

## ✅ **SUCCESS CRITERIA**

### **Quality Gates for All Development**
- Educational comments comprehensive and inside function bodies
- Error handling robust and graceful
- Professional code patterns maintained
- Test coverage comprehensive with dual methodology
- Integration points designed for future connections
- Micro-incremental approach maintained throughout
- Dynamic data structure handling used consistently
- Infrastructure integration patterns followed

### **Behavioral Compliance**
- Authorization requested before ALL file operations
- Content reviewed before making changes
- Testing methodology followed (separate pytest files + `__main__` demonstrations)
- Requirements.txt protocol followed for dependency changes
- Function scope validated against stated purpose
- Test design aligned with function responsibilities

**These behavioral patterns and standards apply to ALL future development projects and must be consistently followed by developer agents.**