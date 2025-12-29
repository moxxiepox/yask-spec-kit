---
date: '2025-12-28'
description: Technical design for emergency project refactoring and organization
status: active
title: Emergency Project Refactoring Design
version: 1.0.0
tags:
  - system/yask
  - yask/type/design
  - yask/status/active
  - refactoring
  - emergency
  - directory/active-projects
  - system/opencode
  - system/code-repair
  - system/first-principles
  - system/meta-prompting
  - type/documentation
  - feature/meta-prompting
  - feature/native-gui
  - status/active

---



# Emergency Project Refactoring Design

## Overview

This design provides a comprehensive technical architecture for reorganizing the Development directory to eliminate clutter, improve navigation, and maintain backward compatibility. The refactoring follows YASK methodology with systematic phases, clear validation checkpoints, and comprehensive rollback procedures.

## Requirements Coverage

**Source Requirements:** #[[file:requirements.md]]

### Requirement Mapping

| Requirement | Design Component | Implementation Approach |
|-------------|------------------|-------------------------|
| 1. Project Organization and Structure | Target Directory Structure, File Organization Strategy | Standardized directory hierarchy with clear project separation |
| 2. File Organization and Naming Conventions | File Organization Strategy, Naming Conventions | Consistent lowercase-hyphen naming with logical grouping |
| 3. Documentation Consolidation | Documentation Consolidation Plan, Archive Management System | Project-based documentation organization with archive system |
| 4. Backup and Archive Management | Backup and Archive Management System, Archive Index | Comprehensive backup system with searchable index |
| 5. YASK Methodology Application | YASK Integration Strategy, Cross-Reference Maintenance | YASK compliance across all projects with updated references |
| 6. Root Directory Cleanup | Root Directory Cleanup Strategy, Cross-Reference Updates | Minimal root directory with essential files only |
| 7. Backward Compatibility and Validation | Validation Strategy, Rollback Procedures | Comprehensive testing with rollback capabilities |
| 8. Migration Strategy and Execution | Migration Strategy, Migration Logging | Phased migration with detailed logging |

## Architecture

### Target Directory Structure

