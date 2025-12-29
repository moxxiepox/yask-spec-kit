---
date: '2025-12-28'
description: Comprehensive documentation patterns for YASK system implementation
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: YASK Documentation Patterns
version: 6.0.0
---

# YASK Documentation Patterns

## Overview

This guide provides comprehensive documentation patterns for YASK system implementation, ensuring consistency, quality, and traceability across all project documentation. These patterns integrate with the QA validation system and cross-reference framework to maintain document integrity throughout the development lifecycle.

## Core Documentation Patterns

### 1. EARS Format Requirements Pattern

**Pattern Structure:**
```
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

**Traceability:** _Design Components: [Component references with #[[]] format]_ | _Tasks: [Task references with #[[]] format]_
```

**Usage Guidelines:**
- Always include all three EARS patterns (WHEN, IF, WHERE) for comprehensive coverage
- Use specific, testable language in acceptance criteria
- Include traceability references to design components and tasks
- Validate EARS format compliance using QA system integration

### 2. Component Specification Pattern

**Pattern Structure:**
```
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
- **Requirements Addressed:** #[[requirements.md]]#[Requirement references]
- **Tasks Implementation:** #[[tasks.md]]#[Task references]
- **Related Components:** #[[design.md]]#[Component references]
```

**Format Variations:**
- **Detailed Format:** For complex components with multiple responsibilities
- **Interface-Focused Format:** For components with clear API contracts
- **Architecture Integration Format:** For system-level components
- **Minimal Format:** For simple, focused components

### 3. Hierarchical Task Pattern

**Pattern Structure:**
```
### Phase [Number]: [Phase Name]
- [ ] [Task Number]. [Task Title]
  - [ ] [Subtask Number]. [Subtask Description]
    - [ ] [Detailed step with specific actions]
  - [ ] [Subtask Number]. [Subtask Description]
  - **Requirements:** #[[requirements.md]]#[Requirement references]
  - **Design Components:** #[[design.md]]#[Component references]
  - **Cross-References:** #[[design.md]]#[Section references]

- [ ]* [Optional Task Number]. [Optional Task Title]
  - [Optional tasks marked with asterisk for deferred implementation]
```

**Implementation Flow Guidance:**
- Complete all Phase 1 tasks before starting Phase 2
- Complete Phase 2 data models before Phase 3 storage
- Complete Phase 3 storage before Phase 4 integration
- Optional tasks (marked with *) can be done in parallel or deferred

### 4. Cross-Reference Pattern

**Standard Reference Format:**
```
#[[document-name.md]]#[section-reference]
```

**Reference Types:**
- **Document References:** #[[requirements.md]]
- **Section References:** @[design.md]#[Components and Interfaces]
- **Specific Element References:** @[requirements.md]#[Requirement 1]: [Title]
- **Architecture References:** @[architecture-readme-template.md]#[Core Systems]

**Validation Requirements:**
- All referenced documents must exist
- All section references must match actual document headings
- All cross-references must be functional
- Traceability matrices must be complete

## Quality Gate Integration Patterns

### Requirements Quality Gate Pattern
```
## Requirements Validation Checklist

- [ ] EARS format compliance validated
- [ ] User stories follow role-capability-benefit structure
- [ ] Acceptance criteria are testable and complete
- [ ] Traceability matrix is complete
- [ ] Cross-references are functional
- [ ] Quality score meets threshold (≥85%)

**Validation Results:**
- EARS Format: ✓ Compliant
- User Stories: ✓ Well-formed
- Acceptance Criteria: ✓ Testable
- Traceability: ✓ Complete
- Cross-References: ✓ Functional
- Overall Quality: ✓ Pass (Score: 92%)
```

### Design Quality Gate Pattern
```
## Design Validation Checklist

- [ ] All requirements mapped to design components
- [ ] Component interfaces are clearly defined
- [ ] Data models support all requirements
- [ ] Error handling covers identified scenarios
- [ ] Testing strategy is comprehensive
- [ ] Cross-references are functional

**Validation Results:**
- Requirements Mapping: ✓ Complete
- Component Interfaces: ✓ Defined
- Data Models: ✓ Complete
- Error Handling: ✓ Comprehensive
- Testing Strategy: ✓ Defined
- Overall Quality: ✓ Pass (Score: 88%)
```

