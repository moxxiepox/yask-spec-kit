---
date: '2025-12-28'
description: Implementation tasks for emergency project refactoring and organization
status: active
title: Emergency Project Refactoring Tasks
version: 1.0.0
tags:
  - system/yask
  - yask/type/tasks
  - yask/status/active
  - refactoring
  - emergency
  - directory/active-projects
  - system/opencode
  - system/code-repair
  - system/first-principles
  - type/documentation
  - feature/native-gui
  - status/active

---



# Emergency Project Refactoring Tasks

## Overview

**Source Documents:**
- Requirements: #[[file:requirements.md]]
- Design: #[[file:design.md]]

This implementation plan breaks down the emergency refactoring into hierarchical tasks that address all requirements and design components systematically.

## Tasks

- [x] 1. Execute Phase 1: Preparation and Backup
  - Create comprehensive pre-refactoring backup
  - Analyze current directory structure
  - Document baseline test results
  - Create migration logging system
  - _Requirements: 8.1, 8.2, 8.3_
  - _Design Components: Migration Strategy, Migration Logging_

- [x] 2. Execute Phase 2: Archive Creation
  - Move backup directories to archives/backups/
  - Move converted notebooks to archives/converted-notebooks/
  - Move old reports to archives/old-reports/
  - Move miscellaneous files to archives/miscellaneous/
  - Create archive indexes for all archive subdirectories
  - _Requirements: 4.1, 4.2, 4.3_
  - _Design Components: Backup and Archive Management System, Archive Index_

- [ ] 3. Execute Phase 3: Documentation Consolidation
  - Move system documentation to system-docs/
  - Consolidate similar reports into comprehensive documents
  - Archive outdated documentation with metadata
  - Update cross-references in documentation
  - _Requirements: 3.1, 3.2, 3.3_
  - _Design Components: Documentation Consolidation Plan_

- [ ] 4. Execute Phase 4: Project Organization
  - Create active-projects/ directory structure
  - Move Native System Monitor to active-projects/native-system-monitor/
  - Move VA Unified Integration to active-projects/va-unified-integration/
  - Move Priority Tracker CLI to active-projects/priority-tracker-cli/
  - Move Code Repair Daemon to active-projects/code-repair-daemon/
  - Move First Principles Integration to active-projects/first-principles-integration/
  - Move Opencode Integration to active-projects/opencode-integration/
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Design Components: Target Directory Structure, File Organization Strategy_

- [ ] 5. Execute Phase 5: Supporting Systems Organization
  - Create supporting-systems/ directory structure
  - Move .opencode/ to supporting-systems/.opencode/
  - Move diff-system/ to supporting-systems/diff-system/
  - Move redis-system/ to supporting-systems/redis-system/
  - Move deployment/ to supporting-systems/deployment/
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Design Components: Target Directory Structure, File Organization Strategy_

- [ ] 6. Execute Phase 6: Research Projects Organization
  - Create research-projects/ directory structure
  - Move SLUDS Physics Engine to research-projects/sluds-physics-engine/
  - Move Thought Framework Research to research-projects/thought-framework-research/
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Design Components: Target Directory Structure, File Organization Strategy_

- [ ] 7. Execute Phase 7: Root Directory Cleanup
  - Identify essential files to keep in root directory
  - Move non-essential files to appropriate locations
  - Update import paths in Python files
  - Update cross-references in documentation
  - _Requirements: 6.1, 6.2, 6.3_
  - _Design Components: Root Directory Cleanup Strategy, Cross-Reference Updates_

- [ ] 8. Execute Phase 8: Cross-Reference Updates
  - Update all cross-references in documentation files
  - Update import paths in Python files
  - Update configuration file references
  - Validate all cross-references are correct
  - _Requirements: 5.1, 5.2, 5.3_
  - _Design Components: Cross-Reference Maintenance_

- [ ] 9. Execute Phase 9: YASK Methodology Application
  - Ensure all active projects have requirements.md
  - Ensure all active projects have design.md
  - Ensure all active projects have tasks.md
  - Create missing YASK documentation using templates
  - Validate YASK compliance across all projects
  - _Requirements: 5.1, 5.2, 5.3_
  - _Design Components: YASK Integration Strategy_

