---
date: '2025-12-28'
description: YASK MCP integration templates and guidelines
status: active
tags:
  - yask
  - yask/type/documentation
  - yask/status/active
title: YASK MCP Integration Templates and Guidelines
version: 6.0.0
---

# YASK MCP Integration Templates and Guidelines

This document provides practical templates and guidelines for implementing MCP tool integrations with YASK while maintaining its core simplicity and flexibility.

## Integration Template Structure

### Template 1: Basic Integration Skeleton

```python
# .yask/integrations/template_basic_integration.py
"""
Basic MCP Integration Template for YASK

This template demonstrates the minimal structure needed to add
optional MCP tool integration to YASK without compromising core functionality.
"""

import os
from typing import Dict, Any, Optional
from pathlib import Path

class BasicMCPIntegration:
    """
    Template for basic MCP tool integration
    
    Key principles:
    - Optional enhancement (disabled by default)
    - Graceful degradation when unavailable
    - No impact on core YASK workflow
    - Clear status reporting
    """
    
    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        self.status = "disabled"
        self.tool_available = False
        
        if enabled:
            self._initialize()
    
    def _initialize(self):
        """Initialize the integration (optional enhancement)"""
        try:
            # Check if required tools are available
            self.tool_available = self._check_tool_availability()
            
            if self.tool_available:
                self.status = "enabled"
                print(f"✅ {self.__class__.__name__} initialized successfully")
            else:
                self.status = "unavailable"
                print(f"⚠️  {self.__class__.__name__} tools not available - running without enhancement")
                
        except Exception as e:
            self.status = "error"
            self.tool_available = False
            print(f"❌ {self.__class__.__name__} initialization failed: {e}")
    
    def _check_tool_availability(self) -> bool:
        """Check if required tools are available on the system"""
        # Override this method in specific integrations
        # Return True if tools are available, False otherwise
        return False
    
    def enhance_validation(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enhance core YASK validation with optional analysis
        
        Args:
            core_result: Result from core YASK validation
            
        Returns:
            Enhanced result with optional analysis
        """
        if not self.enabled or not self.tool_available:
            return {
                **core_result,
                "enhancement_status": "disabled",
                "enhancement_message": f"{self.__class__.__name__} not enabled or available"
            }
        
        try:
            # Perform enhanced analysis
            enhancement_result = self._perform_enhancement(core_result)
            
            return {
                **core_result,
                "enhancement_status": "applied",
                "enhancement_data": enhancement_result
            }
            
        except Exception as e:
            return {
                **core_result,
                "enhancement_status": "error",
                "enhancement_error": str(e)
            }
    
    def _perform_enhancement(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """Perform the specific enhancement analysis"""
        # Override this method in specific integrations
        return {"message": "Enhancement not implemented"}
    
    def get_status(self) -> Dict[str, Any]:
        """Get current integration status"""
        return {
            "integration_name": self.__class__.__name__,
            "enabled": self.enabled,
            "available": self.tool_available,
            "status": self.status
        }

# Convenience function for easy integration
def create_basic_integration(integration_name: str, enabled: bool = False) -> BasicMCPIntegration:
    """Create a basic integration instance"""
    return BasicMCPIntegration(enabled=enabled)
```

### Template 2: Tree-Sitter Integration Template

