---
date: '2025-12-28'
description: Comprehensive document creation guide for spec-driven development
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: Document Patterns & Templates
version: 6.0.0
---

# Document Patterns & Templates

Comprehensive document creation guide for spec-driven development.

## Purpose
This guide provides complete document structures, templates, and formatting guidelines for creating consistent, high-quality specifications.

## Core Principles
1. **Clean, Scannable Content**: Organized, hierarchical format
2. **Essential Information**: Focus on actionable content only
3. **Template-Based Consistency**: Use established patterns
4. **Cross-Reference Support**: Clear links between documents

## Adaptation Guidelines

### Core Requirements (Always Maintain)
- EARS format: `WHEN [event] THEN [system] SHALL [response]`
- Hierarchical task structure with checkboxes
- Requirement traceability across all documents
- Phase progression and approval gates
- Cross-document consistency maintenance

### Contextual Adaptation (Adjust as Needed)
- Document structure based on project complexity and existing patterns
- Communication style and technical detail level based on audience
- Implementation approaches and technology choices
- Template section ordering when it improves clarity
- Additional sections when project complexity demands it

### Adaptation Process
- Use patterns from this document as baseline
- Check existing project documentation for established conventions
- Adapt to user preferences documented in map.md or project standards
- Always preserve core requirements while adapting to context
- Scale documentation appropriately to feature complexity

## Requirements Document

### Template Reference
**CRITICAL**: Load and use the actual file `templates/requirements-template.md` as your structure guide. Do NOT use the examples below as templates - they are for reference only.

### Complete Structure
```markdown
# [Feature Name] Requirements

## Introduction
[Concise feature description and technical approach]

## Requirements

### Requirement 1: [Title]

**User Story:** As a [role], I want [capability], so that [benefit]

#### Acceptance Criteria

1. WHEN [event] THEN [system] SHALL [response]
2. IF [precondition] THEN [system] SHALL [behavior]

### Requirement 2: [Title]

**User Story:** As a [role], I want [capability], so that [benefit]

#### Acceptance Criteria

1. WHEN [event] THEN [system] SHALL [response]
2. WHEN [event] AND [condition] THEN [system] SHALL [behavior]

## Constraints & Assumptions

**Constraints:**
- [Technical/business constraints]

**Assumptions:**
- [Key assumptions about system/users]
```

### EARS Format Rules
- **WHEN**: `WHEN [event] THEN [system] SHALL [response]`
- **IF**: `IF [precondition] THEN [system] SHALL [response]`
- **WHERE**: `WHERE [condition] [system] SHALL [behavior]`

### Content Guidelines
- **User Stories**: Clear role, capability, and benefit
- **Acceptance Criteria**: Testable, unambiguous conditions
- **Constraints**: Technical and business limitations
- **Assumptions**: Key assumptions about system or users

### Conceptual Prototyping & User Intent Analysis Examples
- **Request**: "Build a login system" → **Conceptualize**: Full authentication ecosystem, social login, MFA, user management, security policies
- **Request**: "Add a database" → **Explore**: Data architecture, scalability patterns, backup strategies, performance optimization, future growth
- **Request**: "Make it faster" → **Expand**: Performance monitoring, caching strategies, optimization opportunities, user experience improvements
- **Request**: "Fix the bug" → **Investigate**: Root cause analysis, prevention strategies, code quality improvements, testing enhancements

### Conceptual Expansion Patterns
- **Take user ideas further**: Explore implications, possibilities, and enhancement opportunities
- **Ask "what if" questions**: Encourage exploration of alternatives and creative possibilities
- **Suggest related improvements**: Identify opportunities that complement the main request
- **Explore end ideals**: Help users articulate and refine their ultimate vision

### Self-Sufficiency Examples
- **Missing dependency**: Research installation methods, provide commands, ask for confirmation
- **Unknown technology**: Analyze existing patterns, research documentation, suggest learning approach
- **Configuration needed**: Check existing config files, identify missing settings, propose solutions
- **Capability limitations**: Acknowledge what you cannot do, suggest alternatives or user assistance

## Design Document

### Template Reference
**CRITICAL**: Load and use the actual file `templates/design-template.md` as your structure guide. Do NOT use the examples below as templates - they are for reference only.

