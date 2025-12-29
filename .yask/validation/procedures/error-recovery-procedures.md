---
date: '2025-12-28'
  description: Comprehensive procedures for handling validation failures and errors
    in the YASK system.
  status: active
  tags:
  - yask
  - yask/documentation
  - yask/status/active
  title: YASK Error Recovery Procedures
  version: 6.0.0
---

# YASK Error Recovery Procedures

Comprehensive procedures for handling validation failures and errors in the YASK system.

## Overview

This document provides systematic procedures for recovering from validation failures, implementation errors, and other issues that may arise during the spec-driven development process. The procedures are designed to ensure consistent, reliable error handling and recovery.

## Error Recovery Philosophy

### Core Principles
1. **Systematic Approach**: Use structured procedures rather than ad-hoc fixes
2. **Root Cause Analysis**: Identify and address underlying causes, not just symptoms
3. **Prevention Focus**: Learn from errors to prevent future occurrences
4. **Documentation**: Document all recovery actions for future reference
5. **User Communication**: Keep users informed throughout recovery process

### Recovery Hierarchy
1. **Immediate Stabilization**: Stop the error from causing further damage
2. **Context Preservation**: Preserve working state and data
3. **Root Cause Analysis**: Understand why the error occurred
4. **Solution Implementation**: Apply appropriate fixes
5. **Verification**: Ensure the fix works and doesn't introduce new issues
6. **Documentation**: Record the error and recovery for future reference

## Error Categories and Recovery Procedures

### 1. Missing Context Errors

#### Error Type: Missing Requirements Document
**Symptoms**:
- System cannot find requirements.md file
- Cannot proceed to design phase
- Validation errors about missing context

**Recovery Procedure**:
1. **Immediate Action**
   - Stop current phase progression
   - Preserve any work completed so far
   - Communicate clearly to user about missing requirements

2. **Context Assessment**
   - Verify requirements.md file location and accessibility
   - Check if file exists but is named differently
   - Assess what requirements work has been done

3. **Recovery Options**
   - **Option A**: Create requirements.md from scratch
     - Use requirements-template.md as guide
     - Work with user to capture requirements
     - Follow EARS format guidelines
   - **Option B**: Recover existing requirements
     - Locate requirements in other files
     - Consolidate into proper requirements.md
     - Validate completeness and format

4. **Verification**
   - Ensure requirements.md exists and is readable
   - Validate EARS format compliance
   - Confirm user story completeness
   - Test phase progression

5. **Documentation**
   - Record what caused the missing context
   - Document recovery steps taken
   - Note prevention measures for future

**Example Recovery Script**:
```bash
# Check for requirements file
if [ ! -f "requirements.md" ]; then
    echo "ERROR: requirements.md not found"
    echo "Cannot proceed to design phase without requirements"
    echo "Please create requirements.md using the template"
    echo "Location: .yask/templates/requirements-template.md"
    exit 1
fi
```

#### Error Type: Missing Design Document
**Symptoms**:
- System cannot find design.md file
- Cannot proceed to tasks phase
- Validation errors about missing design context

**Recovery Procedure**:
1. **Immediate Action**
   - Stop tasks phase progression
   - Verify requirements.md is complete and validated
   - Communicate missing design context to user

2. **Context Assessment**
   - Check if design work exists in other files
   - Verify requirements are complete enough for design
   - Assess design complexity and scope

3. **Recovery Options**
   - **Option A**: Create design.md from requirements
     - Load requirements.md and understand scope
     - Use design-template.md as structure guide
     - Address all requirements in design
   - **Option B**: Recover existing design work
     - Find design content in notes or other documents
     - Organize into proper design.md structure
     - Validate requirements coverage

4. **Verification**
   - Ensure design.md addresses all requirements
   - Validate architecture clarity
   - Confirm design decisions are documented
   - Test phase progression to tasks

#### Error Type: Missing Tasks Document
**Symptoms**:
- System cannot find tasks.md file
- Cannot proceed to implementation
- Validation errors about missing task breakdown

**Recovery Procedure**:
1. **Immediate Action**
   - Stop implementation phase
   - Verify both requirements.md and design.md exist
   - Communicate missing tasks context to user

2. **Context Assessment**
   - Review requirements and design for completeness
   - Assess implementation complexity
   - Check for existing task lists or notes

3. **Recovery Options**
   - **Option A**: Create tasks.md from design
     - Load requirements.md and design.md
     - Break down design components into tasks
     - Use tasks-template.md as structure guide
   - **Option B**: Recover existing task work
     - Find task breakdowns in other files
     - Organize into proper hierarchical structure
     - Validate requirement traceability

