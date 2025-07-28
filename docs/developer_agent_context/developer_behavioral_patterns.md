# Developer Agent Behavioral Patterns & Standards

## 🔄 **CRITICAL BEHAVIORAL PATTERNS**

### **Bootstrap Instruction Adherence Protocol - MANDATORY**
**ALWAYS reference bootstrap instructions before file operations**
- ✅ **Before any file placement**: State which bootstrap instruction guides the decision
- ✅ **Test organization**: Component tests go in `tests/10_project_components/` per bootstrap instructions
- ✅ **Infrastructure tests**: System tests go in `tests/20_infrastructure/` per bootstrap instructions
- ✅ **When uncertain**: Ask for confirmation rather than guessing placement
- ✅ **Explicit instruction reference**: "According to bootstrap instructions, [specific guidance], so I will [action]"

### **Authorization Protocol - MANDATORY**
**NEVER make file edits without explicit user approval**
- ❌ Do NOT use filesystem:edit_file without permission
- ❌ Do NOT update any project files automatically  
- ✅ ALWAYS ask "Should I make this change?" or "May I update this file?"
- ✅ Wait for explicit "yes", "proceed", or "approved" before editing
- ✅ Show proposed changes and request approval first
- ✅ **CRITICAL**: Ask → STOP and WAIT → Get approval → Then act
- ❌ **NEVER**: Ask question then immediately proceed without waiting

### **Content Review Protocol - CRITICAL**
**Always check existing content before making changes**
- ✅ **Read existing file content first** to identify redundancies/conflicts
- ✅ **Remove conflicting/outdated content** when adding new features
- ✅ **Clean up while adding** - don't just append
- ✅ **Avoid redundant information** in the same file
- ✅ **Update only relevant sections** - don't change what doesn't need changing

---

## 🧪 **REAL FILE vs MOCK TESTING PRINCIPLES**

### **Testing Hierarchy - MANDATORY**
**Prioritize real files over mocks whenever possible**

**Testing Strategy:**
1. **Real files FIRST** - Use actual test files for success scenarios
2. **Strategic mocks ONLY** - For error conditions that can't be tested with real files
3. **No redundant coverage** - Don't test the same thing with both mocks and real files

### **When to Use Real Files vs Mocks**

**✅ Use Real Files For:**
- Success scenarios and normal workflows
- Integration testing with actual OpenCV operations
- Property validation with real video/file data
- Complete end-to-end functionality testing
- Resource management and cleanup verification

**✅ Use Strategic Mocks For:**
- OpenCV creation failures (`VideoCapture.isOpened() = False`)
- Invalid video properties (zero fps, frame count, resolution)
- OpenCV exceptions (`cv2.error`)
- System-level errors that can't be simulated with real files

**❌ Never Mock:**
- File existence checking (use real temp files)
- Format validation (use real file extensions)
- Successful video loading (use real test videos)
- Normal video property extraction

### **Test Fixture System Standards**

**Flexible Fixture Pattern:**
```python
@pytest.fixture
def test_video_files():
    """Provide real test video files with easy extensibility."""
    fixtures_dir = Path(__file__).parent.parent / "fixtures"
    
    available_files = {
        'valid_video': fixtures_dir / "test_video.mp4",
        # Future files easily added:
        # 'high_res_video': fixtures_dir / "high_res_test.mp4",
        # 'different_format': fixtures_dir / "test_video.avi",
    }
    
    # Verify files exist and skip if missing
    existing_files = {}
    for name, path in available_files.items():
        if path.exists():
            existing_files[name] = path
        else:
            pytest.skip(f"Test video file not found: {path}")
    
    return existing_files
```

### **Test Cleanup and Consolidation Principles**

**Focus on Core Functionality:**
- ✅ **Single comprehensive test class** covering all functionality
- ✅ **Real file tests for main workflows**
- ✅ **Strategic mocks grouped at end for error conditions**
- ❌ **No redundant test classes** (avoid TestEdgeCases, TestIntegration, etc.)
- ❌ **No duplicate test coverage** between mocks and real files

**Test Organization:**
```python
class TestVideoLoader:
    """Single focused class testing all VideoLoader functionality."""
    
    # Real file tests first (primary functionality)
    def test_load_real_video_success(self, test_video_files): pass
    def test_multiple_video_loading(self, test_video_files): pass
    def test_complete_workflow(self, test_video_files): pass
    
    # Strategic mocks last (error conditions only)
    @patch('cv2.VideoCapture')
    def test_opencv_creation_fails(self, mock_videocapture): pass
```

### **Mock Cleanup Guidelines**

**Remove Redundant Mocks:**
- ❌ Mock successful video loading (use real files instead)
- ❌ Mock normal property extraction (use real files instead)
- ❌ Mock resource cleanup with fake videos (use real files instead)
- ❌ Multiple test classes testing same functionality

**Keep Essential Mocks:**
- ✅ OpenCV creation failures
- ✅ Invalid video properties
- ✅ OpenCV exceptions
- ✅ System-level errors

---

## 📁 **TEST FIXTURE MANAGEMENT**

### **Real File Fixture Standards**

**Fixture Location:**
- `tests/fixtures/` - Dedicated directory for test files
- Version controlled test files (small videos only)
- Cross-platform compatible formats (MP4 recommended)

**Future Extensibility:**
- Easy to add new test video files
- Fixture automatically discovers available files
- Tests skip gracefully if files missing
- No hardcoded file dependencies

**Usage in `__main__` Sections:**
```python
if __name__ == "__main__":
    def test_with_real_video_if_available():
        # Check for test video and use if available
        test_video_path = Path(__file__).parent.parent / "fixtures" / "test_video.mp4"
        if test_video_path.exists():
            # Test with real file
        else:
            # Graceful skip with helpful message
```

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

## 🔧 **INFRASTRUCTURE INTEGRATION PATTERNS**

### **Standard Import Pattern (MANDATORY)**
**ALL modules must use this exact pattern:**
```python
# Add project root to Python path for proper imports
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# All imports use absolute paths from project root
from config.config_manager import get_project_config
from src.utils.logger_factory import get_component_logger
from src.video_input.video_utils import check_file_exists
```

**Critical Rules:**
- ✅ ALWAYS add project_root to sys.path
- ✅ ALWAYS use absolute imports from project root
- ❌ NEVER use relative imports (from .module)
- ❌ NEVER use path manipulations beyond project_root

### **Configuration Usage Standard**
```python
# Standard pattern for all modules:
try:
    from config import get_project_config
    from utils.logger_factory import get_component_logger
    logger = get_component_logger('component_name')
    config = get_project_config()
except ImportError:
    # Graceful fallback for standalone usage
    import logging
    logger = logging.getLogger(__name__)
    config = None

# In functions: Use module-level variables
if config:
    settings = config.component.core.setting_name
else:
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