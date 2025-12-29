---
date: '2025-12-28'
  description: Comprehensive testing framework for YASK (Yet Another Spec-Kit) system
    versions 2.21 and 2.21_cf.
  status: active
  tags:
  - yask
  - yask/documentation
  - yask/status/active
  title: YASK Testing Framework
  version: 6.0.0
---

# YASK Testing Framework

Comprehensive testing framework for YASK (Yet Another Spec-Kit) system versions 2.21 and 2.21_cf.

## Overview

This testing framework validates the complete spec-driven development workflow: Requirements → Design → Tasks → Implementation. It ensures both versions (2.21 and 2.21_cf) function correctly and can be tested side-by-side.

## Testing Philosophy

### Core Principles
1. **End-to-End Validation**: Test complete workflows from requirements to implementation
2. **Cross-Document Consistency**: Verify traceability between requirements, design, and tasks
3. **Agent Prompt Effectiveness**: Validate AI agent adherence to spec-dev patterns
4. **Version Comparison**: Systematic comparison of 2.21 vs 2.21_cf behavior
5. **Error Recovery**: Test system behavior under failure conditions
6. **Quality Assurance**: Ensure EARS format compliance and document quality

### Testing Approach
- **Automated Validation**: Scripts for consistent, repeatable testing
- **Manual Verification**: Human validation of AI agent outputs and decisions
- **Side-by-Side Comparison**: Parallel testing of both versions
- **Performance Benchmarking**: Centralized vs distributed prompt performance

## Test Categories

### 1. System Installation Tests
**Purpose**: Validate installer scripts and system setup
**Scope**: Both versions, all installation methods

#### Test Cases
- **Gemini CLI Installation** (`install-gemini.sh`)
  - [ ] Script executes without errors
  - [ ] Files copied to correct locations
  - [ ] TOML configuration created properly
  - [ ] Setup script generates correct workspace structure
  - [ ] Cleanup functionality works

- **Cursor IDE Installation** (`install-cursor.sh`)
  - [ ] Script executes without errors
  - [ ] .cursor/rules structure created correctly
  - [ ] Agent file with frontmatter generated properly
  - [ ] System files accessible to agent

- **System File Integrity**
  - [ ] All template files present and valid
  - [ ] Documentation files accessible
  - [x] AI agent spec management (spec.sh removed)
  - [ ] Version identification working

### 2. Document Creation Tests
**Purpose**: Validate template usage and document generation
**Scope**: All document types, both versions

#### Requirements Document Tests
- [ ] **EARS Format Compliance**
  - WHEN/THEN/SHALL pattern usage
  - IF/THEN/SHALL pattern usage
  - WHERE/SHALL pattern usage
  - No malformed acceptance criteria

- [ ] **User Story Quality**
  - Clear role, capability, benefit structure
  - Consistent formatting
  - Complete stories for all requirements

- [ ] **Document Structure**
  - Introduction section present
  - Requirements section properly organized
  - Constraints and assumptions documented
  - Cross-references functional

#### Design Document Tests
- [ ] **Requirements Coverage**
  - All requirements addressed in design
  - Clear component mapping to requirements
  - Design decisions justified

- [ ] **Architecture Clarity**
  - System components clearly defined
  - Component interfaces specified
  - Integration points documented
  - Error handling strategies defined

- [ ] **Design Decision Format**
  - Options considered documented
  - Rationale provided for decisions
  - Impact analysis included
  - Requirements traceability maintained

#### Tasks Document Tests
- [ ] **Hierarchical Structure**
  - Main tasks with logical numbering
  - Sub-tasks properly indented
  - Checkbox format consistent
  - Optional tasks marked with "*"

- [ ] **Requirement Traceability**
  - Each task references specific requirements
  - Cross-references functional
  - Traceability matrix complete

- [ ] **Implementation Logic**
  - Tasks build logically on each other
  - Dependencies clearly identified
  - Verification criteria included

