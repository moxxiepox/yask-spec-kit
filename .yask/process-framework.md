---
date: '2025-12-28'
description: YASK process framework for systematic workflow management with phase gates and quality checkpoints
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: YASK Process Framework
version: 6.0.0
---

# YASK Process Framework

## Overview

The YASK Process Framework provides systematic workflow management for requirement-to-implementation workflows with phase gates, quality checkpoints, and decision trees for requirement analysis and design validation.

## Phase Gates and Quality Checkpoints

### Phase Gate 1: Requirements → Design Transition
**Entry Criteria:**
- [ ] Complete requirements.md with EARS format compliance
- [ ] All user stories have clear role-capability-benefit structure
- [ ] Acceptance criteria are testable and verifiable
- [ ] Cross-reference functionality is implemented
- [ ] User approval obtained for design phase

**Quality Checkpoints:**
- EARS format validation (WHEN/THEN/SHALL patterns)
- User story completeness verification
- Acceptance criteria testability assessment
- Requirements traceability preparation

**Decision Tree: Requirements Validation**
```
START: Requirements Document Review
├── Is EARS format compliant?
│   ├── YES → Continue to user story validation
│   └── NO → Apply EARS correction framework → REVALIDATE
├── Are user stories complete?
│   ├── YES → Continue to acceptance criteria validation
│   └── NO → Enhance user stories with missing elements → REVALIDATE
├── Are acceptance criteria testable?
│   ├── YES → Continue to cross-reference validation
│   └── NO → Refine criteria for verifiability → REVALIDATE
├── Are cross-references functional?
│   ├── YES → PROCEED to Design Phase
│   └── NO → Implement cross-reference framework → REVALIDATE
```

### Phase Gate 2: Design → Tasks Transition
**Entry Criteria:**
- [ ] Complete design.md addressing all requirements
- [ ] System architecture is clearly defined
- [ ] Component specifications have clear interfaces
- [ ] Design decisions include rationale and trade-offs
- [ ] Error handling strategies are documented
- [ ] User approval obtained for tasks phase

**Quality Checkpoints:**
- Requirements coverage verification
- Architecture feasibility assessment
- Design decision rationale validation
- Component specification completeness

**Decision Tree: Design Validation**
```
START: Design Document Review
├── Are all requirements addressed?
│   ├── YES → Continue to architecture validation
│   └── NO → Complete requirement coverage → REVALIDATE
├── Is architecture feasible?
│   ├── YES → Continue to component validation
│   └── NO → Redesign architecture → REVALIDATE
├── Are components clearly specified?
│   ├── YES → Continue to decision validation
│   └── NO → Enhance component specifications → REVALIDATE
├── Are design decisions justified?
│   ├── YES → PROCEED to Tasks Phase
│   └── NO → Document decision rationale → REVALIDATE
```

### Phase Gate 3: Tasks → Implementation Transition
**Entry Criteria:**
- [ ] Complete tasks.md with hierarchical structure
- [ ] All tasks have requirement traceability
- [ ] Optional tasks are marked with "*"
- [ ] Implementation logic follows dependency order
- [ ] Clear completion criteria defined
- [ ] User task selection confirmed

**Quality Checkpoints:**
- Hierarchical structure compliance
- Requirement traceability verification
- Implementation feasibility assessment
- Optional task identification validation

**Decision Tree: Tasks Validation**
```
START: Tasks Document Review
├── Is hierarchical structure correct?
│   ├── YES → Continue to traceability validation
│   └── NO → Reorganize task hierarchy → REVALIDATE
├── Is requirement traceability complete?
│   ├── YES → Continue to logic validation
│   └── NO → Map tasks to requirements → REVALIDATE
├── Is implementation logic sound?
│   ├── YES → Continue to criteria validation
│   └── NO → Adjust task dependencies → REVALIDATE
├── Are completion criteria clear?
│   ├── YES → PROCEED to Implementation
│   └── NO → Define completion standards → REVALIDATE
```

### Phase Gate 4: Implementation → Completion Transition
**Entry Criteria:**
- [ ] Implementation meets all specifications
- [ ] Code quality and syntax validation passed
- [ ] Functionality tested against requirements
- [ ] Documentation updated to reflect implementation
- [ ] Quality gates satisfied
- [ ] Comprehensive summary provided

**Quality Checkpoints:**
- Specification compliance verification
- Code quality and syntax validation
- Functionality testing against requirements
- Documentation accuracy verification

**Decision Tree: Implementation Validation**
```
START: Implementation Review
├── Does implementation meet specifications?
│   ├── YES → Continue to code quality validation
│   └── NO → Correct implementation → REVALIDATE
├── Is code quality acceptable?
│   ├── YES → Continue to functionality testing
│   └── NO → Improve code quality → REVALIDATE
├── Does functionality pass tests?
│   ├── YES → Continue to documentation validation
│   └── NO → Fix functionality issues → REVALIDATE
├── Is documentation accurate?
│   ├── YES → COMPLETE Implementation
│   └── NO → Update documentation → REVALIDATE
```

## Context Loading Strategy

### Hierarchical Context Loading Protocol

**Tier 1: Core YASK System Files (ALWAYS LOAD FIRST)**
```
Priority Order:
1. yask-system/requirements.md - System requirements
2. yask-system/design.md - System design
3. yask-system/tasks.md - Implementation tasks
4. yask-system/agents.md - AI agent instructions
5. yask-system/.yask/process-framework.md - This framework
```

**Tier 2: YASK Framework Files (LOAD FOR ALL SPEC-DRIVEN INTERACTIONS)**
```
Priority Order:
1. yask-system/.yask/principles.md - Core principles
2. yask-system/.yask/patterns.md - Document patterns
3. yask-system/.yask/process.md - Workflow guidance
4. yask-system/.yask/templates/ - Document templates
5. yask-system/.yask/decision-support.md - Decision frameworks
```

