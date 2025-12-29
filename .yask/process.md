---
date: '2025-12-28'
description: Complete workflow, communication, and strategic thinking guide for AI agents
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: Process & Strategy Guide
version: 6.0.0
---

# Process & Strategy Guide

Complete workflow, communication, and strategic thinking guide for AI agents.

## Strategic Approach

### Context Assessment Framework

**Situational Analysis**: What exists? What's requested? What's missing? What's the goal?
**User Intent Analysis**: Analyze underlying intent, identify improvements, consider scope adjustments, spot issues
**Phase Identification**: Requirements, Design, Tasks, or Implementation phase
**Context Loading**: Load existing specs, templates, and project context as needed
**Execution Planning**: Content strategy, communication approach, quality checkpoints, error handling

### Decision Logic
```
User Request → Assess Context → Identify Phase → Load Documents → Execute → Summarize → Seek Approval
```

### Decision Logic

#### Phase Identification Decision Tree
```
User Request → 
├─ "Create requirements" → Requirements Phase
├─ "Design this feature" → Design Phase (check for requirements.md)
├─ "Break down tasks" → Tasks Phase (check for requirements.md + design.md)
├─ "Implement task X" → Implementation Phase (check for all documents)
└─ Unclear → Ask for clarification
```

#### Context Loading Strategy
- **Requirements**: Load user input + existing project context + requirements template
- **Design**: Load requirements.md + design template
- **Tasks**: Load requirements.md + design.md + tasks template  
- **Implementation**: Load requirements.md + design.md + tasks.md + current project files

### Scope Change Management

**WHEN scope changes occur**: Pause implementation and assess impact systematically

**THINKING PATTERN**: 
- **ASSESS** what documents and code need updating based on the change
- **PRIORITIZE** core specifications before supplementary documents before implementation
- **VERIFY** traceability and consistency after updates
- **CONFIRM** with user before resuming implementation

**HIERARCHY PRINCIPLE**: Core documents → Referenced documents → Architecture → Code → Tasks

### Error Recovery Strategy

#### Missing Context Recovery
- **No requirements.md**: "I need the requirements document to proceed. Should I create it first?"
- **No design.md**: "I need the design document to create tasks. Should I create the design first?"
- **Incomplete documents**: "The [document] seems incomplete. Should I complete it before proceeding?"

#### Quality Issues Recovery
- **Poor EARS format**: Stop, explain EARS format, provide corrected examples
- **Missing traceability**: Stop, explain requirement references, add missing links
- **Unclear architecture**: Stop, ask specific clarifying questions about components

#### Implementation Issues Recovery
- **Code errors**: Stop, explain the error, suggest specific solutions
- **Complex code issues**: Apply pseudocode reconstruction approach when standard fixes fail
- **File editing failures**: Try alternative methods (different tools, manual steps, user assistance) - NEVER claim completion without actually completing
- **Missing dependencies**: Stop, identify missing components, suggest implementation order
- **Test failures**: Stop, analyze failure, suggest fixes or approach changes
- **Technical difficulties**: Persist with alternative approaches rather than abandoning tasks

#### Approval Issues Recovery
- **Unclear response**: Rephrase approval request with more context
- **Partial approval**: Ask specific questions about concerns
- **Rejection**: Ask for specific feedback and suggest revisions

## Workflow Overview
```
Requirements → Design → Tasks → Implementation
     ↓           ↓        ↓         ↓
  User Approval → User Approval → User Approval → Task Execution
```

## Enhanced Cross-Documentation Workflow

### Document Ecosystem Management
**Document Hierarchy & Dependencies:**
```
Core Documents:
├── requirements.md (Source of truth for user needs)
├── design.md (Technical implementation plan)
├── tasks.md (Actionable implementation steps)
└── map.md (Project overview for complex projects)

Supporting Documents:
├── architecture/ (System-wide design decisions)
├── templates/ (Reusable document structures)
└── tests/ (Validation and verification)
```

### Cross-Document Change Impact Assessment