- [ ] 10. Execute Phase 10: Validation and Testing
  - Run all test suites for all projects
  - Compare results to baseline
  - Validate all cross-references
  - Test import paths
  - Verify documentation accessibility
  - _Requirements: 7.1, 7.2, 7.3_
  - _Design Components: Validation Strategy_

- [ ] 11. Execute Phase 11: Documentation Updates
  - Update README.md with new structure
  - Update system documentation with new structure
  - Create migration summary report
  - Update project-specific documentation
  - _Requirements: 3.1, 3.2, 3.3_
  - _Design Components: Documentation Consolidation Plan_

- [ ] 12. Execute Phase 12: Final Validation and Rollback Preparation
  - Run comprehensive final validation
  - Document any remaining issues
  - Create rollback procedures documentation
  - Prepare rollback scripts if needed
  - _Requirements: 7.1, 7.2, 7.3_
  - _Design Components: Validation Strategy, Rollback Procedures_

## Detailed Task Breakdown

### Phase 1: Preparation and Backup

- [ ] 1.1 Create Pre-Refactoring Backup
  - Create archives/backups/2025-12-28-pre-refactor/ directory
  - Copy entire Development directory to backup location
  - Create backup manifest with file metadata
  - Verify backup integrity
  - _Requirements: 8.1, 8.2, 8.3_
  - _Completion Criteria: Complete backup created and verified_

- [ ] 1.2 Analyze Current Directory Structure
  - Catalog all files in root directory
  - Catalog all directories and their contents
  - Identify file types and purposes
  - Document current structure analysis
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Complete directory structure documented_

- [ ] 1.3 Document Baseline Test Results
  - Run all test suites for all projects
  - Document baseline test results
  - Identify any pre-existing issues
  - Create baseline documentation
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: Baseline test results documented_

- [ ] 1.4 Create Migration Logging System
  - Create migration log file
  - Set up logging format with timestamps
  - Create migration tracking spreadsheet
  - Test logging system
  - _Requirements: 8.1, 8.2, 8.3_
  - _Completion Criteria: Migration logging system operational_

### Phase 2: Archive Creation

- [ ] 2.1 Move Backup Directories
  - Move backups/ to archives/backups/
  - Move python_backup/ to archives/backups/
  - Move context_backup/ to archives/backups/
  - Move templates_backup/ to archives/backups/
  - _Requirements: 4.1, 4.2, 4.3_
  - _Completion Criteria: All backup directories moved to archives/backups/_

- [ ] 2.2 Move Converted Notebooks
  - Move converted/ to archives/converted-notebooks/
  - Create archive index for converted notebooks
  - Document notebook conversion history
  - _Requirements: 4.1, 4.2, 4.3_
  - _Completion Criteria: Converted notebooks moved and indexed_

- [ ] 2.3 Move Old Reports
  - Identify all report files in root directory
  - Move reports/ to archives/old-reports/
  - Consolidate similar reports
  - Create archive index for old reports
  - _Requirements: 4.1, 4.2, 4.3_
  - _Completion Criteria: Old reports moved and indexed_

- [ ] 2.4 Move Miscellaneous Files
  - Identify miscellaneous files for archiving
  - Move to archives/miscellaneous/
  - Create archive index for miscellaneous files
  - _Requirements: 4.1, 4.2, 4.3_
  - _Completion Criteria: Miscellaneous files moved and indexed_

### Phase 3: Documentation Consolidation

- [ ] 3.1 Move System Documentation
  - Create system-docs/ directory structure
  - Move installation guides to system-docs/installation/
  - Move API documentation to system-docs/api/
  - Move standards to system-docs/standards/
  - Move guides to system-docs/guides/
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: System documentation organized in system-docs/_

- [ ] 3.2 Consolidate Similar Reports
  - Identify similar reports for consolidation
  - Consolidate test reports into comprehensive document
  - Consolidate status reports into comprehensive document
  - Consolidate analysis reports into comprehensive document
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: Similar reports consolidated_

- [ ] 3.3 Archive Outdated Documentation
  - Identify outdated documentation
  - Archive with metadata (date, reason, superseded by)
  - Update cross-references to current documentation
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: Outdated documentation archived_

- [ ] 3.4 Update Cross-References in Documentation
  - Identify all cross-references in documentation
  - Update to new file locations
  - Validate all updated references
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: All cross-references updated and validated_

### Phase 4: Project Organization

