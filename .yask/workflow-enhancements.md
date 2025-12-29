---
date: '2025-12-28'
description: Cross-documentation workflow enhancements and consistency management procedures
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: Cross-Documentation Workflow Enhancements
version: 6.0.0
---

# Cross-Documentation Workflow Enhancements

## Overview
This document provides detailed procedures for maintaining consistency across requirements, design, tasks, and implementation documents in the YASK system.

## Core Principles

### 1. Proactive Consistency Management
- **Detect** inconsistencies before they impact development
- **Assess** impact scope before making changes
- **Cascade** changes through document hierarchy systematically
- **Validate** consistency after each change

### 2. Traceability Maintenance
- Every requirement must trace to design components
- Every design component must trace to implementation tasks
- Every task must trace back to specific requirements
- Implementation must satisfy all EARS acceptance criteria

### 3. Change Impact Assessment
- Changes in one document trigger assessment of all dependent documents
- Impact assessment follows document hierarchy: requirements → design → tasks → implementation
- Scope changes require comprehensive cross-document updates

## Detailed Procedures

### Procedure 1: Requirements Change Impact Assessment

#### Trigger Conditions
- User modifies requirements.md
- New requirements added to existing document
- Existing requirements removed or significantly changed
- EARS acceptance criteria modified

#### Assessment Steps

**Step 1: Load Current State**
```bash
# Load all related documents for context
read requirements.md
read design.md  
read tasks.md
read map.md (if exists)
```

**Step 2: Impact Analysis**
- Identify which requirements changed
- Map changed requirements to design components
- Identify affected tasks and implementation elements
- Assess scope of impact (local vs. system-wide)

**Step 3: Design Updates Required**
- Review design.md for components addressing changed requirements
- Update design components to reflect new/changed requirements
- Add new design components if requirements added
- Remove obsolete design components if requirements removed
- Validate design decisions against updated requirements

**Step 4: Task Cascade Assessment**
- Review tasks.md for tasks implementing changed design components
- Update tasks to reflect design changes
- Add new tasks for new design components
- Remove obsolete tasks for removed requirements
- Validate task dependencies and sequencing

**Step 5: Traceability Verification**
- Ensure every requirement has corresponding design coverage
- Verify every design component has task implementation
- Check that all tasks trace back to specific requirements
- Validate EARS criteria remain testable

**Step 6: Consistency Validation**
- Run automated consistency checks
- Verify cross-references remain valid
- Ensure document formatting and structure consistency
- Validate implementation feasibility

#### Output
- Updated design.md with changes documented
- Updated tasks.md with cascade changes
- Consistency validation report
- Summary of changes made

### Procedure 2: Design Change Impact Assessment

#### Trigger Conditions
- User modifies design.md
- Architecture decisions changed
- Component interfaces modified
- Technology stack changes
- Design patterns or approaches updated

#### Assessment Steps

**Step 1: Load Current State**
```bash
# Load all related documents for context
read requirements.md
read design.md
read tasks.md
read architecture/ (if exists)
```

**Step 2: Requirements Alignment Check**
- Verify design changes don't conflict with requirements
- Ensure all requirements still have design coverage
- Check that design decisions support requirement fulfillment
- Validate that EARS criteria remain achievable

**Step 3: Task Cascade Assessment**
- Identify which tasks implement changed design components
- Update tasks to reflect design changes
- Assess task dependencies and sequencing
- Validate task feasibility with new design

**Step 4: Implementation Impact Assessment**
- Review how design changes affect implementation approach
- Identify new implementation challenges or opportunities
- Assess resource requirements and timeline impact
- Validate technical feasibility

**Step 5: Traceability Maintenance**
- Ensure all design components trace to requirements
- Verify task implementations align with design
- Check that implementation will satisfy requirements
- Validate cross-document consistency

**Step 6: Documentation Updates**
- Update tasks.md based on design changes
- Update any architecture documentation
- Revise implementation guidance
- Update cross-references and links

#### Output
- Updated tasks.md with design-driven changes
- Implementation approach modifications documented
- Traceability verification report
- Summary of design changes and impacts