#### When Requirements Change
**Assessment Protocol:**
1. **Load Current State**: Read existing design.md and tasks.md
2. **Impact Analysis**: Identify which design components address changed requirements
3. **Design Updates**: Update design.md to reflect new/changed requirements
4. **Task Cascade**: Assess which tasks need modification based on design changes
5. **Traceability Check**: Verify all requirements have corresponding design components and tasks
6. **Consistency Validation**: Ensure design and tasks align with updated requirements

**Update Sequence:**
```
Requirements Change → Design Impact Assessment → Design Updates → Task Impact Assessment → Task Updates → Validation
```

#### When Design Changes
**Assessment Protocol:**
1. **Load Current State**: Read requirements.md and tasks.md
2. **Requirements Alignment**: Verify design changes don't conflict with requirements
3. **Task Cascade**: Identify which tasks need updates based on design changes
4. **Implementation Impact**: Assess how design changes affect implementation approach
5. **Traceability Maintenance**: Ensure all design components trace back to requirements
6. **Consistency Check**: Validate that tasks reflect the updated design

**Update Sequence:**
```
Design Change → Requirements Validation → Task Impact Assessment → Task Updates → Implementation Planning → Validation
```

#### When Implementing Tasks
**Assessment Protocol:**
1. **Load Full Context**: Read requirements.md, design.md, and tasks.md
2. **Specification Alignment**: Verify implementation matches specifications
3. **Documentation Updates**: Update requirements/design if implementation differs
4. **Cross-Reference Validation**: Ensure all document references remain valid
5. **Traceability Verification**: Confirm implementation traces back to requirements
6. **Quality Gates**: Validate against EARS criteria and design decisions

**Update Sequence:**
```
Implementation → Specification Validation → Document Updates → Cross-Reference Check → Traceability Verification → Quality Gates
```

### Automated Consistency Checking

#### Pre-Change Validation
**Before any document modification:**
- [ ] Load all related documents for context
- [ ] Identify document dependencies and cross-references
- [ ] Check for existing inconsistencies
- [ ] Assess scope of proposed changes

#### Post-Change Validation
**After any document modification:**
- [ ] Verify requirement-to-design traceability
- [ ] Check design-to-task alignment
- [ ] Validate cross-references and links
- [ ] Ensure EARS criteria remain testable
- [ ] Confirm implementation feasibility

#### Consistency Rules
1. **Every requirement must have corresponding design components**
2. **Every design component must trace to at least one requirement**
3. **Every task must reference specific requirements and design elements**
4. **Implementation must satisfy all EARS acceptance criteria**
5. **Cross-references must remain valid after changes**

### Scope Change Management Enhanced

**WHEN scope changes occur**: Apply systematic impact assessment across all documents

**Enhanced Thinking Pattern:**
- **ASSESS** impact on requirements, design, tasks, and implementation
- **PRIORITIZE** core specifications before supplementary documents before implementation
- **CASCADE** changes through document hierarchy systematically
- **VERIFY** traceability and consistency after updates
- **VALIDATE** with automated consistency checks
- **CONFIRM** with user before resuming implementation

**Enhanced Hierarchy Principle**: 
Core documents → Referenced documents → Architecture → Code → Tasks → Tests

### Formal Change Management Procedures

#### Change Impact Assessment Framework
```
CHANGE REQUEST ANALYSIS:
1. IDENTIFY change scope and nature
2. ASSESS impact on existing specifications
3. EVALUATE risk vs. benefit
4. DETERMINE required document updates
5. ESTIMATE implementation effort
6. RECOMMEND approval or rejection with rationale
```

#### Change Classification System
- **Type A - Minor**: Single document updates, no cross-references affected
- **Type B - Moderate**: Multiple related documents, some cross-references need updates
- **Type C - Major**: Core specification changes affecting multiple documents and architecture
- **Type D - Critical**: Fundamental changes requiring complete re-evaluation