### 2. Format and Quality Errors

#### Error Type: EARS Format Violations
**Symptoms**:
- Acceptance criteria don't follow EARS format
- Missing "SHALL" keywords
- Incomplete WHEN/THEN patterns

**Recovery Procedure**:
1. **Immediate Action**
   - Identify all malformed acceptance criteria
   - Stop progression until format is corrected
   - Provide specific guidance on format issues

2. **Format Analysis**
   - Review each acceptance criterion individually
   - Identify specific format violations
   - Determine correct EARS pattern needed

3. **Correction Process**
   - **For missing SHALL**: Add "SHALL" to complete pattern
     - Before: "WHEN user submits form THEN system validates"
     - After: "WHEN user submits form THEN system SHALL validate input"
   
   - **For incomplete patterns**: Complete the EARS structure
     - Before: "IF user is authenticated"
     - After: "IF user is authenticated THEN system SHALL grant access"

   - **For vague responses**: Make responses specific and testable
     - Before: "THEN system SHALL be fast"
     - After: "THEN system SHALL respond within 2 seconds"

4. **Validation**
   - Re-run EARS format validation
   - Ensure all criteria follow proper patterns
   - Verify consistency across all requirements

**Example Correction Guide**:
```markdown
## Common EARS Format Fixes

### Missing SHALL
❌ WHEN user clicks submit THEN system validates
✅ WHEN user clicks submit THEN system SHALL validate input

### Incomplete Condition
❌ IF user is authenticated
✅ IF user is authenticated THEN system SHALL grant access

### Vague Response
❌ THEN system SHALL be user-friendly
✅ THEN system SHALL display clear error messages
```

#### Error Type: User Story Issues
**Symptoms**:
- Incomplete user stories (missing "so that")
- Vague role definitions
- Missing user stories for requirements

**Recovery Procedure**:
1. **Immediate Action**
   - Identify incomplete or missing user stories
   - Stop progression until stories are complete
   - Provide guidance on user story structure

2. **Story Analysis**
   - Review each requirement for user story
   - Identify missing components (role, capability, benefit)
   - Assess story quality and clarity

3. **Correction Process**
   - **Add missing stories**: Create complete user stories
     - Format: "As a [role], I want [capability], so that [benefit]"
   
   - **Fix incomplete stories**: Complete missing parts
     - Before: "As a user, I want to login"
     - After: "As a registered user, I want to log into the system, so that I can access my account"
   
   - **Improve vague roles**: Make roles specific
     - Before: "As a user"
     - After: "As a registered customer" or "As a system administrator"

4. **Validation**
   - Ensure all requirements have user stories
   - Verify story completeness and clarity
   - Check for consistent formatting

#### Error Type: Traceability Issues
**Symptoms**:
- Requirements not referenced in design
- Tasks missing requirement references
- Broken cross-document links

**Recovery Procedure**:
1. **Immediate Action**
   - Identify broken traceability links
   - Stop progression until traceability is fixed
   - Map out what links are missing

2. **Traceability Analysis**
   - Create requirements list from requirements.md
   - Check design.md for requirement references
   - Check tasks.md for requirement references
   - Identify gaps in both directions

3. **Recovery Process**
   - **Add missing design references**
     - Map each requirement to design components
     - Add explicit requirement references in design
     - Ensure bidirectional traceability
   
   - **Add missing task references**
     - Add `_Requirements: [references]` to each task
     - Ensure all requirements have corresponding tasks
     - Verify task breakdown completeness

4. **Validation**
   - Run traceability validation script
   - Verify complete requirements coverage
   - Test cross-document reference functionality

### 3. Implementation Errors

#### Error Type: Code Quality Issues
**Symptoms**:
- Code doesn't follow project standards
- Missing error handling
- Poor code structure or organization

**Recovery Procedure**:
1. **Immediate Action**
   - Stop implementation progression
   - Assess code quality issues
   - Identify specific problems

2. **Quality Analysis**
   - Review code against project standards
   - Check for missing error handling
   - Assess code structure and organization
   - Identify security or performance issues

3. **Correction Process**
   - **Apply coding standards**
     - Fix naming conventions
     - Add proper documentation
     - Organize code structure
   
   - **Add error handling**
     - Implement try-catch blocks
     - Add input validation
     - Provide user-friendly error messages
   
   - **Improve code quality**
     - Refactor complex functions
     - Remove code duplication
     - Add unit tests

