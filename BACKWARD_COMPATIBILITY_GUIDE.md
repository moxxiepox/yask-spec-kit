# Backward Compatibility Guide

## Overview

The Backward Compatibility module provides comprehensive support for existing documents, workflows, and templates while enabling smooth migration to the refactored YASK framework version 3.0.

## Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              Backward Compatibility System                  │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      DocumentCompatibilitySystem                    │    │
│  ├─────────────────────────────────────────────────────┤    │
│  │  • Format Version Detection                         │    │
│  │  • Compatibility Analysis                           │    │
│  │  • Document Migration                                │    │
│  │  • Migration Validation                              │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      WorkflowCompatibilitySystem                    │    │
│  ├─────────────────────────────────────────────────────┤    │
│  │  • Workflow Analysis                                 │    │
│  │  • Workflow Preservation                             │    │
│  │  • Workflow Migration                                │    │
│  │  • Workflow Validation                               │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │      IntegrationTestingSystem                       │    │
│  ├─────────────────────────────────────────────────────┤    │
│  │  • Format Detection Tests                            │    │
│  │  • Compatibility Analysis Tests                      │    │
│  │  • Migration Tests                                   │    │
│  │  • Validation Tests                                  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Version Migration Guide

### Version 1.0 → 2.0 → 3.0

#### Version 1.0 (Original YASK)
- **Features**: Basic templates, simple cross-references
- **Cross-Reference Pattern**: `#[[file:requirements.md]]#[Overview]`
- **Template Structure**: Individual template files
- **Compatibility**: Incompatible with versions 2.0 and 3.0

#### Version 2.0 (Enhanced YASK)
- **Features**: Consolidated templates, optimized context
- **Cross-Reference Pattern**: `#[[requirements.md]]#[Overview]`
- **Template Structure**: Consolidated templates
- **Compatibility**: Incompatible with version 1.0, compatible with 3.0

#### Version 3.0 (Refactored YASK)
- **Features**: Performance optimized, backward compatible, smart caching
- **Cross-Reference Pattern**: `#[[requirements.md]]#[Overview]`
- **Template Structure**: Modular templates with inheritance
- **Compatibility**: Incompatible with version 1.0, compatible with 2.0

### Migration Path

```
Version 1.0
    │
    ├── Direct Migration (Recommended)
    │   └──→ Version 3.0
    │       • Automatic pattern conversion
    │       • Performance optimizations
    │       • Smart caching enabled
    │
    └── Two-Step Migration
        ├──→ Version 2.0
        │   • Pattern conversion
        │   • Template consolidation
        │
        └──→ Version 3.0
            • Performance optimizations
            • Smart caching enabled
```

## Document Format Compatibility Matrix

| Feature | Version 1.0 | Version 2.0 | Version 3.0 |
|---------|-------------|-------------|-------------|
| Basic Templates | ✓ | ✓ | ✓ |
| Consolidated Templates | ✗ | ✓ | ✓ |
| Template Inheritance | ✗ | ✗ | ✓ |
| Old Cross-References | ✓ | ✗ | ✗ (auto-convert) |
| New Cross-References | ✗ | ✓ | ✓ |
| Smart Caching | ✗ | ✗ | ✓ |
| Performance Optimization | ✗ | ✗ | ✓ |
| EARS Format Validation | ✓ | ✓ | ✓ |
| Quality Gates | ✓ | ✓ | ✓ |

## Migration Workflow

### Pre-Migration Checklist

- [ ] **Backup Current System**
  - Create backup of `.yask/` directory
  - Backup all document files (requirements.md, design.md, tasks.md)
  - Document current system configuration

- [ ] **Analyze Current Documents**
  - Identify all document versions
  - Count cross-reference patterns
  - List custom templates

- [ ] **Review Migration Requirements**
  - Determine migration complexity (low/medium/high)
  - Identify potential issues
  - Plan migration timeline

### Migration Procedures

#### Step 1: Analyze Compatibility

```python
from pathlib import Path
from .yask.core.backward_compatibility import DocumentCompatibilitySystem

# Initialize compatibility system
project_root = Path(".")
compatibility_system = DocumentCompatibilitySystem(project_root)

# Analyze document compatibility
file_path = project_root / "requirements.md"
info = compatibility_system.analyze_compatibility(file_path)

print(f"Format Version: {info.format_version}")
print(f"Is Compatible: {info.is_compatible}")
print(f"Migration Required: {info.migration_required}")
print(f"Complexity: {info.migration_complexity}")

if info.issues:
    print("\nIssues:")
    for issue in info.issues:
        print(f"  - {issue}")

if info.recommendations:
    print("\nRecommendations:")
    for rec in info.recommendations:
        print(f"  - {rec}")
```

