---
date: '2025-12-28'
description: MCP integration examples for YASK system
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: MCP Integration Examples for YASK
version: 6.0.0
---

# MCP Integration Examples for YASK

This document provides practical examples of how to integrate MCP tools with YASK while maintaining its core simplicity and flexibility.

## Example 1: Tree-Sitter Code Analysis Integration

### Basic Tree-Sitter Integration

```python
# .yask/integrations/tree_sitter_analyzer.py
"""
Optional Tree-Sitter integration for YASK
Provides code syntax validation and pattern recognition
"""

import os
import sys
from typing import Dict, List, Optional, Any
from pathlib import Path

class TreeSitterAnalyzer:
    """Optional Tree-Sitter integration for enhanced code analysis"""
    
    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        self.parser = None
        
        if enabled:
            self._initialize_parser()
    
    def _initialize_parser(self):
        """Initialize Tree-Sitter parser (optional enhancement)"""
        try:
            # Optional dependency - only load if enabled
            from tree_sitter import Language, Parser
            
            # Initialize parser for supported languages
            self.parser = Parser()
            # Note: Language library would need to be built/loaded
            # This is a placeholder for the actual implementation
            print("Tree-Sitter parser initialized (optional enhancement)")
            
        except ImportError:
            print("Tree-Sitter not available - running without code analysis")
            self.enabled = False
    
    def analyze_implementation(self, code_file: Path, requirements: List[str]) -> Dict[str, Any]:
        """
        Analyze code implementation against requirements
        
        Args:
            code_file: Path to the implementation file
            requirements: List of requirement strings
            
        Returns:
            Analysis results (empty if integration disabled)
        """
        if not self.enabled or not self.parser:
            return {
                "status": "integration_disabled",
                "message": "Tree-Sitter integration not enabled or available"
            }
        
        try:
            # Read and parse the code file
            with open(code_file, 'r', encoding='utf-8') as f:
                code_content = f.read()
            
            # Parse the code (placeholder implementation)
            tree = self.parser.parse(code_content.encode())
            
            # Analyze against requirements
            analysis = {
                "status": "analyzed",
                "syntax_valid": True,  # Would be determined by Tree-Sitter
                "complexity_score": self._calculate_complexity(tree),
                "requirement_coverage": self._check_requirement_coverage(tree, requirements),
                "patterns_found": self._identify_patterns(tree),
                "suggestions": self._generate_suggestions(tree, requirements)
            }
            
            return analysis
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Analysis failed: {str(e)}"
            }
    
    def _calculate_complexity(self, tree) -> int:
        """Calculate code complexity score (placeholder)"""
        # Would implement actual Tree-Sitter-based complexity calculation
        return 0
    
    def _check_requirement_coverage(self, tree, requirements: List[str]) -> Dict[str, bool]:
        """Check which requirements are addressed in code"""
        coverage = {}
        for req in requirements:
            # Would implement actual requirement-to-code mapping
            coverage[req] = True  # Placeholder
        return coverage
    
    def _identify_patterns(self, tree) -> List[str]:
        """Identify design patterns in the code"""
        # Would implement pattern recognition using Tree-Sitter
        return []
    
    def _generate_suggestions(self, tree, requirements: List[str]) -> List[str]:
        """Generate improvement suggestions"""
        # Would implement suggestion generation
        return []

# Integration helper function
def analyze_with_tree_sitter(code_file: Path, requirements: List[str]) -> Dict[str, Any]:
    """
    Convenience function for Tree-Sitter analysis
    
    This function demonstrates how YASK can optionally enhance
    its capabilities without compromising core functionality.
    """
    # Check if Tree-Sitter integration is enabled
    enabled = os.getenv('YASK_ENABLE_TREESITTER', 'false').lower() == 'true'
    
    analyzer = TreeSitterAnalyzer(enabled=enabled)
    return analyzer.analyze_implementation(code_file, requirements)
```

### Usage in YASK Workflow