### Complete Structure
```markdown
# [Feature Name] Design

## Overview
[System architecture summary and core innovation]

## Architecture
[High-level system design and integration points]

## Components

### [Component 1]
**Purpose**: [What this component does]
**Responsibilities**: [Key responsibilities]
**Interface**: [API or interface definition]

### [Component 2]
**Purpose**: [What this component does]
**Responsibilities**: [Key responsibilities]
**Interface**: [API or interface definition]

## Error Handling
- **Validation Errors**: [How input validation failures are handled]
- **System Errors**: [How infrastructure failures are handled]
- **Recovery**: [Fallback mechanisms and graceful degradation]

## Testing Strategy
- **Unit Tests**: [Component testing approach]
- **Integration Tests**: [System integration testing]
- **End-to-End Tests**: [User journey testing]

## Design Decisions

### Decision 1: [What was decided]
**Options considered**: [Option 1], [Option 2]
**Rationale**: [Why this option was chosen]
**Impact**: [Impact on system]
**Requirements addressed**: [Requirement references]
```

### Design Decision Format
Each design decision should include:
- **Options considered**: List alternatives that were evaluated
- **Rationale**: Why this option was chosen over others
- **Impact**: Effect on system architecture, performance, or maintainability
- **Requirements addressed**: Which requirements this decision satisfies

### Content Guidelines
- **Overview**: High-level architecture and key innovations
- **Architecture**: System design and integration points
- **Components**: Detailed component specifications with clear interfaces
- **Error Handling**: Comprehensive error scenarios and recovery strategies
- **Testing Strategy**: Approach for validating the design

## Tasks Document

### Template Reference
Use `templates/tasks-template.md` as the starting point.

### Complete Structure
```markdown
# [Feature Name] Implementation Tasks

## Tasks

- [ ] 1. Set up project structure and core interfaces
  - Create directory structure for models, services, repositories, and API components
  - Define interfaces that establish system boundaries
  - _Requirements: [Requirement references]_

- [ ] 2. Implement data models and validation
- [ ] 2.1 Create core data model interfaces and types
  - Write TypeScript interfaces for all data models
  - Implement validation functions for data integrity
  - _Requirements: [Requirement references]_

- [ ] 2.2 Implement User model with validation
  - Write User class with validation methods
  - _Requirements: [Requirement references]_

- [ ]* 2.3 Write unit tests for data models
  - Create unit tests for User model validation
  - Write unit tests for relationship management
  - _Requirements: [Requirement references]_

- [ ] 3. Create storage mechanism
- [ ] 3.1 Implement database connection utilities
  - Write connection management code
  - Create error handling utilities for database operations
  - _Requirements: [Requirement references]_

- [ ] 3.2 Implement repository pattern for data access
  - Code base repository interface
  - Implement concrete repositories with CRUD operations
  - _Requirements: [Requirement references]_
```

### Task Format Rules
- **Hierarchical Structure**: Use numbered main tasks (1, 2, 3) with sub-tasks (1.1, 1.2)
- **Checkbox Format**: `- [ ]` for pending, `- [x]` for completed
- **Optional Tasks**: Mark with `*` (e.g., `- [ ]* 1.2 Optional sub-task`)
- **Implementation Details**: Include specific steps under each task
- **Requirement References**: Use `_Requirements: [references]_` for traceability

### Content Guidelines
- **Incremental Approach**: Each task builds on previous tasks
- **Discrete Steps**: Tasks should be independently completable
- **Clear Verification**: Include how to verify task completion
- **Requirement Traceability**: Link tasks back to specific requirements

## Status Update Patterns

### Task Status Indicators
- `[ ]` - Pending task
- `[🚧]` - In-progress task  
- `[x]` - Completed task

## Reference Patterns

### Cross-References
```markdown
_Requirements: [Requirement references]_
_See design.md for technical details_
```

## Quality Standards

### Requirements
- EARS format: `WHEN [event] THEN [system] SHALL [response]`
- Clear user stories
- Technical precision

### Design  
- Address all requirements
- Clear architecture and rationale
- Component specifications

### Tasks
- Hierarchical structure with sub-tasks
- Discrete, actionable steps
- Requirement references
- Incremental approach