```python
# .yask/integrations/template_treesitter_integration.py
"""
Tree-Sitter Integration Template for YASK

Provides enhanced code analysis capabilities while maintaining
core YASK simplicity and flexibility.
"""

import os
import subprocess
from typing import Dict, List, Any, Optional
from pathlib import Path

class TreeSitterIntegration:
    """
    Tree-Sitter integration for enhanced code analysis
    
    Features:
    - Syntax validation for multiple languages
    - Code complexity analysis
    - Pattern recognition
    - Requirement coverage checking
    """
    
    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        self.parser = None
        self.supported_languages = ['python', 'javascript', 'typescript', 'rust', 'go']
        
        if enabled:
            self._initialize()
    
    def _initialize(self):
        """Initialize Tree-Sitter parser"""
        try:
            # Check if Tree-Sitter is available
            if not self._check_treesitter_available():
                print("Tree-Sitter not available - code analysis disabled")
                return
            
            # Initialize parser (placeholder - would need actual Tree-Sitter setup)
            self.parser = self._create_parser()
            print("✅ Tree-Sitter integration initialized")
            
        except Exception as e:
            print(f"❌ Tree-Sitter initialization failed: {e}")
    
    def _check_treesitter_available(self) -> bool:
        """Check if Tree-Sitter is available"""
        try:
            # Check for tree-sitter command
            result = subprocess.run(['tree-sitter', '--version'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def _create_parser(self):
        """Create Tree-Sitter parser (placeholder)"""
        # In actual implementation, this would:
        # 1. Load Tree-Sitter language libraries
        # 2. Create parser instances for supported languages
        # 3. Set up parsing configurations
        return {"status": "placeholder_parser"}
    
    def analyze_code_file(self, file_path: Path, requirements: List[str]) -> Dict[str, Any]:
        """
        Analyze a code file against requirements
        
        Args:
            file_path: Path to the code file
            requirements: List of requirement strings
            
        Returns:
            Analysis results
        """
        if not self.enabled or not self.parser:
            return {
                "status": "disabled",
                "message": "Tree-Sitter integration not enabled or available"
            }
        
        try:
            # Determine file language
            language = self._detect_language(file_path)
            
            if language not in self.supported_languages:
                return {
                    "status": "unsupported_language",
                    "language": language,
                    "supported_languages": self.supported_languages
                }
            
            # Perform analysis
            analysis_result = {
                "file_path": str(file_path),
                "language": language,
                "syntax_valid": self._validate_syntax(file_path, language),
                "complexity_score": self._calculate_complexity(file_path, language),
                "requirement_coverage": self._check_requirement_coverage(file_path, requirements, language),
                "patterns_found": self._identify_patterns(file_path, language),
                "suggestions": self._generate_suggestions(file_path, requirements, language)
            }
            
            return {
                "status": "analyzed",
                "analysis": analysis_result
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Analysis failed: {str(e)}"
            }
    
    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language from file extension"""
        extension_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.tsx': 'typescript',
            '.rs': 'rust',
            '.go': 'go',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.h': 'c'
        }
        
        return extension_map.get(file_path.suffix, 'unknown')
    
    def _validate_syntax(self, file_path: Path, language: str) -> bool:
        """Validate syntax using Tree-Sitter (placeholder)"""
        # In actual implementation, would use Tree-Sitter to parse and validate
        try:
            content = file_path.read_text()
            # Placeholder: assume syntax is valid if file can be read
            return True
        except Exception:
            return False
    
    def _calculate_complexity(self, file_path: Path, language: str) -> int:
        """Calculate code complexity score (placeholder)"""
        # In actual implementation, would analyze AST for complexity metrics
        try:
            content = file_path.read_text()
            # Simple placeholder: count lines as complexity proxy
            return len(content.splitlines())
        except Exception:
            return 0
    
    def _check_requirement_coverage(self, file_path: Path, requirements: List[str], language: str) -> Dict[str, bool]:
        """Check which requirements are addressed in the code"""
        coverage = {}
        
        try:
            content = file_path.read_text().lower()
            
            for req in requirements:
                # Simple keyword matching (placeholder for actual analysis)
                req_words = req.lower().split()
                matches = sum(1 for word in req_words if word in content)
                coverage[req] = matches > 0
                
        except Exception:
            # If file can't be read, mark all requirements as not covered
            coverage = {req: False for req in requirements}
        
        return coverage
    
    def _identify_patterns(self, file_path: Path, language: str) -> List[str]:
        """Identify design patterns in the code (placeholder)"""
        # In actual implementation, would analyze AST for known patterns
        patterns = []
        
        try:
            content = file_path.read_text()
            
            # Simple pattern detection (placeholder)
            if 'class ' in content:
                patterns.append('object_oriented')
            if 'def ' in content and 'return' in content:
                patterns.append('functional')
            if 'import ' in content or 'from ' in content:
                patterns.append('modular')
                
        except Exception:
            pass
        
        return patterns
    
    def _generate_suggestions(self, file_path: Path, requirements: List[str], language: str) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        
        try:
            content = file_path.read_text()
            
            # Basic suggestions based on common issues
            lines = content.splitlines()
            
            if len(lines) > 100:
                suggestions.append("Consider breaking this file into smaller modules")
            
            if 'TODO' in content or 'FIXME' in content:
                suggestions.append("Address TODO/FIXME comments before finalizing")
            
            if language == 'python' and 'print(' in content:
                suggestions.append("Consider using proper logging instead of print statements")
                
        except Exception:
            pass
        
        return suggestions

# Convenience function
def create_treesitter_integration(enabled: bool = False) -> TreeSitterIntegration:
    """Create Tree-Sitter integration instance"""
    return TreeSitterIntegration(enabled=enabled)
```