#### Step 2: Create Backup

```python
from .yask.core.backward_compatibility import WorkflowCompatibilitySystem

# Initialize workflow system
workflow_system = WorkflowCompatibilitySystem(project_root)

# Define workflow files
workflow_files = [
    project_root / "requirements.md",
    project_root / "design.md",
    project_root / "tasks.md",
]

# Create backup
backup_dir = project_root / ".yask" / "migration_backup"
success = workflow_system.preserve_workflow(workflow_files, backup_dir)

if success:
    print(f"Backup created at: {backup_dir}")
else:
    print("Backup creation failed")
```

#### Step 3: Migrate Documents

```python
# Migrate individual document
result = compatibility_system.migrate_document(file_path)

if result.success:
    print(f"Migration successful: {result.target_file}")
    if result.warnings:
        print("\nWarnings:")
        for warning in result.warnings:
            print(f"  - {warning}")
else:
    print("Migration failed")
    if result.issues:
        print("\nIssues:")
        for issue in result.issues:
            print(f"  - {issue}")
```

#### Step 4: Validate Migration

```python
# Validate migrated document
is_valid, errors = compatibility_system.validate_migrated_document(file_path)

if is_valid:
    print("Document validation passed")
else:
    print("Document validation failed")
    for error in errors:
        print(f"  - {error}")
```

#### Step 5: Run Integration Tests

```python
from .yask.core.backward_compatibility import IntegrationTestingSystem

# Initialize integration testing system
integration_system = IntegrationTestingSystem(project_root)

# Run compatibility tests
results = integration_system.run_compatibility_tests(workflow_files)

print(f"Total Tests: {results['total_tests']}")
print(f"Passed: {results['passed_tests']}")
print(f"Failed: {results['failed_tests']}")
print(f"Overall: {'PASSED' if results['overall_passed'] else 'FAILED'}")

# Generate test report
report = integration_system.generate_test_report()
print("\n" + report)
```

### Command-Line Migration

```bash
# Run compatibility tests
python .yask/core/backward-compatibility.py --project-root . --test

# Migrate documents
python .yask/core/backward-compatibility.py --project-root . --migrate
```

## Rollback Procedures

### Automatic Rollback

If migration fails, the system automatically preserves the original files:

```python
# Check if backup exists
backup_dir = project_root / ".yask" / "migration_backup"

if backup_dir.exists():
    print("Backup available for rollback")
```

### Manual Rollback

```bash
# Restore from backup
cp -r .yask/migration_backup/.yask ./
cp .yask/migration_backup/requirements.md ./
cp .yask/migration_backup/design.md ./
cp .yask/migration_backup/tasks.md ./
```

### Rollback Validation

After rollback, verify system functionality:

```python
# Validate rollback
is_valid, errors = compatibility_system.validate_migrated_document(file_path)

if not is_valid:
    print("Rollback validation failed")
    for error in errors:
        print(f"  - {error}")
```

## Troubleshooting Common Migration Issues

### Issue 1: Old Cross-Reference Patterns

**Symptoms**: Documents contain old `#[[file:requirements.md]]#[Overview]` patterns

**Solution**:
```python
# The migration tool automatically converts old patterns
result = compatibility_system.migrate_document(file_path)

# Verify conversion
with open(file_path, 'r') as f:
    content = f.read()
    if "#[[file:" in content:
        print("Old patterns still present - manual conversion needed")
```

### Issue 2: Template Inheritance Errors

**Symptoms**: Template inheritance fails after migration

**Solution**:
```python
# Check template structure
from .yask.core.performance_optimizer import TemplatePerformanceOptimizer

template_optimizer = TemplatePerformanceOptimizer(
    project_root / ".yask" / "templates"
)

# Validate template
is_valid, errors = template_optimizer.validate_template_optimized(
    "requirements-template-consolidated.md"
)

if not is_valid:
    print("Template validation errors:")
    for error in errors:
        print(f"  - {error}")
```

### Issue 3: Missing Required Sections

**Symptoms**: Documents missing required sections after migration

**Solution**:
```python
# Check for required sections
required_sections = ["Requirements", "Design", "Tasks"]

with open(file_path, 'r') as f:
    content = f.read()

for section in required_sections:
    if section not in content:
        print(f"Missing required section: {section}")
```

### Issue 4: Version Detection Failures

**Symptoms**: System cannot detect document version