```python
# Example: Enhanced requirements validation
def validate_implementation_enhanced(impl_file: Path, requirements: List[str]):
    """Enhanced implementation validation with optional Tree-Sitter"""
    
    # Standard YASK validation (always available)
    basic_validation = {
        "file_exists": impl_file.exists(),
        "file_readable": os.access(impl_file, os.R_OK) if impl_file.exists() else False
    }
    
    # Optional Tree-Sitter enhancement
    tree_sitter_analysis = analyze_with_tree_sitter(impl_file, requirements)
    
    # Combine results
    validation_result = {
        "basic_validation": basic_validation,
        "enhanced_analysis": tree_sitter_analysis,
        "overall_status": "validated" if basic_validation["file_exists"] else "missing_file"
    }
    
    return validation_result
```

## Example 2: Code Health Tools Integration

### TypeScript/JavaScript Analysis

```python
# .yask/integrations/code_health_analyzer.py
"""
Optional code health analysis integration
Supports multiple languages through MCP/LSP protocols
"""

import subprocess
import json
import os
from typing import Dict, List, Optional, Any
from pathlib import Path

class CodeHealthAnalyzer:
    """Optional code health analysis for multiple languages"""
    
    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        self.supported_languages = {
            'typescript': self._analyze_typescript,
            'javascript': self._analyze_javascript,
            'python': self._analyze_python,
            'rust': self._analyze_rust,
            'go': self._analyze_go
        }
    
    def analyze_project(self, project_path: Path) -> Dict[str, Any]:
        """
        Analyze project code health
        
        Args:
            project_path: Root path of the project
            
        Returns:
            Analysis results for all detected languages
        """
        if not self.enabled:
            return {
                "status": "integration_disabled",
                "message": "Code health analysis not enabled"
            }
        
        results = {
            "status": "analyzed",
            "project_path": str(project_path),
            "languages": {},
            "overall_health": "unknown"
        }
        
        # Detect and analyze each language
        for lang, analyzer_func in self.supported_languages.items():
            if self._has_language_files(project_path, lang):
                try:
                    lang_result = analyzer_func(project_path)
                    results["languages"][lang] = lang_result
                except Exception as e:
                    results["languages"][lang] = {
                        "status": "error",
                        "message": str(e)
                    }
        
        # Calculate overall health score
        results["overall_health"] = self._calculate_overall_health(results["languages"])
        
        return results
    
    def _has_language_files(self, project_path: Path, language: str) -> bool:
        """Check if project contains files for the specified language"""
        extensions = {
            'typescript': ['.ts', '.tsx'],
            'javascript': ['.js', '.jsx'],
            'python': ['.py'],
            'rust': ['.rs'],
            'go': ['.go']
        }
        
        lang_extensions = extensions.get(language, [])
        for ext in lang_extensions:
            if any(project_path.rglob(f"*{ext}")):
                return True
        return False
    
    def _analyze_typescript(self, project_path: Path) -> Dict[str, Any]:
        """Analyze TypeScript/JavaScript code health"""
        result = {
            "language": "typescript",
            "status": "analyzed",
            "issues": [],
            "metrics": {}
        }
        
        try:
            # Check if TypeScript is available
            if not self._command_available('tsc'):
                result["status"] = "unavailable"
                result["message"] = "TypeScript compiler not found"
                return result
            
            # Run TypeScript compiler for type checking
            tsc_result = subprocess.run(
                ['tsc', '--noEmit', '--pretty'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if tsc_result.stdout:
                result["issues"].append({
                    "type": "type_error",
                    "output": tsc_result.stdout
                })
            
            if tsc_result.stderr:
                result["issues"].append({
                    "type": "compiler_error",
                    "output": tsc_result.stderr
                })
            
            # Check for ESLint configuration
            eslint_config = project_path / '.eslintrc.json'
            if eslint_config.exists():
                result["metrics"]["eslint_configured"] = True
                
                # Run ESLint if available
                if self._command_available('eslint'):
                    eslint_result = subprocess.run(
                        ['eslint', '.', '--format=json'],
                        cwd=project_path,
                        capture_output=True,
                        text=True
                    )
                    
                    if eslint_result.returncode == 0:
                        try:
                            eslint_data = json.loads(eslint_result.stdout)
                            result["metrics"]["eslint_issues"] = len(eslint_data)
                        except json.JSONDecodeError:
                            pass
            
            result["metrics"]["type_check_passed"] = tsc_result.returncode == 0
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)
        
        return result
    
    def _analyze_javascript(self, project_path: Path) -> Dict[str, Any]:
        """Analyze JavaScript code health"""
        # Similar to TypeScript but without type checking
        return self._analyze_typescript(project_path)
    
    def _analyze_python(self, project_path: Path) -> Dict[str, Any]:
        """Analyze Python code health"""
        result = {
            "language": "python",
            "status": "analyzed",
            "issues": [],
            "metrics": {}
        }
        
        try:
            # Check for common Python analysis tools
            tools = ['flake8', 'pylint', 'black', 'mypy']
            available_tools = [tool for tool in tools if self._command_available(tool)]
            
            for tool in available_tools:
                tool_result = subprocess.run(
                    [tool, '.'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                
                if tool_result.stdout or tool_result.stderr:
                    result["issues"].append({
                        "tool": tool,
                        "output": tool_result.stdout + tool_result.stderr
                    })
            
            result["metrics"]["available_tools"] = available_tools
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)
        
        return result
    
    def _analyze_rust(self, project_path: Path) -> Dict[str, Any]:
        """Analyze Rust code health"""
        result = {
            "language": "rust",
            "status": "analyzed",
            "issues": [],
            "metrics": {}
        }
        
        try:
            # Run cargo check for Rust projects
            if (project_path / 'Cargo.toml').exists():
                cargo_result = subprocess.run(
                    ['cargo', 'check'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                
                if cargo_result.returncode != 0:
                    result["issues"].append({
                        "type": "cargo_check_failed",
                        "output": cargo_result.stderr
                    })
                
                result["metrics"]["cargo_check_passed"] = cargo_result.returncode == 0
                
                # Run clippy if available
                if self._command_available('clippy'):
                    clippy_result = subprocess.run(
                        ['cargo', 'clippy'],
                        cwd=project_path,
                        capture_output=True,
                        text=True
                    )
                    
                    if clippy_result.stdout or clippy_result.stderr:
                        result["issues"].append({
                            "type": "clippy_warnings",
                            "output": clippy_result.stdout + clippy_result.stderr
                        })
        
        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)
        
        return result
    
    def _analyze_go(self, project_path: Path) -> Dict[str, Any]:
        """Analyze Go code health"""
        result = {
            "language": "go",
            "status": "analyzed",
            "issues": [],
            "metrics": {}
        }
        
        try:
            # Run go vet
            vet_result = subprocess.run(
                ['go', 'vet', './...'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if vet_result.stdout or vet_result.stderr:
                result["issues"].append({
                    "type": "go_vet",
                    "output": vet_result.stdout + vet_result.stderr
                })
            
            result["metrics"]["go_vet_passed"] = vet_result.returncode == 0
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)
        
        return result
    
    def _command_available(self, command: str) -> bool:
        """Check if a command is available in PATH"""
        try:
            subprocess.run([command, '--version'], 
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def _calculate_overall_health(self, language_results: Dict[str, Any]) -> str:
        """Calculate overall project health score"""
        if not language_results:
            return "no_analysis"
        
        total_issues = sum(
            len(result.get("issues", [])) 
            for result in language_results.values()
            if isinstance(result, dict) and result.get("status") == "analyzed"
        )
        
        if total_issues == 0:
            return "excellent"
        elif total_issues < 5:
            return "good"
        elif total_issues < 15:
            return "fair"
        else:
            return "needs_attention"

# Integration helper function
def analyze_code_health(project_path: Path) -> Dict[str, Any]:
    """
    Convenience function for code health analysis
    
    Demonstrates optional enhancement without core dependency
    """
    enabled = os.getenv('YASK_ENABLE_CODE_HEALTH', 'false').lower() == 'true'
    
    analyzer = CodeHealthAnalyzer(enabled=enabled)
    return analyzer.analyze_project(project_path)
```