### Procedure 3: Implementation-Driven Updates

#### Trigger Conditions
- Implementation differs from specifications
- Technical constraints require design modifications
- Implementation reveals requirement gaps
- Code changes affect document references

#### Assessment Steps

**Step 1: Load Full Context**
```bash
# Load all specification documents
read requirements.md
read design.md
read tasks.md
read current implementation files
```

**Step 2: Specification Alignment Analysis**
- Compare implementation against requirements
- Identify deviations from design specifications
- Assess impact of deviations on requirements fulfillment
- Validate EARS criteria satisfaction

**Step 3: Documentation Update Requirements**
- Determine if requirements need updates
- Assess if design modifications are needed
- Identify tasks that need revision
- Evaluate need for new documentation

**Step 4: Cross-Reference Validation**
- Check all document links and references
- Validate cross-document traceability
- Ensure implementation traces to requirements
- Verify design decisions are reflected in code

**Step 5: Quality Gates**
- Validate against EARS acceptance criteria
- Check design decision implementation
- Verify task completion criteria
- Ensure code quality standards

**Step 6: Document Updates**
- Update requirements.md if implementation reveals gaps
- Modify design.md to reflect actual implementation
- Update tasks.md with completion status
- Revise cross-references and links

#### Output
- Updated specification documents
- Implementation validation report
- Cross-reference consistency verification
- Quality assessment results

### Procedure 4: Automated Consistency Checking

#### Pre-Change Validation Checklist
Before modifying any document:

- [ ] **Context Loading**: All related documents loaded and read
- [ ] **Dependency Mapping**: Document dependencies and cross-references identified
- [ ] **Current State Analysis**: Existing inconsistencies documented
- [ ] **Change Scope Assessment**: Impact scope of proposed changes evaluated
- [ ] **Baseline Establishment**: Current traceability relationships documented

#### Post-Change Validation Checklist
After modifying any document:

- [ ] **Requirement-Design Traceability**: Every requirement has design coverage
- [ ] **Design-Task Alignment**: Every design component has task implementation
- [ ] **Task-Implementation Mapping**: Every task traces to specific requirements
- [ ] **EARS Criteria Validation**: All acceptance criteria remain testable
- [ ] **Cross-Reference Integrity**: All links and references remain valid
- [ ] **Document Structure Consistency**: Formatting and structure standards maintained

#### Automated Validation Rules

**Rule 1: Requirement Coverage**
```
FOR each requirement in requirements.md:
  FIND corresponding design components in design.md
  IF no design components found:
    REPORT inconsistency: Requirement not addressed in design
```

**Rule 2: Design Traceability**
```
FOR each design component in design.md:
  FIND corresponding requirements in requirements.md
  IF no requirements found:
    REPORT inconsistency: Design component not traced to requirements
```

**Rule 3: Task Implementation**
```
FOR each task in tasks.md:
  FIND corresponding design components and requirements
  IF missing references:
    REPORT inconsistency: Task lacks proper traceability
```

**Rule 4: EARS Format Validation**
```
FOR each acceptance criteria:
  VALIDATE format: WHEN [event] THEN [system] SHALL [response]
  IF invalid format:
    REPORT format error with correction guidance
```

**Rule 5: Cross-Reference Integrity**
```
FOR each #[[file:]] link:
  VALIDATE target file exists
  VALIDATE target section exists
  IF broken link:
    REPORT broken reference with suggested fix
```

### Procedure 5: Scope Change Management

#### Scope Change Detection
- User explicitly requests scope modification
- Implementation reveals requirement gaps
- Technical constraints require approach changes
- Resource limitations affect scope

#### Enhanced Scope Change Protocol

**Step 1: Scope Change Assessment**
- Document current scope and boundaries
- Identify proposed scope modifications
- Assess impact on existing work
- Evaluate resource and timeline implications

**Step 2: Document Impact Analysis**
- Map scope changes to document modifications needed
- Identify which requirements affected
- Assess design component changes required
- Evaluate task structure modifications

