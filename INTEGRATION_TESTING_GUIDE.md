# YASK 3.0 Integration Testing Guide

**Date**: 2025-12-29
**Version**: 3.0.0
**Status**: Complete

---

## Overview

This guide provides comprehensive procedures for running integration tests on the YASK 3.0 framework. Integration testing ensures that all components work together correctly and that the system meets quality standards.

---

## Testing Framework

### Test Structure

The YASK testing framework is organized into several categories:

```
.yask/testing/
├── framework/           # Core testing framework
├── runners/            # Test runners for different categories
├── utilities/          # Test utilities and helpers
└── run-all-tests.sh    # Master test runner
```

### Test Categories

1. **Installation Tests**: Verify YASK installation and setup
2. **Document Tests**: Test document creation, validation, and processing
3. **Error Tests**: Test error handling and recovery
4. **System Tests**: Test system-wide functionality
5. **Template Tests**: Test template system
6. **Version Tests**: Test version compatibility
7. **Workflow Tests**: Test workflow processes
8. **Agent Tests**: Test AI agent integration

---

## Running Tests

### Quick Start

#### Run All Tests

```bash
# Navigate to YASK project directory
cd path/to/yask-system

# Run all tests
./.yask/tests/run-all-tests.sh

# Or using Python
python .yask/testing/run_all_tests.py
```

#### Run Specific Test Category

```bash
# Run installation tests
./.yask/tests/runners/installation-tests.sh

# Run document tests
./.yask/tests/runners/document-tests.sh

# Run error tests
./.yask/tests/runners/error-tests.sh

# Run system tests
./.yask/tests/runners/system-tests.sh

# Run template tests
./.yask/tests/runners/template-tests.sh

# Run version tests
./.yask/tests/runners/version-tests.sh

# Run workflow tests
./.yask/tests/runners/workflow-tests.sh

# Run agent tests
./.yask/tests/runners/agent-tests.sh
```

### Using Python Test Framework

```bash
# Run all tests with verbose output
python .yask/testing/run_all_tests.py --verbose

# Run specific test category
python .yask/testing/run_all_tests.py --category document

# Run tests with coverage
python .yask/testing/run_all_tests.py --coverage

# Run tests and generate report
python .yask/testing/run_all_tests.py --report

# Run tests with specific output format
python .yask/testing/run_all_tests.py --format json
```

---

## Interpreting Test Results

### Test Output Format

#### Standard Output

```
Running YASK Integration Tests...
================================

[INFO] Starting test suite...
[INFO] Running installation tests...
[OK] Installation test 1 passed
[OK] Installation test 2 passed
[INFO] Running document tests...
[OK] Document test 1 passed
[FAIL] Document test 2 failed
[ERROR] Expected: X, Got: Y
[INFO] Running error tests...
[OK] Error test 1 passed
[INFO] Running system tests...
[OK] System test 1 passed

Test Summary:
============
Total Tests: 50
Passed: 48
Failed: 2
Skipped: 0
Success Rate: 96.0%
```

#### JSON Output

```json
{
  "test_suite": "YASK Integration Tests",
  "timestamp": "2025-12-29T12:00:00Z",
  "results": {
    "total_tests": 50,
    "passed": 48,
    "failed": 2,
    "skipped": 0,
    "success_rate": 96.0
  },
  "categories": {
    "installation": {
      "total": 5,
      "passed": 5,
      "failed": 0,
      "success_rate": 100.0
    },
    "document": {
      "total": 10,
      "passed": 8,
      "failed": 2,
      "success_rate": 80.0
    }
  },
  "failures": [
    {
      "test": "Document test 2",
      "category": "document",
      "error": "Expected: X, Got: Y",
      "stack_trace": "..."
    }
  ]
}
```

### Test Metrics

#### Key Metrics

- **Total Tests**: Total number of tests run
- **Passed**: Number of tests that passed
- **Failed**: Number of tests that failed
- **Skipped**: Number of tests skipped
- **Success Rate**: Percentage of tests that passed

#### Quality Gates