## Example 3: Documentation Consistency Validator

```python
# .yask/integrations/documentation_validator.py
"""
Optional documentation consistency validation
Ensures requirements, design, and implementation alignment
"""

import re
from typing import Dict, List, Set, Optional, Any
from pathlib import Path

class DocumentationValidator:
    """Optional documentation consistency validation"""
    
    def __init__(self, enabled: bool = False):
        self.enabled = enabled
    
    def validate_project_consistency(self, project_path: Path) -> Dict[str, Any]:
        """
        Validate consistency across all project documentation
        
        Args:
            project_path: Root path of the project
            
        Returns:
            Validation results
        """
        if not self.enabled:
            return {
                "status": "integration_disabled",
                "message": "Documentation validation not enabled"
            }
        
        # Find all specification documents
        specs = self._find_specification_files(project_path)
        
        validation_result = {
            "status": "validated",
            "specifications_found": specs,
            "consistency_checks": {},
            "recommendations": []
        }
        
        # Perform various consistency checks
        validation_result["consistency_checks"] = {
            "requirement_traceability": self._check_requirement_traceability(specs),
            "design_coverage": self._check_design_coverage(specs),
            "implementation_alignment": self._check_implementation_alignment(specs, project_path),
            "cross_references": self._check_cross_references(specs)
        }
        
        # Generate recommendations
        validation_result["recommendations"] = self._generate_recommendations(
            validation_result["consistency_checks"]
        )
        
        return validation_result
    
    def _find_specification_files(self, project_path: Path) -> Dict[str, Path]:
        """Find all specification-related files"""
        specs = {}
        
        # Common specification file patterns
        patterns = {
            'requirements': ['requirements.md', 'spec.md', '**/requirements.md'],
            'design': ['design.md', 'architecture.md', '**/design.md'],
            'tasks': ['tasks.md', '**/tasks.md'],
            'readme': ['README.md', '**/README.md']
        }
        
        for spec_type, pattern_list in patterns.items():
            for pattern in pattern_list:
                matches = list(project_path.glob(pattern))
                if matches:
                    specs[spec_type] = matches[0]  # Take first match
                    break
        
        return specs
    
    def _check_requirement_traceability(self, specs: Dict[str, Path]) -> Dict[str, Any]:
        """Check if requirements are traceable through design to implementation"""
        result = {
            "status": "checked",
            "traceability_score": 0,
            "missing_links": [],
            "orphaned_requirements": []
        }
        
        if 'requirements' not in specs:
            result["status"] = "no_requirements_file"
            return result
        
        # Read requirements file
        requirements_content = specs['requirements'].read_text()
        
        # Extract requirement identifiers (e.g., REQ-001, REQUIREMENT-1, etc.)
        req_pattern = r'(?:REQ(?:UIREMENT)?[-_\s]*(\d+)|Requirement[-_\s]*(\d+))'
        requirements = re.findall(req_pattern, requirements_content, re.IGNORECASE)
        
        if 'design' in specs:
            design_content = specs['design'].read_text()
            
            # Check which requirements are referenced in design
            referenced_reqs = set()
            for req_match in requirements:
                req_id = req_match[0] or req_match[1]  # Get the actual number
                if req_id in design_content:
                    referenced_reqs.add(req_id)
            
            result["traceability_score"] = len(referenced_reqs) / len(requirements) if requirements else 0
            result["missing_links"] = [req for req in requirements if req[0] not in referenced_reqs and req[1] not in referenced_reqs]
        
        return result
    
    def _check_design_coverage(self, specs: Dict[str, Path]) -> Dict[str, Any]:
        """Check if design adequately covers all requirements"""
        result = {
            "status": "checked",
            "coverage_score": 0,
            "gaps": [],
            "over_engineering": []
        }
        
        if 'requirements' not in specs or 'design' not in specs:
            result["status"] = "missing_files"
            return result
        
        requirements_content = specs['requirements'].read_text()
        design_content = specs['design'].read_text()
        
        # Simple keyword-based coverage check
        req_keywords = self._extract_keywords(requirements_content)
        design_keywords = self._extract_keywords(design_content)
        
        coverage = len(req_keywords & design_keywords) / len(req_keywords) if req_keywords else 0
        result["coverage_score"] = coverage
        
        if coverage < 0.7:
            result["gaps"] = list(req_keywords - design_keywords)
        
        return result
    
    def _check_implementation_alignment(self, specs: Dict[str, Path], project_path: Path) -> Dict[str, Any]:
        """Check if implementation aligns with design and requirements"""
        result = {
            "status": "checked",
            "alignment_score": 0,
            "misalignments": [],
            "missing_implementations": []
        }
        
        # Find implementation files
        impl_files = list(project_path.rglob("*.py")) + \
                    list(project_path.rglob("*.js")) + \
                    list(project_path.rglob("*.ts")) + \
                    list(project_path.rglob("*.rs")) + \
                    list(project_path.rglob("*.go"))
        
        if not impl_files:
            result["status"] = "no_implementation_files"
            return result
        
        # Analyze implementation files
        impl_keywords = set()
        for impl_file in impl_files[:10]:  # Limit to first 10 files for performance
            try:
                content = impl_file.read_text()
                impl_keywords.update(self._extract_keywords(content))
            except Exception:
                continue
        
        if 'design' in specs:
            design_content = specs['design'].read_text()
            design_keywords = self._extract_keywords(design_content)
            
            alignment = len(impl_keywords & design_keywords) / len(design_keywords) if design_keywords else 0
            result["alignment_score"] = alignment
            
            if alignment < 0.5:
                result["misalignments"] = list(design_keywords - impl_keywords)
        
        return result
    
    def _check_cross_references(self, specs: Dict[str, Path]) -> Dict[str, Any]:
        """Check if cross-references between documents are valid"""
        result = {
            "status": "checked",
            "broken_links": [],
            "missing_references": []
        }
        
        # Check for #[[file:]] links mentioned in YASK patterns
        for spec_type, spec_path in specs.items():
            try:
                content = spec_path.read_text()
                # Look for file references
                file_refs = re.findall(r'#\[\[file:([^\]]+)\]\]', content)
                
                for file_ref in file_refs:
                    referenced_file = spec_path.parent / file_ref
                    if not referenced_file.exists():
                        result["broken_links"].append({
                            "source": str(spec_path),
                            "reference": file_ref
                        })
            except Exception:
                continue
        
        return result
    
    def _extract_keywords(self, text: str) -> Set[str]:
        """Extract meaningful keywords from text"""
        # Simple keyword extraction - could be enhanced with NLP
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        
        # Filter out common words
        stop_words = {'this', 'that', 'with', 'from', 'they', 'have', 'been', 'will', 'were', 'said', 'each', 'which', 'their', 'time', 'about', 'would', 'there', 'could', 'other', 'more', 'very', 'what', 'know', 'just', 'first', 'into', 'over', 'think', 'also', 'your', 'work', 'life', 'only', 'new', 'years', 'way', 'may', 'say', 'come', 'its', 'now', 'find', 'long', 'day', 'get', 'made', 'may', 'part'}
        
        return {word for word in words if word not in stop_words}
    
    def _generate_recommendations(self, checks: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on validation results"""
        recommendations = []
        
        # Requirement traceability recommendations
        if 'requirement_traceability' in checks:
            rt_check = checks['requirement_traceability']
            if rt_check.get('traceability_score', 0) < 0.8:
                recommendations.append(
                    "Improve requirement traceability by ensuring all requirements are referenced in design documents"
                )
        
        # Design coverage recommendations
        if 'design_coverage' in checks:
            design_check = checks['design_coverage']
            if design_check.get('coverage_score', 0) < 0.7:
                recommendations.append(
                    "Enhance design document to better cover all requirements"
                )
        
        # Implementation alignment recommendations
        if 'implementation_alignment' in checks:
            impl_check = checks['implementation_alignment']
            if impl_check.get('alignment_score', 0) < 0.5:
                recommendations.append(
                    "Review implementation to ensure alignment with design specifications"
                )
        
        # Cross-reference recommendations
        if 'cross_references' in checks:
            ref_check = checks['cross_references']
            if ref_check.get('broken_links'):
                recommendations.append(
                    "Fix broken file references in documentation"
                )
        
        return recommendations

# Integration helper function
def validate_documentation_consistency(project_path: Path) -> Dict[str, Any]:
    """
    Convenience function for documentation validation
    
    Demonstrates optional enhancement for documentation quality
    """
    enabled = os.getenv('YASK_ENABLE_DOC_VALIDATION', 'false').lower() == 'true'
    
    validator = DocumentationValidator(enabled=enabled)
    return validator.validate_project_consistency(project_path)
```