### Template 3: Code Health Integration Template

```python
# .yask/integrations/template_codehealth_integration.py
"""
Code Health Integration Template for YASK

Provides multi-language code quality analysis while maintaining
YASK's core simplicity and optional enhancement approach.
"""

import subprocess
import json
import os
from typing import Dict, List, Any, Optional
from pathlib import Path

class CodeHealthIntegration:
    """
    Code health analysis integration for multiple languages
    
    Features:
    - Multi-language support (TypeScript, Python, Rust, Go)
    - Tool availability detection
    - Configurable analysis strictness
    - Performance impact monitoring
    """
    
    def __init__(self, enabled: bool = False, strictness: str = "standard"):
        self.enabled = enabled
        self.strictness = strictness  # basic, standard, strict
        self.language_tools = {
            'typescript': self._analyze_typescript,
            'javascript': self._analyze_javascript,
            'python': self._analyze_python,
            'rust': self._analyze_rust,
            'go': self._analyze_go
        }
        
        if enabled:
            self._initialize()
    
    def _initialize(self):
        """Initialize code health analysis tools"""
        try:
            # Check tool availability
            available_tools = self._check_tool_availability()
            
            if not available_tools:
                print("No code health tools available - analysis disabled")
                return
            
            print(f"✅ Code health integration initialized with tools: {available_tools}")
            
        except Exception as e:
            print(f"❌ Code health initialization failed: {e}")
    
    def _check_tool_availability(self) -> List[str]:
        """Check which analysis tools are available"""
        tools_to_check = {
            'typescript': ['tsc', 'eslint'],
            'javascript': ['eslint'],
            'python': ['flake8', 'pylint', 'black', 'mypy'],
            'rust': ['cargo', 'clippy'],
            'go': ['go', 'golint', 'govet']
        }
        
        available = []
        
        for language, tools in tools_to_check.items():
            for tool in tools:
                if self._command_available(tool):
                    available.append(f"{language}:{tool}")
        
        return available
    
    def _command_available(self, command: str) -> bool:
        """Check if a command is available in PATH"""
        try:
            subprocess.run([command, '--version'], 
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def analyze_project(self, project_path: Path) -> Dict[str, Any]:
        """
        Analyze project code health
        
        Args:
            project_path: Root path of the project
            
        Returns:
            Comprehensive analysis results
        """
        if not self.enabled:
            return {
                "status": "disabled",
                "message": "Code health analysis not enabled"
            }
        
        try:
            # Detect languages in project
            languages = self._detect_languages(project_path)
            
            if not languages:
                return {
                    "status": "no_languages_detected",
                    "message": "No supported languages found in project"
                }
            
            # Analyze each language
            language_results = {}
            for language in languages:
                if language in self.language_tools:
                    try:
                        result = self.language_tools[[language|project_path]]
                        language_results[language] = result
                    except Exception as e:
                        language_results[language] = {
                            "status": "error",
                            "message": str(e)
                        }
            
            # Calculate overall health score
            overall_health = self._calculate_overall_health(language_results)
            
            return {
                "status": "analyzed",
                "project_path": str(project_path),
                "detected_languages": languages,
                "language_results": language_results,
                "overall_health": overall_health,
                "analysis_strictness": self.strictness
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Project analysis failed: {str(e)}"
            }
    
    def _detect_languages(self, project_path: Path) -> List[str]:
        """Detect programming languages in the project"""
        language_extensions = {
            'typescript': ['.ts', '.tsx'],
            'javascript': ['.js', '.jsx'],
            'python': ['.py'],
            'rust': ['.rs'],
            'go': ['.go']
        }
        
        detected = []
        
        for language, extensions in language_extensions.items():
            for ext in extensions:
                if any(project_path.rglob(f"*{ext}")):
                    detected.append(language)
                    break
        
        return detected
    
    def _analyze_typescript(self, project_path: Path) -> Dict[str, Any]:
        """Analyze TypeScript code health"""
        result = {
            "language": "typescript",
            "status": "analyzed",
            "issues": [],
            "metrics": {},
            "tools_used": []
        }
        
        try:
            # TypeScript compiler check
            if self._command_available('tsc'):
                tsc_result = subprocess.run(
                    ['tsc', '--noEmit', '--pretty'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                
                result["tools_used"].append("tsc")
                
                if tsc_result.returncode != 0:
                    result["issues"].append({
                        "tool": "tsc",
                        "type": "type_error",
                        "output": tsc_result.stderr
                    })
                
                result["metrics"]["type_check_passed"] = tsc_result.returncode == 0
            
            # ESLint check
            if self._command_available('eslint'):
                eslint_result = subprocess.run(
                    ['eslint', '.', '--format=json'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                
                result["tools_used"].append("eslint")
                
                if eslint_result.returncode == 0:
                    try:
                        eslint_data = json.loads(eslint_result.stdout)
                        result["metrics"]["eslint_issues"] = len(eslint_data)
                    except json.JSONDecodeError:
                        pass
                else:
                    result["issues"].append({
                        "tool": "eslint",
                        "type": "lint_error",
                        "output": eslint_result.stderr
                    })
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)
        
        return result
    
    def _analyze_javascript(self, project_path: Path) -> Dict[str, Any]:
        """Analyze JavaScript code health"""
        # Similar to TypeScript but without type checking
        result = {
            "language": "javascript",
            "status": "analyzed",
            "issues": [],
            "metrics": {},
            "tools_used": []
        }
        
        try:
            # ESLint check
            if self._command_available('eslint'):
                eslint_result = subprocess.run(
                    ['eslint', '.', '--format=json'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                
                result["tools_used"].append("eslint")
                
                if eslint_result.returncode == 0:
                    try:
                        eslint_data = json.loads(eslint_result.stdout)
                        result["metrics"]["eslint_issues"] = len(eslint_data)
                    except json.JSONDecodeError:
                        pass
                else:
                    result["issues"].append({
                        "tool": "eslint",
                        "type": "lint_error",
                        "output": eslint_result.stderr
                    })
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)
        
        return result
    
    def _analyze_python(self, project_path: Path) -> Dict[str, Any]:
        """Analyze Python code health"""
        result = {
            "language": "python",
            "status": "analyzed",
            "issues": [],
            "metrics": {},
            "tools_used": []
        }
        
        python_tools = ['flake8', 'pylint', 'black', 'mypy']
        
        for tool in python_tools:
            if self._command_available(tool):
                try:
                    tool_result = subprocess.run(
                        [tool, '.'],
                        cwd=project_path,
                        capture_output=True,
                        text=True
                    )
                    
                    result["tools_used"].append(tool)
                    
                    if tool_result.stdout or tool_result.stderr:
                        result["issues"].append({
                            "tool": tool,
                            "output": tool_result.stdout + tool_result.stderr
                        })
                    
                    result["metrics"][f"{tool}_passed"] = tool_result.returncode == 0
                    
                except Exception as e:
                    result["issues"].append({
                        "tool": tool,
                        "error": str(e)
                    })
        
        return result
    
    def _analyze_rust(self, project_path: Path) -> Dict[str, Any]:
        """Analyze Rust code health"""
        result = {
            "language": "rust",
            "status": "analyzed",
            "issues": [],
            "metrics": {},
            "tools_used": []
        }
        
        try:
            # Check if this is a Rust project
            if not (project_path / 'Cargo.toml').exists():
                result["status"] = "not_rust_project"
                return result
            
            # Cargo check
            cargo_result = subprocess.run(
                ['cargo', 'check'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            result["tools_used"].append("cargo")
            
            if cargo_result.returncode != 0:
                result["issues"].append({
                    "tool": "cargo",
                    "type": "compilation_error",
                    "output": cargo_result.stderr
                })
            
            result["metrics"]["cargo_check_passed"] = cargo_result.returncode == 0
            
            # Clippy check
            if self._command_available('clippy'):
                clippy_result = subprocess.run(
                    ['cargo', 'clippy'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                
                result["tools_used"].append("clippy")
                
                if clippy_result.stdout or clippy_result.stderr:
                    result["issues"].append({
                        "tool": "clippy",
                        "type": "lint_warnings",
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
            "metrics": {},
            "tools_used": []
        }
        
        try:
            # Go vet
            vet_result = subprocess.run(
                ['go', 'vet', './...'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            result["tools_used"].append("go vet")
            
            if vet_result.stdout or vet_result.stderr:
                result["issues"].append({
                    "tool": "go vet",
                    "output": vet_result.stdout + vet_result.stderr
                })
            
            result["metrics"]["go_vet_passed"] = vet_result.returncode == 0
            
            # Golint (if available)
            if self._command_available('golint'):
                golint_result = subprocess.run(
                    ['golint', './...'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                
                result["tools_used"].append("golint")
                
                if golint_result.stdout:
                    result["issues"].append({
                        "tool": "golint",
                        "output": golint_result.stdout
                    })
            
        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)
        
        return result
    
    def _calculate_overall_health(self, language_results: Dict[str, Any]) -> str:
        """Calculate overall project health score"""
        if not language_results:
            return "no_analysis"
        
        total_issues = 0
        analyzed_languages = 0
        
        for language, result in language_results.items():
            if isinstance(result, dict) and result.get("status") == "analyzed":
                analyzed_languages += 1
                total_issues += len(result.get("issues", []))
        
        if analyzed_languages == 0:
            return "no_analysis"
        
        # Calculate average issues per language
        avg_issues = total_issues / analyzed_languages
        
        if avg_issues == 0:
            return "excellent"
        elif avg_issues < 3:
            return "good"
        elif avg_issues < 8:
            return "fair"
        else:
            return "needs_attention"

# Convenience function
def create_codehealth_integration(enabled: bool = False, strictness: str = "standard") -> CodeHealthIntegration:
    """Create code health integration instance"""
    return CodeHealthIntegration(enabled=enabled, strictness=strictness)
```

