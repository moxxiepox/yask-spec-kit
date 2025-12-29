---
date: '2025-12-28'
description: Spec.sh removal migration guide for YASK system
status: active
title: Spec.sh Removal Migration Guide
version: 6.0.0
tags:
  - system/yask
  - yask/type/documentation
  - yask/status/active
  - directory/active-projects
  - system/opencode
  - type/documentation
  - feature/native-gui
  - status/active

---



# Spec.sh Removal Migration Guide

## Overview
The YASK system has been updated to remove the dependency on the `spec.sh` script. This change simplifies the system by having AI agents handle all spec management directly through natural language interaction.

## What Changed

### Removed Components
- ✅ **`.yask/system/spec.sh`** - The 396-line spec management script has been removed
- ✅ **System directory** - `.yask/system/` directory is now empty and removed
- ✅ **Test references** - Updated test files to reflect spec.sh removal
- ✅ **Documentation references** - Updated all documentation to remove spec.sh mentions

### Updated Components
- ✅ **Installer scripts** - Both `install-gemini.sh` and `install-cursor.sh` no longer reference spec.sh
- ✅ **Test framework** - Updated system tests to verify AI agent functionality instead of script functionality
- ✅ **Documentation** - Updated README.md, CURSOR_INTEGRATION.md, and other docs to reflect the change

## Benefits of Removal

1. **Simplified Architecture** - No external script dependencies
2. **Direct AI Interaction** - Users interact directly with AI agents for spec management
3. **Platform Independence** - Works consistently across all platforms without bash dependencies
4. **Reduced Maintenance** - Fewer components to maintain and test
5. **Natural Workflow** - More intuitive spec creation through conversation

## Migration Steps

### For New Users
No action required. The system now works out-of-the-box with AI agents handling all spec management.

### For Existing Users
If you have existing projects using spec.sh:

1. **Continue using existing specs** - All your existing blueprint/ specifications remain fully functional
2. **Use AI agents instead** - Instead of running `spec.sh new feature-name`, simply tell your AI agent "I want to create a new specification for [feature]"
3. **No file changes needed** - Your existing spec files don't need any modifications

## Updated Workflow

### Before (with spec.sh)
```bash
# Manual script usage
./.yask/system/spec.sh new user-authentication
./.yask/system/spec.sh list
./.yask/system/spec.sh validate user-auth
```

### After (AI agent direct)
```
# Natural language interaction with AI agent
"I want to create a new specification for user authentication"
"Show me all my current specifications"
"Validate my user authentication specification"
```

## System Files Structure

### Current Structure (After Removal)
```
.yask/
├── principles.md              # Core principles and philosophy
├── patterns.md                # Document structures and validation patterns
├── process.md                 # Workflow and communication guidance
├── testing-framework.md       # Testing procedures
├── validation-guidelines.md   # Validation standards
└── templates/                 # Document templates
    ├── requirements-template.md
    ├── design-template.md
    ├── tasks-template.md
    ├── map-template.md
    └── architecture-readme-template.md
```

### Removed Structure
```
.yask/system/           # ← REMOVED
└── spec.sh            # ← REMOVED
```

## Testing Verification

The system has been tested to ensure:
- ✅ AI agents can guide users through spec creation
- ✅ All templates are accessible to agents
- ✅ Installer scripts work without spec.sh
- ✅ Documentation is updated and accurate
- ✅ No broken references remain

## Troubleshooting

### If you encounter issues:
1. **Check AI agent instructions** - Ensure the agent has access to `.yask/` files
2. **Verify file permissions** - Make sure templates are readable
3. **Restart your IDE/CLI** - Some changes require restart to take effect

### Common Questions:

**Q: Can I still create specifications?**
A: Yes, simply tell your AI agent "I want to create a new specification for [feature]" and it will guide you through the process.

**Q: Do my existing specifications still work?**
A: Absolutely. All existing blueprint/ specifications continue to work exactly as before.

**Q: How do I validate specifications?**
A: Ask your AI agent to validate a specification by name, and it will check compliance with YASK standards.

**Q: Is this a breaking change?**
A: No. This is a non-breaking change that only removes an internal dependency. The external API (interacting with AI agents) remains the same.

## Status
✅ **COMPLETED** - spec.sh dependency fully removed from YASK system

---
*Generated as part of YASK system maintenance - spec.sh removal task*