## Supplementary Documents

### Map Document Pattern
**When to create**: For any project with >3 specification documents
**Purpose**: Project structure overview, status tracking, maintenance guidelines

```markdown
# [Project Name]: Project Structure Map

## Project Organization
[Directory structure with explanations]

## Project Status
**Phase**: [current phase]
**Health Score**: [health check results]
**Progress**: [task completion percentage]

## Document Purposes
[Each document's role and update triggers]

## Maintenance Guidelines
[Update procedures and review process]
```

### Architecture Directory Pattern
**When to create**: When design.md >10 pages or >5 major components
**Purpose**: Detailed architectural specifications organized by system area

```
architecture/
├── README.md           # Architecture navigation
├── core-systems/       # Core component specs
├── interfaces/         # API and data models
└── integration/        # System integration patterns
```

## AI Agent Guidelines
**Template Priority**: Always load actual template files from `.yask/templates/` rather than using examples
**Context Loading**: Always read requirements.md, design.md, tasks.md before implementation
**Hierarchical Tasks**: Structure with optional tasks marked "*"
**Single Task Focus**: Execute one task at a time with comprehensive summaries
**Quality Focus**: Working code with proper diagnostic validation
**Clear Traceability**: Link requirements → design → tasks → implementation
**Proactive Quality Assurance**: Anticipate issues, verify formats, ensure compliance with patterns
**Pseudocode Fallback**: For complex code issues, use pseudocode reconstruction approach
**Local-First Dependencies**: Prefer local installations for workspace isolation and project hygiene

## Enhanced AI Reasoning and Decision Frameworks

### Structured Decision-Making Patterns

#### Technical Choice Evaluation Matrix
```
EVALUATION CRITERIA FRAMEWORK:

Performance Impact (Weight: 25%)
- Speed and efficiency implications
- Scalability considerations
- Resource utilization optimization
- Response time requirements

Maintainability (Weight: 20%)
- Code clarity and documentation
- Ease of debugging and testing
- Long-term sustainability
- Team knowledge requirements

Development Complexity (Weight: 20%)
- Implementation difficulty
- Learning curve for team
- Integration complexity
- Time to market implications

Architecture Alignment (Weight: 15%)
- Consistency with existing patterns
- Technology stack compatibility
- Design principle adherence
- Future extensibility

Risk Assessment (Weight: 10%)
- Technical risk evaluation
- Business impact potential
- Mitigation strategy availability
- Rollback complexity

Cost-Benefit Analysis (Weight: 10%)
- Development cost estimation
- Operational cost implications
- ROI potential
- Resource allocation efficiency

DECISION MATRIX TEMPLATE:
Option A: [Score 1-5] × [Weight] = [Weighted Score]
Option B: [Score 1-5] × [Weight] = [Weighted Score]
Option C: [Score 1-5] × [Weight] = [Weighted Score]

SELECT OPTION with highest weighted score + document rationale
```

#### Problem-Solving Thought Processes

**Context Analysis Framework:**
```
SITUATION ASSESSMENT:
1. CURRENT STATE: What exists now?
2. DESIRED STATE: What needs to be achieved?
3. CONSTRAINTS: What limitations exist?
4. RESOURCES: What tools and knowledge are available?
5. STAKEHOLDERS: Who is affected by decisions?
6. TIMELINE: What are the deadlines and milestones?

PROBLEM DECOMPOSITION:
- Break complex problems into manageable components
- Identify interdependencies and relationships
- Prioritize components by impact and complexity
- Plan systematic resolution approach
```

**Option Generation and Evaluation:**
```
OPTION GENERATION:
1. CONVENTIONAL: Standard industry approaches
2. INNOVATIVE: Creative or novel solutions
3. HYBRID: Combination of existing approaches
4. MINIMAL: Minimal viable solution approach
5. COMPREHENSIVE: Full-featured solution

EVALUATION PROCESS:
1. FEASIBILITY: Can it be implemented?
2. EFFECTIVENESS: Will it solve the problem?
3. EFFICIENCY: Is it the best use of resources?
4. SUSTAINABILITY: Can it be maintained long-term?
5. ACCEPTABILITY: Will stakeholders approve?

DECISION CRITERIA:
- Must-have requirements satisfaction
- Nice-to-have feature prioritization
- Risk tolerance consideration
- Resource availability assessment
```