## Integration Guidelines

### 1. Design Principles

#### Core Principles
- **Optional Enhancement**: All integrations disabled by default
- **Graceful Degradation**: System functions normally when integrations fail
- **Non-Intrusive**: Core YASK workflow unchanged
- **Clear Status**: Always report integration status clearly
- **Performance Conscious**: Minimize impact on development workflow

#### Implementation Guidelines
```python
# ✅ Good: Optional enhancement with clear status
def enhance_validation(self, core_result):
    if not self.enabled:
        return {**core_result, "enhancement": "disabled"}
    
    try:
        enhancement = self._perform_analysis()
        return {**core_result, "enhancement": "applied", "data": enhancement}
    except Exception as e:
        return {**core_result, "enhancement": "error", "error": str(e)}

# ❌ Bad: Breaking core functionality
def enhance_validation(self, core_result):
    if not self.enabled:
        raise Exception("Integration required but not enabled")
    
    # This would break YASK's core functionality
```

### 2. Configuration Management

#### Environment-Based Configuration
```bash
# Enable integrations via environment variables
export YASK_ENABLE_TREESITTER=true
export YASK_ENABLE_CODE_HEALTH=true
export YASK_ENABLE_DOC_VALIDATION=true

# Configure strictness levels
export YASK_CODE_HEALTH_STRICTNESS=standard  # basic, standard, strict
export YASK_TREESITTER_TIMEOUT=30
```

