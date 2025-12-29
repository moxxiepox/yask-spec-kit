# YASK 3.0 API Reference

**Date**: 2025-12-29
**Version**: 3.0.0
**Status**: Complete

---

## Overview

This API reference provides comprehensive documentation for all YASK 3.0 modules, including method signatures, parameters, return types, and usage examples.

---

## Table of Contents

1. [Core Modules](#core-modules)
2. [Integration Modules](#integration-modules)
3. [Validation Modules](#validation-modules)
4. [Testing Modules](#testing-modules)
5. [Workflow Modules](#workflow-modules)

---

## Core Modules

### Performance Optimizer

**Module**: `.yask/core/performance-optimizer.py`

#### Class: PerformanceOptimizer

```python
class PerformanceOptimizer:
    """Main performance optimization system for YASK framework"""
    
    def __init__(self, project_root: Path, config: Optional[Dict[str, Any]] = None):
        """
        Initialize performance optimizer
        
        Args:
            project_root: Root directory of the project
            config: Optional configuration dictionary
        """
```

#### Methods

##### optimize_context_loading()

```python
def optimize_context_loading(self) -> Dict[str, Any]:
    """
    Optimize context loading performance
    
    Returns:
        Dictionary containing optimization results:
        - 'improvement_percentage': float - Performance improvement percentage
        - 'before_time': float - Loading time before optimization
        - 'after_time': float - Loading time after optimization
        - 'recommendations': List[str] - Optimization recommendations
    """
```

##### optimize_template_processing()

```python
def optimize_template_processing(self) -> Dict[str, Any]:
    """
    Optimize template processing performance
    
    Returns:
        Dictionary containing optimization results
    """
```

##### benchmark_performance()

```python
def benchmark_performance(self) -> Dict[str, Any]:
    """
    Benchmark current system performance
    
    Returns:
        Dictionary containing performance metrics:
        - 'context_loading_time': float
        - 'template_processing_time': float
        - 'validation_time': float
        - 'cross_reference_time': float
        - 'overall_time': float
    """
```

### Backward Compatibility

**Module**: `.yask/core/backward-compatibility.py`

#### Class: BackwardCompatibilityManager

```python
class BackwardCompatibilityManager:
    """Manages backward compatibility for YASK framework"""
    
    def __init__(self, project_root: Path):
        """
        Initialize backward compatibility manager
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### migrate_document()

```python
def migrate_document(self, document_path: Path) -> bool:
    """
    Migrate a document to YASK 3.0 format
    
    Args:
        document_path: Path to the document to migrate
        
    Returns:
        True if migration successful, False otherwise
    """
```

##### validate_compatibility()

```python
def validate_compatibility(self, document_path: Path) -> Dict[str, Any]:
    """
    Validate document compatibility with YASK 3.0
    
    Args:
        document_path: Path to the document to validate
        
    Returns:
        Dictionary containing validation results:
        - 'compatible': bool - Whether document is compatible
        - 'issues': List[str] - List of compatibility issues
        - 'recommendations': List[str] - Recommendations for fixing issues
    """
```

### System Integration

**Module**: `.yask/core/system-integration.py`

#### Class: SystemIntegration

```python
class SystemIntegration:
    """Manages system integration for YASK framework"""
    
    def __init__(self, project_root: Path):
        """
        Initialize system integration
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### initialize_system()

```python
def initialize_system(self) -> bool:
    """
    Initialize YASK system
    
    Returns:
        True if initialization successful, False otherwise
    """
```

##### check_system_health()

```python
def check_system_health(self) -> Dict[str, Any]:
    """
    Check system health
    
    Returns:
        Dictionary containing health status:
        - 'healthy': bool - Overall system health
        - 'components': Dict[str, bool] - Health of individual components
        - 'issues': List[str] - List of health issues
    """
```

### Documentation Deployment

**Module**: `.yask/core/documentation-deployment.py`

#### Class: DocumentationDeployment

```python
class DocumentationDeployment:
    """Manages documentation deployment for YASK framework"""
    
    def __init__(self, project_root: Path):
        """
        Initialize documentation deployment
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### deploy_documentation()

```python
def deploy_documentation(self) -> bool:
    """
    Deploy documentation
    
    Returns:
        True if deployment successful, False otherwise
    """
```

##### validate_documentation()

```python
def validate_documentation(self) -> Dict[str, Any]:
    """
    Validate documentation
    
    Returns:
        Dictionary containing validation results
    """
```

### Optimized Context Loader

**Module**: `.yask/core/optimized-context-loader.py`

#### Class: OptimizedContextLoader

```python
class OptimizedContextLoader:
    """Main optimized context loading system"""
    
    def __init__(self, project_root: Path, config: Optional[Dict[str, Any]] = None):
        """
        Initialize optimized context loader
        
        Args:
            project_root: Root directory of the project
            config: Optional configuration dictionary
        """
```

#### Methods

##### load_context()

```python
def load_context(self, operation: str, files: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Load context for a specific operation
    
    Args:
        operation: Operation type (e.g., 'create_requirements', 'update_design')
        files: Optional list of specific files to load
        
    Returns:
        Dictionary containing loaded context:
        - 'files': Dict[str, str] - Loaded file contents
        - 'metadata': Dict[str, Any] - Context metadata
        - 'loading_time': float - Time taken to load context
    """
```

##### clear_cache()

```python
def clear_cache(self) -> bool:
    """
    Clear context cache
    
    Returns:
        True if cache cleared successfully, False otherwise
    """
```

### Context Backup Manager

**Module**: `.yask/core/context_backup_manager.py`

#### Class: ContextBackupManager

```python
class ContextBackupManager:
    """Manages context backups for YASK framework"""
    
    def __init__(self, project_root: Path):
        """
        Initialize context backup manager
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### create_backup()

```python
def create_backup(self, backup_name: Optional[str] = None) -> str:
    """
    Create a context backup
    
    Args:
        backup_name: Optional name for the backup
        
    Returns:
        Path to the created backup
    """
```

##### restore_backup()

```python
def restore_backup(self, backup_path: Path) -> bool:
    """
    Restore a context backup
    
    Args:
        backup_path: Path to the backup to restore
        
    Returns:
        True if restore successful, False otherwise
    """
```

---

## Integration Modules

### Core Integration

**Module**: `.yask/integration/core.py`

#### Class: IntegrationCore

```python
class IntegrationCore:
    """Core integration functionality"""
    
    def __init__(self, project_root: Path):
        """
        Initialize integration core
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### integrate_component()

```python
def integrate_component(self, component: str) -> bool:
    """
    Integrate a component into the system
    
    Args:
        component: Component name to integrate
        
    Returns:
        True if integration successful, False otherwise
    """
```

### Orchestrator

**Module**: `.yask/integration/orchestrator.py`

#### Class: IntegrationOrchestrator

```python
class IntegrationOrchestrator:
    """Orchestrates integration processes"""
    
    def __init__(self, project_root: Path):
        """
        Initialize integration orchestrator
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### orchestrate_integration()

```python
def orchestrate_integration(self, components: List[str]) -> Dict[str, Any]:
    """
    Orchestrate integration of multiple components
    
    Args:
        components: List of component names to integrate
        
    Returns:
        Dictionary containing integration results
    """
```

### Plugins

**Module**: `.yask/integration/plugins.py`

#### Class: PluginManager

```python
class PluginManager:
    """Manages plugins for YASK framework"""
    
    def __init__(self, project_root: Path):
        """
        Initialize plugin manager
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### load_plugin()

```python
def load_plugin(self, plugin_name: str) -> bool:
    """
    Load a plugin
    
    Args:
        plugin_name: Name of the plugin to load
        
    Returns:
        True if plugin loaded successfully, False otherwise
    """
```

##### unload_plugin()

```python
def unload_plugin(self, plugin_name: str) -> bool:
    """
    Unload a plugin
    
    Args:
        plugin_name: Name of the plugin to unload
        
    Returns:
        True if plugin unloaded successfully, False otherwise
    """
```

### MCP Integration

**Module**: `.yask/integration/mcp.py`

#### Class: MCPIntegration

```python
class MCPIntegration:
    """Manages MCP (Model Context Protocol) integration"""
    
    def __init__(self, project_root: Path):
        """
        Initialize MCP integration
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### connect_to_mcp()

```python
def connect_to_mcp(self, mcp_url: str) -> bool:
    """
    Connect to MCP server
    
    Args:
        mcp_url: URL of the MCP server
        
    Returns:
        True if connection successful, False otherwise
    """
```

### Tools

**Module**: `.yask/integration/tools.py`

#### Class: IntegrationTools

```python
class IntegrationTools:
    """Integration tools and utilities"""
    
    def __init__(self, project_root: Path):
        """
        Initialize integration tools
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### validate_integration()

```python
def validate_integration(self) -> Dict[str, Any]:
    """
    Validate integration
    
    Returns:
        Dictionary containing validation results
    """
```

### Config

**Module**: `.yask/integration/config.py`

#### Class: ConfigManager

```python
class ConfigManager:
    """Manages configuration for YASK framework"""
    
    def __init__(self, project_root: Path):
        """
        Initialize configuration manager
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### load_config()

```python
def load_config(self, config_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Load configuration
    
    Args:
        config_path: Optional path to configuration file
        
    Returns:
        Dictionary containing configuration
    """
```

##### save_config()

```python
def save_config(self, config: Dict[str, Any], config_path: Optional[Path] = None) -> bool:
    """
    Save configuration
    
    Args:
        config: Configuration dictionary to save
        config_path: Optional path to save configuration
        
    Returns:
        True if save successful, False otherwise
    """
```

---

## Validation Modules

### Quality Assurance Framework

**Module**: `.yask/validation/quality-assurance-framework.py`

#### Class: QualityAssuranceFramework

```python
class QualityAssuranceFramework:
    """Quality assurance framework for YASK"""
    
    def __init__(self, project_root: Path):
        """
        Initialize quality assurance framework
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### run_quality_check()

```python
def run_quality_check(self, check_type: str) -> Dict[str, Any]:
    """
    Run a quality check
    
    Args:
        check_type: Type of quality check to run
        
    Returns:
        Dictionary containing quality check results
    """
```

### Cross-Reference Validator

**Module**: `.yask/validation/cross-reference-validator.py`

#### Class: CrossReferenceValidator

```python
class CrossReferenceValidator:
    """Validates cross-references in documents"""
    
    def __init__(self, project_root: Path):
        """
        Initialize cross-reference validator
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### validate_references()

```python
def validate_references(self, document_path: Path) -> Dict[str, Any]:
    """
    Validate cross-references in a document
    
    Args:
        document_path: Path to the document to validate
        
    Returns:
        Dictionary containing validation results:
        - 'valid': bool - Whether references are valid
        - 'broken_references': List[str] - List of broken references
        - 'warnings': List[str] - List of warnings
    """
```

### Streamlined Quality Gates

**Module**: `.yask/validation/streamlined-quality-gates.py`

#### Class: StreamlinedQualityGates

```python
class StreamlinedQualityGates:
    """Streamlined quality gates for YASK"""
    
    def __init__(self, project_root: Path):
        """
        Initialize streamlined quality gates
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### run_quality_gate()

```python
def run_quality_gate(self, gate_name: str) -> Dict[str, Any]:
    """
    Run a quality gate
    
    Args:
        gate_name: Name of the quality gate to run
        
    Returns:
        Dictionary containing quality gate results
    """
```

---

## Testing Modules

### Test Framework

**Module**: `.yask/testing/framework/test_orchestrator.py`

#### Class: TestOrchestrator

```python
class TestOrchestrator:
    """Orchestrates test execution"""
    
    def __init__(self, project_root: Path):
        """
        Initialize test orchestrator
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### run_tests()

```python
def run_tests(self, test_category: Optional[str] = None) -> Dict[str, Any]:
    """
    Run tests
    
    Args:
        test_category: Optional test category to run
        
    Returns:
        Dictionary containing test results
    """
```

### Quality Metrics

**Module**: `.yask/testing/framework/quality_metrics.py`

#### Class: QualityMetrics

```python
class QualityMetrics:
    """Calculates quality metrics"""
    
    def __init__(self, project_root: Path):
        """
        Initialize quality metrics
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### calculate_metrics()

```python
def calculate_metrics(self) -> Dict[str, Any]:
    """
    Calculate quality metrics
    
    Returns:
        Dictionary containing quality metrics
    """
```

---

## Workflow Modules

### Change Impact Analyzer

**Module**: `.yask/workflow/change-impact-analyzer.py`

#### Class: ChangeImpactAnalyzer

```python
class ChangeImpactAnalyzer:
    """Analyzes impact of changes"""
    
    def __init__(self, project_root: Path):
        """
        Initialize change impact analyzer
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### analyze_impact()

```python
def analyze_impact(self, change: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze impact of a change
    
    Args:
        change: Dictionary describing the change
        
    Returns:
        Dictionary containing impact analysis
    """
```

### Consistency Checker

**Module**: `.yask/workflow/consistency-checker.py`

#### Class: ConsistencyChecker

```python
class ConsistencyChecker:
    """Checks consistency across documents"""
    
    def __init__(self, project_root: Path):
        """
        Initialize consistency checker
        
        Args:
            project_root: Root directory of the project
        """
```

#### Methods

##### check_consistency()

```python
def check_consistency(self) -> Dict[str, Any]:
    """
    Check consistency across documents
    
    Returns:
        Dictionary containing consistency check results
    """
```

---

## Usage Examples

### Example 1: Optimizing Performance

```python
from pathlib import Path
from .yask.core.performance_optimizer import PerformanceOptimizer

# Initialize performance optimizer
optimizer = PerformanceOptimizer(Path("/path/to/project"))

# Optimize context loading
results = optimizer.optimize_context_loading()
print(f"Performance improvement: {results['improvement_percentage']}%")

# Benchmark performance
metrics = optimizer.benchmark_performance()
print(f"Context loading time: {metrics['context_loading_time']}s")
```

### Example 2: Migrating Documents

```python
from pathlib import Path
from .yask.core.backward_compatibility import BackwardCompatibilityManager

# Initialize backward compatibility manager
manager = BackwardCompatibilityManager(Path("/path/to/project"))

# Migrate a document
success = manager.migrate_document(Path("requirements.md"))
if success:
    print("Document migrated successfully")
else:
    print("Migration failed")

# Validate compatibility
results = manager.validate_compatibility(Path("requirements.md"))
if results['compatible']:
    print("Document is compatible")
else:
    print("Issues found:", results['issues'])
```

### Example 3: Loading Context

```python
from pathlib import Path
from .yask.core.optimized_context_loader import OptimizedContextLoader

# Initialize context loader
loader = OptimizedContextLoader(Path("/path/to/project"))

# Load context for operation
context = loader.load_context("create_requirements")
print(f"Loaded {len(context['files'])} files in {context['loading_time']}s")

# Clear cache
loader.clear_cache()
```

### Example 4: Running Tests

```python
from pathlib import Path
from .yask.testing.framework.test_orchestrator import TestOrchestrator

# Initialize test orchestrator
orchestrator = TestOrchestrator(Path("/path/to/project"))

# Run all tests
results = orchestrator.run_tests()
print(f"Passed: {results['passed']}/{results['total']}")

# Run specific category
results = orchestrator.run_tests("document")
print(f"Document tests: {results['passed']}/{results['total']}")
```

---

## Error Handling

### Common Exceptions

#### PerformanceOptimizerError

```python
class PerformanceOptimizerError(Exception):
    """Exception raised for performance optimizer errors"""
    pass
```

#### BackwardCompatibilityError

```python
class BackwardCompatibilityError(Exception):
    """Exception raised for backward compatibility errors"""
    pass
```

#### ContextLoaderError

```python
class ContextLoaderError(Exception):
    """Exception raised for context loader errors"""
    pass
```

### Error Handling Example

```python
from .yask.core.performance_optimizer import PerformanceOptimizer, PerformanceOptimizerError

try:
    optimizer = PerformanceOptimizer(Path("/path/to/project"))
    results = optimizer.optimize_context_loading()
except PerformanceOptimizerError as e:
    print(f"Performance optimization failed: {e}")
    # Handle error
```

---

## Support and Resources

### Documentation

- YASK Architecture: `YASK_REFACTOR_ARCHITECTURE.md`
- Performance Tuning: `PERFORMANCE_TUNING_GUIDE.md`
- Backward Compatibility: `BACKWARD_COMPATIBILITY_GUIDE.md`
- Integration Testing: `INTEGRATION_TESTING_GUIDE.md`

### Community

- GitHub Issues: https://github.com/moxxiepox/yask-spec-kit/issues
- Documentation: https://github.com/moxxiepox/yask-spec-kit/wiki
- Discussions: https://github.com/moxxiepox/yask-spec-kit/discussions

---

## Conclusion

This API reference provides comprehensive documentation for all YASK 3.0 modules. For questions or issues, please refer to the support section or contact the community.

---

**API Reference Version**: 1.0.0
**Last Updated**: 2025-12-29
**YASK Version**: 3.0.0
