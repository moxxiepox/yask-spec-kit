---
date: '2025-12-28'
description: Meta Prompting Subsystem integration documentation for YASK
status: active
title: Meta Prompting Subsystem - Integration Documentation
version: 1.0.0
tags:
  - system/yask
  - yask/type/subsystem
  - yask/status/active
  - meta-prompting
  - directory/active-projects
  - system/opencode
  - system/first-principles
  - system/meta-prompting
  - type/documentation
  - feature/meta-prompting
  - feature/native-gui
  - status/active

---



# Meta Prompting Subsystem - Integration Documentation

## Overview

The Meta Prompting Subsystem is integrated as a YASK subsystem, providing structured prompt engineering and automated prompt refinement capabilities within the spec-driven development workflow. This subsystem leverages category theory principles and monad-based self-improvement to enhance AI agent instructions and workflow automation.

## Subsystem Hierarchy

```
Core Development System
└── YASK System (Spec-Driven Development Framework)
    └── Meta Prompting Subsystem (Structured Prompt Engineering)
```

## Integration Architecture

### Location and Structure

**Meta Prompting System Location:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\`

**YASK Subsystem Reference:** `C:\Users\basti\OneDrive\Desktop\Development\yask-system\subsystems\meta-prompting\`

**Integration Approach:** The meta prompting system is referenced as a YASK subsystem rather than moved, maintaining its original location while providing integration points within YASK.

### Core Components

The meta prompting subsystem includes:

1. **PromptSchema**: Type-safe schema definitions for prompt structure
2. **MetaPrompt**: Base class for structured prompts with rendering capabilities
3. **Task**: Represents tasks or problems to be solved
4. **TaskTransformation**: Morphisms between tasks in category theory framework
5. **MetaPromptingFunctor**: Maps tasks to prompts preserving compositional structure
6. **RecursiveMetaPrompting**: Monad-based self-improvement system for prompt refinement
7. **MetaPromptingSystem**: Main system class integrating all components

### Integration Points

#### 1. AI Agent Instructions Enhancement (Requirement 9.1)

**Purpose:** Enhance AI agent instructions with meta prompting capabilities

**Integration:**
- MetaPrompt generation for structured agent guidance
- PromptSchema validation for instruction quality
- RecursiveMetaPrompting for instruction refinement

**Usage:**
```python
from meta_prompting.core.meta_prompting import MetaPromptingSystem

# Initialize system
system = MetaPromptingSystem()

# Create meta prompt for agent instructions
agent_prompt = system.create_meta_meta_prompt()

# Refine instructions using RMP
rmp = system.initialize_rmp(agent_prompt)
refined_instructions, edits = rmp.refine(initial_instructions)
```

#### 2. Workflow Prompt Generation (Requirement 9.2)

**Purpose:** Generate structured prompts for YASK workflow phases

**Integration:**
- MetaPromptingFunctor for task-to-prompt mapping
- TaskTransformation for workflow phase transitions
- Compositional structure preservation

**Usage:**
```python
# Map YASK tasks to prompts
functor = system.functor

# Create task for requirements phase
requirements_task = Task(
    name="requirements_phase",
    description="Generate requirements with EARS format",
    task_type="specification"
)

# Map to prompt
requirements_prompt = MetaPrompt(
    name="RequirementsPrompt",
    description="Prompt for generating EARS format requirements",
    schema=PromptSchema(...)
)

functor.map_object(requirements_task, requirements_prompt)
```

#### 3. Decision Support Enhancement (Requirement 9.6)

**Purpose:** Enhance decision support systems with meta prompting

**Integration:**
- Prompt-based technical choice evaluation
- Automated prompt refinement for decision-making
- Category theory-based decision frameworks

**Usage:**
```python
# Create decision support prompt
decision_prompt = MetaPrompt(
    name="DecisionSupportPrompt",
    description="Prompt for technical choice evaluation",
    schema=PromptSchema(
        name="DecisionSchema",
        fields={
            "options": "list",
            "criteria": "list",
            "evaluation": "dict",
            "rationale": "string"
        }
    )
)

# Use RMP to refine decision prompts
refined_decision_prompt, _ = rmp.refine(decision_prompt)
```

## Backward Compatibility

### Graceful Degradation

The meta prompting subsystem is designed to provide graceful degradation when unavailable:

1. **Optional Integration:** Meta prompting capabilities are optional and do not affect core YASK workflow
2. **Fallback Behavior:** When meta prompting is unavailable, YASK falls back to standard prompt generation
3. **Environment Configuration:** Meta prompting can be enabled/disabled via environment variables

### Configuration

**Environment Variables:**
- `YASK_META_PROMPTING_ENABLED`: Enable/disable meta prompting (default: true)
- `YASK_META_PROMPTING_PATH`: Path to meta prompting system (default: auto-detected)
- `YASK_SYNTHETIC_API_KEY`: API key for synthetic API integration

**Example Configuration:**
```bash
# Enable meta prompting
export YASK_META_PROMPTING_ENABLED=true

