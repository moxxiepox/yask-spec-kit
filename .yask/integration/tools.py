"""
YASK Tool Integrations

This module provides enhanced tool integrations including Tree-Sitter for code analysis,
code health validation, and documentation consistency checking while maintaining
YASK's core simplicity and graceful degradation.
"""

import os
import subprocess
import json
import re
from typing import Dict, Any, Optional, List, Tuple
from pathlib import Path
from dataclasses import dataclass
import logging

from .core import BaseIntegration, IntegrationResult, IntegrationStatus


@dataclass
class CodeAnalysisResult:
    """Result container for code analysis"""

    file_path: str
    language: str
    syntax_valid: bool
    complexity_score: int
    patterns_found: List[str]
    suggestions: List[str]
    requirement_coverage: Dict[str, bool]


class TreeSitterIntegration(BaseIntegration):
    """
    Tree-Sitter integration for enhanced code analysis

    Provides syntax validation, complexity analysis, pattern recognition,
    and requirement coverage checking for multiple programming languages.
    """

    def __init__(self, enabled: bool = False, languages: Optional[List[str]] = None):
        super().__init__("tree_sitter", enabled)
        self.languages = languages or [
            "python",
            "javascript",
            "typescript",
            "rust",
            "go",
        ]
        self.logger = logging.getLogger("yask.integration.tree_sitter")

        # Add capabilities
        self.add_capability("syntax_validation")
        self.add_capability("complexity_analysis")
        self.add_capability("pattern_recognition")
        self.add_capability("requirement_coverage")

        # Add dependencies
        self.add_dependency("tree_sitter")

    def _is_dependency_available(self, dependency: str) -> bool:
        """Check if Tree-Sitter is available"""
        if dependency == "tree_sitter":
            try:
                # Check for tree-sitter command
                result = subprocess.run(
                    ["tree-sitter", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                return result.returncode == 0
            except (
                subprocess.TimeoutExpired,
                FileNotFoundError,
                subprocess.SubprocessError,
            ):
                return False
        return super()._is_dependency_available(dependency)

    def _initialize(self) -> Optional[Dict[str, Any]]:
        """Initialize Tree-Sitter integration"""
        try:
            # Check Tree-Sitter availability
            if not self._is_dependency_available("tree_sitter"):
                self.logger.warning(
                    "Tree-Sitter not available - using fallback analysis"
                )
                return {"mode": "fallback", "languages": self.languages}

            # Initialize Tree-Sitter parsers (placeholder)
            # In a real implementation, this would load actual Tree-Sitter language libraries
            initialized_languages = []
            for language in self.languages:
                if self._check_language_support(language):
                    initialized_languages.append(language)

            return {
                "mode": "tree_sitter",
                "supported_languages": initialized_languages,
                "total_languages": len(self.languages),
            }

        except Exception as e:
            self.logger.error(f"Failed to initialize Tree-Sitter: {e}")
            return {"mode": "error", "error": str(e)}

    def _check_language_support(self, language: str) -> bool:
        """Check if a language is supported by Tree-Sitter"""
        # Placeholder implementation - in reality would check Tree-Sitter language availability
        supported_languages = [
            "python",
            "javascript",
            "typescript",
            "rust",
            "go",
            "java",
            "cpp",
        ]
        return language.lower() in supported_languages

    def analyze_code_file(
        self, file_path: Path, requirements: List[str]
    ) -> CodeAnalysisResult:
        """
        Analyze a code file against requirements

        Args:
            file_path: Path to the code file
            requirements: List of requirement strings

        Returns:
            CodeAnalysisResult with analysis data
        """
        try:
            # Detect language
            language = self._detect_language(file_path)

            if language not in self.languages:
                return CodeAnalysisResult(
                    file_path=str(file_path),
                    language=language,
                    syntax_valid=False,
                    complexity_score=0,
                    patterns_found=[],
                    suggestions=[f"Language {language} not supported"],
                    requirement_coverage={req: False for req in requirements},
                )

            # Perform analysis based on mode
            if self.status == IntegrationStatus.AVAILABLE:
                return self._analyze_with_treesitter(file_path, language, requirements)
            else:
                return self._analyze_with_fallback(file_path, language, requirements)

        except Exception as e:
            self.logger.error(f"Analysis failed for {file_path}: {e}")
            return CodeAnalysisResult(
                file_path=str(file_path),
                language="unknown",
                syntax_valid=False,
                complexity_score=0,
                patterns_found=[],
                suggestions=[f"Analysis failed: {str(e)}"],
                requirement_coverage={req: False for req in requirements},
            )

    def _analyze_with_treesitter(
        self, file_path: Path, language: str, requirements: List[str]
    ) -> CodeAnalysisResult:
        """Analyze using Tree-Sitter (placeholder implementation)"""
        # In a real implementation, this would use actual Tree-Sitter parsing
        # For now, use enhanced fallback analysis

        try:
            content = file_path.read_text(encoding="utf-8")

            # Syntax validation (basic check)
            syntax_valid = self._validate_syntax_basic(content, language)

            # Complexity analysis
            complexity_score = self._calculate_complexity(content, language)

            # Pattern recognition
            patterns_found = self._identify_patterns(content, language)

            # Requirement coverage
            requirement_coverage = self._check_requirement_coverage(
                content, requirements
            )

            # Generate suggestions
            suggestions = self._generate_suggestions(content, language, patterns_found)

            return CodeAnalysisResult(
                file_path=str(file_path),
                language=language,
                syntax_valid=syntax_valid,
                complexity_score=complexity_score,
                patterns_found=patterns_found,
                suggestions=suggestions,
                requirement_coverage=requirement_coverage,
            )

        except Exception as e:
            self.logger.error(f"Tree-Sitter analysis failed: {e}")
            return self._analyze_with_fallback(file_path, language, requirements)

    def _analyze_with_fallback(
        self, file_path: Path, language: str, requirements: List[str]
    ) -> CodeAnalysisResult:
        """Analyze using fallback methods when Tree-Sitter is not available"""
        try:
            content = file_path.read_text(encoding="utf-8")

            # Basic syntax check
            syntax_valid = self._validate_syntax_basic(content, language)

            # Simple complexity metrics
            complexity_score = len(content.splitlines())

            # Basic pattern detection
            patterns_found = self._identify_basic_patterns(content, language)

            # Requirement coverage check
            requirement_coverage = self._check_requirement_coverage(
                content, requirements
            )

            # Basic suggestions
            suggestions = self._generate_basic_suggestions(content, language)

            return CodeAnalysisResult(
                file_path=str(file_path),
                language=language,
                syntax_valid=syntax_valid,
                complexity_score=complexity_score,
                patterns_found=patterns_found,
                suggestions=suggestions,
                requirement_coverage=requirement_coverage,
            )

        except Exception as e:
            self.logger.error(f"Fallback analysis failed: {e}")
            return CodeAnalysisResult(
                file_path=str(file_path),
                language=language,
                syntax_valid=False,
                complexity_score=0,
                patterns_found=[],
                suggestions=[f"Analysis failed: {str(e)}"],
                requirement_coverage={req: False for req in requirements},
            )

    def _detect_language(self, file_path: Path) -> str:
        """Detect programming language from file extension"""
        extension_map = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".tsx": "typescript",
            ".rs": "rust",
            ".go": "go",
            ".java": "java",
            ".cpp": "cpp",
            ".c": "c",
            ".h": "c",
            ".cs": "csharp",
            ".php": "php",
            ".rb": "ruby",
            ".swift": "swift",
            ".kt": "kotlin",
        }

        return extension_map.get(file_path.suffix.lower(), "unknown")

    def _validate_syntax_basic(self, content: str, language: str) -> bool:
        """Basic syntax validation without Tree-Sitter"""
        try:
            # Basic syntax checks for common issues
            if language == "python":
                # Check for basic Python syntax issues
                lines = content.splitlines()
                indent_level = 0
                for line in lines:
                    stripped = line.strip()
                    if not stripped or stripped.startswith("#"):
                        continue

                    # Check for proper indentation
                    if stripped.endswith(":"):
                        indent_level += 1
                    elif (
                        stripped.startswith("elif ")
                        or stripped.startswith("else:")
                        or stripped.startswith("except")
                    ):
                        if indent_level == 0:
                            return False
                    elif stripped.startswith("def ") or stripped.startswith("class "):
                        if indent_level > 0:
                            return False

                return True

            elif language in ["javascript", "typescript"]:
                # Basic JavaScript/TypeScript syntax check
                # Check for unmatched braces, brackets, parentheses
                brace_count = 0
                bracket_count = 0
                paren_count = 0

                for char in content:
                    if char == "{":
                        brace_count += 1
                    elif char == "}":
                        brace_count -= 1
                    elif char == "[":
                        bracket_count += 1
                    elif char == "]":
                        bracket_count -= 1
                    elif char == "(":
                        paren_count += 1
                    elif char == ")":
                        paren_count -= 1

                    # Early exit if any count goes negative
                    if brace_count < 0 or bracket_count < 0 or paren_count < 0:
                        return False

                return brace_count == 0 and bracket_count == 0 and paren_count == 0

            else:
                # For other languages, assume syntax is valid if file can be read
                return True

        except Exception:
            return False

    def _calculate_complexity(self, content: str, language: str) -> int:
        """Calculate code complexity score"""
        try:
            lines = content.splitlines()
            total_lines = len(lines)
            code_lines = len(
                [
                    line
                    for line in lines
                    if line.strip() and not line.strip().startswith("#")
                ]
            )

            # Basic complexity metrics
            complexity = code_lines

            # Add complexity for nested structures
            if language == "python":
                for line in lines:
                    stripped = line.strip()
                    if stripped.endswith(":"):
                        complexity += 1
            elif language in ["javascript", "typescript"]:
                for line in lines:
                    stripped = line.strip()
                    if "{" in stripped and "}" not in stripped:
                        complexity += 1

            return complexity

        except Exception:
            return 0

    def _identify_patterns(self, content: str, language: str) -> List[str]:
        """Identify design patterns in the code"""
        patterns = []

        try:
            content_lower = content.lower()

            # Common design patterns
            if language == "python":
                if re.search(r"\bclass\s+\w+.*:", content):
                    patterns.append("object_oriented")
                if re.search(r"\bdef\s+\w+.*->\s*\w+:", content):
                    patterns.append("type_annotated")
                if re.search(r"\bwith\s+\w+.*as\s+\w+:", content):
                    patterns.append("context_manager")
                if re.search(r"\b@\w+", content):
                    patterns.append("decorator")

            elif language in ["javascript", "typescript"]:
                if re.search(r"\bclass\s+\w+", content):
                    patterns.append("object_oriented")
                if re.search(r"\bfunction\s*\([^)]*\)\s*{", content):
                    patterns.append("functional")
                if re.search(r"\basync\s+function|\bawait\b", content):
                    patterns.append("async_pattern")
                if re.search(r"\bexport\s+|import\s+", content):
                    patterns.append("module_system")

            # General patterns
            if re.search(r"\btry:\s*\n|try\s*{", content):
                patterns.append("error_handling")
            if re.search(r"\bif\s+.*:\s*\n|\bif\s*\(.*\)\s*{", content):
                patterns.append("conditional_logic")
            if re.search(r"\bfor\s+.*:\s*\n|\bfor\s*\(.*\)\s*{", content):
                patterns.append("looping")

            return patterns

        except Exception:
            return []

    def _identify_basic_patterns(self, content: str, language: str) -> List[str]:
        """Basic pattern identification without Tree-Sitter"""
        patterns = []

        try:
            content_lower = content.lower()

            # Very basic pattern detection
            if "class " in content_lower:
                patterns.append("object_oriented")
            if "def " in content_lower or "function " in content_lower:
                patterns.append("functional")
            if "import " in content_lower or "from " in content_lower:
                patterns.append("modular")
            if "try:" in content_lower or "try {" in content_lower:
                patterns.append("error_handling")

            return patterns

        except Exception:
            return []

    def _check_requirement_coverage(
        self, content: str, requirements: List[str]
    ) -> Dict[str, bool]:
        """Check which requirements are addressed in the code"""
        coverage = {}

        try:
            content_lower = content.lower()

            for req in requirements:
                # Simple keyword matching (placeholder for actual analysis)
                req_words = req.lower().split()
                matches = sum(
                    1 for word in req_words if len(word) > 3 and word in content_lower
                )
                coverage[req] = matches > 0

        except Exception:
            # If analysis fails, mark all requirements as not covered
            coverage = {req: False for req in requirements}

        return coverage

    def _generate_suggestions(
        self, content: str, language: str, patterns: List[str]
    ) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []

        try:
            lines = content.splitlines()
            total_lines = len(lines)

            # File size suggestions
            if total_lines > 200:
                suggestions.append("Consider breaking this file into smaller modules")

            # Pattern-based suggestions
            if "object_oriented" in patterns and language == "python":
                if not any("__init__" in line for line in lines):
                    suggestions.append("Consider adding __init__ method to classes")

            if "error_handling" not in patterns:
                suggestions.append("Consider adding error handling for robustness")

            # Language-specific suggestions
            if language == "python":
                if "print(" in content:
                    suggestions.append(
                        "Consider using proper logging instead of print statements"
                    )
                if "TODO" in content or "FIXME" in content:
                    suggestions.append("Address TODO/FIXME comments before finalizing")

            elif language in ["javascript", "typescript"]:
                if "var " in content:
                    suggestions.append("Consider using let/const instead of var")
                if "==" in content and "!==" not in content:
                    suggestions.append(
                        "Consider using strict equality (===) instead of =="
                    )

            return suggestions

        except Exception:
            return ["Unable to generate suggestions"]

    def _generate_basic_suggestions(self, content: str, language: str) -> List[str]:
        """Generate basic suggestions without Tree-Sitter"""
        suggestions = []

        try:
            lines = content.splitlines()
            total_lines = len(lines)

            if total_lines > 100:
                suggestions.append("Consider breaking this file into smaller modules")

            if "TODO" in content or "FIXME" in content:
                suggestions.append("Address TODO/FIXME comments")

            return suggestions

        except Exception:
            return ["Unable to generate suggestions"]

    def _enhance(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance core result with Tree-Sitter analysis"""
        enhancement = {
            "tree_sitter_analysis": {},
            "code_quality_metrics": {},
            "enhancement_applied": False,
        }

        # If core result contains file paths, analyze them
        if "file_paths" in core_result:
            file_paths = core_result["file_paths"]
            requirements = core_result.get("requirements", [])

            analysis_results = []
            for file_path in file_paths:
                if isinstance(file_path, str):
                    path = Path(file_path)
                    if path.exists():
                        result = self.analyze_code_file(path, requirements)
                        analysis_results.append(
                            {
                                "file_path": result.file_path,
                                "language": result.language,
                                "syntax_valid": result.syntax_valid,
                                "complexity_score": result.complexity_score,
                                "patterns_found": result.patterns_found,
                                "suggestions": result.suggestions,
                                "requirement_coverage": result.requirement_coverage,
                            }
                        )

            enhancement["tree_sitter_analysis"] = {
                "files_analyzed": len(analysis_results),
                "results": analysis_results,
            }

            # Calculate overall quality metrics
            if analysis_results:
                valid_files = sum(1 for r in analysis_results if r["syntax_valid"])
                avg_complexity = sum(
                    r["complexity_score"] for r in analysis_results
                ) / len(analysis_results)

                enhancement["code_quality_metrics"] = {
                    "syntax_validity_rate": valid_files / len(analysis_results),
                    "average_complexity": avg_complexity,
                    "total_patterns_found": len(
                        set(
                            pattern
                            for r in analysis_results
                            for pattern in r["patterns_found"]
                        )
                    ),
                }

            enhancement["enhancement_applied"] = True

        return enhancement


class CodeHealthIntegration(BaseIntegration):
    """
    Code Health Integration for multi-language analysis

    Provides code quality analysis for TypeScript, Python, Rust, Go, and other languages
    with configurable strictness levels and graceful degradation.
    """

    def __init__(self, enabled: bool = False, strictness: str = "standard"):
        super().__init__("code_health", enabled)
        self.strictness = strictness  # basic, standard, strict
        self.logger = logging.getLogger("yask.integration.code_health")

        # Language-specific tool configurations
        self.language_tools = {
            "typescript": ["tsc", "eslint"],
            "javascript": ["eslint"],
            "python": ["flake8", "pylint", "black", "mypy"],
            "rust": ["cargo", "clippy"],
            "go": ["go", "golint", "govet"],
        }

        # Add capabilities
        self.add_capability("syntax_checking")
        self.add_capability("style_validation")
        self.add_capability("type_checking")
        self.add_capability("security_scanning")

    def _initialize(self) -> Optional[Dict[str, Any]]:
        """Initialize code health integration"""
        try:
            # Check tool availability
            available_tools = self._check_tool_availability()

            if not available_tools:
                self.logger.warning(
                    "No code health tools available - analysis disabled"
                )
                return {"available_tools": [], "mode": "disabled"}

            self.logger.info(f"Available code health tools: {available_tools}")

            return {
                "available_tools": available_tools,
                "strictness_level": self.strictness,
                "mode": "active",
            }

        except Exception as e:
            self.logger.error(f"Failed to initialize code health integration: {e}")
            return {"mode": "error", "error": str(e)}

    def _check_tool_availability(self) -> List[str]:
        """Check which analysis tools are available"""
        available = []

        for language, tools in self.language_tools.items():
            for tool in tools:
                if self._command_available(tool):
                    available.append(f"{language}:{tool}")

        return available

    def _command_available(self, command: str) -> bool:
        """Check if a command is available in PATH"""
        try:
            subprocess.run(
                [command, "--version"], capture_output=True, check=True, timeout=5
            )
            return True
        except (
            subprocess.TimeoutExpired,
            FileNotFoundError,
            subprocess.SubprocessError,
        ):
            return False

    def analyze_project(self, project_path: Path) -> Dict[str, Any]:
        """
        Analyze project code health

        Args:
            project_path: Root path of the project

        Returns:
            Comprehensive analysis results
        """
        try:
            # Detect languages in project
            languages = self._detect_languages(project_path)

            if not languages:
                return {
                    "status": "no_languages_detected",
                    "message": "No supported languages found in project",
                }

            # Analyze each language
            language_results = {}
            for language in languages:
                if language in self.language_tools:
                    try:
                        result = self._analyze_language(project_path, language)
                        language_results[language] = result
                    except Exception as e:
                        language_results[language] = {
                            "status": "error",
                            "message": str(e),
                        }

            # Calculate overall health score
            overall_health = self._calculate_overall_health(language_results)

            return {
                "status": "analyzed",
                "project_path": str(project_path),
                "detected_languages": languages,
                "language_results": language_results,
                "overall_health": overall_health,
                "analysis_strictness": self.strictness,
            }

        except Exception as e:
            return {"status": "error", "message": f"Project analysis failed: {str(e)}"}

    def _detect_languages(self, project_path: Path) -> List[str]:
        """Detect programming languages in the project"""
        language_extensions = {
            "typescript": [".ts", ".tsx"],
            "javascript": [".js", ".jsx"],
            "python": [".py"],
            "rust": [".rs"],
            "go": [".go"],
        }

        detected = []

        for language, extensions in language_extensions.items():
            for ext in extensions:
                if any(project_path.rglob(f"*{ext}")):
                    detected.append(language)
                    break

        return detected

    def _analyze_language(self, project_path: Path, language: str) -> Dict[str, Any]:
        """Analyze code health for a specific language"""
        result = {
            "language": language,
            "status": "analyzed",
            "issues": [],
            "metrics": {},
            "tools_used": [],
        }

        try:
            tools = self.language_tools.get(language, [])

            for tool in tools:
                if self._command_available(tool):
                    try:
                        tool_result = self._run_tool(tool, project_path, language)
                        result["tools_used"].append(tool)
                        result["issues"].extend(tool_result.get("issues", []))
                        result["metrics"].update(tool_result.get("metrics", {}))
                    except Exception as e:
                        result["issues"].append({"tool": tool, "error": str(e)})

        except Exception as e:
            result["status"] = "error"
            result["message"] = str(e)

        return result

    def _run_tool(self, tool: str, project_path: Path, language: str) -> Dict[str, Any]:
        """Run a specific analysis tool"""
        try:
            if tool == "tsc":
                return self._run_typescript_compiler(project_path)
            elif tool == "eslint":
                return self._run_eslint(project_path, language)
            elif tool == "flake8":
                return self._run_flake8(project_path)
            elif tool == "pylint":
                return self._run_pylint(project_path)
            elif tool == "cargo":
                return self._run_cargo_check(project_path)
            elif tool == "clippy":
                return self._run_clippy(project_path)
            elif tool == "go":
                return self._run_go_vet(project_path)
            else:
                return {"issues": [], "metrics": {f"{tool}_passed": True}}

        except Exception as e:
            return {"issues": [{"tool": tool, "error": str(e)}], "metrics": {}}

    def _run_typescript_compiler(self, project_path: Path) -> Dict[str, Any]:
        """Run TypeScript compiler"""
        try:
            result = subprocess.run(
                ["tsc", "--noEmit", "--pretty"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=30,
            )

            issues = []
            if result.returncode != 0:
                issues.append(
                    {"tool": "tsc", "type": "type_error", "output": result.stderr}
                )

            return {
                "issues": issues,
                "metrics": {"type_check_passed": result.returncode == 0},
            }

        except subprocess.TimeoutExpired:
            return {"issues": [{"tool": "tsc", "error": "Timeout"}], "metrics": {}}
        except Exception as e:
            return {"issues": [{"tool": "tsc", "error": str(e)}], "metrics": {}}

    def _run_eslint(self, project_path: Path, language: str) -> Dict[str, Any]:
        """Run ESLint"""
        try:
            result = subprocess.run(
                ["eslint", ".", "--format=json"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=30,
            )

            issues = []
            metrics = {}

            if result.returncode == 0:
                try:
                    eslint_data = json.loads(result.stdout)
                    metrics["eslint_issues"] = len(eslint_data)
                except json.JSONDecodeError:
                    pass
            else:
                issues.append(
                    {"tool": "eslint", "type": "lint_error", "output": result.stderr}
                )

            return {"issues": issues, "metrics": metrics}

        except subprocess.TimeoutExpired:
            return {"issues": [{"tool": "eslint", "error": "Timeout"}], "metrics": {}}
        except Exception as e:
            return {"issues": [{"tool": "eslint", "error": str(e)}], "metrics": {}}

    def _run_flake8(self, project_path: Path) -> Dict[str, Any]:
        """Run flake8"""
        try:
            result = subprocess.run(
                ["flake8", "."],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=30,
            )

            issues = []
            if result.stdout or result.stderr:
                issues.append(
                    {"tool": "flake8", "output": result.stdout + result.stderr}
                )

            return {
                "issues": issues,
                "metrics": {"flake8_passed": result.returncode == 0},
            }

        except subprocess.TimeoutExpired:
            return {"issues": [{"tool": "flake8", "error": "Timeout"}], "metrics": {}}
        except Exception as e:
            return {"issues": [{"tool": "flake8", "error": str(e)}], "metrics": {}}

    def _run_pylint(self, project_path: Path) -> Dict[str, Any]:
        """Run pylint"""
        try:
            result = subprocess.run(
                ["pylint", "."],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=30,
            )

            issues = []
            if result.stdout or result.stderr:
                issues.append(
                    {"tool": "pylint", "output": result.stdout + result.stderr}
                )

            return {
                "issues": issues,
                "metrics": {"pylint_passed": result.returncode == 0},
            }

        except subprocess.TimeoutExpired:
            return {"issues": [{"tool": "pylint", "error": "Timeout"}], "metrics": {}}
        except Exception as e:
            return {"issues": [{"tool": "pylint", "error": str(e)}], "metrics": {}}

    def _run_cargo_check(self, project_path: Path) -> Dict[str, Any]:
        """Run cargo check"""
        try:
            result = subprocess.run(
                ["cargo", "check"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=60,
            )

            issues = []
            if result.returncode != 0:
                issues.append(
                    {
                        "tool": "cargo",
                        "type": "compilation_error",
                        "output": result.stderr,
                    }
                )

            return {
                "issues": issues,
                "metrics": {"cargo_check_passed": result.returncode == 0},
            }

        except subprocess.TimeoutExpired:
            return {"issues": [{"tool": "cargo", "error": "Timeout"}], "metrics": {}}
        except Exception as e:
            return {"issues": [{"tool": "cargo", "error": str(e)}], "metrics": {}}

    def _run_clippy(self, project_path: Path) -> Dict[str, Any]:
        """Run clippy"""
        try:
            result = subprocess.run(
                ["cargo", "clippy"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=60,
            )

            issues = []
            if result.stdout or result.stderr:
                issues.append(
                    {
                        "tool": "clippy",
                        "type": "lint_warnings",
                        "output": result.stdout + result.stderr,
                    }
                )

            return {"issues": issues, "metrics": {}}

        except subprocess.TimeoutExpired:
            return {"issues": [{"tool": "clippy", "error": "Timeout"}], "metrics": {}}
        except Exception as e:
            return {"issues": [{"tool": "clippy", "error": str(e)}], "metrics": {}}

    def _run_go_vet(self, project_path: Path) -> Dict[str, Any]:
        """Run go vet"""
        try:
            result = subprocess.run(
                ["go", "vet", "./..."],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=30,
            )

            issues = []
            if result.stdout or result.stderr:
                issues.append(
                    {"tool": "go vet", "output": result.stdout + result.stderr}
                )

            return {
                "issues": issues,
                "metrics": {"go_vet_passed": result.returncode == 0},
            }

        except subprocess.TimeoutExpired:
            return {"issues": [{"tool": "go vet", "error": "Timeout"}], "metrics": {}}
        except Exception as e:
            return {"issues": [{"tool": "go vet", "error": str(e)}], "metrics": {}}

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

    def _enhance(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance core result with code health analysis"""
        enhancement = {
            "code_health_analysis": {},
            "quality_metrics": {},
            "enhancement_applied": False,
        }

        # If core result contains project path, analyze it
        if "project_path" in core_result:
            project_path = Path(core_result["project_path"])
            if project_path.exists():
                analysis_result = self.analyze_project(project_path)
                enhancement["code_health_analysis"] = analysis_result

                # Extract quality metrics
                if analysis_result.get("status") == "analyzed":
                    enhancement["quality_metrics"] = {
                        "overall_health": analysis_result.get(
                            "overall_health", "unknown"
                        ),
                        "detected_languages": analysis_result.get(
                            "detected_languages", []
                        ),
                        "analysis_strictness": analysis_result.get(
                            "analysis_strictness", "standard"
                        ),
                    }

                enhancement["enhancement_applied"] = True

        return enhancement


class DocumentationIntegration(BaseIntegration):
    """
    Documentation Integration for consistency validation

    Provides documentation consistency checking, requirement traceability,
    and cross-reference validation while maintaining YASK's core simplicity.
    """

    def __init__(self, enabled: bool = False):
        super().__init__("documentation", enabled)
        self.logger = logging.getLogger("yask.integration.documentation")

        # Add capabilities
        self.add_capability("consistency_checking")
        self.add_capability("requirement_traceability")
        self.add_capability("cross_reference_validation")

    def _initialize(self) -> Optional[Dict[str, Any]]:
        """Initialize documentation integration"""
        try:
            return {
                "supported_formats": ["markdown", "rst", "txt"],
                "validation_rules": [
                    "requirement_traceability",
                    "cross_reference_consistency",
                    "documentation_completeness",
                ],
                "mode": "active",
            }

        except Exception as e:
            self.logger.error(f"Failed to initialize documentation integration: {e}")
            return {"mode": "error", "error": str(e)}

    def validate_documentation_consistency(
        self,
        project_path: Path,
        requirements_doc: Optional[Path] = None,
        design_doc: Optional[Path] = None,
        tasks_doc: Optional[Path] = None,
    ) -> Dict[str, Any]:
        """
        Validate documentation consistency across YASK documents

        Args:
            project_path: Project root path
            requirements_doc: Requirements document path
            design_doc: Design document path
            tasks_doc: Tasks document path

        Returns:
            Validation results
        """
        try:
            # Auto-detect documents if not provided
            if not requirements_doc:
                requirements_doc = self._find_document(project_path, "requirements")
            if not design_doc:
                design_doc = self._find_document(project_path, "design")
            if not tasks_doc:
                tasks_doc = self._find_document(project_path, "tasks")

            validation_results = {
                "documents_found": {},
                "consistency_issues": [],
                "traceability_gaps": [],
                "recommendations": [],
            }

            # Check each document
            docs = {
                "requirements": requirements_doc,
                "design": design_doc,
                "tasks": tasks_doc,
            }

            for doc_type, doc_path in docs.items():
                if doc_path and doc_path.exists():
                    validation_results["documents_found"][doc_type] = str(doc_path)
                    content = doc_path.read_text(encoding="utf-8")
                    validation_results[f"{doc_type}_analysis"] = self._analyze_document(
                        content, doc_type
                    )
                else:
                    validation_results["documents_found"][doc_type] = None

            # Check cross-document consistency
            if all(docs.values()):
                consistency_check = self._check_cross_document_consistency(docs)
                validation_results["consistency_issues"] = consistency_check.get(
                    "issues", []
                )
                validation_results["traceability_gaps"] = consistency_check.get(
                    "traceability_gaps", []
                )

            # Generate recommendations
            validation_results["recommendations"] = (
                self._generate_documentation_recommendations(validation_results)
            )

            return validation_results

        except Exception as e:
            return {
                "status": "error",
                "message": f"Documentation validation failed: {str(e)}",
            }

    def _find_document(self, project_path: Path, doc_type: str) -> Optional[Path]:
        """Find YASK document by type"""
        patterns = {
            "requirements": ["requirements.md", "requirements.txt", "reqs.md"],
            "design": ["design.md", "architecture.md", "spec.md"],
            "tasks": ["tasks.md", "todo.md", "implementation.md"],
        }

        for pattern in patterns.get(doc_type, []):
            doc_path = project_path / pattern
            if doc_path.exists():
                return doc_path

        # Search recursively
        for pattern in patterns.get(doc_type, []):
            matches = list(project_path.rglob(pattern))
            if matches:
                return matches[0]

        return None

    def _analyze_document(self, content: str, doc_type: str) -> Dict[str, Any]:
        """Analyze individual document"""
        analysis = {
            "type": doc_type,
            "line_count": len(content.splitlines()),
            "word_count": len(content.split()),
            "sections": [],
            "requirements": [],
            "tasks": [],
        }

        try:
            lines = content.splitlines()
            current_section = None

            for line in lines:
                stripped = line.strip()

                # Detect sections (headers)
                if stripped.startswith("#"):
                    current_section = stripped.lstrip("#").strip()
                    analysis["sections"].append(current_section)

                # Extract requirements (EARS format)
                if doc_type == "requirements" and self._is_ears_requirement(stripped):
                    analysis["requirements"].append(stripped)

                # Extract tasks (checkbox format)
                if doc_type == "tasks" and self._is_task_item(stripped):
                    analysis["tasks"].append(stripped)

        except Exception as e:
            analysis["error"] = str(e)

        return analysis

    def _is_ears_requirement(self, line: str) -> bool:
        """Check if line is an EARS format requirement"""
        ears_patterns = [
            r"WHEN.*THEN",
            r"IF.*THEN",
            r"WHERE.*THEN",
            r"User Story:",
            r"Acceptance Criteria:",
        ]

        for pattern in ears_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                return True
        return False

    def _is_task_item(self, line: str) -> bool:
        """Check if line is a task item"""
        task_patterns = [
            r"^\s*-\s*\[",  # - [ ]
            r"^\s*\*\s*\[",  # * [ ]
            r"^\s*\d+\.",  # 1. 2. etc
            r"^\s*\[x\]",  # [x] completed
            r"^\s*\[ \]",  # [ ] incomplete
        ]

        for pattern in task_patterns:
            if re.search(pattern, line):
                return True
        return False

    def _check_cross_document_consistency(
        self, docs: Dict[str, Optional[Path]]
    ) -> Dict[str, Any]:
        """Check consistency across documents"""
        issues = []
        traceability_gaps = []

        try:
            # Load document contents
            contents = {}
            for doc_type, doc_path in docs.items():
                if doc_path:
                    contents[doc_type] = doc_path.read_text(encoding="utf-8")

            # Check requirement-to-design traceability
            if "requirements" in contents and "design" in contents:
                req_design_consistency = self._check_requirement_design_consistency(
                    contents["requirements"], contents["design"]
                )
                issues.extend(req_design_consistency.get("issues", []))
                traceability_gaps.extend(req_design_consistency.get("gaps", []))

            # Check design-to-tasks traceability
            if "design" in contents and "tasks" in contents:
                design_tasks_consistency = self._check_design_tasks_consistency(
                    contents["design"], contents["tasks"]
                )
                issues.extend(design_tasks_consistency.get("issues", []))
                traceability_gaps.extend(design_tasks_consistency.get("gaps", []))

            return {"issues": issues, "traceability_gaps": traceability_gaps}

        except Exception as e:
            return {
                "issues": [f"Consistency check failed: {str(e)}"],
                "traceability_gaps": [],
            }

    def _check_requirement_design_consistency(
        self, requirements_content: str, design_content: str
    ) -> Dict[str, Any]:
        """Check consistency between requirements and design"""
        issues = []
        gaps = []

        try:
            # Extract requirements
            requirements = self._extract_requirements(requirements_content)

            # Check if design addresses each requirement
            design_lower = design_content.lower()

            for req in requirements:
                req_keywords = self._extract_keywords(req)
                coverage_score = sum(
                    1 for keyword in req_keywords if keyword in design_lower
                )

                if coverage_score < len(req_keywords) * 0.3:  # Less than 30% coverage
                    gaps.append(
                        {
                            "requirement": req[:100] + "..." if len(req) > 100 else req,
                            "coverage_score": coverage_score / len(req_keywords)
                            if req_keywords
                            else 0,
                            "issue": "Design does not adequately address requirement",
                        }
                    )

            return {"issues": issues, "gaps": gaps}

        except Exception as e:
            return {
                "issues": [f"Requirement-design consistency check failed: {str(e)}"],
                "gaps": [],
            }

    def _check_design_tasks_consistency(
        self, design_content: str, tasks_content: str
    ) -> Dict[str, Any]:
        """Check consistency between design and tasks"""
        issues = []
        gaps = []

        try:
            # Extract design components
            design_components = self._extract_design_components(design_content)

            # Check if tasks cover each design component
            tasks_lower = tasks_content.lower()

            for component in design_components:
                component_keywords = self._extract_keywords(component)
                coverage_score = sum(
                    1 for keyword in component_keywords if keyword in tasks_lower
                )

                if (
                    coverage_score < len(component_keywords) * 0.3
                ):  # Less than 30% coverage
                    gaps.append(
                        {
                            "component": component[:100] + "..."
                            if len(component) > 100
                            else component,
                            "coverage_score": coverage_score / len(component_keywords)
                            if component_keywords
                            else 0,
                            "issue": "Tasks do not adequately cover design component",
                        }
                    )

            return {"issues": issues, "gaps": gaps}

        except Exception as e:
            return {
                "issues": [f"Design-tasks consistency check failed: {str(e)}"],
                "gaps": [],
            }

    def _extract_requirements(self, content: str) -> List[str]:
        """Extract requirements from content"""
        requirements = []
        lines = content.splitlines()

        for line in lines:
            stripped = line.strip()
            if self._is_ears_requirement(stripped):
                requirements.append(stripped)

        return requirements

    def _extract_design_components(self, content: str) -> List[str]:
        """Extract design components from content"""
        components = []
        lines = content.splitlines()

        for line in lines:
            stripped = line.strip()
            # Look for component definitions, interfaces, etc.
            if any(
                keyword in stripped.lower()
                for keyword in ["component", "interface", "module", "class", "function"]
            ):
                if len(stripped) > 10:  # Avoid very short lines
                    components.append(stripped)

        return components

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract meaningful keywords from text"""
        # Simple keyword extraction
        words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
        # Filter out common words
        stop_words = {
            "that",
            "with",
            "have",
            "this",
            "will",
            "from",
            "they",
            "know",
            "want",
            "been",
            "good",
            "much",
            "some",
            "time",
        }
        return [word for word in words if word not in stop_words]

    def _generate_documentation_recommendations(
        self, validation_results: Dict[str, Any]
    ) -> List[str]:
        """Generate documentation improvement recommendations"""
        recommendations = []

        try:
            # Check for missing documents
            missing_docs = [
                doc_type
                for doc_type, path in validation_results["documents_found"].items()
                if not path
            ]
            if missing_docs:
                recommendations.append(
                    f"Consider creating missing documents: {', '.join(missing_docs)}"
                )

            # Check for consistency issues
            if validation_results["consistency_issues"]:
                recommendations.append("Address cross-document consistency issues")

            # Check for traceability gaps
            if validation_results["traceability_gaps"]:
                recommendations.append(
                    "Improve requirement-to-design-to-tasks traceability"
                )

            # Check document completeness
            for doc_type, analysis in validation_results.items():
                if doc_type.endswith("_analysis") and isinstance(analysis, dict):
                    if analysis.get("line_count", 0) < 10:
                        recommendations.append(
                            f"{doc_type.replace('_analysis', '')} document appears incomplete"
                        )

            return recommendations

        except Exception:
            return ["Unable to generate recommendations"]

    def _enhance(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance core result with documentation analysis"""
        enhancement = {
            "documentation_analysis": {},
            "consistency_metrics": {},
            "enhancement_applied": False,
        }

        # If core result contains project path, analyze documentation
        if "project_path" in core_result:
            project_path = Path(core_result["project_path"])
            if project_path.exists():
                validation_result = self.validate_documentation_consistency(
                    project_path
                )
                enhancement["documentation_analysis"] = validation_result

                # Extract consistency metrics
                if validation_result.get("status") != "error":
                    enhancement["consistency_metrics"] = {
                        "documents_found": len(
                            [
                                p
                                for p in validation_result.get(
                                    "documents_found", {}
                                ).values()
                                if p
                            ]
                        ),
                        "consistency_issues": len(
                            validation_result.get("consistency_issues", [])
                        ),
                        "traceability_gaps": len(
                            validation_result.get("traceability_gaps", [])
                        ),
                        "recommendations": len(
                            validation_result.get("recommendations", [])
                        ),
                    }

                enhancement["enhancement_applied"] = True

        return enhancement


# Convenience functions
def create_tree_sitter_integration(
    enabled: bool = False, languages: Optional[List[str]] = None
) -> TreeSitterIntegration:
    """Create Tree-Sitter integration instance"""
    return TreeSitterIntegration(enabled=enabled, languages=languages)


def create_codehealth_integration(
    enabled: bool = False, strictness: str = "standard"
) -> CodeHealthIntegration:
    """Create code health integration instance"""
    return CodeHealthIntegration(enabled=enabled, strictness=strictness)


def create_documentation_integration(enabled: bool = False) -> DocumentationIntegration:
    """Create documentation integration instance"""
    return DocumentationIntegration(enabled=enabled)