- [ ] 4.1 Create Active Projects Directory Structure
  - Create active-projects/ directory
  - Create subdirectories for each active project
  - Create src/, tests/, docs/, scripts/ subdirectories for each project
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Active projects directory structure created_

- [ ] 4.2 Move Native System Monitor
  - Move src/ to active-projects/native-system-monitor/src/
  - Move tests/ to active-projects/native-system-monitor/tests/
  - Create docs/ directory and move documentation
  - Create scripts/ directory and move scripts
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Native System Monitor moved and functional_

- [ ] 4.3 Move VA Unified Integration
  - Move integration/ to active-projects/va-unified-integration/src/
  - Move integration/tests/ to active-projects/va-unified-integration/tests/
  - Create docs/ directory and move documentation
  - Create scripts/ directory and move scripts
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: VA Unified Integration moved and functional_

- [ ] 4.4 Move Priority Tracker CLI
  - Move Priority Tracker/ to active-projects/priority-tracker-cli/
  - Ensure src/, tests/, docs/, scripts/ structure
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Priority Tracker CLI moved and functional_

- [ ] 4.5 Move Code Repair Daemon
  - Move code-repair-daemon/ to active-projects/code-repair-daemon/
  - Ensure src/, tests/, docs/, scripts/ structure
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Code Repair Daemon moved and functional_

- [ ] 4.6 Move First Principles Integration
  - Move first-principles-integration/ to active-projects/first-principles-integration/
  - Ensure src/, tests/, docs/, scripts/ structure
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: First Principles Integration moved and functional_

- [ ] 4.7 Move Opencode Integration
  - Move opencode-integration files to active-projects/opencode-integration/
  - Create src/, tests/, docs/, scripts/ structure
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Opencode Integration moved and functional_

### Phase 5: Supporting Systems Organization

- [ ] 5.1 Create Supporting Systems Directory Structure
  - Create supporting-systems/ directory
  - Create subdirectories for each supporting system
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Supporting systems directory structure created_

- [ ] 5.2 Move Opencode System
  - Move .opencode/ to supporting-systems/.opencode/
  - Verify all subagents and workflows are intact
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Opencode system moved and functional_

- [ ] 5.3 Move Diff System
  - Move diff/ to supporting-systems/diff-system/diff/
  - Move diff-apply/ to supporting-systems/diff-system/diff-apply/
  - Move diff scripts to supporting-systems/diff-system/scripts/
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Diff system moved and functional_

- [ ] 5.4 Move Redis System
  - Move redis/ to supporting-systems/redis-system/redis/
  - Move redis-windows/ to supporting-systems/redis-system/redis-windows/
  - Move redis5-windows/ to supporting-systems/redis-system/redis5-windows/
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Redis system moved and functional_

- [ ] 5.5 Move Deployment System
  - Move deployment/ to supporting-systems/deployment/deployment/
  - Move docker-compose.yml to supporting-systems/deployment/
  - Move config/ to supporting-systems/deployment/config/
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Deployment system moved and functional_

### Phase 6: Research Projects Organization

- [ ] 6.1 Create Research Projects Directory Structure
  - Create research-projects/ directory
  - Create subdirectories for each research project
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Research projects directory structure created_

- [ ] 6.2 Move SLUDS Physics Engine
  - Move SLUDS (Simulation.Lab.Under.Direct.Supervision)/ to research-projects/sluds-physics-engine/
  - Ensure src/, tests/, docs/ structure
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: SLUDS Physics Engine moved and functional_

- [ ] 6.3 Move Thought Framework Research
  - Move Thought Framework Research Using LLMs/ to research-projects/thought-framework-research/
  - Ensure src/, tests/, docs/ structure
  - Update import paths
  - _Requirements: 1.1, 1.2, 1.3, 1.4_
  - _Completion Criteria: Thought Framework Research moved and functional_

### Phase 7: Root Directory Cleanup

- [ ] 7.1 Identify Essential Files
  - Identify files to keep in root directory
  - Create list of essential files
  - Verify essential files are necessary
  - _Requirements: 6.1, 6.2, 6.3_
  - _Completion Criteria: Essential files identified and documented_

- [ ] 7.2 Move Non-Essential Files
  - Move project-specific files to project directories
  - Move documentation to system-docs/ or project docs/
  - Move scripts to scripts/ or project scripts/
  - _Requirements: 6.1, 6.2, 6.3_
  - _Completion Criteria: Non-essential files moved to appropriate locations_