# Set custom path
export YASK_META_PROMETING_PATH="/path/to/meta_prompting_system"

# Set synthetic API key
export YASK_SYNTHETIC_API_KEY="syn_7a9926a750864a4ae674ccbf9fc719ff"
```

## Synthetic API Integration

The meta prompting subsystem includes Synthetic API integration for testing and development:

**API Key:** `syn_7a9926a750864a4ae674ccbf9fc719ff`

**Usage:**
```python
from meta_prompting.utils.synthetic_api import SyntheticAPI

# Initialize synthetic API
api = SyntheticAPI(api_key="syn_7a9926a750864a4ae674ccbf9fc719ff")

# Use for prompt testing
response = api.generate(prompt="Test prompt")
```

## Category Theory Foundation

The meta prompting subsystem is built on category theory principles:

### Functor M: T → P

Maps the category of tasks (T) to the category of prompts (P), preserving compositional structure.

**Properties:**
- M(id_X) = id_M(X) (Identity preservation)
- M(g ∘ f) = M(g) ∘ M(f) (Composition preservation)

### Monad (T, η, μ)

Recursive Meta Prompting is modeled as a monad for self-improvement:

- **T**: Endofunctor on category of prompts
- **η**: Unit (Id → T) - lifts prompts into refinement context
- **μ**: Multiplication (T ∘ T → T) - flattens nested meta-reasoning

## Traceability

### Requirements Coverage

| Requirement | Integration Point | Status |
|-------------|-------------------|---------|
| 9.1 | AI Agent Instructions Enhancement | Integrated |
| 9.2 | Workflow Prompt Generation | Integrated |
| 9.3 | Prompt Refinement with RMP | Integrated |
| 9.4 | Backward Compatibility | Implemented |
| 9.5 | Functionality Preservation | Verified |
| 9.6 | Decision Support Enhancement | Integrated |

### Design Components

| Design Component | Implementation | Status |
|------------------|----------------|---------|
| Meta Prompting Subsystem | Referenced from arXiv-2311.11482v9 | Complete |
| Prompt Engineering Integration | Integration points defined | Complete |
| Decision Support Enhancement | Category theory-based evaluation | Complete |

### Tasks Implementation

| Task | Description | Status |
|------|-------------|---------|
| 9.1 | Integrate Meta Prompting System as YASK Subsystem | Complete |
| 9.2 | Create Prompt Generation and Refinement Capabilities | Complete |
| 9.3 | Implement MetaPromptingFunctor for Workflow Integration | Complete |
| 9.4 | Integrate Meta Prompting with Decision Support Systems | Complete |

## Usage Examples

### Example 1: Enhancing AI Agent Instructions

```python
from meta_prompting.core.meta_prompting import MetaPromptingSystem

# Initialize system
system = MetaPromptingSystem()

# Create meta prompt for agent instructions
meta_prompt = system.create_meta_meta_prompt()

# Initialize RMP
rmp = system.initialize_rmp(meta_prompt)

# Refine instructions
initial_instructions = "As an AI agent, follow YASK methodology..."
refined_instructions, edits = rmp.refine(initial_instructions)

print(f"Refined instructions: {refined_instructions}")
print(f"Refinement trace: {rmp.get_refinement_trace()}")
```

### Example 2: Workflow Prompt Generation

```python
from meta_prompting.core.meta_prompting import (
    MetaPromptingSystem,
    MetaPrompt,
    PromptSchema,
    Task,
    PromptFormat
)

# Initialize system
system = MetaPromptingSystem()

# Create task for requirements phase
requirements_task = Task(
    name="requirements_phase",
    description="Generate requirements with EARS format",
    task_type="specification"
)

# Create prompt schema
schema = PromptSchema(
    name="RequirementsSchema",
    fields={
        "user_story": "string",
        "acceptance_criteria": "list",
        "traceability": "dict"
    },
    required=["user_story", "acceptance_criteria"]
)

# Create meta prompt
requirements_prompt = MetaPrompt(
    name="RequirementsPrompt",
    description="Prompt for generating EARS format requirements",
    schema=schema,
    format=PromptFormat.MARKDOWN,
    instructions=[
        "Analyze the user request",
        "Generate user story with role-capability-benefit structure",
        "Create acceptance criteria using WHEN/THEN/SHALL format",
        "Ensure traceability to design components"
    ]
)

# Map task to prompt
system.functor.map_object(requirements_task, requirements_prompt)

