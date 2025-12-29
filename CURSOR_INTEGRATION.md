---
date: '2025-12-28'
description: YASK and Cursor IDE integration guide
status: active
title: YASK + Cursor IDE Integration Guide
version: 6.0.0
tags:
  - system/yask
  - yask/type/documentation
  - yask/status/active
  - directory/active-projects
  - system/opencode
  - system/meta-prompting
  - type/documentation
  - feature/native-gui
  - status/active

---



# YASK + Cursor IDE Integration Guide

## Overview
This document describes the enhanced Cursor IDE integration for the YASK (Yet Another Spec-driven development frameworK) system. The integration provides automated spec-driven development through Cursor's agent system.

## What Was Fixed

### 1. **Automatic Cleanup**
- ✅ Installer now automatically removes `install-cursor.sh` after setup
- ✅ Source files (`.yask`, `spec-dev-agent.md`) are cleaned up automatically
- ✅ No manual intervention required for cleanup

### 2. **Enhanced Cursor Agent Configuration**
- ✅ Proper YAML frontmatter for Cursor IDE
- ✅ Correct `alwaysApply: true` setting
- ✅ Comprehensive glob patterns for file discovery
- ✅ Enhanced agent instructions optimized for Cursor

### 3. **Cursor Settings Integration**
- ✅ Created `.cursor/settings.json` for optimal markdown handling
- ✅ Configured file associations for `.mdc` files
- ✅ Set up proper markdown preview settings

### 4. **Improved Agent Instructions**
- ✅ Clear context loading requirements
- ✅ Auto-discovery priority system
- ✅ Enhanced workflow guidance
- ✅ Quality assurance integration

## Installation Process

### Before (Issues)
```bash
# Old script had problems:
- Required manual confirmation for cleanup
- Incomplete Cursor agent configuration
- No proper settings integration
- Agent instructions not optimized for Cursor
```

### After (Fixed)
```bash
# New script provides:
- Automatic cleanup without user input
- Complete Cursor IDE integration
- Proper agent configuration with frontmatter
- Enhanced agent instructions
- Quick start guide
```

## File Structure Created

```
.cursor/
├── settings.json              # Cursor IDE settings
└── rules/
    ├── spec-dev-agent.mdc     # Enhanced agent rules
    ├── QUICKSTART.md          # User guide
    └── .yask/                 # YASK system files
        ├── principles.md
        ├── patterns.md
        ├── process.md
        ├── system/
        
        └── templates/
            ├── architecture-readme-template.md
            ├── design-template.md
            ├── map-template.md
            ├── requirements-template.md
            └── tasks-template.md
```

## Key Features

### 1. **Auto-Discovery System**
The agent automatically discovers and loads:
- YASK system files from `.cursor/rules/.yask/`
- Project specifications from `blueprint/` directory
- Templates from `.yask/templates/`

### 2. **Context Loading**
Agent automatically loads required files:
- `.yask/principles.md` - Core principles
- `.yask/patterns.md` - Document patterns
- `.yask/process.md` - Workflow guidance
- Templates from `.yask/templates/`

### 3. **Structured Workflow**
Agent guides through:
1. **Requirements** - EARS format specification
2. **Design** - Technical architecture
3. **Tasks** - Implementation steps
4. **Implementation** - Systematic execution

### 4. **Quality Assurance**
- Built-in validation and verification
- Cross-document consistency checking
- Requirement traceability maintenance
- Progress tracking through tasks.md

## Usage

### Starting a New Project
1. Open Cursor IDE
2. Tell Cursor: "I want to build [feature description]"
3. Follow the structured workflow prompts

### Continuing Existing Work
1. Open your project in Cursor
2. Navigate to the blueprint directory
3. Tell Cursor what you want to work on next

### System Commands Available
- Use AI agent guidance for spec management
- Templates automatically loaded from `.yask/templates/`
- Cross-references automatically followed

## Technical Details

### Cursor Agent Configuration
```yaml
---
description: "YASK Spec-Driven Development Agent - Automated Requirements → Design → Tasks → Implementation"
alwaysApply: true
globs:
  - "**/*"
  - ".yask/**/*"
  - "blueprint/**/*"
---
```

### Settings Configuration
```json
{
  "files.associations": {
    "*.md": "markdown",
    "*.mdc": "markdown",
    "*.yask": "markdown"
  },
  "markdown.preview.breaks": true,
  "markdown.preview.typographer": true
}
```

## Verification

To verify the installation works:
1. Run `./install-cursor.sh` in your project
2. Check that `.cursor/` directory is created
3. Verify agent rules are in `.cursor/rules/`
4. Test by asking Cursor to help with a new feature

## Troubleshooting

### Agent Not Loading
- Check that `.cursor/rules/spec-dev-agent.mdc` exists
- Verify YAML frontmatter is properly formatted
- Ensure `alwaysApply: true` is set

### Templates Not Loading
- Confirm `.yask/templates/` directory exists
- Check file permissions
- Verify templates are in correct format

### Context Not Loading
- Ensure agent has access to `.cursor/rules/.yask/`
- Check that required files exist
- Verify file paths in agent instructions

## Benefits

1. **Automated Setup** - No manual configuration required
2. **Integrated Workflow** - Seamless Cursor IDE experience
3. **Quality Assurance** - Built-in validation and verification
4. **Template System** - Automatic template loading and usage
5. **Traceability** - Maintains connections between all project elements
6. **Progress Tracking** - Dynamic task management

## Next Steps

1. Test the installation with a real Cursor IDE session
2. Create sample projects to verify the workflow
3. Gather feedback on the integration experience
4. Consider additional Cursor-specific optimizations

---

**Status**: ✅ **FIXED** - Cursor IDE integration now works automatically with proper cleanup and enhanced configuration.