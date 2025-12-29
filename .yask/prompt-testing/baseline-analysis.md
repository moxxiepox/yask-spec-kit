---
date: '2025-12-28'
description: YASK baseline analysis of current distributed approach
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: YASK Baseline Analysis - Current Distributed Approach
version: 6.0.0
---

# YASK Baseline Analysis: Current Distributed Approach

## Current System Architecture

### Distributed Files (Current Approach)
The YASK system currently uses 4 separate files for context:

1. **spec-dev-agent.md** (188 lines)
   - Main agent instructions and mission
   - Core axioms and operational rules
   - Process workflow and phase execution
   - Communication patterns and quality standards

2. **principles.md** (124 lines)
   - Core philosophical foundations
   - System rules and philosophy
   - Human-AI collaboration guidelines
   - Quality standards and best practices

3. **patterns.md** (609 lines)
   - Document structures and templates
   - EARS format specifications
   - Task hierarchy patterns
   - Cross-reference validation
   - Pseudocode fallback patterns

4. **process.md** (341 lines)
   - Strategic approach and decision logic
   - Phase execution procedures
   - Self-sufficiency framework
   - Communication strategy
   - Error recovery patterns

### Current Context Loading Strategy
- **Phase-Specific**: Load existing specs + MUST READ corresponding template
- **Complex Projects**: Load map.md and architecture templates when present
- **Document References**: Follow #[[file:]] links and cross-references
- **Template Priority**: ALWAYS load actual template files

### Performance Characteristics
- **Strengths**: Modular, focused content, clear separation of concerns
- **Weaknesses**: Multiple file loading overhead, potential context fragmentation
- **Context Efficiency**: Streamlined for AI consumption but requires multiple reads

## Identified Issues

### Centralized Prompt Problems
1. **'Collage' Approach**: Concatenating all files into single prompt
   - Should perform identically but shows degraded results
   - Particularly problematic with models having sub-par instruction adherence
   - Context comprehension degradation observed

2. **'Jigsaw' Approach**: Restructured centralized format
   - Initial versions created but need refinement
   - Format and wording optimization required
   - Results and adherence validation needed

3. **Paradoxical Behavior**: 
   - 4 separate files with redundancies improve functionality
   - Even when loaded at secondary point, performance is better
   - Suggests something about file boundaries aids comprehension

## Research Questions

1. **Why does file separation improve performance?**
   - Cognitive load distribution?
   - Attention anchoring?
   - Context boundary effects?

2. **What causes centralized prompt degradation?**
   - Information density?
   - Instruction adherence issues?
   - Context window management?

3. **How can we optimize centralized approaches?**
   - Better formatting strategies?
   - Structural improvements?
   - Hybrid approaches?

## Testing Framework Requirements

### Performance Metrics
- **Context Comprehension**: Ability to understand and apply system rules
- **Instruction Adherence**: Following EARS format, task hierarchy, etc.
- **Output Quality**: Quality of generated specifications and code
- **Consistency**: Cross-document consistency and traceability
- **Error Recovery**: Handling of edge cases and recovery strategies

### Test Scenarios
- Requirements generation with EARS format
- Design document creation with architecture decisions
- Task breakdown with hierarchical structure
- Implementation guidance with context loading
- Cross-document consistency validation
- Error recovery and fallback procedures

### Model Comparison
- High-adherence models (GPT-4, Claude)
- Medium-adherence models (GPT-3.5, Gemini Pro)
- Lower-adherence models (smaller models)

## Next Steps
1. Create centralized prompt variations
2. Build automated testing framework
3. Design performance measurement system
4. Test across different models and scenarios
5. Analyze results and optimize approaches