#### Configuration File Support
```yaml
# .yask/integrations.yaml
integrations:
  tree_sitter:
    enabled: false
    languages: [python, javascript, typescript]
    timeout: 30
  
  code_health:
    enabled: false
    strictness: standard
    tools:
      typescript: true
      python: true
  
  documentation:
    enabled: false
    consistency_check: true
```

### 3. Error Handling Patterns

#### Safe Integration Calls
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
result = safe_integration_call(analyze_with_treesitter, file_path, requirements)
```

#### Status Reporting
```python
def get_integration_status():
    """Get comprehensive integration status"""
    return {
        "tree_sitter": {
            "enabled": os.getenv('YASK_ENABLE_TREESITTER') == 'true',
            "available": check_treesitter_available(),
            "status": "ready" if check_treesitter_available() else "unavailable"
        },
        "code_health": {
            "enabled": os.getenv('YASK_ENABLE_CODE_HEALTH') == 'true',
            "available": check_code_health_tools(),
            "status": "ready" if check_code_health_tools() else "unavailable"
        }
    }
```

### 4. Performance Considerations

#### Async Processing
```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def enhanced_analysis_async(core_result, integrations):
    """Perform enhanced analysis asynchronously"""
    tasks = []
    
    for integration_name, integration in integrations.items():
        if integration.enabled:
            task = asyncio.create_task(
                run_integration_async(integration, core_result)
            )
            tasks.append((integration_name, task))
    
    # Wait for all integrations with timeout
    results = {}
    for name, task in tasks:
        try:
            results[name] = await asyncio.wait_for(task, timeout=30.0)
        except asyncio.TimeoutError:
            results[name] = {"status": "timeout", "message": "Analysis timed out"}
    
    return results
