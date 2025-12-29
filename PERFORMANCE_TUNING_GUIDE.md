# Performance Tuning Guide

## Overview

This guide provides comprehensive instructions for measuring, tuning, and optimizing the performance of the YASK framework (version 3.0). It covers performance measurement techniques, caching parameter tuning, template processing optimization, monitoring procedures, benchmarking, and troubleshooting.

## Table of Contents

1. [Measuring Performance Improvements](#measuring-performance-improvements)
2. [Tuning Caching Parameters](#tuning-caching-parameters)
3. [Optimizing Template Processing](#optimizing-template-processing)
4. [Performance Monitoring and Reporting](#performance-monitoring-and-reporting)
5. [Benchmarking Procedures](#benchmarking-procedures)
6. [Performance Troubleshooting](#performance-troubleshooting)

---

## Measuring Performance Improvements

### Understanding Performance Metrics

The YASK framework tracks several key performance metrics:

```python
@dataclass
class PerformanceMetrics:
    operation: str              # Operation being measured
    duration_ms: float          # Actual execution time
    baseline_ms: float          # Baseline execution time
    improvement_percent: float  # Percentage improvement
    cache_hits: int             # Number of cache hits
    cache_misses: int           # Number of cache misses
    memory_usage_mb: float      # Memory usage in MB
    timestamp: datetime         # Measurement timestamp
```

### Setting Up Performance Measurement

#### Step 1: Establish Baselines

Before optimization, establish baseline measurements:

```python
from pathlib import Path
from .yask.core.performance_optimizer import SystemPerformanceOptimizer

# Initialize optimizer
project_root = Path(".")
optimizer = SystemPerformanceOptimizer(project_root)

# Measure baseline performance
baseline_result = optimizer.measure_performance(
    operation="template_processing",
    baseline_ms=100.0,  # Expected baseline
    func=optimizer.template_optimizer.process_template_optimized,
    "requirements-template-consolidated.md"
)

print(f"Baseline duration: {baseline_result.metrics.duration_ms:.2f}ms")
print(f"Baseline improvement: {baseline_result.metrics.improvement_percent:.1f}%")
```

#### Step 2: Measure Current Performance

```python
# Measure current performance
current_result = optimizer.measure_performance(
    operation="template_processing",
    baseline_ms=baseline_result.metrics.duration_ms,
    func=optimizer.template_optimizer.process_template_optimized,
    "requirements-template-consolidated.md"
)

print(f"Current duration: {current_result.metrics.duration_ms:.2f}ms")
print(f"Current improvement: {current_result.metrics.improvement_percent:.1f}%")
```

#### Step 3: Compare Results

```python
# Calculate improvement
improvement = baseline_result.metrics.duration_ms - current_result.metrics.duration_ms
improvement_percent = (improvement / baseline_result.metrics.duration_ms) * 100

print(f"Performance improvement: {improvement:.2f}ms ({improvement_percent:.1f}%)")
```

### Performance Measurement Best Practices

1. **Consistent Environment**: Measure in the same environment each time
2. **Multiple Runs**: Take multiple measurements and average them
3. **Warm-up Runs**: Perform warm-up runs before measuring
4. **Isolate Operations**: Measure one operation at a time
5. **Document Conditions**: Record system conditions during measurement

### Example: Comprehensive Performance Measurement

```python
import time
from statistics import mean

def measure_operation_multiple_times(optimizer, operation, func, *args, **kwargs):
    """Measure operation multiple times and return statistics."""
    results = []
    
    # Warm-up run
    func(*args, **kwargs)
    
    # Measure 10 times
    for _ in range(10):
        result = optimizer.measure_performance(
            operation=operation,
            baseline_ms=100.0,
            func=func,
            *args,
            **kwargs
        )
        results.append(result.metrics.duration_ms)
    
    # Calculate statistics
    avg_duration = mean(results)
    min_duration = min(results)
    max_duration = max(results)
    
    return {
        'average': avg_duration,
        'minimum': min_duration,
        'maximum': max_duration,
        'all_results': results
    }

# Measure template processing
stats = measure_operation_multiple_times(
    optimizer,
    "template_processing",
    optimizer.template_optimizer.process_template_optimized,
    "requirements-template-consolidated.md"
)

print(f"Average duration: {stats['average']:.2f}ms")
print(f"Min duration: {stats['minimum']:.2f}ms")
print(f"Max duration: {stats['maximum']:.2f}ms")
```

---

## Tuning Caching Parameters

### Understanding Cache Configuration

The YASK framework uses multiple cache layers:

1. **Template Cache**: Stores processed templates
2. **Inheritance Cache**: Stores template inheritance results
3. **Validation Cache**: Stores template validation results
4. **Context Cache**: Stores loaded contexts

### Cache TTL Configuration

#### Default TTL Settings

```python
# In TemplatePerformanceOptimizer.__init__
self._cache_ttl = timedelta(hours=24)  # Default: 24 hours
```

#### Adjusting Cache TTL

**For Frequent Updates** (development environment):

```python
from datetime import timedelta

# Short TTL for frequent updates
optimizer = TemplatePerformanceOptimizer(template_dir)
optimizer._cache_ttl = timedelta(hours=1)  # 1 hour TTL
```

**For Stable Templates** (production environment):

```python
# Long TTL for stable templates
optimizer = TemplatePerformanceOptimizer(template_dir)
optimizer._cache_ttl = timedelta(days=7)  # 7 days TTL
```

**For Testing** (rapid iteration):

```python
# Very short TTL for testing
optimizer = TemplatePerformanceOptimizer(template_dir)
optimizer._cache_ttl = timedelta(minutes=15)  # 15 minutes TTL
```

### Cache Size Management

#### Monitoring Cache Size

```python
# Get current cache statistics
stats = optimizer.get_cache_stats()

print(f"Template cache size: {stats['template_cache_size']}")
print(f"Inheritance cache size: {stats['inheritance_cache_size']}")
print(f"Validation cache size: {stats['validation_cache_size']}")
print(f"Total cached items: {stats['total_cached_items']}")
```

#### Implementing Cache Size Limits

```python
class TemplatePerformanceOptimizer:
    def __init__(self, template_dir: Path, max_cache_size: int = 1000):
        self.template_dir = template_dir
        self.max_cache_size = max_cache_size
        self._cache_ttl = timedelta(hours=24)
        # ... rest of initialization
    
    def _check_cache_size(self):
        """Check if cache exceeds size limit and evict if necessary."""
        stats = self.get_cache_stats()
        
        if stats['total_cached_items'] > self.max_cache_size:
            self._evict_oldest_entries()
    
    def _evict_oldest_entries(self):
        """Evict oldest cache entries to free space."""
        # Sort cache entries by timestamp
        sorted_entries = sorted(
            self.template_cache.items(),
            key=lambda x: x[1]['timestamp']
        )
        
        # Evict oldest entries
        entries_to_remove = len(sorted_entries) - self.max_cache_size
        for i in range(entries_to_remove):
            key, _ = sorted_entries[i]
            del self.template_cache[key]
```

#### Clearing Cache

```python
# Clear all caches
optimizer.template_cache.clear()
optimizer.inheritance_cache.clear()
optimizer.validation_cache.clear()

# Clear specific cache
optimizer.template_cache.clear()
```

### Cache Hit Rate Optimization

#### Monitoring Cache Hit Rates

```python
def calculate_cache_hit_rate(optimizer):
    """Calculate cache hit rate."""
    stats = optimizer.get_cache_stats()
    
    total_requests = stats['cache_hits'] + stats['cache_misses']
    if total_requests == 0:
        return 0.0
    
    hit_rate = (stats['cache_hits'] / total_requests) * 100
    return hit_rate

# Calculate hit rate
hit_rate = calculate_cache_hit_rate(optimizer)
print(f"Cache hit rate: {hit_rate:.1f}%")
```

#### Improving Cache Hit Rate

1. **Increase TTL**: Longer TTL means more cache hits
2. **Preload Cache**: Load frequently used templates into cache
3. **Optimize Cache Keys**: Ensure cache keys are consistent
4. **Reduce Cache Evictions**: Implement smart eviction policies

**Example: Preloading Cache**

```python
def preload_cache(optimizer, template_names):
    """Preload frequently used templates into cache."""
    for template_name in template_names:
        optimizer.process_template_optimized(template_name)
    
    print(f"Preloaded {len(template_names)} templates")

# Preload frequently used templates
frequently_used = [
    "requirements-template-consolidated.md",
    "design-template-consolidated.md",
    "tasks-template-consolidated.md"
]
preload_cache(optimizer, frequently_used)
```

---

## Optimizing Template Processing

### Template Inheritance Optimization

#### Understanding Template Inheritance

Template inheritance allows templates to extend base templates:

```python
# Base template
base_template = """
# Base Template

{{ content }}
"""

# Child template
child_template = """
# Child Template

{{ extends: base-template.md }}

## Additional Content

This is additional content.
"""
```

#### Optimizing Inheritance Processing

```python
from .yask.templates.template_inheritance_processor import TemplateInheritanceProcessor

# Initialize processor
processor = TemplateInheritanceProcessor(template_dir)

# Process template with inheritance
result = processor.process_template("child-template.md")

# Check if inheritance was used
if result.inheritance_used:
    print(f"Template extends: {result.parent_template}")
    print(f"Inheritance depth: {result.inheritance_depth}")
```

#### Best Practices for Template Inheritance

1. **Keep Inheritance Shallow**: Avoid deep inheritance hierarchies
2. **Reuse Base Templates**: Create reusable base templates
3. **Minimize Overrides**: Only override necessary sections
4. **Document Inheritance**: Document template inheritance relationships

### Template Validation Optimization

#### Optimizing Validation Rules

```python
# Configure validation rules
validation_rules = {
    'required_sections': ['Overview', 'Requirements', 'Design'],
    'format_rules': {
        'markdown': True,
        'ears_format': True
    },
    'cross_reference_rules': {
        'validate_links': True,
        'check_broken_references': True
    }
}

# Validate with optimized rules
is_valid, errors = optimizer.validate_template_optimized(
    "requirements-template-consolidated.md",
    validation_rules=validation_rules
)
```

#### Batch Validation

```python
def batch_validate_templates(optimizer, template_names):
    """Validate multiple templates in batch."""
    results = {}
    
    for template_name in template_names:
        is_valid, errors = optimizer.validate_template_optimized(template_name)
        results[template_name] = {
            'valid': is_valid,
            'errors': errors
        }
    
    return results

# Batch validate templates
templates = [
    "requirements-template-consolidated.md",
    "design-template-consolidated.md",
    "tasks-template-consolidated.md"
]
results = batch_validate_templates(optimizer, templates)

for template_name, result in results.items():
    status = "✓" if result['valid'] else "✗"
    print(f"{status} {template_name}")
    if not result['valid']:
        for error in result['errors']:
            print(f"  - {error}")
```

### Parallel Template Processing

#### Using ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_templates_parallel(optimizer, template_names, max_workers=4):
    """Process multiple templates in parallel."""
    results = {}
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_template = {
            executor.submit(
                optimizer.process_template_optimized,
                template_name
            ): template_name
            for template_name in template_names
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_template):
            template_name = future_to_template[future]
            try:
                result = future.result()
                results[template_name] = result
            except Exception as e:
                results[template_name] = f"Error: {e}"
    
    return results

# Process templates in parallel
templates = [
    "requirements-template-consolidated.md",
    "design-template-consolidated.md",
    "tasks-template-consolidated.md",
    "component-template-consolidated.md"
]
results = process_templates_parallel(optimizer, templates)

for template_name, result in results.items():
    print(f"Processed: {template_name}")
```

---

## Performance Monitoring and Reporting

### Real-Time Performance Monitoring

#### Setting Up Monitoring

```python
import time
from datetime import datetime

class PerformanceMonitor:
    def __init__(self, optimizer):
        self.optimizer = optimizer
        self.monitoring_active = False
    
    def start_monitoring(self, interval_seconds=60):
        """Start real-time performance monitoring."""
        self.monitoring_active = True
        
        while self.monitoring_active:
            # Get performance summary
            summary = self.optimizer.get_performance_summary()
            
            # Print summary
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[{timestamp}] Performance Summary:")
            print(f"  Latest improvement: {summary['latest_metrics']['improvement_percent']:.1f}%")
            print(f"  Average improvement: {summary['average_improvement']:.1f}%")
            print(f"  Target met: {summary['target_met']}")
            print(f"  Total measurements: {summary['total_measurements']}")
            
            # Wait for next interval
            time.sleep(interval_seconds)
    
    def stop_monitoring(self):
        """Stop performance monitoring."""
        self.monitoring_active = False

# Start monitoring
monitor = PerformanceMonitor(optimizer)
monitor.start_monitoring(interval_seconds=60)
```

### Performance Reporting

#### Generating Performance Reports

```python
def generate_performance_report(optimizer, output_file="performance_report.md"):
    """Generate comprehensive performance report."""
    summary = optimizer.get_performance_summary()
    cache_stats = optimizer.get_cache_stats()
    
    report = f"""# YASK Performance Report

**Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Performance Summary

- **Latest Improvement**: {summary['latest_metrics']['improvement_percent']:.1f}%
- **Average Improvement**: {summary['average_improvement']:.1f}%
- **Target Met**: {summary['target_met']}
- **Total Measurements**: {summary['total_measurements']}

## Cache Statistics

- **Template Cache Size**: {cache_stats['template_cache_size']}
- **Inheritance Cache Size**: {cache_stats['inheritance_cache_size']}
- **Validation Cache Size**: {cache_stats['validation_cache_size']}
- **Total Cached Items**: {cache_stats['total_cached_items']}
- **Cache Hits**: {cache_stats['cache_hits']}
- **Cache Misses**: {cache_stats['cache_misses']}

## Performance History

"""
    
    # Add performance history
    for metrics in optimizer.performance_history[-10:]:
        report += f"- {metrics.operation}: {metrics.improvement_percent:.1f}% improvement\n"
    
    # Write report to file
    with open(output_file, 'w') as f:
        f.write(report)
    
    print(f"Performance report generated: {output_file}")

# Generate report
generate_performance_report(optimizer)
```

### Performance Alerts

#### Setting Up Performance Alerts

```python
class PerformanceAlertSystem:
    def __init__(self, optimizer, threshold_percent=40.0):
        self.optimizer = optimizer
        self.threshold_percent = threshold_percent
    
    def check_performance(self):
        """Check if performance meets threshold."""
        summary = self.optimizer.get_performance_summary()
        
        if not summary['target_met']:
            latest = summary['latest_metrics']['improvement_percent']
            print(f"⚠️  Performance Alert: {latest:.1f}% improvement (target: {self.threshold_percent}%)")
            return False
        
        print(f"✓ Performance OK: {summary['latest_metrics']['improvement_percent']:.1f}% improvement")
        return True
    
    def monitor_performance(self, interval_seconds=300):
        """Monitor performance and send alerts."""
        while True:
            self.check_performance()
            time.sleep(interval_seconds)

# Set up alerts
alert_system = PerformanceAlertSystem(optimizer, threshold_percent=40.0)
alert_system.monitor_performance(interval_seconds=300)
```

---

## Benchmarking Procedures

### Creating Benchmark Suite

#### Benchmark Template

```python
import time
from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    operation: str
    duration_ms: float
    baseline_ms: float
    improvement_percent: float
    timestamp: datetime

class BenchmarkSuite:
    def __init__(self, optimizer):
        self.optimizer = optimizer
        self.results = []
    
    def run_benchmark(self, operation, func, *args, **kwargs):
        """Run a single benchmark."""
        # Warm-up run
        func(*args, **kwargs)
        
        # Measure performance
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        duration_ms = (end_time - start_time) * 1000
        
        # Calculate improvement
        baseline_ms = 100.0  # Default baseline
        improvement_percent = ((baseline_ms - duration_ms) / baseline_ms) * 100
        
        # Store result
        benchmark_result = BenchmarkResult(
            operation=operation,
            duration_ms=duration_ms,
            baseline_ms=baseline_ms,
            improvement_percent=improvement_percent,
            timestamp=datetime.now()
        )
        self.results.append(benchmark_result)
        
        return benchmark_result
    
    def generate_report(self):
        """Generate benchmark report."""
        report = "# Benchmark Report\n\n"
        
        for result in self.results:
            report += f"## {result.operation}\n"
            report += f"- Duration: {result.duration_ms:.2f}ms\n"
            report += f"- Baseline: {result.baseline_ms:.2f}ms\n"
            report += f"- Improvement: {result.improvement_percent:.1f}%\n"
            report += f"- Timestamp: {result.timestamp}\n\n"
        
        return report
```

#### Running Benchmarks

```python
# Initialize benchmark suite
benchmark_suite = BenchmarkSuite(optimizer)

# Run benchmarks
benchmark_suite.run_benchmark(
    "Template Processing",
    optimizer.template_optimizer.process_template_optimized,
    "requirements-template-consolidated.md"
)

benchmark_suite.run_benchmark(
    "Context Loading",
    optimizer.context_loader.load_context,
    "requirements"
)

benchmark_suite.run_benchmark(
    "Cross-Reference Validation",
    optimizer.cross_reference_validator.validate_references,
    "requirements.md"
)

# Generate report
report = benchmark_suite.generate_report()
print(report)
```

### Comparative Benchmarking

#### Comparing Before and After

```python
def compare_performance(before_optimizer, after_optimizer, operation, func, *args, **kwargs):
    """Compare performance before and after optimization."""
    # Measure before
    before_result = before_optimizer.measure_performance(
        operation=operation,
        baseline_ms=100.0,
        func=func,
        *args,
        **kwargs
    )
    
    # Measure after
    after_result = after_optimizer.measure_performance(
        operation=operation,
        baseline_ms=100.0,
        func=func,
        *args,
        **kwargs
    )
    
    # Calculate improvement
    improvement = before_result.metrics.duration_ms - after_result.metrics.duration_ms
    improvement_percent = (improvement / before_result.metrics.duration_ms) * 100
    
    print(f"Before: {before_result.metrics.duration_ms:.2f}ms")
    print(f"After: {after_result.metrics.duration_ms:.2f}ms")
    print(f"Improvement: {improvement:.2f}ms ({improvement_percent:.1f}%)")
    
    return {
        'before': before_result.metrics.duration_ms,
        'after': after_result.metrics.duration_ms,
        'improvement': improvement,
        'improvement_percent': improvement_percent
    }

# Compare performance
comparison = compare_performance(
    before_optimizer,
    after_optimizer,
    "template_processing",
    optimizer.template_optimizer.process_template_optimized,
    "requirements-template-consolidated.md"
)
```

---

## Performance Troubleshooting

### Common Performance Issues

#### Issue 1: Low Cache Hit Rate

**Symptoms**: Cache hit rate below 70%

**Diagnosis**:
```python
hit_rate = calculate_cache_hit_rate(optimizer)
print(f"Cache hit rate: {hit_rate:.1f}%")
```

**Solutions**:
1. Increase cache TTL
2. Preload frequently used templates
3. Check cache key consistency
4. Reduce cache evictions

```python
# Increase TTL
optimizer._cache_ttl = timedelta(hours=48)

# Preload cache
preload_cache(optimizer, frequently_used)
```

#### Issue 2: High Memory Usage

**Symptoms**: Memory usage exceeds expected limits

**Diagnosis**:
```python
import psutil
import os

process = psutil.Process(os.getpid())
memory_info = process.memory_info()
print(f"Memory usage: {memory_info.rss / 1024 / 1024:.2f} MB")
```

**Solutions**:
1. Implement cache size limits
2. Clear cache periodically
3. Reduce cache TTL
4. Optimize cache key generation

```python
# Implement cache size limit
optimizer = TemplatePerformanceOptimizer(template_dir, max_cache_size=500)

# Clear cache
optimizer.template_cache.clear()
```

#### Issue 3: Slow Template Processing

**Symptoms**: Template processing takes longer than expected

**Diagnosis**:
```python
result = optimizer.measure_performance(
    operation="template_processing",
    baseline_ms=100.0,
    func=optimizer.template_optimizer.process_template_optimized,
    "requirements-template-consolidated.md"
)

print(f"Duration: {result.metrics.duration_ms:.2f}ms")
print(f"Improvement: {result.metrics.improvement_percent:.1f}%")
```

**Solutions**:
1. Check cache configuration
2. Optimize template inheritance
3. Reduce template complexity
4. Use parallel processing

```python
# Check cache stats
stats = optimizer.get_cache_stats()
print(f"Cache hits: {stats['cache_hits']}")
print(f"Cache misses: {stats['cache_misses']}")

# Use parallel processing
results = process_templates_parallel(optimizer, templates)
```

#### Issue 4: Performance Degradation Over Time

**Symptoms**: Performance gradually decreases

**Diagnosis**:
```python
# Track performance over time
for i in range(10):
    result = optimizer.measure_performance(
        operation="template_processing",
        baseline_ms=100.0,
        func=optimizer.template_optimizer.process_template_optimized,
        "requirements-template-consolidated.md"
    )
    print(f"Run {i+1}: {result.metrics.duration_ms:.2f}ms")
    time.sleep(10)
```

**Solutions**:
1. Clear cache periodically
2. Monitor memory usage
3. Check for memory leaks
4. Restart optimizer periodically

```python
# Clear cache periodically
import time

while True:
    optimizer.template_cache.clear()
    time.sleep(3600)  # Clear every hour
```

### Performance Optimization Checklist

- [ ] Establish baseline measurements
- [ ] Monitor cache hit rates
- [ ] Tune cache TTL settings
- [ ] Implement cache size limits
- [ ] Preload frequently used templates
- [ ] Use parallel processing for batch operations
- [ ] Monitor memory usage
- [ ] Clear cache periodically
- [ ] Track performance over time
- [ ] Generate regular performance reports

## Related Documentation

- [Performance Optimizer Guide](PERFORMANCE_OPTIMIZER_GUIDE.md)
- [YASK Refactor Architecture](YASK_REFACTOR_ARCHITECTURE.md)
- [API Reference](API_REFERENCE.md)
- [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md)
