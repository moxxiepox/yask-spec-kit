---
date: '2025-12-28'
description: Consolidated framework template for YASK system
status: active
tags:
  - yask
  - yask/type/template
  - yask/status/active
title: Framework Template - Consolidated
version: 6.0.0
---

# YASK Framework Template

{% extends "base-template.md" %}

{% block document_type %}Framework{% endblock %}
{% block validation_requirements %}Framework Integration, Pattern Consistency, Intelligence Systems{% endblock %}
{% block quality_gates %}Framework Quality Gate{% endblock %}

## Overview

This framework template provides comprehensive guidance for YASK system implementation, including documentation patterns, template selection intelligence, prompting strategies, and integration mechanisms. It serves as the central intelligence system for optimal YASK usage.

## Documentation Patterns

### Core Documentation Patterns

#### 1. EARS Format Requirements Pattern
```markdown
### Requirement [Number]: [Clear, Actionable Title]

**User Story:** As a [specific role/user type], I want [specific capability/feature], so that [specific benefit/value]

#### Acceptance Criteria

**EARS Format Validation Required:**
- [ ] WHEN [specific event/trigger] THEN [system/component] SHALL [specific response/behavior]
- [ ] IF [specific condition/precondition] THEN [system/component] SHALL [specific behavior/response]
- [ ] WHERE [specific context/location] THEN [system/component] SHALL [specific behavior/response]

**Additional Criteria:**
- [ ] [Additional testable criterion with clear pass/fail conditions]
- [ ] [Performance or quality requirement if applicable]

**Traceability:** _Design Components: [Component references with @[] format]_ | _Tasks: [Task references with @[] format]_
```

#### 2. Component Specification Pattern
```markdown
### [Component Name] - [Specification Format Type]

**Purpose:** [Clear statement of what this component does and why it exists]

**Responsibilities:**
- [Primary responsibility 1 with specific scope]
- [Primary responsibility 2 with boundaries]
- [Primary responsibility 3 with dependencies]

**Interface:**
- **Input:** [What data/parameters it receives and from where]
- **Output:** [What data/results it produces and where they go]
- **Dependencies:** [What other components/services it depends on]

**Cross-References:**
- **Requirements Addressed:** @[requirements.md]#[Requirement references]
- **Tasks Implementation:** @[tasks.md]#[Task references]
- **Related Components:** @[design.md]#[Component references]
```

#### 3. Hierarchical Task Pattern
```markdown
### Phase [Number]: [Phase Name]
- [ ] [Task Number]. [Task Title]
  - [ ] [Subtask Number]. [Subtask Description]
    - [ ] [Detailed step with specific actions]
  - [ ] [Subtask Number]. [Subtask Description]
  - **Requirements:** @[requirements.md]#[Requirement references]
  - **Design Components:** @[design.md]#[Component references]
  - **Cross-References:** @[design.md]#[Section references]

- [ ]* [Optional Task Number]. [Optional Task Title]
  - [Optional tasks marked with asterisk for deferred implementation]
```

## Template Selection Intelligence

### Project Complexity Assessment

| Complexity Level | Characteristics | Recommended Templates | Additional Guidance |
|------------------|-----------------|----------------------|-------------------|
| **Simple** | Single feature, minimal dependencies, straightforward requirements | requirements-template-consolidated.md, design-template-consolidated.md (basic sections), tasks-template-consolidated.md | Use minimal template sections, focus on core functionality |
| **Medium** | Multiple components, some dependencies, moderate complexity | All core templates + component-template-consolidated.md | Include detailed component specifications and interface definitions |
| **Complex** | Multiple systems, significant dependencies, enterprise-level | All templates + architecture-readme-template.md | Comprehensive architecture documentation and integration patterns |
| **Enterprise** | Large-scale systems, multiple teams, regulatory requirements | All templates + cross-reference-template-consolidated.md | Full traceability, compliance documentation, and quality gates |

### Intelligent Template Selection Process