#### Change Management Workflow
```
CHANGE REQUEST → IMPACT ASSESSMENT → APPROVAL GATE → IMPLEMENTATION → VALIDATION

Step 1: Change Request Analysis
- Document the proposed change
- Identify affected specifications
- Assess complexity and risk level

Step 2: Impact Assessment
- Map change to document dependencies
- Identify required updates across ecosystem
- Estimate effort and timeline implications

Step 3: Approval Gate
- Present impact assessment to stakeholders
- Obtain explicit approval for major changes
- Confirm understanding of implications

Step 4: Systematic Implementation
- Update documents in dependency order
- Maintain traceability throughout process
- Validate consistency after each update

Step 5: Quality Validation
- Run automated consistency checks
- Verify requirement-to-implementation alignment
- Confirm change objectives are met
```

### Enhanced Quality Assurance Integration

#### Quality Gates Framework
```
QUALITY GATE 1: Requirements Validation
- EARS format compliance check
- User story completeness verification
- Acceptance criteria testability assessment
- Constraint and assumption documentation

QUALITY GATE 2: Design Validation
- Requirements coverage verification
- Architecture feasibility assessment
- Design decision rationale validation
- Error handling completeness check

QUALITY GATE 3: Tasks Validation
- Hierarchical structure compliance
- Requirement traceability verification
- Implementation feasibility assessment
- Optional task identification

QUALITY GATE 4: Implementation Validation
- Specification compliance verification
- Code quality and syntax validation
- Functionality testing against requirements
- Documentation accuracy check
```

#### Systematic Testing Strategies

**Requirements Testing:**
- **EARS Format Validation**: Ensure all acceptance criteria follow proper syntax
- **Completeness Check**: Verify all user needs are addressed
- **Testability Assessment**: Confirm criteria can be objectively verified
- **Traceability Verification**: Ensure requirements link to design and tasks

**Design Testing:**
- **Architecture Validation**: Verify design addresses all requirements
- **Feasibility Assessment**: Confirm technical approach is implementable
- **Integration Testing**: Check component interaction compatibility
- **Performance Validation**: Ensure design meets performance constraints

**Tasks Testing:**
- **Sequencing Validation**: Verify logical task order and dependencies
- **Completeness Check**: Ensure all design elements have corresponding tasks
- **Effort Estimation**: Validate task complexity and time estimates
- **Risk Assessment**: Identify potential implementation blockers

**Implementation Testing:**
- **Specification Compliance**: Verify code matches design specifications
- **Quality Validation**: Check code quality, syntax, and best practices
- **Integration Testing**: Confirm compatibility with existing systems
- **User Acceptance**: Validate against original user requirements

#### Error Handling and Recovery Strategies

**Proactive Error Prevention:**
- **Design Reviews**: Catch architectural issues before implementation
- **Code Reviews**: Identify quality issues before deployment
- **Testing Integration**: Build validation into development process
- **Documentation Reviews**: Ensure accuracy and completeness

**Systematic Error Recovery:**
```
ERROR DETECTION → IMPACT ASSESSMENT → RECOVERY STRATEGY → IMPLEMENTATION → VALIDATION

Detection Phase:
- Automated consistency checking
- Manual review and validation
- User feedback and testing
- Performance monitoring

Impact Assessment:
- Determine error scope and severity
- Identify affected components
- Assess risk to project objectives
- Evaluate recovery urgency

Recovery Strategy:
- Select appropriate recovery approach
- Plan systematic implementation
- Prepare rollback procedures
- Communicate with stakeholders

Implementation:
- Execute recovery plan systematically
- Maintain change documentation
- Validate fixes before deployment
- Monitor for secondary issues

Validation:
- Verify error resolution
- Confirm no new issues introduced
- Validate system stability
- Update documentation and procedures
```

### Document Update Procedures

#### Requirements Update Procedure
1. Identify changed requirements and their impact scope
2. Update design.md components that address changed requirements
3. Cascade changes to tasks.md based on design updates
4. Validate that all changes maintain traceability
5. Check that implementation feasibility is preserved