**Step 3: Systematic Document Updates**
- Update requirements.md with scope changes
- Modify design.md to reflect new scope
- Restructure tasks.md based on scope modifications
- Update cross-references and links

**Step 4: Traceability Reconstruction**
- Rebuild requirement-to-design traceability
- Re-establish design-to-task mapping
- Verify implementation-to-requirement connections
- Validate EARS criteria alignment

**Step 5: Consistency Validation**
- Run comprehensive consistency checks
- Validate all cross-document relationships
- Ensure implementation feasibility
- Verify quality standards maintained

**Step 6: User Confirmation**
- Present scope change impact summary
- Document all modifications made
- Seek user approval for scope changes
- Confirm implementation approach

### Procedure 6: Quality Assurance Integration

#### Quality Checkpoints
- **Requirements Quality**: EARS format, user story clarity, testability
- **Design Quality**: Requirements coverage, architecture clarity, feasibility
- **Task Quality**: Hierarchical structure, traceability, actionability
- **Implementation Quality**: Specification compliance, code quality, testing

#### Quality Validation Tools
- **Automated Format Checking**: EARS criteria validation
- **Traceability Verification**: Cross-document relationship validation
- **Consistency Analysis**: Document alignment verification
- **Implementation Validation**: Code-to-specification compliance

#### Quality Gates
1. **Pre-Implementation**: All documents complete and consistent
2. **During Implementation**: Regular consistency checks and updates
3. **Post-Implementation**: Comprehensive validation against specifications
4. **Final Review**: Complete traceability and quality verification

## Implementation Guidelines

### Agent Behavior Modifications

#### Enhanced Context Loading
- Always load ALL related documents before making changes
- Identify document dependencies and cross-references
- Assess current consistency state
- Document baseline before modifications

#### Proactive Change Assessment
- Evaluate impact scope before making changes
- Cascade changes through document hierarchy systematically
- Validate consistency after each modification
- Maintain traceability throughout process

#### Quality Integration
- Apply quality checks at each workflow stage
- Validate against established standards
- Use automated tools for consistency verification
- Maintain comprehensive documentation of changes

### Tool Integration

#### Document Management
- Use version control for all document changes
- Implement automated consistency checking
- Maintain change logs and impact assessments
- Provide rollback capabilities for problematic changes

#### Validation Automation
- Implement automated EARS format checking
- Create traceability verification tools
- Develop cross-reference validation
- Build consistency analysis capabilities

#### Workflow Integration
- Integrate procedures into existing workflow
- Provide clear triggers for each procedure
- Create user-friendly validation reports
- Enable automated consistency monitoring

## Success Metrics

### Consistency Metrics
- **Cross-Document Consistency**: Percentage of documents in consistent state
- **Traceability Completeness**: Percentage of requirements with full traceability
- **Change Impact Accuracy**: Accuracy of impact assessments
- **Quality Gate Pass Rate**: Percentage of changes passing quality checks

### Efficiency Metrics
- **Change Processing Time**: Time to assess and implement document changes
- **Consistency Validation Time**: Time to validate document consistency
- **Error Detection Rate**: Percentage of inconsistencies caught before implementation
- **User Satisfaction**: User feedback on workflow effectiveness

### Quality Metrics
- **Document Quality Scores**: Quality ratings for each document type
- **Implementation Accuracy**: Percentage of implementations matching specifications
- **Requirement Coverage**: Percentage of requirements with complete design coverage
- **EARS Compliance**: Percentage of acceptance criteria in proper format

## Continuous Improvement

### Feedback Collection
- Monitor workflow effectiveness
- Collect user feedback on procedures
- Track consistency issues and resolutions
- Analyze change impact assessment accuracy

### Procedure Refinement
- Update procedures based on usage patterns
- Enhance automation based on common issues
- Improve validation rules based on discovered gaps
- Optimize workflow based on efficiency metrics

### Tool Enhancement
- Develop new validation tools based on needs
- Improve existing automation capabilities
- Integrate additional quality checks
- Enhance reporting and analysis features