#### Step 1: Project Assessment
```
Project Assessment Checklist:
□ Number of requirements (Simple: 1-5, Medium: 6-15, Complex: 16+)
□ Number of components (Simple: 1-3, Medium: 4-10, Complex: 11+)
□ Integration complexity (Low/Medium/High)
□ Stakeholder count (Simple: 1-3, Medium: 4-8, Complex: 9+)
□ Regulatory requirements (Yes/No)
□ Performance requirements (Standard/High/Enterprise)
```

#### Step 2: Template Selection
Based on assessment results:
- **Simple:** requirements-template-consolidated.md + design-template-consolidated.md + tasks-template-consolidated.md
- **Medium:** All above + component-template-consolidated.md
- **Complex:** All above + architecture-readme-template.md
- **Enterprise:** All templates + cross-reference-template-consolidated.md

#### Step 3: Template Customization
Apply complexity-based adaptations:
- Remove unnecessary sections for simple projects
- Add detailed sections for complex projects
- Include quality gates for enterprise projects
- Adapt cross-reference patterns based on project size

## AI Prompting Strategies

### Context Setting Framework
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

### Phase-Specific Prompting Patterns

#### Requirements Phase Prompts
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

#### Design Phase Prompts
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

#### Tasks Phase Prompts
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

## Quality Gate Integration

### Template-Specific Quality Gates

#### Requirements Quality Gate
- [ ] EARS format compliance validated
- [ ] User stories follow role-capability-benefit structure
- [ ] Acceptance criteria are testable and complete
- [ ] Traceability matrix is complete

#### Design Quality Gate
- [ ] All requirements mapped to design components
- [ ] Component interfaces are clearly defined
- [ ] Data models support all requirements
- [ ] Error handling covers identified scenarios

#### Tasks Quality Gate
- [ ] All design components have implementation tasks
- [ ] Task hierarchy supports implementation flow
- [ ] Cross-references are functional
- [ ] Quality gates are integrated

#### Component Quality Gate
- [ ] Interface contracts are complete
- [ ] Integration points are defined
- [ ] Quality attributes are specified
- [ ] Testing strategy is defined

### Automated Validation Integration
```
Template Selection Validation:
✓ Complexity assessment completed
✓ Appropriate templates selected
✓ Quality gates configured
✓ Cross-reference framework integrated
✓ QA system validation enabled
```

## Integration Patterns

### QA System Integration Pattern
```
## QA Integration Points

**EARS Format Validation:**
- Automated checking during requirements creation
- Real-time correction guidance for malformed acceptance criteria
- Quality scoring with improvement suggestions

**Cross-Reference Validation:**
- Automated reference checking during document updates
- Broken link detection and repair guidance
- Traceability completeness verification

**Consistency Validation:**
- Cross-document synchronization checking
- Impact assessment for document changes
- Automated update recommendations
```

### Template Evolution Guidelines

#### When to Add Templates
- Project complexity increases
- New stakeholder requirements emerge
- Regulatory compliance needed
- Integration complexity grows

#### When to Simplify Templates
- Project scope reduces
- Unused sections identified
- Stakeholder feedback indicates overhead
- Quality gates show diminishing returns

#### Maintenance Procedures
1. **Regular Assessment:** Review template effectiveness quarterly
2. **Stakeholder Feedback:** Collect usage feedback from project teams
3. **Quality Metrics:** Analyze quality gate results for template optimization
4. **Template Updates:** Update templates based on lessons learned

## Performance Optimization

### Template Processing Optimization
- **Template Caching:** Cache frequently used templates
- **Lazy Loading:** Load template sections only when needed
- **Batch Processing:** Process multiple templates simultaneously
- **Smart Preloading:** Preload commonly used template components

### Cross-Reference Resolution Optimization
- **Pattern Caching:** Cache frequently used reference patterns
- **Context-Aware Resolution:** Use smart context inference
- **Parallel Processing:** Resolve multiple references simultaneously
- **Incremental Updates:** Only update changed references