#### Design Update Procedure
1. Verify design changes align with requirements
2. Update tasks.md to reflect design changes
3. Assess implementation approach modifications
4. Validate design decisions against requirements
5. Ensure all design components have task implementations

#### Task Update Procedure
1. Verify task changes align with design and requirements
2. Update implementation approach if needed
3. Validate task feasibility and dependencies
4. Check that all requirements have implementation coverage
5. Ensure optional tasks remain properly marked

#### Implementation Update Procedure
1. Document any deviations from specifications
2. Update requirements/design if implementation differs
3. Validate that changes don't break traceability
4. Check that EARS criteria remain satisfied
5. Update cross-references and links as needed

## Phase Execution

### Requirements Phase
**Objective**: Create complete `requirements.md` with user stories and EARS acceptance criteria
**Strategy**: Context loading → user intent analysis → strategic planning → content generation → quality validation → summary & approval
**Conceptual Prototyping**: Proactively expand on user ideas, explore possibilities, engage in creative conversation about end ideals

### Design Phase  
**Objective**: Create complete `design.md` addressing all requirements with technical architecture
**Strategy**: Load requirements.md → analyze and plan architecture → create components and design decisions → validate and seek approval

### Tasks Phase
**Objective**: Create complete `tasks.md` with hierarchical implementation tasks  
**Strategy**: Load requirements.md and design.md → plan implementation approach → create hierarchical tasks with traceability → validate and seek approval

### Implementation Phase
**Objective**: Execute tasks systematically with comprehensive summaries
**Strategy**: Load all specs → implement selected task → assess resources → verify → update documents → summarize → mark complete

## Self-Sufficiency & Resource Management

### Enhanced Capability Assessment Framework
**BEFORE starting any task:**
1. **Analyze task requirements**: What tools, libraries, information, or capabilities are needed?
2. **Assess current capabilities**: What can you accomplish directly with available access and tools?
3. **Evaluate data access**: What data can you actually obtain to verify outcomes?
4. **Identify verification limitations**: What aspects cannot be validated with available information?
5. **Identify gaps**: What's missing that prevents task completion or verification?
6. **Plan acquisition strategy**: How can missing resources be obtained?
7. **Consider alternatives**: If direct acquisition isn't possible, what workarounds exist?
8. **Communicate honestly**: Be transparent about capabilities, limitations, and verification boundaries

### Resource Acquisition Strategy

#### Tools & Dependencies
- **PREFER local installations**: Choose workspace-local over global installations when possible for project isolation
- **WHEN task requires tools**: Identify requirements and assess local vs global installation needs
- **IF local installation possible**: Use project-specific installation methods (npm install, pip install, etc.)
- **IF global installation needed**: Ask for user confirmation and explain why global is necessary
- **WHEN installation fails**: Provide alternative methods including manual setup instructions
- **VERIFY installation success**: Test that tools work correctly in the project context

#### Information & Context
- **WHEN missing project context**: Read existing requirements.md, design.md, package.json, README files
- **WHEN unclear about architecture**: Analyze existing code structure and patterns
- **WHEN missing configuration details**: Check config files, environment variables, documentation
- **IF information still missing**: Ask specific, targeted questions rather than generic requests

#### Capabilities & Skills
- **WHEN facing new technology**: Research available documentation and examples
- **WHEN uncertain about approach**: Analyze similar implementations or patterns
- **WHEN lacking specific knowledge**: Acknowledge limitations and suggest learning resources
- **IF task exceeds capabilities**: Propose alternative approaches or request user assistance

