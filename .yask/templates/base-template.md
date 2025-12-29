---
date: '2025-12-28'
description: Base template framework for YASK system templates
status: active
tags:
  - yask
  - yask/type/template
  - yask/status/active
title: YASK Base Template Framework
version: 6.0.0
---

# YASK Base Template Framework

## Overview

This base template provides common patterns, validation hooks, and structural elements that are inherited by all specialized YASK templates. It ensures consistency, quality validation, and maintainability across the entire template system.

## Common Template Structure

### Standard Header Pattern
```markdown
# [Document Title]

## Introduction

[Concise description of document purpose and scope. Include context about what this document covers and how it fits into the overall project structure.]

## Document Purpose

**Document Type:** [Requirements|Design|Tasks|Component|Framework]
**Complexity Level:** [Simple|Medium|Complex|Enterprise]
**Integration Pattern:** [Standalone|Dependent|Shared|External]
**Quality Gate:** [Phase-specific validation requirements]
```

### Cross-Reference Integration
```markdown
## Cross-Document References

**Requirements Document:** @[requirements.md]
**Design Document:** @[design.md]  
**Tasks Document:** @[tasks.md]
**Project Map:** @[map.md] (if applicable)
**Architecture Overview:** @[architecture-readme-template.md]

## Traceability Matrix

| Element | Requirements | Design Components | Tasks | Status |
|---------|-------------|------------------|-------|---------|
| [Element Name] | @[requirements.md]#[Reference] | @[design.md]#[Reference] | @[tasks.md]#[Reference] | [ ] |
```

### Quality Gate Integration
```markdown
## Quality Validation

### Pre-Validation Checklist
- [ ] EARS format compliance validated (if requirements document)
- [ ] Cross-reference integrity verified
- [ ] Document structure follows template guidelines
- [ ] Quality standards met for complexity level

### Validation Results
- **Format Compliance:** ✓ Compliant
- **Cross-References:** ✓ Functional  
- **Quality Score:** ✓ Pass ([Score]%)
- **Overall Status:** ✓ Ready for phase progression
```

### Change Management
```markdown
## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| [Date] | [Description] | [Documents affected and how] |
| [Date] | [Description] | [Documents affected and how] |
```

## Template Inheritance Patterns

### Base Template Inheritance
```markdown
<!-- Inherit from base template -->
{% extends "base-template.md" %}

{% block document_type %}Requirements{% endblock %}
{% block validation_requirements %}EARS Format, Cross-References{% endblock %}
{% block quality_gates %}Requirements Quality Gate{% endblock %}
```

### Specialized Template Extensions
```markdown
## Specialized Sections

### Requirements-Specific Sections
- User Stories with role-capability-benefit structure
- EARS format acceptance criteria
- Traceability to design and tasks

### Design-Specific Sections  
- Architecture overview and component mapping
- Interface specifications and data models
- Error handling and testing strategies

### Tasks-Specific Sections
- Hierarchical implementation breakdown
- Phase-based development flow
- Quality gates and validation checkpoints
```

## Validation Hooks

### EARS Format Validation
```markdown
**EARS Format Validation Required:**
- [ ] WHEN [specific event/trigger] THEN [system/component] SHALL [specific response/behavior]
- [ ] IF [specific condition/precondition] THEN [system/component] SHALL [specific behavior/response]  
- [ ] WHERE [specific context/location] THEN [system/component] SHALL [specific behavior/response]
```

### Cross-Reference Validation
```markdown
**Cross-Reference Validation:**
- [ ] All @[requirements.md] references point to existing files
- [ ] All #[Overview] references match actual headings
- [ ] Traceability matrix is complete and accurate
- [ ] Quality gates are integrated and functional
```

### Quality Standards Validation
```markdown
**Quality Standards:**
- [ ] Document follows complexity-appropriate template sections
- [ ] Content is complete and actionable
- [ ] Language is clear and unambiguous
- [ ] Integration with QA system is functional
```

## Template Selection Intelligence

### Complexity-Based Template Selection
```markdown
## Template Selection Guidance

**Simple Projects (1-5 requirements):**
- Use: Requirements Template, Design Template (basic), Tasks Template
- Quality Gates: Basic validation
- Cross-References: Simple @[requirements.md] format

**Medium Projects (6-15 requirements):**
- Use: All core templates + Component Template
- Quality Gates: Full validation suite
- Cross-References: Enhanced @[design.md]#[Overview] format

**Complex Projects (16+ requirements):**
- Use: Complete template suite + Framework Template
- Quality Gates: Comprehensive validation
- Cross-References: Full traceability with automated checking
```

## Error Recovery Patterns

### Missing Context Recovery
```markdown
## Missing Context Recovery

**Scenario:** Required documents or sections are missing

**Recovery Strategy:**
1. Identify missing elements using cross-reference validation
2. Create missing documents using appropriate templates
3. Update references to point to correct locations
4. Validate consistency and completeness

**Fallback Approach:**
- Use minimal viable document structure
- Provide placeholder content with clear TODO markers
- Establish basic traceability framework
```

### Quality Validation Error Recovery
```markdown
## Quality Validation Error Recovery

**Scenario:** Document fails quality validation

**Recovery Strategy:**
1. Identify specific validation failures
2. Provide correction guidance with examples
3. Update document content systematically
4. Re-validate to confirm fixes

**Automated Corrections:**
- EARS format violations → Template-based corrections
- Broken references → Automated link repair
- Missing sections → Template section insertion
```

## Integration with QA System

### Automated Validation Integration
```markdown
## QA System Integration

**Validation Points:**
- Document creation and updates
- Cross-reference integrity checking
- Quality gate progression validation
- Consistency verification across documents

**Automated Checks:**
- EARS format compliance validation
- Cross-reference functionality testing
- Quality score calculation and reporting
- Traceability completeness verification
```

### Performance Monitoring
```markdown
## Performance Monitoring

**Metrics Tracked:**
- Document creation time
- Validation execution time
- Cross-reference resolution speed
- Overall system responsiveness

**Optimization Targets:**
- 40-60% improvement in context loading
- Streamlined validation processing
- Enhanced cross-reference resolution
- Improved template processing efficiency
```

## Backward Compatibility

### Legacy Format Support
```markdown
## Backward Compatibility

**Supported Legacy Patterns:**
- #[[file:section]] references (automatically converted)
- Old template structures (mapped to new templates)
- Existing quality gates (maintained functionality)

**Migration Support:**
- Automated pattern conversion
- Compatibility mode options
- Gradual transition guidance
- Rollback capabilities
```

## Usage Guidelines

### Template Customization
- Inherit from base template for consistency
- Override specific sections as needed
- Maintain validation hooks and quality gates
- Use complexity-appropriate template sections

### Quality Assurance
- Validate against base template standards
- Ensure cross-reference integrity
- Maintain traceability completeness
- Follow change management procedures

### Performance Optimization
- Use template caching for repeated operations
- Implement lazy loading for large documents
- Optimize cross-reference resolution
- Monitor and measure performance improvements

## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| 2024-12-17 | Initial base template framework implementation | All YASK templates affected - foundation for consolidation |
| 2024-12-17 | Added template inheritance patterns | Modular template architecture enabled |
| 2024-12-17 | Integrated quality gate validation | Comprehensive validation framework established |