### 3. Workflow Integration Tests
**Purpose**: Validate end-to-end spec-dev workflow
**Scope**: Complete workflows, both versions

#### Phase Progression Tests
- [ ] **Requirements → Design Transition**
  - Design phase loads requirements correctly
  - All requirements addressed in design
  - User approval mechanism functional
  - Phase summary comprehensive

- [ ] **Design → Tasks Transition**
  - Tasks phase loads both requirements and design
  - Task breakdown addresses all design components
  - Hierarchical structure follows design
  - User approval mechanism functional

- [ ] **Tasks → Implementation Transition**
  - Implementation phase loads all documents
  - Single task focus maintained
  - Context loading comprehensive
  - Task completion verification

#### Cross-Document Consistency Tests
- [ ] **Requirement Changes**
  - Design updates when requirements change
  - Tasks update when design changes
  - Traceability maintained throughout
  - Consistency validation functional

- [ ] **Scope Change Management**
  - Impact assessment when scope changes
  - Document prioritization correct
  - User confirmation required
  - Update cascade functional

### 4. Agent Prompt Effectiveness Tests
**Purpose**: Validate AI agent adherence to spec-dev patterns
**Scope**: Agent behavior, both versions

#### Prompt Adherence Tests
- [ ] **Context Loading**
  - Agent reads all relevant documents
  - Template files loaded correctly
  - Project context assessed properly
  - Missing context handled gracefully

- [ ] **Phase-Specific Behavior**
  - Requirements phase: EARS format, user stories
  - Design phase: Architecture, decisions, coverage
  - Tasks phase: Hierarchical structure, traceability
  - Implementation phase: Single task focus, summaries

- [ ] **Quality Standards**
  - EARS format compliance enforced
  - Comprehensive summaries provided
  - User approval sought at phase boundaries
  - Cross-document consistency maintained

#### Communication Pattern Tests
- [ ] **Proactive Behavior**
  - Strategic thinking demonstrated
  - Comprehensive analysis provided
  - Quality checkpoints implemented
  - Error handling proactive

- [ ] **Approval Workflow**
  - Clear approval requests
  - Comprehensive summaries before approval
  - Phase completion properly identified
  - User feedback incorporation

### 5. Error Recovery Tests
**Purpose**: Validate system behavior under failure conditions
**Scope**: Error scenarios, both versions

#### Missing Context Recovery
- [ ] **No requirements.md**
  - Graceful error handling
  - Clear guidance provided
  - Recovery suggestions offered
  - System doesn't crash

- [ ] **No design.md**
  - Appropriate error message
  - Context requirement explained
  - Recovery path suggested
  - System stability maintained

- [ ] **Incomplete Documents**
  - Quality issues identified
  - Specific guidance provided
  - Completion assistance offered
  - User education provided

#### Implementation Error Recovery
- [ ] **Code Errors**
  - Error analysis provided
  - Specific solutions suggested
  - Alternative approaches offered
  - No false completion claims

- [ ] **File Editing Failures**
  - Alternative methods attempted
  - Manual steps suggested
  - User assistance requested when needed
  - Persistence demonstrated

- [ ] **Missing Dependencies**
  - Requirements identified
  - Installation guidance provided
  - Alternative methods suggested
  - Verification steps included

### 6. Version Comparison Tests
**Purpose**: Systematic comparison of 2.21 vs 2.21_cf
**Scope**: Both versions, all functionality

#### Performance Comparison
- [ ] **Centralized vs Distributed Prompts**
  - Response time measurement
  - Context comprehension assessment
  - Quality consistency evaluation
  - Resource usage comparison

- [ ] **Functionality Parity**
  - Feature completeness comparison
  - Output quality assessment
  - Error handling comparison
  - User experience evaluation

#### Behavioral Differences
- [ ] **Prompt Processing**
  - Context loading differences
  - Decision-making variations
  - Communication style differences
  - Quality standard adherence