```

#### Caching Results
```python
import hashlib
import json
from functools import lru_cache

class CachedIntegration:
    def __init__(self):
        self.cache = {}
    
    def _get_cache_key(self, file_path, requirements):
        """Generate cache key for analysis results"""
        content = file_path.read_text() if file_path.exists() else ""
        req_hash = hashlib.md5(json.dumps(requirements, sort_keys=True).encode()).hexdigest()
        return f"{file_path}:{req_hash}:{hashlib.md5(content.encode()).hexdigest()}"
    
    def analyze_with_cache(self, file_path, requirements):
        """Analyze with caching to improve performance"""
        cache_key = self._get_cache_key(file_path, requirements)
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = self._perform_analysis(file_path, requirements)
        self.cache[cache_key] = result
        return result
```

### 5. Testing Integration Templates

#### Unit Test Template
```python
# test_integration_template.py
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path

class TestBasicIntegration(unittest.TestCase):
    def setUp(self):
        self.integration = BasicMCPIntegration(enabled=True)
    
    def test_integration_disabled_by_default(self):
        integration = BasicMCPIntegration()
        self.assertFalse(integration.enabled)
        self.assertEqual(integration.status, "disabled")
    
    def test_integration_status_reporting(self):
        status = self.integration.get_status()
        self.assertIn("integration_name", status)
        self.assertIn("enabled", status)
        self.assertIn("status", status)
    
    def test_enhancement_with_disabled_integration(self):
        core_result = {"file_exists": True}
        enhanced = self.integration.enhance_validation(core_result)
        
        self.assertEqual(enhanced["enhancement_status"], "disabled")
        self.assertIn("enhancement_message", enhanced)

class TestTreeSitterIntegration(unittest.TestCase):
    def setUp(self):
        self.integration = TreeSitterIntegration(enabled=True)
        self.test_file = Path("/tmp/test.py")
        self.test_file.write_text("print('hello world')")
    
    def test_language_detection(self):
        language = self.integration._detect_language(self.test_file)
        self.assertEqual(language, "python")
    
    def test_analysis_with_disabled_integration(self):
        result = self.integration.analyze_code_file(self.test_file, ["test requirement"])
        self.assertEqual(result["status"], "disabled")
    
    def tearDown(self):
        if self.test_file.exists():
            self.test_file.unlink()