## Example 4: Enhanced YASK Workflow Integration

```python
# .yask/integrations/enhanced_yask_workflow.py
"""
Enhanced YASK workflow with optional MCP integrations
Demonstrates how to add capabilities without compromising core simplicity
"""

import os
from pathlib import Path
from typing import Dict, List, Any, Optional

# Import our optional integrations
from .tree_sitter_analyzer import analyze_with_tree_sitter
from .code_health_analyzer import analyze_code_health
from .documentation_validator import validate_documentation_consistency

class EnhancedYASKWorkflow:
    """
    Enhanced YASK workflow that optionally integrates MCP tools
    
    This class demonstrates how YASK can be enhanced with powerful
    tools while maintaining its core simplicity and flexibility.
    """
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.integrations_enabled = self._check_integration_status()
    
    def _check_integration_status(self) -> Dict[str, bool]:
        """Check which integrations are enabled via environment variables"""
        return {
            'tree_sitter': os.getenv('YASK_ENABLE_TREESITTER', 'false').lower() == 'true',
            'code_health': os.getenv('YASK_ENABLE_CODE_HEALTH', 'false').lower() == 'true',
            'doc_validation': os.getenv('YASK_ENABLE_DOC_VALIDATION', 'false').lower() == 'true'
        }
    
    def enhanced_implementation_validation(self, impl_file: Path, requirements: List[str]) -> Dict[str, Any]:
        """
        Enhanced implementation validation with optional tools
        
        This method shows how YASK can provide enhanced validation
        without making it a requirement or breaking core functionality.
        """
        # Core YASK validation (always available)
        core_validation = {
            "file_exists": impl_file.exists(),
            "file_readable": os.access(impl_file, os.R_OK) if impl_file.exists() else False,
            "file_size": impl_file.stat().st_size if impl_file.exists() else 0
        }
        
        # Optional enhancements
        enhancements = {}
        
        if self.integrations_enabled['tree_sitter']:
            enhancements['tree_sitter_analysis'] = analyze_with_tree_sitter(impl_file, requirements)
        
        # Combine results
        result = {
            "core_validation": core_validation,
            "enhancements": enhancements,
            "overall_status": self._determine_overall_status(core_validation, enhancements),
            "recommendations": self._generate_recommendations(core_validation, enhancements)
        }
        
        return result
    
    def enhanced_project_analysis(self) -> Dict[str, Any]:
        """
        Enhanced project analysis with optional tools
        
        Provides comprehensive project health analysis when integrations are enabled
        """
        # Core project analysis (always available)
        core_analysis = {
            "project_path": str(self.project_path),
            "has_specifications": self._check_specifications(),
            "has_implementation": self._check_implementation_files(),
            "project_structure": self._analyze_project_structure()
        }
        
        # Optional enhancements
        enhancements = {}
        
        if self.integrations_enabled['code_health']:
            enhancements['code_health'] = analyze_code_health(self.project_path)
        
        if self.integrations_enabled['doc_validation']:
            enhancements['documentation_consistency'] = validate_documentation_consistency(self.project_path)
        
        # Combine results
        result = {
            "core_analysis": core_analysis,
            "enhancements": enhancements,
            "overall_health": self._calculate_overall_health(core_analysis, enhancements),
            "integration_status": self.integrations_enabled
        }
        
        return result
    
    def _check_specifications(self) -> bool:
        """Check if project has specification files"""
        spec_patterns = ['requirements.md', 'design.md', 'tasks.md']
        return any((self.project_path / pattern).exists() for pattern in spec_patterns)
    
    def _check_implementation_files(self) -> bool:
        """Check if project has implementation files"""
        impl_extensions = ['.py', '.js', '.ts', '.rs', '.go', '.java', '.cpp', '.c']
        return any(self.project_path.rglob(f"*{ext}") for ext in impl_extensions)
    
    def _analyze_project_structure(self) -> Dict[str, int]:
        """Analyze basic project structure"""
        structure = {
            "total_files": 0,
            "documentation_files": 0,
            "implementation_files": 0,
            "config_files": 0
        }
        
        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                structure["total_files"] += 1
                
                if file_path.suffix in ['.md', '.txt', '.rst']:
                    structure["documentation_files"] += 1
                elif file_path.suffix in ['.py', '.js', '.ts', '.rs', '.go', '.java', '.cpp', '.c']:
                    structure["implementation_files"] += 1
                elif file_path.suffix in ['.json', '.yaml', '.yml', '.toml', '.ini', '.cfg']:
                    structure["config_files"] += 1
        
        return structure
    
    def _determine_overall_status(self, core_validation: Dict[str, Any], enhancements: Dict[str, Any]) -> str:
        """Determine overall validation status"""
        if not core_validation.get("file_exists"):
            return "missing_file"
        
        # Check if any enhancement found critical issues
        for enhancement in enhancements.values():
            if isinstance(enhancement, dict) and enhancement.get("status") == "error":
                return "validation_error"
        
        return "validated"
    
    def _generate_recommendations(self, core_validation: Dict[str, Any], enhancements: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on validation results"""
        recommendations = []
        
        # Core recommendations
        if not core_validation.get("file_exists"):
            recommendations.append("Implementation file is missing")
        
        # Enhancement-based recommendations
        for enhancement_name, enhancement_data in enhancements.items():
            if isinstance(enhancement_data, dict) and "recommendations" in enhancement_data:
                recommendations.extend(enhancement_data["recommendations"])
        
        return recommendations
    
    def _calculate_overall_health(self, core_analysis: Dict[str, Any], enhancements: Dict[str, Any]) -> str:
        """Calculate overall project health"""
        # Base health on core analysis
        if not core_analysis.get("has_specifications"):
            return "needs_structure"
        
        if not core_analysis.get("has_implementation"):
            return "no_implementation"
        
        # Check enhancement results
        health_scores = []
        
        if 'code_health' in enhancements:
            code_health = enhancements['code_health']
            if isinstance(code_health, dict):
                overall_health = code_health.get('overall_health', 'unknown')
                if overall_health == 'excellent':
                    health_scores.append(4)
                elif overall_health == 'good':
                    health_scores.append(3)
                elif overall_health == 'fair':
                    health_scores.append(2)
                else:
                    health_scores.append(1)
        
        if 'documentation_consistency' in enhancements:
            doc_consistency = enhancements['documentation_consistency']
            if isinstance(doc_consistency, dict):
                # Simple scoring based on number of recommendations
                recommendations = doc_consistency.get('recommendations', [])
                if len(recommendations) == 0:
                    health_scores.append(4)
                elif len(recommendations) <= 2:
                    health_scores.append(3)
                elif len(recommendations) <= 5:
                    health_scores.append(2)
                else:
                    health_scores.append(1)
        
        # Calculate average health score
        if health_scores:
            avg_score = sum(health_scores) / len(health_scores)
            if avg_score >= 3.5:
                return "excellent"
            elif avg_score >= 2.5:
                return "good"
            elif avg_score >= 1.5:
                return "fair"
            else:
                return "needs_attention"
        
        return "basic"  # No enhancements available

# Usage example
def demonstrate_enhanced_yask():
    """Demonstrate enhanced YASK workflow"""
    project_path = Path("./my_project")
    
    # Initialize enhanced workflow
    workflow = EnhancedYASKWorkflow(project_path)
    
    # Perform enhanced analysis
    analysis = workflow.enhanced_project_analysis()
    
    print("YASK Enhanced Analysis Results:")
    print(f"Overall Health: {analysis['overall_health']}")
    print(f"Integration Status: {analysis['integration_status']}")
    
    if analysis['enhancements']:
        print("\nEnhancements Applied:")
        for enhancement_name in analysis['enhancements'].keys():
            print(f"- {enhancement_name}")
    
    return analysis
```