### Advanced Prompting Strategies

#### Context Setting and Communication Patterns

**Project Context Establishment:**
```
CONTEXT LOADING PROTOCOL:
1. READ all relevant specification documents
2. ANALYZE current project phase and objectives
3. IDENTIFY constraints, assumptions, and dependencies
4. CLARIFY success criteria and quality standards
5. CONFIRM understanding with stakeholder validation

COMMUNICATION FRAMEWORK:
- Use clear, specific language
- Provide comprehensive context before requests
- Ask clarifying questions when uncertain
- Summarize understanding for confirmation
- Document decisions and rationale
```

**Phase Transition Communication:**
```
REQUIREMENTS → DESIGN TRANSITION:
"Based on approved requirements, I will create a comprehensive technical design that:
- Addresses all specified requirements
- Provides clear architecture and component definitions
- Includes design decisions with rationale
- Plans for error handling and testing
- Maintains traceability to requirements"

DESIGN → TASKS TRANSITION:
"Breaking down the approved design into actionable implementation tasks:
- Decomposing components into discrete coding steps
- Sequencing tasks for logical implementation flow
- Maintaining requirement traceability
- Identifying optional tasks for testing and enhancements"

TASKS → IMPLEMENTATION TRANSITION:
"Executing the selected implementation task:
- Loading complete specification context
- Implementing functionality with quality validation
- Verifying against requirements and design
- Providing comprehensive progress summary"
```

#### Quality Assurance Prompting

**Pre-Implementation Validation:**
```
QUALITY CHECK PROTOCOL:
1. FORMAT COMPLIANCE: Verify document structure and template adherence
2. CONTENT COMPLETENESS: Ensure all required sections are present
3. LOGICAL CONSISTENCY: Check for internal contradictions
4. TRACEABILITY VERIFICATION: Confirm requirement-to-implementation links
5. FEASIBILITY ASSESSMENT: Validate technical approach viability

VALIDATION QUESTIONS:
- Does this meet all specified requirements?
- Is the approach technically sound and feasible?
- Are there any gaps or inconsistencies?
- Will this integrate properly with existing systems?
- What are the potential risks and mitigation strategies?
```

**Post-Implementation Verification:**
```
IMPLEMENTATION VALIDATION:
1. FUNCTIONALITY TESTING: Verify against acceptance criteria
2. CODE QUALITY ANALYSIS: Check syntax, structure, and best practices
3. INTEGRATION TESTING: Confirm compatibility with existing systems
4. PERFORMANCE VALIDATION: Ensure efficiency and scalability
5. DOCUMENTATION ACCURACY: Verify documentation reflects implementation

VERIFICATION CHECKLIST:
- [ ] All acceptance criteria satisfied
- [ ] Code passes syntax and quality checks
- [ ] Integration points work correctly
- [ ] Performance meets requirements
- [ ] Documentation is accurate and complete
- [ ] No regression issues introduced
```

### Enhanced Template Usage Guidelines

#### Template Selection and Adaptation

**Template Selection Criteria:**
```
TEMPLATE SELECTION MATRIX:

Project Complexity:
- Simple (1-3 requirements) → Basic templates
- Moderate (4-10 requirements) → Standard templates
- Complex (10+ requirements) → Enhanced templates with architecture

Team Size:
- Solo developer → Streamlined templates
- Small team (2-5) → Standard templates
- Large team (5+) → Comprehensive templates with detailed traceability

Technical Domain:
- Web development → Standard templates
- System programming → Enhanced technical templates
- Data science → Specialized domain templates
- Mobile development → Platform-specific templates

Documentation Needs:
- Minimal → Basic templates
- Standard → Regular templates
- Comprehensive → Detailed templates with extensive cross-referencing
```

**Template Adaptation Guidelines:**
```
ADAPTATION PRINCIPLES:
1. PRESERVE core structure and required elements
2. ENHANCE sections based on project complexity
3. CUSTOMIZE examples to match domain and technology
4. MAINTAIN consistency across all project documents
5. SCALE documentation appropriately to feature scope

ADAPTATION CHECKLIST:
- [ ] Core template structure maintained
- [ ] Required sections present and complete
- [ ] Domain-specific examples included
- [ ] Technology-specific considerations addressed
- [ ] Cross-references updated for project context
- [ ] Quality standards maintained throughout
```