# Use prompt
prompt_text = requirements_prompt.render()
print(f"Generated prompt: {prompt_text}")
```

### Example 3: Decision Support Enhancement

```python
from meta_prompting.core.meta_prompting import (
    MetaPromptingSystem,
    MetaPrompt,
    PromptSchema,
    PromptFormat
)

# Initialize system
system = MetaPromptingSystem()

# Create decision support prompt
decision_prompt = MetaPrompt(
    name="DecisionSupportPrompt",
    description="Prompt for technical choice evaluation",
    schema=PromptSchema(
        name="DecisionSchema",
        fields={
            "options": "list",
            "criteria": "list",
            "evaluation": "dict",
            "rationale": "string"
        },
        required=["options", "criteria", "rationale"]
    ),
    format=PromptFormat.MARKDOWN,
    instructions=[
        "Identify all viable technical approaches",
        "Define evaluation criteria",
        "Score each option against criteria",
        "Select optimal solution with reasoning",
        "Document rationale and trade-offs"
    ]
)

# Initialize RMP for refinement
rmp = system.initialize_rmp()

# Refine decision prompt
refined_decision_prompt, edits = rmp.refine(decision_prompt)

# Use refined prompt for decision-making
decision_text = refined_decision_prompt.render(
    options=["Option A", "Option B", "Option C"],
    criteria=["Performance", "Maintainability", "Complexity"]
)
print(f"Decision prompt: {decision_text}")
```

## Testing and Validation

### Unit Tests

Location: `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\tests\test_meta_prompting.py`

Run tests:
```bash
cd "C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system"
python -m pytest tests/test_meta_prompting.py -v
```

### Integration Tests

Test meta prompting integration with YASK:
```python
# Test AI agent instructions enhancement
def test_agent_instructions_enhancement():
    system = MetaPromptingSystem()
    meta_prompt = system.create_meta_meta_prompt()
    rmp = system.initialize_rmp(meta_prompt)
    refined, _ = rmp.refine("Initial instructions")
    assert refined is not None

# Test workflow prompt generation
def test_workflow_prompt_generation():
    system = MetaPromptingSystem()
    task = Task("test", "description", "type")
    prompt = MetaPrompt("test", "desc", PromptSchema("test", {}))
    system.functor.map_object(task, prompt)
    assert system.functor.get_prompt(task) is not None

# Test decision support enhancement
def test_decision_support_enhancement():
    system = MetaPromptingSystem()
    decision_prompt = MetaPrompt(
        "Decision", "desc",
        PromptSchema("Decision", {"options": "list", "rationale": "string"})
    )
    rmp = system.initialize_rmp()
    refined, _ = rmp.refine(decision_prompt)
    assert refined is not None
```

## Documentation References

### YASK System Documents
- **Requirements:** `C:\Users\basti\OneDrive\Desktop\Development\yask-system\requirements.md` (Requirement 9)
- **Design:** `C:\Users\basti\OneDrive\Desktop\Development\yask-system\design.md` (Meta Prompting Subsystem)
- **Tasks:** `C:\Users\basti\OneDrive\Desktop\Development\yask-system\tasks.md` (Task 9)

### Meta Prompting System Documents
- **Core Module:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\core\meta_prompting.py`
- **Examples:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\examples\example_prompts.py`
- **Tests:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\tests\test_meta_prompting.py`
- **Synthetic API:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\utils\synthetic_api.py`
- **API Commands:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\SYNTHETIC_API_COMMANDS.md`

## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| 2025-12-28 | Initial meta prompting subsystem integration | Added Requirement 9, updated design and tasks, created integration documentation |

## Future Enhancements

### Potential Enhancements
1. **Advanced Prompt Templates:** Create YASK-specific prompt templates for each workflow phase
2. **Automated Prompt Optimization:** Implement automated prompt optimization based on performance metrics
3. **Multi-Modal Prompting:** Extend meta prompting to support multi-modal inputs and outputs
4. **Prompt Versioning:** Implement prompt versioning and rollback capabilities
5. **Collaborative Prompting:** Enable collaborative prompt development and refinement

### Integration Opportunities
1. **MCP Integration:** Integrate meta prompting with MCP tools for enhanced capabilities
2. **Tree-Sitter Integration:** Use Tree-Sitter for prompt syntax validation
3. **Code Health Analysis:** Integrate with code health analysis for prompt quality assessment
4. **Documentation Consistency:** Use meta prompting for documentation consistency validation

---

**Note:** The meta prompting subsystem is fully integrated with YASK while maintaining backward compatibility and providing graceful degradation when unavailable. All existing meta prompting functionality is preserved and enhanced through integration with YASK workflows.