### Tasks Quality Gate Pattern
```
## Tasks Validation Checklist

- [ ] All design components have implementation tasks
- [ ] Task hierarchy supports implementation flow
- [ ] Cross-references are functional
- [ ] Quality gates are integrated
- [ ] Implementation flow is logical
- [ ] Optional tasks are properly marked

**Validation Results:**
- Design Mapping: ✓ Complete
- Task Hierarchy: ✓ Logical
- Cross-References: ✓ Functional
- Quality Gates: ✓ Integrated
- Implementation Flow: ✓ Clear
- Overall Quality: ✓ Pass (Score: 90%)
```

## Documentation Consistency Patterns

### Change Log Pattern
```
## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| [Date] | [Description of change] | [Which documents affected and how] |
| [Date] | [Description of change] | [Which documents affected and how] |
```

### Cross-Document References Pattern
```
## Cross-Document References

**Requirements Document:** #[[requirements.md]]
**Design Document:** #[[design.md]]
**Tasks Document:** #[[tasks.md]]
**Project Map:** #[[map.md]] (if applicable)
**Architecture Overview:** #[[architecture-readme-template.md]]
```

### Traceability Matrix Pattern
```
## Cross-Document Traceability

### Requirements Coverage

| Task ID | Requirements Addressed | Design Components | Status |
|---------|----------------------|------------------|---------|
| 1 | #[[requirements.md]]#[Requirement references] | #[[design.md]]#[Component references] | [ ] |
| 2.1 | #[[requirements.md]]#[Requirement references] | #[[design.md]]#[Component references] | [ ] |
```

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

### Template Selection Intelligence Pattern
```
## Template Selection Process

**Step 1: Project Assessment**
- Complexity level determination
- Stakeholder requirement analysis
- Integration complexity evaluation

**Step 2: Template Selection**
- Simple: Core templates only
- Medium: Core + component specifications
- Complex: All templates + architecture documentation
- Enterprise: Full template suite + cross-reference framework

**Step 3: Quality Gate Configuration**
- Automated validation setup
- Quality threshold configuration
- Integration with QA system
```

## Usage Examples

### Simple Feature Documentation Pattern
```
# User Authentication Requirements

## Introduction
Simple user authentication feature for web application with basic login/logout functionality.

## Requirements

### Requirement 1: User Login
**User Story:** As a registered user, I want to log into the system, so that I can access my personalized content.

#### Acceptance Criteria
- [ ] WHEN user enters valid credentials THEN system SHALL grant access and redirect to dashboard
- [ ] IF user enters invalid credentials THEN system SHALL display error message and remain on login page
- [ ] WHERE user session expires THEN system SHALL require re-authentication

**Traceability:** _Design Components: AuthenticationService_ | _Tasks: 1.1, 1.2_
```

### Complex System Documentation Pattern
```
# Enterprise Data Platform Design

## Overview
Comprehensive data platform supporting real-time analytics, batch processing, and machine learning workloads across multiple data sources.

## Architecture
[Detailed architecture with multiple components and integration patterns]

## Components and Interfaces
[Detailed component specifications with cross-references]

## Data Models
[Comprehensive data models with validation rules]

## Error Handling
[Systematic error handling with recovery strategies]

## Testing Strategy
[Multi-level testing approach with quality gates]
```

## Maintenance Patterns

### Regular Validation Pattern
```
## Monthly Documentation Review

**Validation Checklist:**
- [ ] All cross-references functional
- [ ] Traceability matrices complete
- [ ] Quality gates passing
- [ ] Template usage appropriate
- [ ] Change logs updated

**Action Items:**
- Fix any broken references
- Update incomplete traceability
- Address quality gate failures
- Optimize template usage
- Update change documentation
```

### Continuous Improvement Pattern
```
## Documentation Quality Improvement

**Metrics Tracking:**
- Cross-reference integrity rate
- Quality gate pass rate
- Template usage effectiveness
- Documentation completeness score

**Improvement Actions:**
- Update templates based on usage patterns
- Enhance validation rules based on common errors
- Optimize cross-reference patterns for better navigation
- Streamline documentation based on stakeholder feedback
```

## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| [Date] | Initial documentation patterns implementation | All YASK templates and documentation affected |
| [Date] | Added quality gate integration patterns | QA system integration completed |
| [Date] | Enhanced cross-reference validation patterns | Improved traceability and consistency |
| [Date] | Added template selection intelligence patterns | Optimized template usage for different project types |