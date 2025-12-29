---
date: '2025-12-28'
description: AI prompting strategies template for YASK system
status: active
tags:
  - yask
  - yask/type/template
  - yask/status/active
title: AI Prompting Strategies Template
version: 6.0.0
---

# AI Prompting Strategies Template

## Purpose
This template provides structured prompting patterns for effective AI collaboration throughout the spec-driven development process.

## Context Setting Framework

### Project Context Establishment
```
LOAD and ANALYZE the following project context:
- Current specifications: [List relevant documents]
- Technical constraints: [Define limitations and requirements]
- Phase objectives: [Clarify current goals and deliverables]
- Quality standards: [Establish expected output quality]
- Success criteria: [Define what constitutes completion]

ESTABLISH baseline understanding:
- What problem are we solving?
- Who are the stakeholders?
- What are the success metrics?
- What are the constraints?
- What has been decided vs. what needs decision?
```

## Phase-Specific Prompting Patterns

### Requirements Phase Prompts

#### Initial Requirements Generation
```
CREATE comprehensive requirements document following EARS format:
1. ANALYZE user intent and underlying goals
2. GENERATE user stories with clear role, capability, benefit
3. FORMULATE acceptance criteria using WHEN/IF/WHERE syntax
4. IDENTIFY constraints, assumptions, and edge cases
5. VALIDATE completeness and testability
6. PROVIDE comprehensive summary of approach and rationale

USER INPUT: [Insert user feature request]
PROJECT CONTEXT: [Insert relevant background]
CONSTRAINTS: [Insert known limitations]
```

#### Requirements Validation
```
VALIDATE requirements document for completeness and quality:
1. CHECK EARS format compliance for all acceptance criteria
2. VERIFY user stories include clear role, capability, and benefit
3. ASSESS testability of acceptance criteria
4. IDENTIFY missing requirements or gaps
5. EVALUATE consistency and clarity
6. RECOMMEND improvements with specific examples

REQUIREMENTS DOCUMENT: [Insert requirements content]
VALIDATION CRITERIA: [Insert quality standards]
```

### Design Phase Prompts

#### Technical Design Creation
```
CREATE technical design addressing all requirements:
1. LOAD requirements.md for complete context
2. RESEARCH technical approaches and best practices
3. DEFINE system architecture and component interactions
4. SPECIFY data models, interfaces, and APIs
5. PLAN error handling and testing strategies
6. DOCUMENT design decisions with rationale
7. VALIDATE coverage of all requirements

REQUIREMENTS CONTEXT: [Insert requirements summary]
TECHNICAL CONSTRAINTS: [Insert limitations]
ARCHITECTURE PREFERENCES: [Insert architectural guidelines]
```

#### Design Review and Validation
```
REVIEW and VALIDATE technical design:
1. VERIFY all requirements are addressed
2. ASSESS architecture feasibility and scalability
3. EVALUATE design decisions and rationale
4. CHECK component interaction clarity
5. VALIDATE error handling completeness
6. RECOMMEND improvements with specific guidance

DESIGN DOCUMENT: [Insert design content]
REVIEW CRITERIA: [Insert evaluation standards]
CONSTRAINTS: [Insert technical limitations]
```

### Tasks Phase Prompts

#### Task Breakdown and Planning
```
BREAK design into actionable implementation tasks:
1. LOAD requirements.md and design.md for full context
2. DECOMPOSE design components into discrete coding tasks
3. SEQUENCE tasks for logical implementation flow
4. REFERENCE requirements for traceability
5. MARK optional tasks with '*' for testing and enhancements
6. VALIDATE task completeness and feasibility

DESIGN CONTEXT: [Insert design summary]
IMPLEMENTATION CONSTRAINTS: [Insert limitations]
PRIORITY REQUIREMENTS: [Insert critical requirements]
```

#### Task Validation and Optimization
```
VALIDATE and OPTIMIZE implementation tasks:
1. CHECK hierarchical structure and logical sequencing
2. VERIFY requirement traceability for each task
3. ASSESS task complexity and effort estimation
4. IDENTIFY dependencies and potential blockers
5. RECOMMEND optimization and risk mitigation

TASKS DOCUMENT: [Insert tasks content]
VALIDATION CRITERIA: [Insert quality standards]
RISK FACTORS: [Insert known risks]
```

### Implementation Phase Prompts

