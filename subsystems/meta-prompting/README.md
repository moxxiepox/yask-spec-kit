---
date: '2025-12-28'
description: Meta Prompting Subsystem README for YASK
status: active
title: Meta Prompting Subsystem - README
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
  - status/active

---



# Meta Prompting Subsystem

## Overview

The Meta Prompting Subsystem is a YASK subsystem that provides structured prompt engineering and automated prompt refinement capabilities. It is based on category theory principles and monad-based self-improvement, enabling AI agents to generate and refine structured prompts within the spec-driven development workflow.

## Location

**Original System:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\`

**YASK Subsystem Reference:** `C:\Users\basti\OneDrive\Desktop\Development\yask-system\subsystems\meta-prompting\`

## Core Components

### 1. PromptSchema
Type-safe schema definitions for prompt structure validation.

### 2. MetaPrompt
Base class for structured prompts with rendering capabilities in multiple formats (JSON, Markdown, XML, Plain).

### 3. Task
Represents tasks or problems to be solved in the category theory framework.

### 4. TaskTransformation
Morphisms between tasks, enabling compositional problem-solving strategies.

### 5. MetaPromptingFunctor
Maps tasks to prompts preserving compositional structure (M: T → P).

### 6. RecursiveMetaPrompting
Monad-based self-improvement system for automated prompt refinement.

### 7. MetaPromptingSystem
Main system class integrating all components.

## Integration with YASK

### AI Agent Instructions Enhancement
Meta prompting enhances AI agent instructions by:
- Generating structured prompts following category theory principles
- Refining instructions using RecursiveMetaPrompting
- Validating prompts using PromptSchema

### Workflow Prompt Generation
Meta prompting supports YASK workflows by:
- Mapping workflow tasks to structured prompts
- Preserving compositional structure across workflow phases
- Generating phase-specific prompts (Requirements, Design, Tasks, Implementation)

### Decision Support Enhancement
Meta prompting enhances decision support by:
- Creating prompt-based technical choice evaluation frameworks
- Automating prompt refinement for decision-making processes
- Providing category theory-based decision frameworks

## Usage

### Basic Usage

```python
from meta_prompting.core.meta_prompting import MetaPromptingSystem

# Initialize system
system = MetaPromptingSystem()

# Create meta prompt
meta_prompt = system.create_meta_meta_prompt()

# Initialize RMP
rmp = system.initialize_rmp(meta_prompt)

# Refine instructions
refined_instructions, edits = rmp.refine(initial_instructions)
```

### Workflow Integration

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
    format=PromptFormat.MARKDOWN
)

# Map task to prompt
system.functor.map_object(requirements_task, requirements_prompt)
```

## Configuration

### Environment Variables

- `YASK_META_PROMPTING_ENABLED`: Enable/disable meta prompting (default: true)
- `YASK_META_PROMETING_PATH`: Path to meta prompting system (default: auto-detected)
- `YASK_SYNTHETIC_API_KEY`: API key for synthetic API integration

### Example Configuration

```bash
# Enable meta prompting
export YASK_META_PROMPTING_ENABLED=true

# Set custom path
export YASK_META_PROMETING_PATH="/path/to/meta_prompting_system"

# Set synthetic API key
export YASK_SYNTHETIC_API_KEY="syn_7a9926a750864a4ae674ccbf9fc719ff"
```

## Synthetic API Integration

The meta prompting subsystem includes Synthetic API integration for testing and development.

**API Key:** `syn_7a9926a750864a4ae674ccbf9fc719ff`

**Usage:**
```python
from meta_prompting.utils.synthetic_api import SyntheticAPI

# Initialize synthetic API
api = SyntheticAPI(api_key="syn_7a9926a750864a4ae674ccbf9fc719ff")

# Use for prompt testing
response = api.generate(prompt="Test prompt")
```

## Testing

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
```

## Documentation

- **Integration Documentation:** `INTEGRATION.md`
- **Core Module:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\core\meta_prompting.py`
- **Examples:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\examples\example_prompts.py`
- **Tests:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\tests\test_meta_prompting.py`
- **Synthetic API:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\utils\synthetic_api.py`
- **API Commands:** `C:\Users\basti\OneDrive\Desktop\Development\arXiv-2311.11482v9\meta_prompting_system\SYNTHETIC_API_COMMANDS.md`

## Backward Compatibility

The meta prompting subsystem provides graceful degradation when unavailable:

1. **Optional Integration:** Meta prompting capabilities are optional and do not affect core YASK workflow
2. **Fallback Behavior:** When meta prompting is unavailable, YASK falls back to standard prompt generation
3. **Environment Configuration:** Meta prompting can be enabled/disabled via environment variables

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

## License

This subsystem is part of the YASK system and follows the same licensing terms.

## Support

For issues, questions, or contributions related to the meta prompting subsystem, please refer to the main YASK documentation and issue tracking system.

---

**Note:** The meta prompting subsystem is fully integrated with YASK while maintaining backward compatibility and providing graceful degradation when unavailable. All existing meta prompting functionality is preserved and enhanced through integration with YASK workflows.