- **Critical**: All tests must pass (100% success rate)
- **High**: At least 95% success rate
- **Medium**: At least 90% success rate
- **Low**: At least 80% success rate

---

## Debugging Test Failures

### Common Failure Patterns

#### 1. Import Errors

**Symptoms**: Tests fail with import errors

**Solutions**:
```bash
# Check Python path
python -c "import sys; print(sys.path)"

# Verify module locations
python -c "import os; print(os.getcwd())"

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

#### 2. File Not Found Errors

**Symptoms**: Tests fail with file not found errors

**Solutions**:
```bash
# Check file existence
ls -la .yask/core/

# Verify file permissions
chmod +x .yask/tests/run-all-tests.sh

# Check working directory
pwd
```

#### 3. Validation Errors

**Symptoms**: Tests fail with validation errors

**Solutions**:
```bash
# Run validation manually
python .yask/validation/quality-assurance-framework.py --check-all

# Check validation cache
cat .yask/validation_cache/*.json

# Fix validation issues
python .yask/validation/comprehensive-reference-fixer.py --fix
```

#### 4. Performance Failures

**Symptoms**: Tests fail due to performance issues

**Solutions**:
```bash
# Run performance benchmark
python .yask/core/performance-optimizer.py --benchmark

# Check performance metrics
cat .yask/performance_metrics.json

# Optimize configuration
python .yask/core/performance-optimizer.py --optimize
```

### Debug Mode

#### Enable Debug Logging

```bash
# Set debug environment variable
export YASK_DEBUG=1

# Run tests with debug output
./.yask/tests/run-all-tests.sh --debug

# Or using Python
python .yask/testing/run_all_tests.py --debug
```

#### Generate Diagnostic Report

```bash
# Generate comprehensive diagnostic report
python .yask/core/system-integration.py --diagnose

# Review diagnostic report
cat YASK_DIAGNOSTIC_REPORT.md
```

---

## Quality Gate Procedures

### Pre-Commit Quality Gates

#### Run Pre-Commit Tests

```bash
# Run pre-commit test suite
./.yask/tests/run-all-tests.sh --pre-commit

# Or using Python
python .yask/testing/run_all_tests.py --pre-commit
```

#### Pre-Commit Checklist

- [ ] All installation tests pass
- [ ] All document tests pass
- [ ] All error tests pass
- [ ] All system tests pass
- [ ] All template tests pass
- [ ] All version tests pass
- [ ] All workflow tests pass
- [ ] All agent tests pass
- [ ] Success rate >= 95%
- [ ] No critical failures

### Pre-Push Quality Gates

#### Run Pre-Push Tests

```bash
# Run pre-push test suite
./.yask/tests/run-all-tests.sh --pre-push

# Or using Python
python .yask/testing/run_all_tests.py --pre-push
```

#### Pre-Push Checklist

- [ ] All pre-commit tests pass
- [ ] Integration tests pass
- [ ] Performance tests pass
- [ ] Quality metrics meet standards
- [ ] Documentation is up to date
- [ ] No regressions detected

### Pre-Release Quality Gates

#### Run Pre-Release Tests

```bash
# Run pre-release test suite
./.yask/tests/run-all-tests.sh --pre-release

# Or using Python
python .yask/testing/run_all_tests.py --pre-release
```

#### Pre-Release Checklist

- [ ] All pre-push tests pass
- [ ] Full integration test suite passes
- [ ] Performance benchmarks met
- [ ] Security tests pass
- [ ] Documentation complete
- [ ] Release notes prepared
- [ ] Backward compatibility verified

---

## Continuous Integration

### GitHub Actions Integration

#### Workflow Configuration

```yaml
name: YASK Integration Tests

on:
  push:
    branches: [ main, feature/* ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          python .yask/testing/run_all_tests.py --report
      - name: Upload test results
        uses: actions/upload-artifact@v2
        with:
          name: test-results
          path: test-reports/
```

### Local CI Simulation

```bash
# Simulate CI pipeline
python .yask/testing/run_all_tests.py --ci

# Generate CI report
python .yask/testing/run_all_tests.py --ci --report
```

---

## Test Coverage

### Measuring Coverage

```bash
# Run tests with coverage
python .yask/testing/run_all_tests.py --coverage

# Generate coverage report
python .yask/testing/run_all_tests.py --coverage --report
```

### Coverage Targets

- **Core Modules**: >= 90%
- **Integration Modules**: >= 85%
- **Validation Modules**: >= 90%
- **Testing Framework**: >= 80%
- **Overall**: >= 85%

---

## Performance Testing

### Running Performance Tests

```bash
# Run performance benchmarks
python .yask/core/performance-optimizer.py --benchmark

# Compare with baseline
python .yask/core/performance-optimizer.py --compare

# Generate performance report
python .yask/core/performance-optimizer.py --report
```

### Performance Metrics

- **Context Loading Time**: < 2 seconds
- **Template Processing Time**: < 1 second
- **Validation Time**: < 3 seconds
- **Cross-Reference Resolution**: < 1 second
- **Overall System Response**: < 5 seconds

---

## Troubleshooting

### Common Issues

#### Issue 1: Tests Hang

**Symptoms**: Tests hang and don't complete

**Solutions**:
```bash
# Check for infinite loops
# Review test code for potential issues

# Run with timeout
timeout 300 ./.yask/tests/run-all-tests.sh

# Check system resources
top
```

#### Issue 2: Intermittent Failures

**Symptoms**: Tests fail intermittently

**Solutions**:
```bash
# Run tests multiple times
for i in {1..5}; do ./.yask/tests/run-all-tests.sh; done

# Check for race conditions
# Review test code for concurrency issues

# Run tests in isolation
./.yask/tests/runners/document-tests.sh
```

#### Issue 3: Memory Issues

**Symptoms**: Tests fail due to memory issues

**Solutions**:
```bash
# Check memory usage
free -h

# Run tests with memory limit
ulimit -v 1048576
./.yask/tests/run-all-tests.sh

# Clear cache
rm -rf .yask/cache/*
```

---

## Best Practices

### Test Development

1. **Write Clear Tests**: Tests should be self-documenting
2. **Test One Thing**: Each test should verify one specific behavior
3. **Use Descriptive Names**: Test names should describe what they test
4. **Maintain Independence**: Tests should not depend on each other
5. **Clean Up**: Tests should clean up after themselves

### Test Maintenance

1. **Update Tests**: Keep tests updated with code changes
2. **Remove Dead Tests**: Remove tests that are no longer relevant
3. **Refactor Tests**: Refactor tests to improve maintainability
4. **Document Tests**: Document complex test scenarios
5. **Review Coverage**: Regularly review test coverage

### Continuous Improvement

1. **Monitor Metrics**: Track test metrics over time
2. **Identify Trends**: Look for trends in test results
3. **Address Issues**: Address issues promptly
4. **Improve Quality**: Continuously improve test quality
5. **Share Knowledge**: Share test knowledge with team

---

## Support and Resources

### Documentation

- YASK Architecture: `YASK_REFACTOR_ARCHITECTURE.md`
- Performance Tuning: `PERFORMANCE_TUNING_GUIDE.md`
- Backward Compatibility: `BACKWARD_COMPATIBILITY_GUIDE.md`
- API Reference: `API_REFERENCE.md`

### Tools

- Test Framework: `.yask/testing/`
- Quality Assurance: `.yask/validation/`
- Performance Optimizer: `.yask/core/performance-optimizer.py`

### Community

- GitHub Issues: https://github.com/moxxiepox/yask-spec-kit/issues
- Documentation: https://github.com/moxxiepox/yask-spec-kit/wiki
- Discussions: https://github.com/moxxiepox/yask-spec-kit/discussions

---

## Conclusion

This integration testing guide provides comprehensive procedures for running and interpreting tests on the YASK 3.0 framework. By following these procedures, you can ensure that your YASK installation meets quality standards and performs as expected.

For questions or issues, please refer to the troubleshooting section or contact support.

---

**Integration Testing Guide Version**: 1.0.0
**Last Updated**: 2025-12-29
**YASK Version**: 3.0.0