4. **Verification**
   - Run code quality checks
   - Test error handling scenarios
   - Verify functionality still works
   - Check performance impact

#### Error Type: Context Loading Failures
**Symptoms**:
- Implementation doesn't load required context
- Missing understanding of requirements/design
- Implementation doesn't match specifications

**Recovery Procedure**:
1. **Immediate Action**
   - Stop implementation
   - Verify all spec documents are accessible
   - Assess what context is missing

2. **Context Recovery**
   - **Reload requirements.md**
     - Read and understand all requirements
     - Verify EARS format compliance
     - Note acceptance criteria details
   
   - **Reload design.md**
     - Understand architecture and components
     - Review design decisions and rationale
     - Note interface specifications
   
   - **Reload tasks.md**
     - Understand task breakdown
     - Note requirement references
     - Verify task scope and boundaries

3. **Implementation Correction**
   - Restart implementation with full context
   - Ensure implementation addresses requirements
   - Verify design architecture is followed
   - Maintain task focus and scope

4. **Verification**
   - Test implementation against requirements
   - Verify design compliance
   - Check task completion criteria

### 4. System and Environment Errors

#### Error Type: Dependency Issues
**Symptoms**:
- Missing required tools or libraries
- Version incompatibilities
- Installation failures

**Recovery Procedure**:
1. **Immediate Action**
   - Stop implementation
   - Identify missing dependencies
   - Assess impact on current task

2. **Dependency Analysis**
   - List all required tools and libraries
   - Check current installations
   - Identify version requirements
   - Assess installation options

3. **Recovery Process**
   - **Local Installation** (Preferred)
     - Install tools locally in project directory
     - Use package managers (npm, pip, etc.)
     - Verify installation success
   
   - **Global Installation** (When necessary)
     - Get user confirmation for global install
     - Install system-wide tools
     - Verify system integration
   
   - **Alternative Solutions**
     - Find alternative tools
     - Use online services
     - Implement workarounds

4. **Verification**
   - Test dependency functionality
   - Verify version compatibility
   - Check integration with project
   - Document dependency requirements

#### Error Type: File System Issues
**Symptoms**:
- File permission problems
- Disk space issues
- File corruption or loss

**Recovery Procedure**:
1. **Immediate Action**
   - Stop all file operations
   - Assess extent of file system issues
   - Preserve working data

2. **Issue Assessment**
   - Check file permissions and accessibility
   - Verify disk space availability
   - Identify corrupted or missing files
   - Assess data loss impact

3. **Recovery Process**
   - **Permission Issues**
     - Fix file and directory permissions
     - Ensure read/write access
     - Verify ownership settings
   
   - **Space Issues**
     - Clean up temporary files
     - Move large files to appropriate locations
     - Free up disk space
   
   - **Corruption Recovery**
     - Restore from backups
     - Recover from version control
     - Rebuild corrupted files

4. **Verification**
   - Test file accessibility
   - Verify data integrity
   - Check system stability
   - Document recovery actions

## Recovery Decision Matrix

### Error Severity Assessment
| Severity | Impact | Recovery Time | Action Required |
|----------|--------|---------------|-----------------|
| **Critical** | System unusable | Immediate | Stop all operations, fix immediately |
| **High** | Major functionality broken | Within hour | Pause operations, fix before proceeding |
| **Medium** | Some functionality affected | Same day | Fix when convenient, document issue |
| **Low** | Minor issues | Next cycle | Note for future improvement |

### Recovery Priority Matrix
| Error Type | Severity | Recovery Approach | User Communication |
|------------|----------|-------------------|-------------------|
| Missing Context | Critical | Immediate recreation | High priority, detailed guidance |
| Format Violations | High | Systematic correction | Clear examples and templates |
| Quality Issues | Medium | Gradual improvement | Suggestions and best practices |
| Environment Issues | High | Technical resolution | Technical details and options |

## Recovery Documentation Template

### Error Report Template
```markdown
# Error Recovery Report

## Error Information
- **Date/Time**: [When error occurred]
- **Error Type**: [Category of error]
- **Severity**: [Critical/High/Medium/Low]
- **Phase Affected**: [Requirements/Design/Tasks/Implementation]

## Error Description
- **Symptoms**: [What was observed]
- **Impact**: [How it affected the system]
- **Root Cause**: [Why it happened]

## Recovery Actions
- **Immediate Actions**: [What was done first]
- **Analysis Steps**: [How the problem was analyzed]
- **Solution Implementation**: [How it was fixed]
- **Verification**: [How the fix was validated]

## Prevention Measures
- **Root Cause Prevention**: [How to prevent recurrence]
- **Early Detection**: [How to catch this earlier]
- **Process Improvements**: [How to improve the process]

## Lessons Learned
- **Key Insights**: [What was learned]
- **Process Changes**: [What should change]
- **Training Needs**: [What training is needed]
```