- [ ] 7.3 Update Import Paths in Python Files
  - Identify all Python files with import paths
  - Update import paths to new locations
  - Validate import paths are correct
  - _Requirements: 6.1, 6.2, 6.3_
  - _Completion Criteria: All import paths updated and validated_

- [ ] 7.4 Update Cross-References in Documentation
  - Identify all cross-references in root documentation
  - Update to new file locations
  - Validate all updated references
  - _Requirements: 6.1, 6.2, 6.3_
  - _Completion Criteria: All cross-references updated and validated_

### Phase 8: Cross-Reference Updates

- [ ] 8.1 Update Cross-References in Documentation Files
  - Scan all documentation files for cross-references
  - Update cross-references to new file locations
  - Validate all updated references
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All documentation cross-references updated and validated_

- [ ] 8.2 Update Import Paths in Python Files
  - Scan all Python files for import paths
  - Update import paths to new locations
  - Validate import paths are correct
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All Python import paths updated and validated_

- [ ] 8.3 Update Configuration File References
  - Scan all configuration files for references
  - Update references to new file locations
  - Validate all updated references
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All configuration file references updated and validated_

- [ ] 8.4 Validate All Cross-References
  - Run comprehensive cross-reference validation
  - Identify any broken references
  - Fix broken references
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All cross-references validated and working_

### Phase 9: YASK Methodology Application

- [ ] 9.1 Ensure All Active Projects Have Requirements.md
  - Check each active project for requirements.md
  - Create missing requirements.md using YASK templates
  - Validate EARS format compliance
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All active projects have requirements.md_

- [ ] 9.2 Ensure All Active Projects Have Design.md
  - Check each active project for design.md
  - Create missing design.md using YASK templates
  - Validate design completeness
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All active projects have design.md_

- [ ] 9.3 Ensure All Active Projects Have Tasks.md
  - Check each active project for tasks.md
  - Create missing tasks.md using YASK templates
  - Validate task structure and traceability
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All active projects have tasks.md_

- [ ] 9.4 Create Missing YASK Documentation Using Templates
  - Load YASK templates from yask-system/.yask/templates/
  - Apply templates to projects missing documentation
  - Customize templates for each project
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: Missing YASK documentation created using templates_

- [ ] 9.5 Validate YASK Compliance Across All Projects
  - Validate EARS format in all requirements.md
  - Validate design completeness in all design.md
  - Validate task structure in all tasks.md
  - Validate cross-references between documents
  - _Requirements: 5.1, 5.2, 5.3_
  - _Completion Criteria: All projects YASK compliant_

### Phase 10: Validation and Testing

- [ ] 10.1 Run All Test Suites for All Projects
  - Run Native System Monitor tests
  - Run VA Unified Integration tests
  - Run Priority Tracker CLI tests
  - Run Code Repair Daemon tests
  - Run First Principles Integration tests
  - Run Opencode Integration tests
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: All test suites executed_

- [ ] 10.2 Compare Results to Baseline
  - Compare test results to baseline
  - Identify any regressions
  - Document any differences
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: Test results compared to baseline_

- [ ] 10.3 Validate All Cross-References
  - Run cross-reference validation
  - Identify any broken references
  - Fix broken references
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: All cross-references validated_

- [ ] 10.4 Test Import Paths
  - Test all import paths in Python files
  - Identify any broken imports
  - Fix broken imports
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: All import paths tested and working_

- [ ] 10.5 Verify Documentation Accessibility
  - Verify all documentation is accessible
  - Test all documentation links
  - Fix any broken links
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: All documentation accessible_

### Phase 11: Documentation Updates

- [ ] 11.1 Update README.md with New Structure
  - Update project overview
  - Update directory structure documentation
  - Update quick start commands
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: README.md updated with new structure_

- [ ] 11.2 Update System Documentation with New Structure
  - Update installation guides
  - Update API documentation
  - Update user guides
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: System documentation updated_

- [ ] 11.3 Create Migration Summary Report
  - Document all file movements
  - Document all changes made
  - Document any issues encountered
  - Document validation results
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: Migration summary report created_