#### Cross-Document Consistency Patterns

**Traceability Maintenance:**
```
TRACEABILITY FRAMEWORK:
1. REQUIREMENT IDENTIFICATION: Unique IDs for each requirement
2. DESIGN MAPPING: Link design components to specific requirements
3. TASK BREAKDOWN: Reference requirements in each implementation task
4. IMPLEMENTATION VALIDATION: Verify code satisfies specific requirements
5. TEST COVERAGE: Ensure tests validate requirement satisfaction

CONSISTENCY VALIDATION:
- Every requirement must have design coverage
- Every design component must trace to requirements
- Every task must reference specific requirements
- Every implementation must satisfy traced requirements
- Every test must validate specific acceptance criteria
```

**Change Impact Assessment:**
```
CHANGE IMPACT ANALYSIS:
1. IDENTIFY changed elements and scope
2. MAP dependencies and relationships
3. ASSESS impact on related documents
4. PLAN systematic updates across ecosystem
5. VALIDATE consistency after changes

IMPACT ASSESSMENT MATRIX:
Document Type | Change Type | Impact Level | Update Required
Requirements  | Content     | High         | Design + Tasks
Design        | Architecture| High         | Requirements + Tasks
Design        | Component   | Medium       | Tasks only
Tasks         | Sequencing  | Low          | Implementation only
Implementation| Code        | Low          | Documentation only
```

## AI Agent Communication Patterns

### Requirements Phase
- **Prompt**: Generate requirements with user stories and EARS acceptance criteria
- **Approval**: Ask for user approval to proceed to design phase
- **Behavior**: Provide comprehensive summary of approach and rationale

### Design Phase
- **Prompt**: Create technical design addressing all requirements with clear decisions
- **Approval**: Ask for user approval to proceed to implementation planning
- **Behavior**: Explain design decisions, trade-offs, and how they address requirements

### Tasks Phase
- **Prompt**: Break design into hierarchical tasks with requirement references
- **Approval**: Ask for user approval, explaining the task prioritization approach
- **Behavior**: Explain task breakdown, dependencies, and implementation approach

### Implementation Phase
- **Prompt**: "Execute user-selected task, read all spec documents for context, provide comprehensive summary"
- **Approval**: Get task selection from user, complete one task at a time
- **Behavior**: Context-aware implementation with detailed summaries

## Effective Prompting Guidelines

1. **Be Phase-Specific**: Reference the current phase and expected outputs
2. **Request Comprehensive Summaries**: Ask for explanations of approach and rationale
3. **Specify Context Loading**: Mention reading all spec documents before implementation
4. **Use Exact Approval Questions**: Use the specific approval questions from each phase
5. **Reference Standards**: Mention EARS format, hierarchical tasks, and verification criteria

## Common Prompting Mistakes

❌ **Avoid**: "Create a design document"
✅ **Use**: "Create a design.md document addressing all requirements from requirements.md, with clear architecture and design decisions"

❌ **Avoid**: "Make a task list"  
✅ **Use**: "Generate tasks.md with hierarchical checkbox format, requirement references, and mark optional tasks with '*'"

❌ **Avoid**: "Implement the feature"
✅ **Use**: "Execute the selected task from tasks.md, read all spec documents for context, implement the functionality, and provide a comprehensive summary"

## Related Documents
- **System Overview**: [[principles.md]] - Complete system guide with principles and philosophy
- **Process Guide**: [[process.md]] - Workflow and communication guidance

## Available Templates

### Core Document Templates
- **`templates/requirements-template.md`** - EARS-formatted requirements document
- **`templates/design-template.md`** - Comprehensive technical design document  
- **`templates/tasks-template.md`** - Implementation task breakdown

### Specialized Templates
- **`templates/map-template.md`** - Project structure overview for complex features
- **`templates/architecture-readme-template.md`** - Detailed architecture specifications

## Template Usage Guidelines

