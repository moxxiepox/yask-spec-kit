---
date: '2025-12-28'
description: Standardized template for creating validation test cases in the YASK system
status: active
tags:
  - yask
  - yask/type/template
  - yask/status/active
title: Test Case Template
version: 6.0.0
---

# Test Case Template

Standardized template for creating validation test cases in the YASK system.

## Test Case Information

### Test Case ID
`TC-[CATEGORY]-[NUMBER]`

### Test Case Name
`[Descriptive test case name]`

### Test Category
- [ ] Requirements Validation
- [ ] Design Validation  
- [ ] Tasks Validation
- [ ] Implementation Validation
- [ ] Cross-Document Consistency
- [ ] EARS Format Validation
- [ ] User Story Validation
- [ ] Traceability Validation
- [ ] Error Recovery
- [ ] Integration Testing

### Priority
- [ ] Critical (Must pass)
- [ ] High (Should pass)
- [ ] Medium (Could pass)
- [ ] Low (Nice to have)

### Test Type
- [ ] Functional Test
- [ ] Validation Test
- [ ] Regression Test
- [ ] Integration Test
- [ ] Error Handling Test
- [ ] Performance Test

## Test Objective

### Purpose
[Clear statement of what this test case validates]

### Expected Outcome
[What should happen when the test is executed successfully]

## Test Data

### Input Data
```
[Specific input data or document content needed for this test]
```

### Expected Output
```
[Expected validation results or output]
```

### Test Environment
- **YASK Version**: [2.21 | 2.21_cf | Both]
- **Operating System**: [Windows | macOS | Linux]
- **Required Files**: [List of files needed]
- **Dependencies**: [Any required tools or libraries]

## Test Steps

### Pre-conditions
1. [ ] [Prerequisite condition 1]
2. [ ] [Prerequisite condition 2]
3. [ ] [Prerequisite condition 3]

### Test Procedure
1. [Step 1: Action to perform]
2. [Step 2: Action to perform]
3. [Step 3: Action to perform]
4. [Step 4: Action to perform]
5. [Step 5: Action to perform]

### Expected Results
1. [Expected result for step 1]
2. [Expected result for step 2]
3. [Expected result for step 3]
4. [Expected result for step 4]
5. [Expected result for step 5]

## Test Case Examples

### Example 1: EARS Format Validation Test

#### Test Case ID
`TC-EARS-001`

#### Test Case Name
`Validate WHEN/THEN/SHALL Pattern`

#### Test Category
- [x] EARS Format Validation
- [x] Requirements Validation

#### Priority
- [x] Critical (Must pass)

#### Test Objective
**Purpose**: Ensure requirements document contains properly formatted EARS criteria using WHEN/THEN/SHALL pattern

**Expected Outcome**: All acceptance criteria follow the pattern "WHEN [event] THEN [system] SHALL [response]"

#### Test Data
**Input Data**:
```markdown
### Requirement 1: User Authentication

**User Story:** As a registered user, I want to log into the system, so that I can access my account

#### Acceptance Criteria

1. WHEN user enters valid credentials THEN system SHALL authenticate user
2. WHEN user enters invalid credentials THEN system SHALL display error message
3. WHEN user session expires THEN system SHALL require re-authentication
```

**Expected Output**:
- All acceptance criteria pass EARS format validation
- No malformed criteria detected
- Consistent system terminology used

#### Test Steps
1. [ ] Create requirements.md with test data
2. [ ] Run validation script: `./validate-specs.sh`
3. [ ] Check EARS format validation results
4. [ ] Verify all criteria follow WHEN/THEN/SHALL pattern
5. [ ] Confirm no format errors reported

#### Expected Results
1. [x] requirements.md created successfully
2. [x] Validation script executes without errors
3. [x] EARS format validation passes
4. [x] All criteria follow correct pattern
5. [x] No format errors in output

---

### Example 2: Traceability Validation Test

#### Test Case ID
`TC-TRACE-001`

#### Test Case Name
`Validate Requirements-to-Design Traceability`

#### Test Category
- [x] Cross-Document Consistency
- [x] Traceability Validation

#### Priority
- [x] High (Should pass)

#### Test Objective
**Purpose**: Ensure all requirements are properly referenced in the design document