- [ ] **Workflow Execution**
  - Phase transition behavior
  - Approval workflow differences
  - Error recovery variations
  - Cross-document consistency

### 7. Template Validation Tests
**Purpose**: Validate template functionality and usage
**Scope**: All templates, both versions

#### Template Structure Tests
- [ ] **Requirements Template**
  - EARS format placeholders
  - User story structure
  - Section organization
  - Cross-reference support

- [ ] **Design Template**
  - Architecture sections
  - Component specifications
  - Decision documentation
  - Error handling sections

- [ ] **Tasks Template**
  - Hierarchical structure
  - Checkbox formatting
  - Requirement references
  - Optional task marking

#### Template Adaptation Tests
- [ ] **Contextual Adaptation**
  - Template adjustment for project complexity
  - Audience-appropriate content
  - Technology-specific adaptations
  - Section reordering when beneficial

- [ ] **Quality Preservation**
  - Core requirements maintained
  - EARS format preserved
  - Traceability maintained
  - Cross-reference functionality

## Test Execution Procedures

### Pre-Testing Setup

#### Environment Preparation
1. **Clean Workspace Setup**
   ```bash
   # Create isolated test directories
   mkdir -p test-environments/{2.21,2.21_cf}
   cd test-environments/2.21
   # Install version 2.21
   cd ../2.21_cf
   # Install version 2.21_cf
   ```

2. **Test Data Preparation**
   - Create sample project requirements
   - Prepare test scenarios for each phase
   - Set up expected outputs for validation
   - Configure version-specific settings

#### Baseline Establishment
1. **Version Identification**
   - Document version-specific features
   - Identify configuration differences
   - Establish expected behavioral patterns
   - Create version comparison matrix

### Test Execution Workflow

#### Daily Testing Routine
1. **System Health Check**
   - Run installation validation tests
   - Verify system file integrity
   - Check template accessibility
   - Validate agent prompt loading

2. **Workflow Validation**
   - Execute complete end-to-end test
   - Validate document creation
   - Test cross-document consistency
   - Verify agent prompt effectiveness

3. **Error Scenario Testing**
   - Test missing context recovery
   - Validate implementation error handling
   - Test scope change management
   - Verify graceful degradation

#### Weekly Comprehensive Testing
1. **Full Version Comparison**
   - Run all test categories for both versions
   - Document behavioral differences
   - Assess performance variations
   - Evaluate quality consistency

2. **Regression Testing**
   - Re-run previous test scenarios
   - Validate bug fix effectiveness
   - Ensure no functionality regression
   - Document any new issues

### Test Result Documentation

#### Test Report Structure
```markdown
# Test Report - [Date]

## Test Environment
- Version: [2.21|2.21_cf]
- Platform: [OS/Environment details]
- Test Duration: [Time taken]

## Test Results Summary
- Total Tests: [Count]
- Passed: [Count]
- Failed: [Count]
- Warnings: [Count]

## Detailed Results
[Per-category detailed results]

## Version Comparison
[Behavioral differences documented]

## Issues Identenced
[List of issues found]

## Recommendations
[Improvement suggestions]
```

#### Issue Tracking
- **Severity Levels**: Critical, High, Medium, Low
- **Categories**: Installation, Workflow, Agent Behavior, Templates, Documentation
- **Status Tracking**: Open, In Progress, Resolved, Deferred
- **Version Attribution**: 2.21 only, 2.21_cf only, Both versions

## Automated Testing Scripts