```
Development/
├── README.md                           # Main project overview
├── requirements.md                     # System-wide requirements
├── design.md                           # System-wide design
├── tasks.md                            # System-wide tasks
├── AGENTS.md                           # YASK agent instructions
├── .gitignore                          # Git ignore rules
├── requirements.txt                    # Python dependencies
├── pytest.ini                          # Test configuration
├── .coverage                           # Coverage data
│
├── active-projects/                    # Active development projects
│   ├── native-system-monitor/          # Native System Monitor
│   │   ├── src/                        # Source code
│   │   ├── tests/                     # Tests
│   │   ├── docs/                      # Documentation
│   │   │   ├── requirements.md
│   │   │   ├── design.md
│   │   │   └── tasks.md
│   │   ├── scripts/                   # Utility scripts
│   │   └── README.md
│   │
│   ├── va-unified-integration/         # VA Unified Integration
│   │   ├── src/                        # Source code
│   │   ├── tests/                     # Tests
│   │   ├── docs/                      # Documentation
│   │   │   ├── requirements.md
│   │   │   ├── design.md
│   │   │   └── tasks.md
│   │   ├── scripts/                   # Utility scripts
│   │   └── README.md
│   │
│   ├── priority-tracker-cli/           # Priority Tracker CLI
│   │   ├── src/                        # Source code
│   │   ├── tests/                     # Tests
│   │   ├── docs/                      # Documentation
│   │   │   ├── requirements.md
│   │   │   ├── design.md
│   │   │   └── tasks.md
│   │   ├── scripts/                   # Utility scripts
│   │   └── README.md
│   │
│   ├── code-repair-daemon/             # Code Repair Daemon
│   │   ├── src/                        # Source code
│   │   ├── tests/                     # Tests
│   │   ├── docs/                      # Documentation
│   │   │   ├── requirements.md
│   │   │   ├── design.md
│   │   │   └── tasks.md
│   │   ├── scripts/                   # Utility scripts
│   │   └── README.md
│   │
│   ├── first-principles-integration/   # First Principles Integration
│   │   ├── src/                        # Source code
│   │   ├── tests/                     # Tests
│   │   ├── docs/                      # Documentation
│   │   │   ├── requirements.md
│   │   │   ├── design.md
│   │   │   └── tasks.md
│   │   ├── scripts/                   # Utility scripts
│   │   └── README.md
│   │
│   └── opencode-integration/           # Opencode Integration
│       ├── src/                        # Source code
│       ├── tests/                     # Tests
│       ├── docs/                      # Documentation
│       │   ├── requirements.md
│       │   ├── design.md
│       │   └── tasks.md
│       ├── scripts/                   # Utility scripts
│       └── README.md
│
├── yask-system/                        # YASK Framework
│   ├── requirements.md                 # YASK requirements
│   ├── design.md                       # YASK design
│   ├── tasks.md                        # YASK tasks
│   ├── agents.md                       # YASK agent instructions
│   ├── to-do.md                        # YASK TODO
│   ├── .yask/                          # YASK framework files
│   │   ├── principles.md
│   │   ├── patterns.md
│   │   ├── process.md
│   │   └── templates/                  # YASK templates
│   │       ├── requirements-template.md
│   │       ├── design-template.md
│   │       └── tasks-template.md
│   ├── subsystems/                     # YASK subsystems
│   │   └── meta-prompting/             # Meta Prompting Subsystem
│   │       ├── core/
│   │       ├── examples/
│   │       ├── tests/
│   │       ├── utils/
│   │       └── README.md
│   └── refactoring/                    # Refactoring project
│       ├── requirements.md
│       ├── design.md
│       └── tasks.md
│
├── supporting-systems/                 # Supporting systems and tools
│   ├── .opencode/                      # Opencode system
│   │   ├── subagents/                  # Subagent implementations
│   │   ├── workflows/                  # Workflow definitions
│   │   ├── config/                     # Configuration files
│   │   └── tests/                      # Opencode tests
│   │
│   ├── diff-system/                    # Diff management system
│   │   ├── diff/                       # Core diff functionality
│   │   ├── diff-apply/                 # Diff application
│   │   └── scripts/                    # Diff scripts
│   │
│   ├── redis-system/                   # Redis configuration
│   │   ├── redis/                      # Redis files
│   │   ├── redis-windows/              # Windows Redis
│   │   └── redis5-windows/             # Redis 5 Windows
│   │
│   └── deployment/                     # Deployment configurations
│       ├── deployment/                 # Deployment scripts
│       ├── docker-compose.yml          # Docker configuration
│       └── config/                     # Configuration files
│
├── research-projects/                  # Research and experimental projects
│   ├── sluds-physics-engine/           # SLUDS Physics Engine
│   │   ├── src/
│   │   ├── tests/
│   │   ├── docs/
│   │   └── README.md
│   │
│   └── thought-framework-research/     # Thought Framework Research
│       ├── src/
│       ├── tests/
│       ├── docs/
│       └── README.md
│
├── archives/                           # Archived materials
│   ├── backups/                        # Backup archives
│   │   ├── 2025-12-28-pre-refactor/    # Pre-refactoring backup
│   │   └── dated-backups/              # Date-based backups
│   │
│   ├── converted-notebooks/            # Converted Jupyter notebooks
│   │   └── archive-index.md            # Archive index
│   │
│   ├── old-reports/                    # Historical reports
│   │   └── archive-index.md            # Archive index
│   │
│   └── miscellaneous/                  # Miscellaneous archived files
│       └── archive-index.md            # Archive index
│
├── system-docs/                        # System-wide documentation
│   ├── installation/                   # Installation guides
│   │   └── INSTALLATION.md
│   │
│   ├── api/                            # API documentation
│   │   └── API_DOCUMENTATION.md
│   │
│   ├── standards/                      # Standards and policies
│   │   ├── ATTACHMENT_REFERENCE_STANDARD.md
│   │   ├── OBSIDIAN_STANDARDIZATION_SPEC.md
│   │   └── NATIVE_DEARPYGUI_POLICY.md
│   │
│   └── guides/                         # User guides
│       ├── SCRIPT_USAGE_GUIDE.md
│       └── DAEMON_MANAGEMENT_GUIDE.md
│
└── scripts/                            # System-wide utility scripts
    ├── migration/                      # Migration scripts
    ├── validation/                     # Validation scripts
    └── utilities/                      # Utility scripts
```