#### Task Execution
```
EXECUTE selected task with comprehensive approach:
1. LOAD all specification documents for complete context
2. ANALYZE task requirements and success criteria
3. ACQUIRE necessary resources and dependencies
4. IMPLEMENT functionality with quality validation
5. VERIFY against requirements and design specifications
6. UPDATE documentation to reflect implementation
7. PROVIDE detailed summary of accomplishments

TASK CONTEXT: [Insert task details]
SPECIFICATIONS: [Insert relevant spec sections]
SUCCESS CRITERIA: [Insert completion standards]
```

#### Implementation Review
```
REVIEW implementation for quality and compliance:
1. VERIFY functionality against task requirements
2. CHECK code quality and best practices adherence
3. VALIDATE integration with existing systems
4. ASSESS performance and efficiency
5. CONFIRM documentation accuracy
6. RECOMMEND improvements if needed

IMPLEMENTATION: [Insert code or implementation details]
QUALITY STANDARDS: [Insert evaluation criteria]
INTEGRATION CONTEXT: [Insert system context]
```

## Communication and Feedback Patterns

### Change Request Handling
```
WHEN scope changes are requested:
1. PAUSE current implementation
2. ASSESS impact on existing specifications
3. IDENTIFY documents requiring updates
4. PRIORITIZE core specifications before supplementary documents
5. UPDATE specifications systematically
6. VALIDATE consistency across all documents
7. CONFIRM changes with user before proceeding

CHANGE REQUEST: [Insert proposed change]
CURRENT STATE: [Insert current specifications]
IMPACT ASSESSMENT: [Insert evaluation results]
```

### Iterative Refinement
```
FOR continuous improvement:
1. COLLECT feedback on current deliverables
2. ANALYZE specific improvement areas
3. IMPLEMENT targeted enhancements
4. VALIDATE improvements against standards
5. SEEK confirmation before proceeding
6. DOCUMENT lessons learned for future reference

FEEDBACK: [Insert user feedback]
CURRENT DELIVERABLE: [Insert content being refined]
IMPROVEMENT AREAS: [Insert specific focus areas]
```

## Quality Assurance Integration

### Pre-Delivery Validation
```
ENSURE quality through systematic checks:
1. FORMAT compliance with established templates
2. CONTENT completeness against requirements
3. TRACEABILITY maintenance across documents
4. CONSISTENCY validation between related files
5. FUNCTIONALITY verification against specifications
6. ERROR handling and edge case consideration

DELIVERABLE: [Insert content to validate]
QUALITY CRITERIA: [Insert evaluation standards]
REQUIREMENTS: [Insert relevant requirements]
```

### Post-Implementation Verification
```
VALIDATE implementation quality:
1. SYNTAX and code quality analysis
2. FUNCTIONALITY testing against requirements
3. INTEGRATION verification with existing systems
4. PERFORMANCE validation against constraints
5. DOCUMENTATION accuracy and completeness
6. USER acceptance criteria satisfaction

IMPLEMENTATION: [Insert implementation details]
TEST CRITERIA: [Insert validation standards]
SYSTEM CONTEXT: [Insert integration information]
```

## Decision-Making Frameworks

### Technical Choice Evaluation
```
EVALUATE technical options systematically:
1. IDENTIFY all viable approaches
2. DEFINE evaluation criteria with weights
3. SCORE each option against criteria
4. CALCULATE weighted scores
5. SELECT optimal solution with rationale
6. DOCUMENT decision factors for future reference

OPTIONS: [Insert alternative approaches]
CRITERIA: [Insert evaluation factors]
CONSTRAINTS: [Insert limitations]
```

### Problem-Solving Patterns
```
APPLY structured problem-solving approach:
1. DEFINE problem clearly and completely
2. ANALYZE root causes and contributing factors
3. GENERATE multiple solution options
4. EVALUATE solutions against success criteria
5. SELECT and implement optimal solution
6. VALIDATE solution effectiveness
7. DOCUMENT lessons learned

PROBLEM STATEMENT: [Insert problem description]
SUCCESS CRITERIA: [Insert solution requirements]
CONSTRAINTS: [Insert limitations]
```

## Usage Guidelines

### Template Customization
- Adapt prompts to specific project context and requirements
- Include relevant background information and constraints
- Customize evaluation criteria based on project priorities
- Adjust quality standards to match project complexity

### Best Practices
- Always provide comprehensive context before making requests
- Use specific, actionable language in prompts
- Include validation criteria and success measures
- Document decisions and rationale for future reference
- Seek confirmation before proceeding to next phases

### Quality Assurance
- Validate outputs against established standards
- Check for completeness and consistency
- Verify traceability across all documents
- Confirm functionality meets specified requirements
- Document any deviations and their rationale

---

*This template provides structured patterns for effective AI collaboration while maintaining the flexibility to adapt to specific project needs and contexts.*