**Tier 3: Project-Specific Files (LOAD BASED ON PROJECT CONTEXT)**
```
Priority Order:
1. requirements.md - Project requirements
2. design.md - Project design
3. tasks.md - Project tasks
4. map.md - Project overview
5. architecture/ - System design decisions
```

**Tier 4: Subagent Integration Files (LOAD FOR DELEGATION SCENARIOS)**
```
Priority Order:
1. .opencode/ - Subagent configuration
2. .opencode/subagents/ - Subagent capabilities
3. .opencode/workflows/ - Delegation patterns
4. .opencode/validation/ - Quality gates
```

### Dependency Awareness Framework

**Context Dependency Mapping:**
```
REQUIREMENTS PHASE:
├── User Input Analysis
├── Existing Project Context
├── YASK System Requirements
├── EARS Format Templates
└── Quality Standards

DESIGN PHASE:
├── Complete Requirements Context
├── YASK Design Framework
├── Architecture Patterns
├── Component Specifications
└── Error Handling Strategies

TASKS PHASE:
├── Requirements + Design Context
├── YASK Task Patterns
├── Implementation Strategies
├── Dependency Analysis
└── Quality Checkpoints

IMPLEMENTATION PHASE:
├── All Previous Context
├── YASK Implementation Guidance
├── Quality Validation Tools
├── Error Recovery Procedures
└── Completion Criteria
```

## Decision Trees for Requirement Analysis

### Requirement Analysis Decision Tree
```
START: Requirement Analysis
├── Is requirement clear and unambiguous?
│   ├── YES → Continue to completeness check
│   └── NO → Apply clarification framework → ANALYZE AGAIN
├── Is requirement complete?
│   ├── YES → Continue to testability check
│   └── NO → Apply completeness framework → ANALYZE AGAIN
├── Is requirement testable?
│   ├── YES → Continue to feasibility check
│   └── NO → Apply testability framework → ANALYZE AGAIN
├── Is requirement feasible?
│   ├── YES → Continue to priority check
│   └── NO → Apply feasibility framework → ANALYZE AGAIN
├── Is priority clearly defined?
│   ├── YES → APPROVE requirement
│   └── NO → Apply prioritization framework → ANALYZE AGAIN
```

### Design Validation Decision Tree
```
START: Design Validation
├── Does design address all requirements?
│   ├── YES → Continue to architecture check
│   └── NO → Complete requirement coverage → VALIDATE AGAIN
├── Is architecture scalable?
│   ├── YES → Continue to component check
│   └── NO → Improve architecture → VALIDATE AGAIN
├── Are components well-defined?
│   ├── YES → Continue to interface check
│   └── NO → Define components clearly → VALIDATE AGAIN
├── Are interfaces clear?
│   ├── YES → Continue to error handling check
│   └── NO → Clarify interfaces → VALIDATE AGAIN
├── Is error handling comprehensive?
│   ├── YES → APPROVE design
│   └── NO → Enhance error handling → VALIDATE AGAIN
```

## Quality Checkpoint Procedures

### Pre-Phase Quality Check
```
QUALITY GATE EXECUTION:
1. LOAD relevant context files
2. APPLY validation criteria
3. EXECUTE decision tree analysis
4. DOCUMENT validation results
5. SEEK user approval if required
6. PROCEED to next phase or CORRECT issues
```

### Post-Phase Quality Check
```
QUALITY VERIFICATION:
1. REVIEW phase deliverables
2. VALIDATE against entry criteria
3. CONFIRM user satisfaction
4. UPDATE traceability matrices
5. PREPARE for next phase
6. DOCUMENT phase completion
```

### Continuous Quality Monitoring
```
ONGOING VALIDATION:
- Monitor context loading completeness
- Track decision tree execution results
- Validate quality gate compliance
- Assess user satisfaction levels
- Identify improvement opportunities
- Update framework based on learnings
```

## Implementation Guidelines

### Phase Progression Rules
1. **No Phase Skipping**: Each phase must be completed before proceeding
2. **Quality Gate Compliance**: All quality checkpoints must pass
3. **User Approval Required**: User confirmation needed at each phase boundary
4. **Context Preservation**: Maintain context throughout workflow
5. **Traceability Maintenance**: Keep requirement-to-implementation mapping

### Error Handling in Phase Transitions
1. **Detection**: Identify quality gate failures promptly
2. **Classification**: Categorize errors by type and severity
3. **Recovery**: Apply appropriate correction frameworks
4. **Validation**: Re-validate after corrections
5. **Documentation**: Record errors and resolutions

### Performance Optimization
1. **Context Caching**: Cache loaded context for efficiency
2. **Parallel Validation**: Validate multiple criteria simultaneously
3. **Early Detection**: Identify issues as early as possible
4. **Incremental Validation**: Validate in stages rather than batches
5. **User Communication**: Keep users informed of progress and issues

## Integration with YASK System

### Requirements Addressed
- **Requirement 1.1**: Structured workflow guidance with phase progression
- **Requirement 1.2**: Context loading strategy with dependency awareness
- **Requirement 1.3**: Decision-making frameworks with evaluation criteria

### Design Components Implemented
- **Process Framework**: Complete workflow management system
- **Quality Gates**: Systematic validation checkpoints
- **Decision Trees**: Requirement analysis and design validation frameworks

### Tasks Completion
- **Task 1.2**: Process Framework implementation complete
- **Task 1.3**: Decision Support Systems integration complete
- **Task 1.4**: Error Recovery Systems integration complete

---

**Framework Version**: 1.0  
**Last Updated**: 2024-12-17  
**YASK System Integration**: Complete