**Expected Outcome**: Complete bidirectional traceability between requirements and design components

#### Test Data
**Input Data**:
```markdown
# requirements.md
### Requirement 1: User Authentication
### Requirement 2: Data Validation
### Requirement 3: Error Handling

# design.md
## Components
### Authentication Component
Addresses requirements 1 and 3.

### Validation Component  
Addresses requirement 2.
```

**Expected Output**:
- All requirements referenced in design
- Design components mapped to requirements
- Complete traceability matrix

#### Test Steps
1. [ ] Create requirements.md with numbered requirements
2. [ ] Create design.md with component references
3. [ ] Run traceability validation
4. [ ] Check requirement coverage in design
5. [ ] Verify bidirectional references

#### Expected Results
1. [x] All 3 requirements found in design
2. [x] Component mapping complete
3. [x] No orphaned requirements
4. [x] Traceability validation passes

---

### Example 3: Error Recovery Test

#### Test Case ID
`TC-ERROR-001`

#### Test Case Name
`Validate Missing Context Recovery`

#### Test Category
- [x] Error Recovery
- [x] Implementation Validation

#### Priority
- [x] Critical (Must pass)

#### Test Objective
**Purpose**: Ensure system handles missing context gracefully and provides clear recovery guidance

**Expected Outcome**: Clear error message with specific recovery steps when context is missing

#### Test Data
**Input Data**:
- No requirements.md file present
- Attempt to proceed to design phase

**Expected Output**:
- Clear error message about missing requirements
- Specific guidance on creating requirements.md
- System remains stable

#### Test Steps
1. [ ] Remove or rename requirements.md
2. [ ] Attempt to create design.md
3. [ ] Observe error handling behavior
4. [ ] Verify error message clarity
5. [ ] Test system recovery after adding requirements

#### Expected Results
1. [x] Clear error message displayed
2. [x] Specific recovery guidance provided
3. [x] System remains stable
4. [x] Recovery possible after adding requirements

---

## Test Execution Log

### Execution Details
- **Executed By**: [Name]
- **Execution Date**: [Date]
- **Execution Time**: [Time]
- **Test Environment**: [Environment details]

### Test Results
- **Status**: [ ] Passed [ ] Failed [ ] Blocked [ ] Skipped
- **Actual Results**: [What actually happened]
- **Deviations**: [Any deviations from expected results]
- **Issues Found**: [List of issues discovered]

### Attachments
- [ ] Screenshots
- [ ] Log files
- [ ] Generated reports
- [ ] Error messages

### Notes
[Any additional notes about the test execution]

## Test Case Maintenance

### Version History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial version | [Name] |

### Review Information
- **Last Review Date**: [Date]
- **Next Review Date**: [Date]
- **Reviewed By**: [Name]
- **Approval Status**: [ ] Approved [ ] Needs Revision

### Related Test Cases
- **Prerequisites**: [List of test cases that must pass first]
- **Dependencies**: [List of related test cases]
- **Supersedes**: [List of test cases this one replaces]

---

## Usage Instructions

1. **Copy Template**: Copy this template for each new test case
2. **Fill Sections**: Complete all relevant sections with specific test details
3. **Validate Completeness**: Ensure all required fields are filled
4. **Review**: Have test case reviewed by team members
5. **Execute**: Run test case following the documented steps
6. **Document Results**: Record actual results in execution log
7. **Maintain**: Keep test case updated as requirements change

## Common Test Case Categories

### Requirements Validation Tests
- EARS format compliance
- User story completeness
- Acceptance criteria testability
- Constraint documentation

### Design Validation Tests
- Requirements coverage
- Architecture clarity
- Component specification
- Error handling design

### Tasks Validation Tests
- Hierarchical structure
- Requirement traceability
- Implementation logic
- Optional task marking

### Implementation Validation Tests
- Context loading
- Single task focus
- Code quality
- Comprehensive summaries

### Cross-Document Consistency Tests
- Requirements-to-design mapping
- Design-to-tasks mapping
- Tasks-to-implementation mapping
- Change impact analysis

---

*This template should be used for creating comprehensive test cases for YASK system validation. Each test case should be specific, measurable, and repeatable.*