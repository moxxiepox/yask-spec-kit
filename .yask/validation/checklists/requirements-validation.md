---
date: '2025-12-28'
  description: Comprehensive checklist for validating requirements documents in the
    YASK system.
  status: active
  tags:
  - yask
  - yask/documentation
  - yask/status/active
  title: Requirements Validation Checklist
  version: 6.0.0
---

# Requirements Validation Checklist

Comprehensive checklist for validating requirements documents in the YASK system.

## Pre-Validation Setup
- [ ] **Document Accessibility**: requirements.md file exists and is readable
- [ ] **Template Compliance**: Document follows requirements-template.md structure
- [ ] **Basic Structure**: Document has Introduction and Requirements sections
- [ ] **File Encoding**: Document uses UTF-8 encoding
- [ ] **Markdown Format**: Document properly formatted in Markdown

## EARS Format Validation

### Core EARS Pattern Compliance
- [ ] **WHEN/THEN/SHALL Pattern**: All acceptance criteria use `WHEN [event] THEN [system] SHALL [response]`
- [ ] **IF/THEN/SHALL Pattern**: Conditional criteria use `IF [precondition] THEN [system] SHALL [behavior]`
- [ ] **WHERE/SHALL Pattern**: Contextual criteria use `WHERE [condition] [system] SHALL [behavior]`
- [ ] **SHALL Keyword**: All acceptance criteria include mandatory "SHALL" keyword
- [ ] **Consistent Terminology**: System references use consistent terminology throughout

### EARS Format Quality Checks
- [ ] **No Mixed Patterns**: Single requirement doesn't mix different EARS patterns inappropriately
- [ ] **Complete Events**: All WHEN clauses specify clear, actionable events
- [ ] **Specific Responses**: All SHALL clauses specify measurable, testable responses
- [ ] **Proper Grammar**: EARS sentences are grammatically correct and clear
- [ ] **No Ambiguity**: Acceptance criteria are unambiguous and specific

### Common EARS Errors to Check
- [ ] **Missing SHALL**: Acceptance criteria missing mandatory "SHALL" keyword
- [ ] **Vague Events**: WHEN clauses with unclear or non-specific events
- [ ] **Non-Testable Responses**: SHALL clauses with subjective or non-verifiable responses
- [ ] **Incomplete Conditions**: IF/WHERE clauses missing necessary conditions
- [ ] **Inconsistent System Names**: System referred to by different names in same requirement

## User Story Validation

### User Story Structure
- [ ] **Role Definition**: Each requirement has clear user or system role identified
- [ ] **Capability Statement**: User story describes specific functionality or behavior
- [ ] **Benefit Rationale**: User story includes clear value proposition or business reason
- [ ] **Complete Stories**: All requirements have corresponding user stories
- [ ] **Consistent Format**: All user stories follow same structure pattern

### User Story Quality
- [ ] **Clear Role**: Role is specific and well-defined (not generic "user")
- [ ] **Action-Oriented Capability**: Capability describes what user wants to do, not how
- [ ] **Meaningful Benefit**: Benefit clearly explains why user wants this capability
- [ ] **Business Value**: Benefits align with business objectives or user needs
- [ ] **No Implementation Details**: User stories focus on user needs, not technical solutions

### User Story Format Validation
- [ ] **Standard Format**: Stories follow "As a [role], I want [capability], so that [benefit]" format
- [ ] **Proper Grammar**: User stories are grammatically correct
- [ ] **Consistent Voice**: All user stories use consistent voice and tone
- [ ] **Appropriate Length**: User stories are concise but complete
- [ ] **No Overlap**: User stories don't duplicate functionality across requirements

## Completeness Validation

### Functional Requirements Coverage
- [ ] **Core Functionality**: All primary user capabilities documented
- [ ] **User Interactions**: User interaction patterns and workflows addressed
- [ ] **Data Requirements**: Data input, processing, and output requirements specified
- [ ] **Integration Points**: External system integration requirements documented
- [ ] **User Interface**: UI/UX requirements specified where applicable

### Non-Functional Requirements
- [ ] **Performance**: Performance requirements and constraints documented
- [ ] **Security**: Security requirements and constraints specified
- [ ] **Usability**: Usability requirements and user experience constraints
- [ ] **Reliability**: Reliability and availability requirements specified
- [ ] **Scalability**: Scalability requirements and growth constraints

### Constraints and Assumptions
- [ ] **Technical Constraints**: Technical limitations and constraints documented
- [ ] **Business Constraints**: Business rules and constraints specified
- [ ] **Resource Constraints**: Resource limitations and constraints documented
- [ ] **System Assumptions**: Key assumptions about system environment documented
- [ ] **User Assumptions**: Assumptions about user behavior and capabilities documented

### Edge Cases and Error Conditions
- [ ] **Error Scenarios**: Error conditions and failure modes addressed
- [ ] **Boundary Conditions**: Edge cases and boundary conditions considered
- [ ] **Exception Handling**: Exception scenarios and handling requirements specified
- [ ] **Recovery Scenarios**: System recovery and fallback scenarios addressed
- [ ] **Data Validation**: Input validation and data integrity requirements specified

## Testability Validation

### Objective Verification
- [ ] **Measurable Criteria**: Acceptance criteria can be measured or observed
- [ ] **Clear Success Conditions**: Pass/fail conditions are unambiguous
- [ ] **Testable Scenarios**: All acceptance criteria have corresponding test scenarios
- [ ] **Objective Language**: No subjective terms like "user-friendly" or "intuitive"
- [ ] **Quantifiable Metrics**: Performance and quality metrics are quantifiable

