---
date: '2025-12-28'
description: YASK system project structure map and navigation guide
status: active
title: YASK System - Project Structure Map
version: 6.0.0
tags:
  - system/yask
  - yask/type/documentation
  - yask/status/active
  - directory/active-projects
  - type/documentation
  - feature/native-gui
  - status/active

---



# YASK System: Project Structure Map

## Project Organization

```
yask-system/
├── .yask/                          # YASK framework and templates
│   ├── templates/                  # Document templates
│   ├── validation/                 # Quality gates and validation
│   ├── workflow/                   # Process automation
│   ├── testing/                    # Test framework
│   └── integration/                # System integration
├── Core Documents                  # Primary specifications
│   ├── requirements.md             # WHAT we need to build
│   ├── design.md                   # HOW we'll build it
│   ├── tasks.md                    # Implementation steps
│   └── map.md                      # Project structure and status
├── Test Reports                    # Validation and quality metrics
│   ├── test-reports/               # Comprehensive test results
│   └── test-logs/                  # Execution logs
└── System Tools                    # Automation and utilities
    ├── yask_coordination_test.py   # System validation
    └── comprehensive_health_check.py # System monitoring
```

## Document Purposes

### Core Specifications
- **requirements.md**: User stories and EARS acceptance criteria for YASK system
- **design.md**: Technical architecture overview with system integration patterns
- **tasks.md**: Actionable implementation tasks with verification checkpoints
- **map.md**: Project structure, status, and maintenance guide (this document)