## Configuration Examples

### Environment-Based Configuration

```bash
# .env file for YASK MCP integrations
# Copy to your project and customize as needed

# Enable Tree-Sitter integration
YASK_ENABLE_TREESITTER=true

# Enable code health analysis
YASK_ENABLE_CODE_HEALTH=true

# Enable documentation validation
YASK_ENABLE_DOC_VALIDATION=true

# Optional: Configure specific tools
TYPESCRIPT_ANALYZER_ENABLED=true
PYTHON_ANALYZER_ENABLED=true
RUST_ANALYZER_ENABLED=true

# Optional: Set analysis strictness level
CODE_HEALTH_STRICTNESS=standard  # basic, standard, strict
```

### YAML Configuration

```yaml
# .yask/mcp-integrations.yaml
# Optional MCP integration configuration

# Global integration settings
integrations:
  # Tree-Sitter integration
  tree_sitter:
    enabled: false
    languages:
      - python
      - javascript
      - typescript
      - rust
    validation_level: "standard"  # basic, standard, strict
    timeout_seconds: 30
  
  # Code health analysis
  code_health:
    enabled: false
    tools:
      typescript:
        enabled: true
        strict_mode: false
      javascript:
        enabled: true
        eslint_config: ".eslintrc.json"
      python:
        enabled: true
        tools: ["flake8", "black", "mypy"]
      rust:
        enabled: true
        tools: ["clippy", "fmt"]
      go:
        enabled: true
        tools: ["vet", "fmt"]
    fail_on_critical: false
  
  # Documentation validation
  documentation:
    enabled: false
    consistency_check: true
    requirement_traceability: true
    cross_reference_validation: true
    keyword_coverage_threshold: 0.7
  
  # MCP servers
  mcp_servers:
    github:
      enabled: false
      token: "${GITHUB_TOKEN}"
    filesystem:
      enabled: true
    custom_servers: []

# Performance settings
performance:
  max_analysis_time: 60
  parallel_analysis: true
  cache_results: true
  cache_ttl_hours: 24

# Reporting settings
reporting:
  generate_reports: true
  report_format: "markdown"  # markdown, json, html
  include_suggestions: true
  include_metrics: true
```