### For AI Agents
1. **Reference templates** when creating documents (don't copy, use as structure guide)
2. **Follow the established patterns** while adapting content to the specific feature
3. **Maintain consistency** across all specifications in a project
4. **Use placeholder conventions** for customizable elements

### Template Structure Standards
All templates follow a consistent structure:
- **Clear title** with feature name
- **Introduction section** with context and purpose
- **Main content sections** with structured, scannable content
- **Cross-references** to related documents when applicable

### Placeholder Conventions
Templates use these placeholder conventions:
- `[Feature Name]` - Name of the feature being specified
- `[Title]` - Section or requirement title
- `[role]` - User role in user stories
- `[capability]` - What the user wants to do
- `[benefit]` - Why the user wants this capability
- `[event]` - Trigger condition in EARS format
- `[system]` - The system being specified
- `[response]` - Expected system behavior

## Quality Standards

### Document Quality Checklist
- [ ] **Clear structure** with logical section organization
- [ ] **Scannable format** with headers and bullet points
- [ ] **Actionable content** with specific guidance
- [ ] **EARS format** followed in requirements
- [ ] **Design addresses all requirements**
- [ ] **Tasks are hierarchical and actionable**
- [ ] **Requirements traced to design/tasks**
- [ ] **Cross-reference support** for document relationships

### Content Standards
- **Requirements**: EARS format, clear user stories, technical precision
- **Design**: Address all requirements, clear architecture and rationale, component specifications
- **Tasks**: Hierarchical structure with sub-tasks, discrete actionable steps, requirement references, incremental approach

## Supplementary Documents

### Map Document (Complex Projects)
**When to create**: For projects with >3 specification documents
**Template**: `templates/map-template.md`
**Purpose**: Project structure overview, status tracking, navigation guide

### Architecture Directory (Large Systems)
**When to create**: When design.md >10 pages or >5 major components
**Template**: `templates/architecture-readme-template.md`
**Purpose**: Detailed architectural specifications organized by system area

## Cross-References

### Document Relationships
```markdown
_Requirements: [Requirement references]_
_See design.md for technical details_
_Related: requirements.md → design.md → tasks.md_
```

### Cross-Reference Validation Patterns
- **WHEN adding new requirement** → check if design.md needs updates, add references
- **WHEN modifying design** → verify all requirements are still addressed, update task references
- **WHEN implementing tasks** → ensure requirement traceability is maintained
- **VALIDATE traceability** → every task should reference specific requirements
- **CHECK consistency** → requirement changes should cascade to design and tasks

### Navigation Patterns
- **Internal References**: `*See [[Section|#section]] for details*`
- **External References**: `*See [[Design Document]] for architecture*`
- **Requirement Traceability**: `_Requirements: 1.1, 1.2, 4.6_`

### Requirement Traceability Examples
```markdown
# In design.md
## Component Architecture
This addresses requirements 1.1 (user authentication) and 2.3 (data validation).

# In tasks.md  
- [ ] 1.1 Implement user login
  - Create authentication service
  - _Requirements: 1.1, 1.2_
```

## Key Patterns
- **Clean Structure**: No YAML frontmatter or JSON blocks
- **EARS Format**: Proper acceptance criteria structure  
- **Hierarchical Tasks**: Clear main tasks with sub-tasks
- **Optional Tasks**: Testing marked with "*"
- **Requirement Traceability**: Clear links between phases

*See actual template files in `.yask/templates/` for complete examples*

### Quality Assurance Patterns

#### Issue Anticipation
- **WHEN creating requirements** → check for missing edge cases, unclear acceptance criteria
- **WHEN designing architecture** → anticipate scalability issues, integration problems
- **WHEN implementing code** → verify against requirements, check for common bugs
- **BEFORE task completion** → run diagnostics, verify functionality, update documentation

#### Cross-Document Validation
- **BEFORE making changes** → identify all files that will be affected
- **DURING implementation** → maintain traceability between requirements, design, and code
- **AFTER completion** → verify all related documents reflect current state
- **WHEN updating requirements** → check if design and tasks need corresponding updates
- **WHEN modifying design** → ensure requirements are still addressed and tasks remain valid

#### Scope Change Management
- **WHEN scope changes occur** → pause implementation and assess impact systematically
- **ASSESS** what documents and code need updating based on the change
- **PRIORITIZE** core specifications before supplementary documents before implementation
- **VERIFY** traceability and consistency after updates

#### Limitation Evaluation
- **BEFORE claiming completion** → assess what data you can actually access for verification
- **WHEN limited access prevents validation** → document what was verified vs. what was assumed
- **DURING implementation** → actively seek error messages, console output, diagnostic results
- **AFTER changes** → incorporate system feedback into validation assessment

## Pseudocode Fallback Patterns

### When to Use Pseudocode Reconstruction
- **Complex indentation issues** that resist standard fixing approaches
- **Syntax errors** that are difficult to isolate and resolve
- **Code structure problems** where the logic is sound but implementation is broken
- **Legacy code analysis** where existing code needs to be understood and refactored

### Pseudocode Reconstruction Process

#### Step 1: Extract Logic Structure
```markdown
# Original problematic code analysis
1. Identify the core logic flow and decision points
2. Extract comments and function/method names as logic indicators
3. Map out the intended data flow and transformations
4. Note the expected inputs, outputs, and side effects
```

#### Step 2: Create Structured Pseudocode
```markdown
# Use standard pseudocode conventions
BEGIN function_name(parameters)
    IF condition THEN
        action_1
        action_2
    ELSE
        alternative_action
    END IF
    
    FOR each item IN collection
        process_item(item)
    END FOR
    
    RETURN result
END function_name
```

#### Step 3: Reconstruct Implementation
```markdown
# Implementation reconstruction approach
1. Use pseudocode as the authoritative logic reference
2. Implement each pseudocode block as clean, properly formatted code
3. Verify syntax and structure against language standards
4. Test logical flow against original requirements
5. Compare with original code to ensure functionality preservation
```

#### Step 4: Validation and Integration
```markdown
# Quality assurance for reconstructed code
1. Run syntax validation on reconstructed code
2. Compare logical flow with pseudocode reference
3. Verify against EARS acceptance criteria when applicable
4. Test integration with existing codebase
5. Document any changes from original implementation
```

### Pseudocode Standards Reference

#### Standard Pseudocode Conventions
- **BEGIN/END**: Function and block boundaries
- **IF/THEN/ELSE/END IF**: Conditional logic
- **FOR/WHILE/END FOR/END WHILE**: Iteration
- **CALL/RETURN**: Function calls and returns
- **SET/GET**: Variable assignment and retrieval
- **INPUT/OUTPUT**: Data input and output operations

#### Structured Logic Patterns
```markdown
# Decision Making
IF condition THEN
    action
ELSE IF alternative_condition THEN
    alternative_action
ELSE
    default_action
END IF

# Iteration
FOR each element IN collection
    process(element)
END FOR

WHILE condition IS true
    perform_action
    update_condition
END WHILE

# Function Definition
BEGIN function_name(parameter1, parameter2)
    local_variable = process(parameter1)
    result = calculate(local_variable, parameter2)
    RETURN result
END function_name
```

### Integration with Existing Workflows

#### When Standard Approaches Fail
1. **FIRST**: Attempt standard syntax fixing and code analysis
2. **IF issues persist**: Apply pseudocode reconstruction approach
3. **DOCUMENT**: Note that pseudocode fallback was used and why
4. **VERIFY**: Ensure reconstructed code meets all requirements

#### Pseudocode File Management
- **Create temporary pseudocode files** when needed for complex reconstruction
- **Reference pseudocode in implementation summaries** when used
- **Preserve pseudocode files** as documentation for complex logic
- **Cross-reference** between pseudocode and final implementation

#### Quality Assurance Integration
```markdown
# Enhanced validation when using pseudocode fallback
- VERIFY pseudocode accurately represents intended logic
- ENSURE reconstructed code implements pseudocode correctly
- TEST functionality against original requirements
- DOCUMENT reconstruction process and rationale
- VALIDATE integration with existing codebase
```

### Usage for AI Agents
These examples show the expected output format for each phase. Use them as reference when generating specifications to ensure consistency with current streamlined patterns.

**Pseudocode Fallback Usage**: When encountering complex code issues that resist standard approaches, apply the pseudocode reconstruction process as a systematic fallback method.

*For workflow and communication guidance, see `process.md`*