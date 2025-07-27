# Collaboration Patterns & User Preferences\n\n## 🎯 **USER COMMUNICATION STYLE**\n\n### **Preferred Response Patterns:**\n- **Succinct answers** until elaboration requested\n- **Real-world examples and analogies** when explaining concepts\n- **Ask before generating output** - no assumptions about user needs\n- **Question when ambiguous** - better to clarify than guess wrong\n\n### **\"Iterate\" Command Protocol:**\n**Definition**: Take prompt + response → self-critique → improve → return only improved answer\n**Process**: Iterate minimum 3 times before presenting final result\n**Application**: Use for complex problems requiring refinement\n\n### **Working Style Preferences:**\n- **Efficiency-focused** - minimize redundant work\n- **Methodical approach** - slow, safe, transparent development\n- **Small increments** - build piece by piece with validation\n- **Professional standards** - industry-grade quality with educational value\n\n### **Testing and Coverage Standards:**
- **Portable configuration** - `.coveragerc` version controlled for team consistency
- **Comprehensive documentation** - `PYTEST_COMMANDS.md` reference for all team members
- **Realistic coverage targets** - Exclude demonstration code for achievable goals
- **Development workflow integration** - Quick check → coverage analysis → deep investigation
- **Cross-platform compatibility** - Configuration works on all development environments

---

## 🧠 **ADVANCED DEVELOPMENT PATTERNS**

### **Test Design and Validation:**
- **Test cases must align with function design and scope**
- **Question test assumptions before writing** - what should this function actually do?
- **Don't assume edge cases are failures** - validate against single responsibility principle
- **When tests fail, first ask: "Should this actually fail?"**
- **Distinguish between code bugs vs incorrect test expectations**
- **Test failures might indicate wrong test design, not wrong code**

### **Content Review Before Updates:**
- **Always check existing content before making changes**
- **Read existing file content first** to identify redundancies/conflicts
- **Remove conflicting/outdated content** when adding new features
- **Clean up while adding** - don't just append
- **Avoid redundant information** in the same file
- **Update only relevant sections** - don't change what doesn't need changing

### **Function Scope Validation:**
- **Single responsibility principle** - test what the function claims to do
- **Function name should match function scope** (e.g., validate_video_format = extension validation only)
- **When making design choices, explicitly state what function will/won't do**
- **Align all related components** (tests, docs, implementation) with design decisions
- **Separate concerns** - don't test filesystem validation in format validation

---\n\n## 🔧 **TECHNICAL COMMUNICATION PATTERNS**\n\n### **Documentation Approach:**\n- **Component-based organization** - dedicated subfolders with meaningful names\n- **Professional visualization** - UML/Mermaid over custom HTML\n- **No redundancy** - eliminate duplicate files and formats\n- **Educational focus** - code should teach concepts while maintaining quality\n\n### **File Operation Preferences:**\n- **Targeted updates** - use `filesystem:edit_file` for specific sections\n- **Default to option #2** - update existing sections unless ambiguity exists\n- **Avoid regenerating** entire files unnecessarily\n- **Double-check when uncertain** to prevent file corruption\n\n### **Development Philosophy:**\n- **Micro-incremental building** - one small piece at a time\n- **Test immediately** after each piece\n- **No combination building** - never multiple features simultaneously\n- **User approval gates** before major progression\n- **Educational value** maintained throughout\n\n---\n\n## 📋 **CONTEXT UPDATE COMMANDS**

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

---