### Verification Methods
- [ ] **Testing Approach**: Clear approach for testing each acceptance criterion
- [ ] **Test Data**: Test data requirements and scenarios identified
- [ ] **Expected Results**: Expected outcomes and success criteria defined
- [ ] **Verification Tools**: Tools and methods for verification identified
- [ ] **Validation Process**: Process for validating requirement completion defined

## Document Quality Validation

### Structure and Organization
- [ ] **Logical Flow**: Requirements flow logically from introduction to details
- [ ] **Clear Sectioning**: Document properly divided into logical sections
- [ ] **Consistent Formatting**: Consistent formatting throughout document
- [ ] **Proper Headers**: Appropriate header hierarchy and structure
- [ ] **Scannable Content**: Content is organized for easy scanning and reference

### Content Quality
- [ ] **Clear Language**: Language is clear, concise, and professional
- [ ] **Consistent Terminology**: Technical terms used consistently throughout
- [ ] **No Jargon**: Unnecessary technical jargon avoided or explained
- [ ] **Complete Sentences**: All sentences are complete and grammatically correct
- [ ] **Professional Tone**: Professional, business-appropriate tone maintained

### Cross-Reference Validation
- [ ] **Internal References**: Internal document references are functional
- [ ] **External References**: External document references are valid
- [ ] **Link Validation**: All links and references work correctly
- [ ] **Traceability**: Clear traceability between requirements and acceptance criteria
- [ ] **Version Control**: Document version and update information included

## Traceability Validation

### Requirement Traceability
- [ ] **Unique Identification**: Each requirement has unique identifier
- [ ] **Clear Dependencies**: Dependencies between requirements clearly documented
- [ ] **Priority Levels**: Requirement priorities clearly indicated
- [ ] **Status Tracking**: Requirement status and progress tracking included
- [ ] **Change History**: Requirement change history and versioning documented

### Acceptance Criteria Traceability
- [ ] **Requirement Mapping**: Each acceptance criterion maps to specific requirement
- [ ] **Test Case Links**: Acceptance criteria link to corresponding test cases
- [ ] **Implementation Links**: Acceptance criteria link to implementation tasks
- [ ] **Design Links**: Acceptance criteria link to design components
- [ ] **Validation Links**: Acceptance criteria link to validation procedures

## Compliance Validation

### Template Compliance
- [ ] **Template Structure**: Document follows requirements-template.md structure
- [ ] **Required Sections**: All required template sections present
- [ ] **Optional Sections**: Optional template sections used appropriately
- [ ] **Placeholder Replacement**: All template placeholders properly replaced
- [ ] **Custom Sections**: Custom sections added appropriately and consistently

### Standards Compliance
- [ ] **EARS Standards**: Document complies with EARS format standards
- [ ] **User Story Standards**: User stories comply with standard format
- [ ] **Documentation Standards**: Document meets organizational documentation standards
- [ ] **Quality Standards**: Document meets quality and completeness standards
- [ ] **Review Standards**: Document ready for formal review process

## Final Validation

### Completeness Check
- [ ] **All Sections Complete**: All document sections are complete and detailed
- [ ] **No Placeholders**: No unfilled placeholders or template remnants
- [ ] **No Missing Information**: No obvious missing information or gaps
- [ ] **Ready for Review**: Document ready for stakeholder review and approval
- [ ] **Implementation Ready**: Requirements clear enough for design phase to begin

### Quality Assurance
- [ ] **Peer Review Ready**: Document ready for peer review process
- [ ] **Stakeholder Ready**: Document ready for stakeholder review
- [ ] **Approval Ready**: Document ready for formal approval process
- [ ] **Baseline Ready**: Document ready to serve as project baseline
- [ ] **Maintenance Ready**: Document structure supports future maintenance and updates

## Validation Results Documentation

### Issues Found
- [ ] **Critical Issues**: List of critical issues that must be fixed
- [ ] **Major Issues**: List of major issues that should be addressed
- [ ] **Minor Issues**: List of minor issues that could be improved
- [ ] **Suggestions**: List of suggestions for improvement
- [ ] **Best Practices**: Best practice recommendations for future requirements

### Validation Summary
- [ ] **Overall Assessment**: Overall quality assessment of requirements document
- [ ] **Compliance Score**: Compliance score with validation criteria
- [ ] **Readiness Assessment**: Assessment of readiness for next phase
- [ ] **Recommendations**: Specific recommendations for improvement
- [ ] **Next Steps**: Clear next steps for requirement refinement or approval

---

## Usage Instructions

1. **Pre-Validation**: Ensure requirements.md file exists and is accessible
2. **Systematic Validation**: Work through checklist systematically, checking each item
3. **Issue Documentation**: Document all issues found with specific line references
4. **Severity Assessment**: Assess severity of each issue (Critical, Major, Minor)
5. **Remediation**: Address issues before proceeding to design phase
6. **Re-validation**: Re-validate after making corrections
7. **Approval**: Obtain approval only after all critical and major issues resolved

## Common Issues and Solutions

### EARS Format Issues
- **Issue**: Missing "SHALL" keyword
- **Solution**: Add "SHALL" to complete EARS pattern
- **Example**: "WHEN user submits form THEN system SHALL validate input"

### User Story Issues
- **Issue**: Vague role definition
- **Solution**: Replace "user" with specific role
- **Example**: "As a registered customer" instead of "As a user"

### Completeness Issues
- **Issue**: Missing error handling requirements
- **Solution**: Add acceptance criteria for error scenarios
- **Example**: "WHEN system encounters error THEN system SHALL display error message"

### Testability Issues
- **Issue**: Subjective acceptance criteria
- **Solution**: Replace subjective terms with measurable criteria
- **Example**: "System SHALL respond within 2 seconds" instead of "System SHALL be fast"

---

*This checklist should be used in conjunction with the YASK Validation Guidelines and Testing Procedures for comprehensive requirements validation.*