### YASK Framework Components
- **.yask/templates/**: Document templates and patterns for consistent creation
- **.yask/validation/**: Quality gates, validation procedures, and correction engines
- **.yask/workflow/**: Process automation and consistency checking tools
- **.yask/testing/**: Test framework and validation runners

## Navigation Guide

### By Development Phase
- **Planning**: [[Requirements]] → [[Design]] → [[Tasks]]
- **Implementation**: [[Tasks]] → System Implementation
- **Validation**: [[Testing Strategy|design.md#testing-strategy]] → [[Acceptance Criteria|requirements.md#acceptance-criteria]]

### By System Component
- **Core System**: #[[file::.yask]] → #[[file::.yask/templates]] → #[[file::.yask/validation]]
- **Testing**: #[[file::.yask/testing]] → #[[file::.yask/validation/quality-gates]]
- **Integration**: #[[file::.yask/integration]] → #[[file::.yask/workflow]]

### Cross-Reference Patterns
- **Internal References**: *See #[[file::.yask]] for comprehensive system information.*
- **Requirement Traceability**: _Requirements: 1.1, 1.2, 4.6_
- **Document Relationships**: Links between requirements → design → tasks → implementation

## Project Status

### Current Phase
**Phase**: validation_and_testing
**Status**: active_development

### Development Progress
**Completion**: 85% complete (based on task checkboxes and test results)

### Quality Metrics
- **Cross-Reference Validation**: Target 95%+ (currently being optimized)
- **EARS Format Compliance**: 100% (32/32 criteria)
- **Document Completeness**: 100% (3/3 core files)
- **System Stability**: 95% (high stability demonstrated)

## Document Relationships

```
requirements.md (WHAT) → design.md (HOW) → tasks.md (WHEN) → implementation
        ↓                    ↓                    ↓
    .yask/              .yask/              .yask/
    templates           validation          workflow
        ↓                    ↓                    ↓
    patterns           quality-gates       automation
```

## Maintenance Guidelines

### Update Triggers
- **requirements.md**: New features, scope changes, acceptance criteria updates
- **design.md**: Architecture decisions, technical challenges, interface changes
- **tasks.md**: Implementation approach changes, task completion
- **map.md**: Project structure changes, status updates
- **.yask/**: Framework updates, template changes, validation improvements

### Status Updates
- Update task checkboxes in tasks.md as work progresses
- Update phase status in map.md when transitioning between phases
- Run validation tools after significant document changes
- Monitor cross-reference validation metrics

### Review Process
1. **Requirements**: Stakeholder review → Technical feasibility assessment
2. **Design**: Architecture review → Implementation feasibility validation
3. **Tasks**: Development team review → Effort estimation verification
4. **Map**: Team review → Organization clarity confirmation

## Development Phases

### Phase 1: Requirements ✅ COMPLETED
**Goal**: Define WHAT needs to be built
**Output**: Approved requirements.md with EARS format
**Success**: All user stories have testable acceptance criteria

### Phase 2: Design ✅ COMPLETED
**Goal**: Define HOW it will be built
**Output**: Technical design with architecture references
**Success**: All requirements addressed in design

### Phase 3: Tasks ✅ COMPLETED
**Goal**: Define implementation steps
**Output**: Actionable task breakdown with verification
**Success**: Clear implementation roadmap approved

### Phase 4: Implementation & Testing 🔄 IN PROGRESS
**Goal**: Build and validate the system systematically
**Output**: Working implementation with comprehensive tests
**Success**: All tasks completed and validated

## File Organization

### Naming Conventions
- **Specifications**: Descriptive names (requirements.md, design.md, tasks.md)
- **Framework**: YASK-specific organization (.yask/ directory structure)
- **Templates**: Clear purpose indicators (map-template.md, requirements-template.md)

### Directory Principles
- **Separation of concerns**: Specs, framework, tests, reports in separate directories
- **Logical grouping**: Related functionality grouped within .yask/ structure
- **Scalability**: Structure supports growth without reorganization
- **Clarity**: Directory names clearly indicate purpose and function

## Cross-Reference Validation

### Valid Reference Patterns
- **Document Links**: #[[file:requirements.md]], #[[file:design.md]], #[[file:tasks.md]]
- **Framework Links**: #[[file:.yask]], #[[file:.yask/templates]], #[[file:.yask/validation]]
- **Template Links**: #[[file:yask-system/.yask/templates/architecture-readme-template.md]] (template files)

### Validation Status
- **Total References**: 178
- **Valid References**: 130 (73.0%)
- **Target**: 95%+ (169+ references)
- **Focus Areas**: map.md creation, template reference resolution

## Quality Assurance

### Validation Checkpoints
- **EARS Format Compliance**: 100% maintained
- **Document Completeness**: All core documents present and valid
- **Cross-Reference Integrity**: Improving from 73% to 95%+
- **System Stability**: 95% demonstrated across all test suites

### Continuous Improvement
- Regular cross-reference validation runs
- Template consistency checks
- Framework integration testing
- Performance monitoring and optimization
#links 
- [[VA_UNIFIED_DOCUMENTATION#VA Unified - Complete Documentation]]
- [[VA_UNIFIED_DOCUMENTATION#📊 Project Overview]]
- [[VA_UNIFIED_DOCUMENTATION]] (Lines: 3-6)
- [[VA_UNIFIED_TODO#Executive Summary]]
- [[VA_UNIFIED_TODO#VA Unified - Master TODO & Project Status]]
- [[VA_UNIFIED_TODO#2. VA Unified Integration System]]
- [[VA_UNIFIED_DOCUMENTATION]] (Lines: 78-85)
- [[VA_UNIFIED_DOCUMENTATION#Project Status (Updated Dec 15, 2025)]]
- [[VA_UNIFIED_TODO]] (Lines: 13-20)
- [[todo#Multi-Project Integration Status]]
- [[README#VA Unified Integration System - Complete Setup Guide]]
- [[VA_UNIFIED_TODO#Current Test Summary]]
- [[SYSTEM_STATUS_REPORT#📈 System Health Dashboard]]
- [[todo#VA Unified System Integration]]
- [[VA_UNIFIED_DOCUMENTATION#📚 Additional Resources]]
- [[FINAL_WORK_SUMMARY_REPORT#🚀 System Components Status]]
- [[VA_UNIFIED_TODO#🎯 Core Projects]]
- [[README#Table of Contents]]
- [[todo#Priority CLI Tool - TODO & Roadmap]]
- [[requirements#Dependencies]]
- [[todo#Project Ecosystem Status]]