**Solution**:
```python
# Manually specify version
version = compatibility_system.detect_format_version(file_path)

if version == "1.0":
    print("Document is version 1.0 - migration required")
elif version == "2.0":
    print("Document is version 2.0 - migration to 3.0 recommended")
else:
    print("Document is version 3.0 - no migration needed")
```

## Compatibility Modes

### Legacy Mode

Run system in legacy mode for version 1.0 documents:

```python
# Use legacy mode for old documents
compatibility_mode = CompatibilityMode.LEGACY

# System will use old processing methods
# No performance optimizations
# Old cross-reference patterns supported
```

### Migrated Mode

Run system in migrated mode for version 3.0 documents:

```python
# Use migrated mode for new documents
compatibility_mode = CompatibilityMode.MIGRATED

# System will use optimized processing
# Performance optimizations enabled
# New cross-reference patterns used
```

### Hybrid Mode

Run system in hybrid mode for mixed documents:

```python
# Use hybrid mode for mixed documents
compatibility_mode = CompatibilityMode.HYBRID

# System will detect version per document
# Apply appropriate processing
# Support both old and new patterns
```

## Best Practices

### 1. Always Backup Before Migration

```python
# Create comprehensive backup
backup_dir = project_root / f".yask-backup-{datetime.now().strftime('%Y%m%d')}"
backup_dir.mkdir(parents=True, exist_ok=True)

# Backup all YASK files
shutil.copytree(project_root / ".yask", backup_dir / ".yask")
for doc in ["requirements.md", "design.md", "tasks.md"]:
    shutil.copy2(project_root / doc, backup_dir / doc)
```

### 2. Test Migration on Copy First

```python
# Create test copy
test_dir = project_root / "migration-test"
shutil.copytree(project_root, test_dir)

# Test migration on copy
test_system = DocumentCompatibilitySystem(test_dir)
result = test_system.migrate_document(test_dir / "requirements.md")

# Verify before migrating original
if result.success:
    print("Test migration successful - safe to proceed")
else:
    print("Test migration failed - review issues")
```

### 3. Validate After Each Step

```python
# Validate after migration
is_valid, errors = compatibility_system.validate_migrated_document(file_path)

if not is_valid:
    print("Migration validation failed - review errors")
    for error in errors:
        print(f"  - {error}")
    # Consider rollback
```

### 4. Monitor Performance After Migration

```python
from .yask.core.performance_optimizer import SystemPerformanceOptimizer

# Monitor performance
optimizer = SystemPerformanceOptimizer(project_root)
summary = optimizer.get_performance_summary()

print(f"Performance improvement: {summary['average_improvement']}")
print(f"Target met: {summary['target_met']}")
```

## API Reference

### DocumentCompatibilitySystem

#### Methods

- `detect_format_version(file_path: Path) -> str`
  - Detect document format version
  - Returns version string ("1.0", "2.0", "3.0")

- `analyze_compatibility(file_path: Path) -> DocumentCompatibilityInfo`
  - Analyze document compatibility
  - Returns compatibility information

- `migrate_document(source_file: Path, target_file: Optional[Path] = None) -> MigrationResult`
  - Migrate document to current format
  - Returns migration result

- `validate_migrated_document(file_path: Path) -> Tuple[bool, List[str]]`
  - Validate migrated document
  - Returns (is_valid, errors)

### WorkflowCompatibilitySystem

#### Methods

- `analyze_workflow_compatibility(workflow_files: List[Path]) -> Dict[str, Any]`
  - Analyze workflow compatibility
  - Returns analysis results

- `preserve_workflow(workflow_files: List[Path], backup_dir: Path) -> bool`
  - Preserve workflow before migration
  - Returns success status

- `migrate_workflow(workflow_files: List[Path], backup_dir: Optional[Path] = None) -> Dict[str, Any]`
  - Migrate entire workflow
  - Returns migration results

- `validate_migrated_workflow(workflow_files: List[Path]) -> Dict[str, Any]`
  - Validate migrated workflow
  - Returns validation results

### IntegrationTestingSystem

#### Methods

- `run_compatibility_tests(workflow_files: List[Path]) -> Dict[str, Any]`
  - Run comprehensive compatibility tests
  - Returns test results

- `generate_test_report() -> str`
  - Generate comprehensive test report
  - Returns formatted report

## Related Documentation

- [Migration Guide Enhanced](MIGRATION_GUIDE_ENHANCED.md)
- [YASK Refactor Architecture](YASK_REFACTOR_ARCHITECTURE.md)
- [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md)
- [API Reference](API_REFERENCE.md)