if __name__ == '__main__':
    unittest.main()
```

#### Integration Test Template
```python
# test_integration_workflow.py
import os
import tempfile
from pathlib import Path

def test_enhanced_yask_workflow():
    """Test YASK workflow with and without integrations"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir)
        
        # Create test project structure
        (project_path / "requirements.md").write_text("# Test Requirements")
        (project_path / "design.md").write_text("# Test Design")
        (project_path / "implementation.py").write_text("def hello(): return 'world'")
        
        # Test without integrations
        os.environ['YASK_ENABLE_TREESITTER'] = 'false'
        os.environ['YASK_ENABLE_CODE_HEALTH'] = 'false'
        
        workflow = EnhancedYASKWorkflow(project_path)
        result_basic = workflow.enhanced_project_analysis()
        
        assert result_basic["overall_health"] == "basic"
        assert len(result_basic["enhancements"]) == 0
        
        # Test with integrations enabled
        os.environ['YASK_ENABLE_TREESITTER'] = 'true'
        os.environ['YASK_ENABLE_CODE_HEALTH'] = 'true'
        
        workflow = EnhancedYASKWorkflow(project_path)
        result_enhanced = workflow.enhanced_project_analysis()
        
        # Should have enhancements (even if they fail gracefully)
        assert "enhancements" in result_enhanced
```

### 6. Documentation Templates

#### Integration README Template
```markdown
# [Integration Name] for YASK

## Overview
Brief description of what this integration adds to YASK.

## Features
- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Installation
```bash
# Install required tools
[installation commands]

# Enable integration
export YASK_ENABLE_[INTEGRATION]=true
```

## Configuration
```yaml
# .yask/integrations.yaml
integrations:
  [integration_name]:
    enabled: true
    # configuration options
```

## Usage Examples
```python
# Basic usage
integration = create_[[integration_name|enabled=True]]
result = integration.enhance_validation(core_result)

# Advanced usage
result = integration.analyze_[[target|[parameters]]]
```

## Status Reporting
The integration provides clear status reporting:
- `disabled`: Integration not enabled
- `available`: Tools available and ready
- `error`: Integration failed to initialize
- `analyzed`: Analysis completed successfully

## Performance Considerations
- Analysis time: ~X seconds for typical projects
- Memory usage: ~X MB additional
- CPU impact: Minimal (background processing)

## Troubleshooting
Common issues and solutions:
1. **Issue**: Tools not found
   **Solution**: Install required tools and ensure they're in PATH
   
2. **Issue**: Analysis timeout
   **Solution**: Increase timeout configuration or reduce scope

## Contributing
Guidelines for contributing to this integration.
```

### 7. Migration Guide Template

```markdown
# Migration Guide: Adding [Integration Name] to YASK

## Before (Core YASK Only)
```python
# Standard YASK validation
def validate_implementation(file_path, requirements):
    return {
        "file_exists": file_path.exists(),
        "file_readable": os.access(file_path, os.R_OK)
    }
```

## After (With Integration)
```python
# Enhanced YASK validation
def validate_implementation(file_path, requirements):
    # Core validation (always available)
    core_result = {
        "file_exists": file_path.exists(),
        "file_readable": os.access(file_path, os.R_OK)
    }
    
    # Optional enhancement
    if is_integration_enabled("[integration]"):
        enhancement = analyze_with_[[integration|file_path, requirements]]
        core_result["enhancement"] = enhancement
    
    return core_result
```

## Step-by-Step Migration
1. **Install Integration**: [installation steps]
2. **Enable Integration**: Set environment variable or config
3. **Test Integration**: Verify tools are available
4. **Update Code**: Add enhancement calls where beneficial
5. **Monitor Performance**: Ensure no negative impact

## Backward Compatibility
- All existing YASK code continues to work unchanged
- Integrations are purely additive enhancements
- Core functionality unaffected by integration status
```

These templates and guidelines provide a comprehensive foundation for implementing MCP tool integrations with YASK while maintaining its core principles of simplicity, flexibility, and optional enhancement.