## 📋 **SESSION MANAGEMENT PATTERNS**\n\n### **\"Update Sesh\" Command:**\n**Trigger**: User says \"update sesh\"\n**Action**: Comprehensive session log updates with ALL context since last update\n**Detail Level**: Every instruction, decision, and refinement - no matter how small\n**Purpose**: Build institutional memory for long-term collaboration tuning\n\n### **Context Building Strategy:**\n- **Capture every interaction** that affects methodology\n- **Document rationale** behind architectural decisions\n- **Track preference evolution** and working style refinements\n- **Build reusable patterns** for future project acceleration\n\n### **Efficiency Patterns:**\n- **Architect leads methodology** - comprehensive planning reduces development issues\n- **User provides requirements** - clear communication of needs and constraints\n- **Documentation drives development** - thorough specifications enable rapid implementation\n\n---\n\n## 🎨 **VISUAL DOCUMENTATION PREFERENCES**\n\n### **Professional Standards:**\n- **UML/Mermaid diagrams** - industry-standard visualizations\n- **GitHub native support** - text-based, version control friendly\n- **Multiple diagram types** - class, sequence, state, component, flow\n- **Educational annotations** - explain concepts within diagrams\n\n### **Organization Principles:**\n- **Component-centric** - all related docs in single subfolder\n- **Meaningful file names** - descriptive over numbered conventions\n- **Scalable structure** - template approach for future components\n- **Integration clarity** - show how pieces connect\n\n---\n\n### **Latest Documentation Structure Evolution (Current Session)**
- **Phase-based organization** - docs structured by development phases (Phase1-5)
- **Numbered component files** - sequential workflow for developer agents
  - `01_bootstrap_instructions.md` - Foundation knowledge (start here)
  - `02_context_validation_tests.md` - Understanding verification
  - `03_visual_architecture_diagrams.md` - Visual structure
  - `04_technical_specifications.md` - Implementation details
- **Template standardization** - reusable pattern for all future components
- **Workflow clarity** - eliminates confusion about file sequence
- **Developer efficiency** - logical progression from context to code

---

## 🚀 **PROJECT DEVELOPMENT PATTERNS**\n\n### **Developer Agent Approach:**\n- **Technical design documents** - comprehensive component specifications\n- **Two-phase process** - architect designs, developer implements\n- **Micro-incremental execution** - build smallest pieces first\n- **Educational code standards** - readability over optimization\n\n### **Quality Assurance:**\n- **Immediate testing** after each micro-increment\n- **Professional architecture** with educational clarity\n- **Error handling** graceful failures, meaningful messages\n- **Integration planning** - design for future component connections\n\n### **Validation Gates:**\n- **Unit tests** for each piece\n- **Manual testing** with real data\n- **Code review** for educational value\n- **User approval** before major progression\n\n---\n\n## 🔄 **CONTINUOUS IMPROVEMENT PATTERNS**\n\n### **Methodology Evolution:**\n- **Capture learnings** from each project phase\n- **Refine processes** based on efficiency discoveries\n- **Update templates** for future project acceleration\n- **Build institutional knowledge** for long-term collaboration\n\n### **Context Optimization:**\n- **Hierarchical documentation** to manage context window limits\n- **Specialized knowledge files** for different aspects\n- **Quick reference cards** for key patterns\n- **Session archival** when logs become too large\n\n### **Personal Architect Tuning:**\n- **Deep context tracking** for collaboration efficiency\n- **Pattern recognition** in user preferences\n- **Anticipatory guidance** based on established patterns\n- **Adaptive methodology** that improves over time\n\n---\n\n## 💡 **KEY SUCCESS FACTORS**\n\n### **Communication:**\n- Ask for clarification when uncertain\n- Provide context for decisions and recommendations\n- Maintain transparency in architectural choices\n- Respect user's time with efficient interactions\n\n### **Technical Delivery:**\n- Professional quality with educational value\n- Project-specific customization over generic templates\n- Efficient file operations and targeted updates\n- Industry-standard visualization and documentation\n\n### **Collaboration:**\n- Build institutional memory through detailed context tracking\n- Evolve methodology based on discovered efficiencies\n- Maintain consistency in patterns and approaches\n- Enable rapid project acceleration through proven templates\n\n**This document captures the collaborative patterns and preferences that enable highly-tuned personal architect services.**"