## Components and Interfaces

### File Organization Strategy

**Purpose**: Provide systematic file organization with consistent naming conventions and logical grouping

**Key Methods**:
- File categorization by project and type
- Naming convention enforcement (lowercase-hyphen)
- Cross-reference maintenance and updates
- Archive management with indexing

**Organization Rules**:
- All project files go into `active-projects/{project-name}/`
- Documentation goes into `docs/` subdirectory within each project
- Tests go into `tests/` subdirectory within each project
- Scripts go into `scripts/` subdirectory within each project
- System-wide scripts go into `scripts/` at root level
- Archives go into `archives/` with appropriate subdirectories

**Requirements Addressed:** 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4

### Documentation Consolidation Plan

**Purpose**: Consolidate scattered documentation into organized, navigable structure

**Key Methods**:
- Project-based documentation grouping
- Report consolidation and archiving
- Cross-reference updates
- Archive indexing

**Consolidation Strategy**:
1. Move project-specific documentation to `active-projects/{project}/docs/`
2. Consolidate similar reports into comprehensive documents
3. Archive outdated documentation with metadata
4. Update all cross-references to new locations
5. Create archive indexes for searchable retrieval

**Requirements Addressed:** 3.1, 3.2, 3.3

### Backup and Archive Management System

**Purpose**: Provide systematic backup and archive management with searchable indexing

**Key Methods**:
- Pre-refactoring backup creation
- Archive manifest generation
- Archive index creation
- Searchable archive retrieval

**Backup Strategy**:
1. Create complete pre-refactoring backup in `archives/backups/2025-12-28-pre-refactor/`
2. Maintain archive manifest with metadata (original location, date, reason)
3. Create searchable archive indexes for each archive subdirectory
4. Implement archive retrieval procedures

**Archive Structure**:
```
archives/
├── backups/
│   └── 2025-12-28-pre-refactor/
│       ├── manifest.json              # Complete file manifest
│       └── [original directory structure]
├── converted-notebooks/
│   └── archive-index.md               # Searchable index
├── old-reports/
│   └── archive-index.md               # Searchable index
└── miscellaneous/
    └── archive-index.md               # Searchable index
```

**Requirements Addressed:** 4.1, 4.2, 4.3

### YASK Integration Strategy

**Purpose**: Ensure all projects follow YASK methodology consistently

**Key Methods**:
- YASK documentation creation for projects lacking it
- Cross-reference maintenance and updates
- YASK template application
- YASK compliance validation

**Integration Approach**:
1. Ensure all active projects have `requirements.md`, `design.md`, `tasks.md`
2. Create missing YASK documentation using YASK templates
3. Update all cross-references to reflect new file locations
4. Validate YASK compliance across all projects

**Requirements Addressed:** 5.1, 5.2, 5.3

### Root Directory Cleanup Strategy

**Purpose**: Minimize root directory to essential files only

**Key Methods**:
- File categorization and movement
- Essential file identification
- Cross-reference updates
- Import path updates

**Cleanup Rules**:
- Keep only essential system files in root: `README.md`, `requirements.md`, `design.md`, `tasks.md`, `AGENTS.md`, `.gitignore`, `requirements.txt`, `pytest.ini`
- Move all project-specific files to appropriate project directories
- Move all documentation to `system-docs/` or project `docs/`
- Move all scripts to `scripts/` or project `scripts/`
- Update all cross-references and import paths

**Requirements Addressed:** 6.1, 6.2, 6.3