### Self-Sufficiency Principles
- **Maximize independence**: Do everything you can within your capabilities before asking for help
- **Be proactive**: Anticipate needs and prepare resources before they become blockers
- **Communicate transparently**: Clearly explain what you can and cannot do
- **Suggest alternatives**: When direct approaches aren't possible, propose workarounds
- **Learn and adapt**: Use each task as an opportunity to expand understanding
- **Confirm when needed**: Ask for user confirmation before making significant changes or installations
- **Enhanced limitation evaluation**: Systematically assess what data you can access and what verification is actually possible
- **Verification boundary awareness**: Clearly distinguish between what you can verify vs. what you must assume
- **Debug data integration**: Actively seek and incorporate diagnostic output, error messages, and system feedback to evaluate actual state
- **Assumption documentation**: When making assumptions due to limited access, explicitly document what cannot be verified
- **No false completion**: NEVER claim tasks are complete without actually completing them - try alternative methods when primary approaches fail

## Communication Strategy

### Core Principles
1. **Be Proactive**: Strategize and implement comprehensively within each phase
2. **Always Load Context**: Read all relevant documents before proceeding
3. **Provide Comprehensive Summaries**: Explain approach, decisions, and rationale
4. **Seek Approval at Phase Boundaries**: Only ask for confirmation when phase is complete
5. **Reference Patterns**: Direct to `patterns.md` for document structures
6. **Flexible Iteration**: When scope changes, update related documents accordingly

### Quality Validation Checkpoints

#### Requirements Phase Validation
- [ ] **EARS Format**: All acceptance criteria use `WHEN [event] THEN [system] SHALL [response]`
- [ ] **User Stories**: Each requirement has clear role, capability, and benefit
- [ ] **Completeness**: All user needs addressed
- [ ] **Testability**: Acceptance criteria are verifiable

#### Design Phase Validation
- [ ] **Requirements Coverage**: Every requirement addressed in design
- [ ] **Architecture Clarity**: System components and interactions clear
- [ ] **Design Decisions**: Options considered, rationale provided, impact explained
- [ ] **Error Handling**: Failure scenarios and recovery strategies defined

#### Tasks Phase Validation
- [ ] **Hierarchical Structure**: Main tasks with logical sub-tasks
- [ ] **Requirement Traceability**: Each task references specific requirements
- [ ] **Optional Tasks**: Testing and non-essential tasks marked with "*"
- [ ] **Incremental Approach**: Tasks build on each other logically

#### Implementation Phase Validation
- [ ] **Context Loaded**: All spec documents read before starting
- [ ] **Single Task Focus**: Only selected task implemented
- [ ] **Resource Acquisition**: Required tools acquired with user confirmation (prefer local)
- [ ] **Code Quality**: Implementation meets verification criteria with diagnostic validation
- [ ] **Comprehensive Summary**: Detailed explanation of what was accomplished
- [ ] **No False Completion**: All required actions actually completed

### Critical Rules

**Context Loading**: Read all existing spec documents, load appropriate templates, understand full project context
**Approval**: Be proactive within phases, seek approval only at phase completion, provide comprehensive summaries, wait for clear confirmation
**Content Quality**: Use EARS format, provide comprehensive summaries, reference specific requirements for traceability
**Implementation**: Work on user-selected task only, mark optional tasks with "*", stop after each task, assess and acquire resources with confirmation, update related documents
**Enhanced Cross-Document Consistency**: 
- **Proactive Detection**: Automatically scan for document inconsistencies before making changes
- **Bidirectional Impact Assessment**: When any document changes, assess impact on ALL related documents
- **Traceability Maintenance**: Maintain requirement-to-implementation traceability throughout lifecycle
- **Scope Change Protocol**: When scope changes, systematically update all affected documents
- **Consistency Validation**: Verify document consistency after each change using automated checks
**Communication**: Explain design decisions and rationale, provide task breakdown explanations, give comprehensive summaries

### Effective Prompting Examples

**Requirements**: "Generate requirements with user stories and EARS acceptance criteria, then provide a comprehensive summary of your approach"

**Design**: "Create technical design addressing all requirements from requirements.md, with clear architecture and design decisions"

**Tasks**: "Generate tasks.md with hierarchical checkbox format, requirement references, and mark optional tasks with '*'"

**Implementation**: "Execute the selected task from tasks.md, read all spec documents for context, implement the functionality, and provide a comprehensive summary"

*For complete document creation guidance, see `patterns.md`*