## Error Handling Patterns

### Missing Context Recovery Pattern
```
## Missing Context Recovery

**Scenario:** AI agent lacks required context files or documents

**Recovery Strategy:**
1. Identify missing documents using cross-reference validation
2. Provide clear guidance on required context with specific file loading instructions
3. Offer to create missing documents using appropriate templates
4. Guide user through context setup with step-by-step procedures

**Fallback Approach:**
- Create minimal viable documents using core templates
- Provide placeholder content with clear TODO markers
- Establish basic traceability framework
- Schedule follow-up validation after context completion
```

### Quality Validation Error Recovery Pattern
```
## Quality Validation Error Recovery

**Scenario:** EARS format violations, cross-document inconsistencies, or traceability gaps

**Recovery Strategy:**
1. Identify specific validation errors using QA system
2. Provide correction guidance with format examples
3. Update documents with corrected content
4. Re-run validation to confirm fixes

**Fallback Approach:**
- Automated consistency checking with systematic correction procedures
- Template-based content generation for missing sections
- Cross-reference repair with validation confirmation
```

## Usage Examples

### Simple Feature Documentation Pattern
```
Selected Templates:
- requirements-template-consolidated.md (basic sections only)
- design-template-consolidated.md (overview + basic components)
- tasks-template-consolidated.md (minimal phases)

Quality Gates:
- Basic EARS validation
- Simple cross-reference checking
```

### Medium Complexity System
```
Selected Templates:
- requirements-template-consolidated.md (full template)
- design-template-consolidated.md (detailed components)
- tasks-template-consolidated.md (phased approach)
- component-template-consolidated.md (key components)

Quality Gates:
- Full EARS validation
- Component interface validation
- Cross-reference integrity checking
```

### Enterprise System
```
Selected Templates:
- All templates
- cross-reference-template-consolidated.md
- Full architecture documentation

Quality Gates:
- Comprehensive validation suite
- Automated consistency checking
- Full traceability verification
- Compliance validation
```

## Traceability Matrix

| Framework Element | Requirements | Design Components | Tasks | Status |
|-------------------|-------------|------------------|-------|---------|
| Documentation Patterns | @[requirements.md]#[Pattern references] | @[design.md]#[Pattern references] | @[tasks.md]#[Pattern references] | [ ] |
| Template Selection | @[requirements.md]#[Complexity assessment] | @[design.md]#[Template mapping] | @[tasks.md]#[Selection validation] | [ ] |
| Quality Gates | @[requirements.md]#[Quality requirements] | @[design.md]#[Quality components] | @[tasks.md]#[Quality tasks] | [ ] |
| Integration Patterns | @[requirements.md]#[Integration needs] | @[design.md]#[Integration design] | @[tasks.md]#[Integration tasks] | [ ] |

## Quality Validation

### Framework Quality Gate
- [ ] All documentation patterns are consistent and complete
- [ ] Template selection intelligence provides accurate guidance
- [ ] Quality gates are integrated across all templates
- [ ] Integration patterns support all project types
- [ ] Error handling patterns are comprehensive
- [ ] Performance optimization is implemented
- [ ] Quality score meets threshold (≥90%)

### Validation Results
- **Documentation Patterns:** ✓ Complete
- **Template Intelligence:** ✓ Accurate
- **Quality Gates:** ✓ Integrated
- **Integration Patterns:** ✓ Comprehensive
- **Error Handling:** ✓ Robust
- **Performance:** ✓ Optimized
- **Overall Quality:** ✓ Pass (Score: [X]%)

## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| 2024-12-17 | Consolidated framework template implementation | All YASK templates affected - unified framework intelligence |
| 2024-12-17 | Integrated template selection intelligence | Enhanced user experience and template optimization |
| 2024-12-17 | Added comprehensive prompting strategies | Improved AI collaboration and effectiveness |
| 2024-12-17 | Implemented performance optimization | Enhanced system efficiency and responsiveness |