- [ ] 11.4 Update Project-Specific Documentation
  - Update README.md for each project
  - Update project-specific documentation
  - Update project-specific guides
  - _Requirements: 3.1, 3.2, 3.3_
  - _Completion Criteria: Project-specific documentation updated_

### Phase 12: Final Validation and Rollback Preparation

- [ ] 12.1 Run Comprehensive Final Validation
  - Run all test suites
  - Validate all cross-references
  - Validate all import paths
  - Validate all documentation
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: Comprehensive final validation complete_

- [ ] 12.2 Document Any Remaining Issues
  - Identify any remaining issues
  - Document issues with details
  - Provide recommendations for resolution
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: Remaining issues documented_

- [ ] 12.3 Create Rollback Procedures Documentation
  - Document rollback procedures
  - Create rollback scripts if needed
  - Test rollback procedures
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: Rollback procedures documented_

- [ ] 12.4 Prepare Rollback Scripts if Needed
  - Create rollback scripts
  - Test rollback scripts
  - Document rollback script usage
  - _Requirements: 7.1, 7.2, 7.3_
  - _Completion Criteria: Rollback scripts prepared and tested_

## Cross-Document Traceability

### Requirements Coverage

| Task ID | Requirements Addressed | Design Components | Status |
|---------|----------------------|------------------|---------|
| 1 | 8.1, 8.2, 8.3 | Migration Strategy, Migration Logging | [ ] |
| 2 | 4.1, 4.2, 4.3 | Backup and Archive Management System, Archive Index | [ ] |
| 3 | 3.1, 3.2, 3.3 | Documentation Consolidation Plan | [ ] |
| 4 | 1.1, 1.2, 1.3, 1.4 | Target Directory Structure, File Organization Strategy | [ ] |
| 5 | 1.1, 1.2, 1.3, 1.4 | Target Directory Structure, File Organization Strategy | [ ] |
| 6 | 1.1, 1.2, 1.3, 1.4 | Target Directory Structure, File Organization Strategy | [ ] |
| 7 | 6.1, 6.2, 6.3 | Root Directory Cleanup Strategy, Cross-Reference Updates | [ ] |
| 8 | 5.1, 5.2, 5.3 | Cross-Reference Maintenance | [ ] |
| 9 | 5.1, 5.2, 5.3 | YASK Integration Strategy | [ ] |
| 10 | 7.1, 7.2, 7.3 | Validation Strategy | [ ] |
| 11 | 3.1, 3.2, 3.3 | Documentation Consolidation Plan | [ ] |
| 12 | 7.1, 7.2, 7.3 | Validation Strategy, Rollback Procedures | [ ] |

## Implementation Notes

This implementation plan addresses all emergency refactoring requirements through systematic execution of 12 phases with 48 detailed tasks. The hierarchical task structure ensures proper sequencing and dependency management while maintaining traceability to requirements and design components.

**Key Implementation Priorities:**
1. Complete backup creation before any file movement (Phase 1)
2. Archive creation before project organization (Phase 2)
3. Project organization before root directory cleanup (Phases 4-6, then 7)
4. Cross-reference updates before validation (Phase 8, then 10)
5. Validation before documentation updates (Phase 10, then 11)
6. Rollback preparation throughout (Phase 12)

**Risk Mitigation:**
- Complete backup before any changes
- Validation after each phase
- Rollback procedures documented
- Migration logging throughout
- Baseline testing for comparison

**Estimated Timeline:**
- Phase 1: 2-3 hours (backup and preparation)
- Phase 2: 1-2 hours (archive creation)
- Phase 3: 2-3 hours (documentation consolidation)
- Phase 4: 3-4 hours (project organization)
- Phase 5: 1-2 hours (supporting systems)
- Phase 6: 1-2 hours (research projects)
- Phase 7: 2-3 hours (root directory cleanup)
- Phase 8: 2-3 hours (cross-reference updates)
- Phase 9: 2-3 hours (YASK methodology)
- Phase 10: 3-4 hours (validation and testing)
- Phase 11: 2-3 hours (documentation updates)
- Phase 12: 1-2 hours (final validation and rollback)

**Total Estimated Time: 22-34 hours**

## Change Log

| Date | Task | Change | Impact Assessment |
|------|------|--------|-------------------|
| 2025-12-28 | All | Initial emergency refactoring task breakdown | All requirements and design components addressed |