## Recovery Tools and Scripts

### Automated Recovery Scripts
```bash
#!/bin/bash
# Auto-recovery script for common YASK errors

# Check for missing files
check_required_files() {
    local required_files=("requirements.md" "design.md" "tasks.md")
    local missing_files=()
    
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            missing_files+=("$file")
        fi
    done
    
    if [ ${#missing_files[@]} -gt 0 ]; then
        echo "ERROR: Missing required files: ${missing_files[*]}"
        echo "Please create these files before proceeding"
        return 1
    fi
    
    return 0
}

# Check EARS format
validate_ears_format() {
    local ears_patterns=("WHEN.*THEN.*SHALL" "IF.*THEN.*SHALL" "WHERE.*SHALL")
    local issues_found=0
    
    for pattern in "${ears_patterns[@]}"; do
        if ! grep -E "$pattern" requirements.md > /dev/null; then
            echo "WARNING: No EARS pattern found: $pattern"
            ((issues_found++))
        fi
    done
    
    return $issues_found
}

# Main recovery check
main() {
    echo "Running YASK error recovery check..."
    
    if ! check_required_files; then
        exit 1
    fi
    
    if ! validate_ears_format; then
        echo "EARS format issues found. Please review requirements.md"
        exit 1
    fi
    
    echo "No critical errors found. System appears healthy."
}
```

### Recovery Verification Script
```bash
#!/bin/bash
# Verify that recovery actions were successful

verify_recovery() {
    local test_name="$1"
    local test_command="$2"
    
    echo "Testing: $test_name"
    if eval "$test_command"; then
        echo "✓ PASS: $test_name"
        return 0
    else
        echo "✗ FAIL: $test_name"
        return 1
    fi
}

# Run verification tests
run_verification() {
    local failed_tests=0
    
    verify_recovery "Requirements file exists" "[ -f requirements.md ]" || ((failed_tests++))
    verify_recovery "Design file exists" "[ -f design.md ]" || ((failed_tests++))
    verify_recovery "Tasks file exists" "[ -f tasks.md ]" || ((failed_tests++))
    verify_recovery "EARS format valid" "grep -q 'WHEN.*THEN.*SHALL' requirements.md" || ((failed_tests++))
    verify_recovery "User stories present" "grep -q 'As a.*I want.*so that' requirements.md" || ((failed_tests++))
    
    if [ $failed_tests -eq 0 ]; then
        echo "All verification tests passed!"
        return 0
    else
        echo "$failed_tests verification tests failed"
        return 1
    fi
}
```

## Best Practices for Error Recovery

### Prevention Strategies
1. **Regular Validation**: Run validation checks frequently
2. **Backup Strategy**: Maintain backups of important documents
3. **Template Usage**: Always use provided templates
4. **Incremental Progress**: Make small, validated changes
5. **Documentation**: Keep detailed records of decisions

### Communication Guidelines
1. **Clear Error Messages**: Provide specific, actionable error descriptions
2. **Recovery Guidance**: Offer step-by-step recovery instructions
3. **Progress Updates**: Keep users informed of recovery progress
4. **Learning Focus**: Use errors as learning opportunities
5. **Positive Tone**: Maintain encouraging, solution-focused communication

### Quality Assurance
1. **Root Cause Analysis**: Always identify underlying causes
2. **Comprehensive Testing**: Verify fixes don't introduce new issues
3. **Documentation**: Record all recovery actions and outcomes
4. **Process Improvement**: Use errors to improve processes
5. **Knowledge Sharing**: Share learnings with team members

## Conclusion

Effective error recovery is essential for maintaining productivity and quality in the YASK system. By following these systematic procedures, teams can quickly recover from errors while learning to prevent similar issues in the future.

The key to successful error recovery is:
- **Immediate response** to prevent further issues
- **Systematic analysis** to understand root causes
- **Clear communication** with all stakeholders
- **Thorough verification** to ensure fixes work
- **Continuous improvement** to prevent recurrence

Regular review and updates of these procedures will ensure they remain effective as the YASK system evolves.