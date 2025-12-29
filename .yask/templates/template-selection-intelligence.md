---
date: '2025-12-28'
description: YASK template selection intelligence for project characteristics and complexity
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: YASK Template Selection Intelligence
version: 6.0.0
---

# YASK Template Selection Intelligence

## Overview

This document provides intelligent guidance for selecting the appropriate YASK templates based on project characteristics, complexity, and requirements. The system adapts template usage to match project needs while maintaining consistency and quality standards.

## Template Selection Matrix

### Project Complexity Assessment

| Complexity Level | Characteristics | Recommended Templates | Additional Guidance |
|------------------|-----------------|----------------------|-------------------|
| **Simple** | Single feature, minimal dependencies, straightforward requirements | requirements-template.md, design-template.md (basic sections), tasks-template.md | Use minimal template sections, focus on core functionality |
| **Medium** | Multiple components, some dependencies, moderate complexity | All core templates + component-specification-template.md | Include detailed component specifications and interface definitions |
| **Complex** | Multiple systems, significant dependencies, enterprise-level | All templates + architecture-readme-template.md | Comprehensive architecture documentation and integration patterns |
| **Enterprise** | Large-scale systems, multiple teams, regulatory requirements | All templates + cross-reference-framework.md | Full traceability, compliance documentation, and quality gates |

### Document Type Selection

#### Requirements Documentation
**Use Case:** When defining what the system should do
**Template:** requirements-template.md
**Selection Criteria:**
- [ ] Need to define user stories and acceptance criteria
- [ ] Require EARS format validation
- [ ] Need traceability to design and tasks
- [ ] Multiple stakeholders involved

**Adaptation Guidelines:**
- Simple projects: Focus on core requirements sections
- Complex projects: Include detailed constraints and assumptions
- Enterprise projects: Add compliance and regulatory requirements

#### Design Documentation
**Use Case:** When defining how the system will work
**Template:** design-template.md
**Selection Criteria:**
- [ ] Need to specify system architecture
- [ ] Require component interface definitions
- [ ] Need data model specifications
- [ ] Multiple implementation approaches possible

**Adaptation Guidelines:**
- Simple projects: Use basic component formats
- Medium projects: Include detailed interface specifications
- Complex projects: Add comprehensive error handling and testing strategies

#### Implementation Tasks
**Use Case:** When planning how to build the system
**Template:** tasks-template.md
**Selection Criteria:**
- [ ] Need to break down implementation into manageable tasks
- [ ] Require hierarchical task structure
- [ ] Need traceability to requirements and design
- [ ] Multiple development phases involved

**Adaptation Guidelines:**
- Simple projects: Basic task breakdown with minimal phases
- Medium projects: Detailed phases with cross-references
- Complex projects: Comprehensive implementation flow with quality gates

#### Component Specifications
**Use Case:** When defining detailed component interfaces and behavior
**Template:** component-specification-template.md
**Selection Criteria:**
- [ ] Need detailed interface contracts
- [ ] Require technical implementation details
- [ ] Multiple integration points involved
- [ ] Complex component interactions

**Adaptation Guidelines:**
- Use for medium complexity and above projects
- Required for components with external dependencies
- Essential for shared or reusable components

#### Architecture Documentation
**Use Case:** When documenting system-wide architectural decisions
**Template:** architecture-readme-template.md
**Selection Criteria:**
- [ ] Multiple architectural areas to document
- [ ] Need navigation between architectural documents
- [ ] Complex system integration patterns
- [ ] Enterprise-level architecture decisions

**Adaptation Guidelines:**
- Use for complex and enterprise projects
- Create subdirectories for different architectural areas
- Link architectural decisions to implementation tasks

## Intelligent Template Selection Process

### Step 1: Project Assessment
```
Project Assessment Checklist:
□ Number of requirements (Simple: 1-5, Medium: 6-15, Complex: 16+)
□ Number of components (Simple: 1-3, Medium: 4-10, Complex: 11+)
□ Integration complexity (Low/Medium/High)
□ Stakeholder count (Simple: 1-3, Medium: 4-8, Complex: 9+)
□ Regulatory requirements (Yes/No)
□ Performance requirements (Standard/High/Enterprise)
```

### Step 2: Template Selection
Based on assessment results:
- **Simple:** requirements-template.md + design-template.md + tasks-template.md
- **Medium:** All above + component-specification-template.md
- **Complex:** All above + architecture-readme-template.md
- **Enterprise:** All templates + cross-reference-framework.md

### Step 3: Template Customization
Apply complexity-based adaptations:
- Remove unnecessary sections for simple projects
- Add detailed sections for complex projects
- Include quality gates for enterprise projects
- Adapt cross-reference patterns based on project size

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

## Cross-Reference Framework Integration

### Reference Pattern Selection
- **Simple Projects:** Basic #[[document]] references
- **Medium Projects:** #[[document]]#[section] references
- **Complex Projects:** Full cross-reference framework with validation
- **Enterprise Projects:** Complete traceability with automated checking

### Traceability Requirements
- **Simple:** Basic requirement-to-task mapping
- **Medium:** Requirement-to-design-to-task mapping
- **Complex:** Full traceability with impact assessment
- **Enterprise:** Automated traceability with quality metrics

## Usage Examples

### Simple Feature Implementation
```
Selected Templates:
- requirements-template.md (basic sections only)
- design-template.md (overview + basic components)
- tasks-template.md (minimal phases)

Quality Gates:
- Basic EARS validation
- Simple cross-reference checking
```

### Medium Complexity System
```
Selected Templates:
- requirements-template.md (full template)
- design-template.md (detailed components)
- tasks-template.md (phased approach)
- component-specification-template.md (key components)

Quality Gates:
- Full EARS validation
- Component interface validation
- Cross-reference integrity checking
```

### Enterprise System
```
Selected Templates:
- All templates
- cross-reference-framework.md
- Full architecture documentation

Quality Gates:
- Comprehensive validation suite
- Automated consistency checking
- Full traceability verification
- Compliance validation
```

## Template Evolution Guidelines

### When to Add Templates
- Project complexity increases
- New stakeholder requirements emerge
- Regulatory compliance needed
- Integration complexity grows

### When to Simplify Templates
- Project scope reduces
- Unused sections identified
- Stakeholder feedback indicates overhead
- Quality gates show diminishing returns

### Maintenance Procedures
1. **Regular Assessment:** Review template effectiveness quarterly
2. **Stakeholder Feedback:** Collect usage feedback from project teams
3. **Quality Metrics:** Analyze quality gate results for template optimization
4. **Template Updates:** Update templates based on lessons learned

## Integration with QA System

### Validation Integration Points
- **Template Selection Validation:** Ensures appropriate templates chosen
- **Content Validation:** Validates template content against quality standards
- **Cross-Reference Validation:** Ensures all references are functional
- **Traceability Validation:** Verifies complete requirement mapping

### Automated Quality Checks
```
Template Quality Assessment:
✓ Template selection appropriateness
✓ Content completeness and quality
✓ Cross-reference integrity
✓ Traceability completeness
✓ Quality gate compliance
```

## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| [Date] | Initial template selection intelligence implementation | Template selection guidance for all project types |
| [Date] | Added quality gate integration | Automated validation of template usage |
| [Date] | Enhanced complexity assessment | Improved template selection accuracy |