---
date: '2025-12-28'
description: YASK cross-reference framework for traceability and consistency
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: YASK Cross-Reference Framework
version: 6.0.0
---

# YASK Cross-Reference Framework

## Overview

This framework provides standardized patterns for cross-document references and validation mechanisms to ensure traceability and consistency across all YASK documentation.

## Reference Patterns

### Standard Reference Format
```
#[[document-name.md]]#[section-reference]
```

### Document Types and Patterns

#### Requirements Document References
- **Source Requirements:** #[[requirements.md]]
- **Specific Requirement:** @[requirements.md]#[Requirement 1]: [Title]
- **Acceptance Criteria:** @[requirements.md]#[Acceptance Criteria]
- **User Story:** @[requirements.md]#[User Story]

#### Design Document References
- **Design Overview:** @[design.md]#[Overview]
- **Architecture Section:** @[design.md]#[Architecture]
- **Components:** @[design.md]#[Components and Interfaces]
- **Data Models:** @[design.md]#[Data Models]
- **Error Handling:** @[design.md]#[Error Handling]
- **Testing Strategy:** @[design.md]#[Testing Strategy]

#### Tasks Document References
- **Task Overview:** @[tasks.md]#[Overview]
- **Specific Task:** @[tasks.md]#[1]. [Task Title]
- **Phase Reference:** @[tasks.md]#[Phase 1]: [Phase Name]
- **Implementation Notes:** @[tasks.md]#[Implementation Notes]

#### Architecture Directory References
- **Architecture Overview:** #[[architecture-readme-template.md]]
- **Core Systems:** @[architecture-readme-template.md]#[Core Systems]
- **Interfaces:** @[architecture-readme-template.md]#[Interfaces]
- **Integration:** @[architecture-readme-template.md]#[Integration]

#### Map Document References (if applicable)
- **Project Map:** #[[map.md]]
- **Component Map:** @[map.md]#[Component Overview]
- **Integration Map:** @[map.md]#[Integration Patterns]

## Validation Mechanisms

### Reference Validation Rules

#### 1. Document Existence Check
- **Rule:** All #[[document]] references must point to existing files
- **Validation:** Automated checking during quality gates
- **Error Handling:** Missing document references must be resolved before approval

#### 2. Section Reference Validation
- **Rule:** ##[section] references must match actual document headings
- **Validation:** Pattern matching against document structure
- **Error Handling:** Invalid section references trigger validation warnings

#### 3. Traceability Matrix Validation
- **Rule:** All requirements must have corresponding design components and tasks
- **Validation:** Cross-reference matrix verification
- **Error Handling:** Missing traceability links require completion before phase progression

### Automated Reference Checking

#### Pre-Change Validation
```
Reference Check: ✓ All cross-references valid
Document Existence: ✓ All referenced documents found
Section Links: ✓ All section references match
Traceability: ✓ Complete requirement-to-implementation mapping
```

#### Post-Change Validation
```
Impact Assessment: [List affected documents]
Reference Updates: [List references that need updating]
Consistency Check: [Validation results]
Quality Gate: [Pass/Fail with reasons]
```

## Cross-Document Traceability

### Requirements Traceability
```
Requirement → Design Component → Implementation Task → Validation
     ↓              ↓                    ↓              ↓
  @[req.md]#[   ]@[design.md]#[    ]@[tasks.md]#[   ]#[[validation]]
```

### Design Traceability
```
Architecture → Components → Interfaces → Data Models → Testing
     ↓            ↓            ↓            ↓           ↓
#[[arch]]#    #[[design]]#   #[[design]]#  #[[design]]# #[[design]]#
```

### Implementation Traceability
```
Task → Code → Tests → Documentation → Validation Results
  ↓      ↓      ↓           ↓              ↓
#[[tasks]]# [Files]  #[[tests]]#   #[[docs]]#     #[[validation]]
```

## Quality Gates Integration

### Phase Gate Validation
- **Requirements Gate:** All requirements have EARS format and traceability
- **Design Gate:** All components mapped to requirements with clear interfaces
- **Tasks Gate:** All tasks traceable to design components with implementation flow
- **Implementation Gate:** All code traceable to tasks with validation results

### Consistency Validation
- **Cross-Reference Integrity:** All references functional and accurate
- **Traceability Completeness:** Full requirement-to-implementation mapping
- **Document Synchronization:** All documents reflect current state
- **Quality Metrics:** Document quality scores within acceptable ranges

## Error Recovery Procedures

### Missing Reference Recovery
1. **Identify Missing Document:** Determine which referenced document doesn't exist
2. **Create Missing Document:** Use appropriate template to create required document
3. **Update References:** Ensure all cross-references are accurate
4. **Validate Consistency:** Run full cross-reference validation

### Broken Link Recovery
1. **Identify Broken Link:** Find section references that don't match headings
2. **Update Section References:** Correct ##[section] references to match actual headings
3. **Validate Document Structure:** Ensure all documents follow template structure
4. **Re-run Validation:** Confirm all references are now functional

### Traceability Gap Recovery
1. **Identify Gap:** Find requirements without corresponding design components or tasks
2. **Create Missing Elements:** Add required design components or implementation tasks
3. **Update Traceability:** Ensure all traceability matrices are complete
4. **Validate Completeness:** Confirm full traceability mapping exists

## Integration with QA System

### Validation Integration Points
- **EARS Format Validation:** Validates requirement format and structure
- **Cross-Reference Validation:** Checks all document references
- **Consistency Validation:** Ensures document synchronization
- **Quality Gate Validation:** Validates phase progression criteria

### Automated Quality Checks
```
EARS Format Check: ✓ Requirements follow EARS structure
Reference Integrity: ✓ All cross-references functional
Traceability Matrix: ✓ Complete requirement mapping
Document Consistency: ✓ All documents synchronized
Quality Gate Status: ✓ Ready for phase progression
```

## Usage Guidelines

### When Creating References
1. Use standard #[[document]]#[section] format
2. Ensure all referenced documents exist
3. Validate section references match actual headings
4. Update traceability matrices when adding new elements

### When Modifying Documents
1. Check impact on cross-references before changes
2. Update related documents if structure changes
3. Validate all references remain functional
4. Run consistency validation after modifications

### When Validating Documents
1. Run automated reference checking
2. Validate traceability completeness
3. Check quality gate criteria
4. Document any issues and recovery actions

## Change Log

| Date | Change | Impact Assessment |
|------|--------|-------------------|
| [Date] | Initial cross-reference framework implementation | All documentation templates affected |
| [Date] | Added validation mechanisms integration | QA system integration completed |
| [Date] | Enhanced traceability patterns | Complete requirement-to-implementation mapping |