### Test Runner Structure
```
.yask/tests/
├── runners/
│   ├── system-tests.sh          # System installation tests
│   ├── document-tests.sh        # Document creation tests
│   ├── workflow-tests.sh        # End-to-end workflow tests
│   ├── agent-tests.sh           # Agent prompt effectiveness tests
│   ├── error-tests.sh           # Error recovery tests
│   ├── version-tests.sh         # Version comparison tests
│   └── template-tests.sh        # Template validation tests
├── utilities/
│   ├── test-helpers.sh          # Shared testing utilities
│   ├── validation-functions.sh  # Validation logic
│   ├── comparison-tools.sh      # Version comparison tools
│   └── reporting.sh             # Test reporting utilities
├── data/
│   ├── test-scenarios/          # Test case definitions
│   ├── expected-outputs/        # Expected test results
│   └── version-configs/         # Version-specific configurations
└── reports/
    ├── daily/                   # Daily test reports
    ├── weekly/                  # Weekly comprehensive reports
    └── historical/              # Historical test data
```

### Script Execution Framework
1. **Individual Test Categories**
   - Run specific test categories independently
   - Generate category-specific reports
   - Support selective re-testing

2. **Comprehensive Test Suites**
   - Execute all test categories
   - Generate comprehensive reports
   - Support parallel execution

3. **Continuous Integration**
   - Automated test execution
   - Integration with version control
   - Automated reporting and alerting

## Quality Metrics

### Document Quality Metrics
- **EARS Compliance**: Percentage of acceptance criteria following EARS format
- **User Story Completeness**: Percentage of requirements with complete user stories
- **Cross-Reference Accuracy**: Percentage of valid cross-document references
- **Template Adherence**: Percentage of documents following template structure

### Workflow Quality Metrics
- **Phase Completion Rate**: Percentage of workflows completing all phases
- **Approval Success Rate**: Percentage of phase approvals obtained
- **Error Recovery Rate**: Percentage of errors successfully recovered
- **Context Loading Accuracy**: Percentage of contexts properly loaded

### Agent Performance Metrics
- **Prompt Adherence**: Percentage of responses following spec-dev patterns
- **Quality Consistency**: Variance in output quality across sessions
- **Response Time**: Average time for agent responses
- **User Satisfaction**: Subjective rating of agent effectiveness

### Version Comparison Metrics
- **Functional Parity**: Percentage of features working identically
- **Performance Difference**: Response time and quality variations
- **Behavioral Consistency**: Decision-making pattern similarities
- **Error Rate Comparison**: Error frequency and type differences

## Continuous Improvement

### Test Framework Evolution
1. **Regular Review Cycle**
   - Monthly test effectiveness review
   - Quarterly framework updates
   - Annual comprehensive overhaul

2. **Feedback Integration**
   - User feedback incorporation
   - Developer input integration
   - Performance optimization

3. **Best Practice Development**
   - Testing pattern documentation
   - Success story sharing
   - Lessons learned capture

### Knowledge Management
1. **Test Case Library**
   - Maintain comprehensive test case database
   - Regular test case updates
   - Version-specific test variations

2. **Documentation Maintenance**
   - Keep testing framework documentation current
   - Update procedures based on learnings
   - Maintain version comparison records

3. **Training and Onboarding**
   - Testing framework training materials
   - New tester onboarding procedures
   - Best practice sharing sessions

---

## Quick Start Guide

### Running Basic Tests
```bash
# Navigate to test directory
cd .yask/tests

# Run system installation tests
./runners/system-tests.sh

# Run document creation tests
./runners/document-tests.sh

# Run complete workflow test
./runners/workflow-tests.sh

# Run version comparison
./runners/version-tests.sh --compare
```

### Generating Reports
```bash
# Generate daily test report
./utilities/reporting.sh --daily

# Generate comprehensive weekly report
./utilities/reporting.sh --weekly --comprehensive

# Generate version comparison report
./utilities/reporting.sh --version-compare
```

### Custom Test Scenarios
```bash
# Run specific test scenario
./runners/workflow-tests.sh --scenario "user-authentication"

# Test with custom data
./runners/document-tests.sh --data "custom-test-data/"

# Validate specific version
./runners/system-tests.sh --version "2.21_cf"
```

This testing framework provides comprehensive validation of the YASK system across both versions, ensuring reliable spec-driven development workflows and maintaining quality standards throughout the development process.