## Best Practices for Integration Usage

### 1. Gradual Adoption
```python
# Start with basic integrations
os.environ['YASK_ENABLE_TREESITTER'] = 'false'
os.environ['YASK_ENABLE_CODE_HEALTH'] = 'false'
os.environ['YASK_ENABLE_DOC_VALIDATION'] = 'false'

# Enable one integration at a time
os.environ['YASK_ENABLE_TREESITTER'] = 'true'  # Enable Tree-Sitter first

# Test and validate results
# Then enable additional integrations as needed
```

### 2. Clear Documentation
```markdown
# Project Integration Status

## Enabled Integrations
- ✅ Tree-Sitter: Enhanced code analysis
- ❌ Code Health: Disabled (not needed for this project)
- ❌ Documentation Validation: Disabled (manual review preferred)

## Rationale
Tree-Sitter provides valuable syntax validation without significant overhead.
Other integrations are disabled to maintain simplicity for this small project.

## Configuration
See `.env` file for detailed integration settings.
```

### 3. Performance Monitoring
```python
import time
from contextlib import contextmanager

@contextmanager
def measure_integration_time(integration_name):
    """Context manager to measure integration performance"""
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        print(f"{integration_name} took {duration:.2f} seconds")

# Usage in integration
with measure_integration_time("Tree-Sitter Analysis"):
    result = analyze_with_tree_sitter(file_path, requirements)
```

### 4. Error Handling
```python
def safe_integration_call(integration_func, *args, **kwargs):
    """Safely call integration functions with fallback"""
    try:
        return integration_func(*args, **kwargs)
    except Exception as e:
        return {
            "status": "error",
            "message": f"Integration failed: {str(e)}",
            "fallback": "core_functionality_only"
        }

# Usage
result = safe_integration_call(analyze_with_tree_sitter, impl_file, requirements)
```

These examples demonstrate how YASK can be enhanced with powerful MCP tools while maintaining its core principles of simplicity, flexibility, and platform independence. The integrations are truly optional and provide clear value when enabled without compromising the system's core functionality when disabled.