---
date: '2025-12-28'
description: YASK prompt performance testing framework for centralized vs distributed approaches
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: YASK Prompt Performance Testing Framework
version: 6.0.0
---

# YASK Prompt Performance Testing Framework

## Overview
This framework tests and optimizes centralized vs distributed prompt approaches for the YASK spec-driven development system.

## Current Issues
- 'Collage' centralized prompt produces worse results in models with sub-par instruction adherence
- Results degrade versus central+3 instruction method (distributed approach)
- 'Jigsaw' centralized prompt needs refinement
- Odd behavior: 4 different files with redundancies improve functionality even when loaded at secondary point
- 'Collage' centralized prompt should perform identically but doesn't

## Testing Approach
1. **Baseline Analysis**: Document current distributed approach performance
2. **Centralized Variants**: Test 'collage' and 'jigsaw' centralized prompts
3. **Hybrid Approaches**: Test combinations and optimizations
4. **Model Comparison**: Test across different AI models
5. **Performance Metrics**: Measure context comprehension, instruction adherence, output quality

## Test Scenarios
- Requirements generation
- Design document creation
- Task breakdown
- Implementation guidance
- Cross-document consistency
- Error recovery

## Deliverables
- Performance comparison results
- Optimized prompt recommendations
- Testing framework for ongoing validation
- Documentation of findings and best practices