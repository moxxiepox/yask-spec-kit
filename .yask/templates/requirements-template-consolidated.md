---
date: '2025-12-28'
description: Consolidated requirements template for YASK system
status: active
tags:
  - yask
  - yask/type/template
  - yask/status/active
title: Requirements Template - Consolidated
version: 6.0.0
---

# [Feature Name] Requirements

{% extends "base-template.md" %}

{% block document_type %}Requirements{% endblock %}
{% block validation_requirements %}EARS Format, User Stories, Traceability{% endblock %}
{% block quality_gates %}Requirements Quality Gate{% endblock %}

## Introduction

[Concise feature description, purpose, and technical approach. Include context about the problem being solved and the value proposition for stakeholders.]

## Requirements

### Requirement 1: [Clear, Actionable Title]

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

### Requirement 2: [Clear, Actionable Title]

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

## Cross-Document References

**Design Document:** @[design.md]
**Tasks Document:** @[tasks.md]
**Related Specifications:** @[map.md] (if applicable)

## Traceability Matrix

| Requirement | Design Components | Tasks | Status |
|-------------|------------------|-------|---------|
| Requirement 1 | @[design.md]#[Component references] | @[tasks.md]#[Task references] | [ ] |
| Requirement 2 | @[design.md]#[Component references] | @[tasks.md]#[Task references] | [ ] |

## Constraints & Assumptions

**Constraints:**
- [Technical/business constraints]

**Assumptions:**
- [Key assumptions about system/users]

## Quality Validation

### Requirements Quality Gate
- [ ] EARS format compliance validated for all requirements
- [ ] User stories follow role-capability-benefit structure
- [ ] Acceptance criteria are testable and complete
- [ ] Traceability matrix is complete and accurate
- [ ] Cross-references are functional and validated
- [ ] Quality score meets threshold (≥85%)

### Validation Results
- **EARS Format:** ✓ Compliant
- **User Stories:** ✓ Well-formed
- **Acceptance Criteria:** ✓ Testable
- **Traceability:** ✓ Complete
- **Cross-References:** ✓ Functional
- **Overall Quality:** ✓ Pass (Score: [X]%)

## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| [Date] | [Description] | [Documents affected] |