### Validation Strategy

**Purpose**: Ensure all projects continue working after refactoring

**Key Methods**:
- Pre-refactoring baseline testing
- Post-refactoring validation testing
- Cross-reference validation
- Import path validation

**Validation Procedures**:
1. Run all test suites before refactoring to establish baseline
2. Execute refactoring in phases with validation after each phase
3. Run all test suites after refactoring to verify functionality
4. Validate all cross-references and import paths
5. Document any issues and provide rollback procedures

**Requirements Addressed:** 7.1, 7.2, 7.3

### Migration Strategy

**Purpose**: Execute systematic migration with minimal disruption and risk

**Key Methods**:
- Phased migration approach
- Checkpoint validation
- Comprehensive logging
- Rollback procedures

**Migration Phases**:
1. **Phase 1: Preparation** - Create backups, analyze current structure
2. **Phase 2: Archive Creation** - Move archives to `archives/`
3. **Phase 3: Documentation Consolidation** - Organize documentation
4. **Phase 4: Project Organization** - Move projects to `active-projects/`
5. **Phase 5: Root Directory Cleanup** - Clean root directory
6. **Phase 6: Cross-Reference Updates** - Update all references
7. **Phase 7: Validation** - Run comprehensive tests
8. **Phase 8: Documentation Updates** - Update all documentation

**Migration Logging**:
- Maintain detailed migration log with timestamps
- Log all file movements and modifications
- Record validation results at each checkpoint
- Document any issues and resolutions

**Requirements Addressed:** 8.1, 8.2, 8.3

## Error Handling

### Migration Errors

**Scenario**: File movement fails due to permissions or locks

**Recovery Strategy**:
1. Log error with detailed information
2. Skip problematic file and continue
3. Document skipped files in migration log
4. Provide manual resolution instructions
5. Continue with remaining files

**Fallback Approach**: Manual file movement with user guidance

### Validation Failures

**Scenario**: Tests fail after refactoring

**Recovery Strategy**:
1. Identify specific test failures
2. Analyze root cause (import paths, missing files, etc.)
3. Attempt automatic fixes (import path updates)
4. If automatic fix fails, provide rollback procedures
5. Document issues and resolution steps

**Fallback Approach**: Rollback to pre-refactoring state

### Cross-Reference Errors

**Scenario**: Broken cross-references after file movement

**Recovery Strategy**:
1. Identify all broken references
2. Update references to new file locations
3. Validate all updated references
4. Document any unresolvable references
5. Provide manual correction guidance

**Fallback Approach**: Create reference mapping document for manual updates

## Testing Strategy

### Pre-Refactoring Testing

**Approach**: Establish baseline functionality before refactoring

**Test Scenarios**:
- Run all test suites for all projects
- Document baseline test results
- Identify any pre-existing issues
- Create baseline documentation

**Validation Criteria**: All tests pass or pre-existing issues documented

### Post-Refactoring Testing

**Approach**: Validate functionality after refactoring

**Test Scenarios**:
- Run all test suites for all projects
- Compare results to baseline
- Validate all cross-references
- Test import paths
- Verify documentation accessibility

**Validation Criteria**: All tests pass, cross-references valid, documentation accessible

### Rollback Testing

**Approach**: Validate rollback procedures

**Test Scenarios**:
- Test rollback from each migration phase
- Verify complete restoration of pre-refactoring state
- Validate all functionality after rollback
- Document rollback procedures

**Validation Criteria**: Rollback restores complete pre-refactoring state

## Cross-Document References

**Requirements Document:** #[[file:requirements.md]]
**Tasks Document:** #[[file:tasks.md]]
**YASK System:** #[[file:../../yask-system/requirements.md]], #[[file:../../yask-system/design.md]], #[[file:../../yask-system/tasks.md]]

## Change Log

| Date | Change | Requirements Impact | Tasks Impact |
|------|--------|-------------------|--------------|
| 2025-12-28 | Initial emergency refactoring design specification | All 8 requirements addressed | All tasks defined |
