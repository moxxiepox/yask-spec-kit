---
date: '2025-12-28'
  description: "validation_policy:
   Overall validation level
  level: {{validation_level|enum('basic',\
    \ 'standard', 'strict', 'comprehensive')}}
  
   Validation stages
  stages:
\
    \     Pre-execution validation
    pr..."
  status: active
    title: Markdown-Exec Validation Template
  version: 6.0.0
tags:
  - system/yask
  - yask/documentation
  - yask/status/active
  - directory/active-projects
  - type/documentation
  - status/active

---

# Markdown-Exec Validation Template

## Template Structure

```yaml
# MARKDOWN-EXEC-VALIDATION-CONFIG
# Version: 1.0
# Last Updated: {{timestamp}}
# Applies to: [code_block_id or pattern]

validation_policy:
  # Overall validation level
  level: {{validation_level|enum('basic', 'standard', 'strict', 'comprehensive')}}
  
  # Validation stages
  stages:
    # Pre-execution validation
    pre_execution:
      enabled: {{pre_exec_enabled|default(true)}}
      checks:
        - syntax_validation
        - security_scan
        - dependency_check
        - placeholder_validation
        - schema_compliance
      
      # Syntax validation settings
      syntax_validation:
        enabled: {{syntax_validation_enabled|default(true)}}
        strict_mode: {{syntax_strict_mode|default(false)}}
        language_specific:
          python:
            check_imports: {{python_check_imports|default(true)}}
            check_syntax: {{python_check_syntax|default(true)}}
            max_line_length: {{python_max_line_length|default(100)}}
            require_type_hints: {{python_require_type_hints|default(false)}}
          javascript:
            check_syntax: {{js_check_syntax|default(true)}}
            check_semicolons: {{js_check_semicolons|default(false)}}
            max_line_length: {{js_max_line_length|default(100)}}
            es_version: {{js_es_version|default('es2020')}}
          typescript:
            check_syntax: {{ts_check_syntax|default(true)}}
            check_types: {{ts_check_types|default(true)}}
            strict_mode: {{ts_strict_mode|default(true)}}
            max_line_length: {{ts_max_line_length|default(100)}}
          bash:
            check_syntax: {{bash_check_syntax|default(true)}}
            shellcheck_enabled: {{bash_shellcheck_enabled|default(true)}}
            strict_mode: {{bash_strict_mode|default(false)}}
      
      # Security scan settings
      security_scan:
        enabled: {{security_scan_enabled|default(true)}}
        scan_types:
          - dangerous_functions
          - unsafe_imports
          - filesystem_access
          - network_operations
          - code_injection_patterns
          - privilege_escalation
        
        # Dangerous function patterns
        dangerous_functions:
          python:
            - eval
            - exec
            - compile
            - __import__
            - input
            - raw_input
          javascript:
            - eval
            - Function
            - setTimeout
            - setInterval
            - execScript
          bash:
            - eval
            - exec
            - source
            - .
        
        # Unsafe import patterns
        unsafe_imports:
          python:
            - os.system
            - subprocess.call
            - subprocess.Popen
            - commands.getoutput
          javascript:
            - child_process
            - fs.promises
            - util.promisify
        
        # Severity levels
        severity_levels:
          critical: {{critical_threshold|default(1)}}
          high: {{high_threshold|default(3)}}
          medium: {{medium_threshold|default(5)}}
          low: {{low_threshold|default(10)}}
        
        # Action on violation
        violation_action: {{violation_action|enum('block', 'warn', 'log')}}
      
      # Dependency check settings
      dependency_check:
        enabled: {{dependency_check_enabled|default(true)}}
        check_types:
          - availability
          - version_compatibility
          - security_vulnerabilities
          - license_compliance
        
        # Package managers
        package_managers:
          python: {{python_package_manager|default('pip')}}
          javascript: {{js_package_manager|default('npm')}}
          typescript: {{ts_package_manager|default('npm')}}
        
        # Version constraints
        version_constraints:
          allow_prerelease: {{allow_prerelease|default(false)}}
          allow_git_urls: {{allow_git_urls|default(false)}}
          max_age_days: {{max_package_age_days|default(365)}}
      
      # Placeholder validation
      placeholder_validation:
        enabled: {{placeholder_validation_enabled|default(true)}}
        required_placeholders: {{required_placeholders|default([])}}
        optional_placeholders: {{optional_placeholders|default([])}}
        validate_defaults: {{validate_defaults|default(true)}}
        
        # Placeholder patterns
        patterns:
          variable: {{variable_pattern|default('\\{\{\\w+\\}\\}')}}
          with_default: {{default_pattern|default('\\{\{\\w+\\|[^}]+\\}\\}')}}
          with_type: {{type_pattern|default('\\{\{\\w+\\|type\\([^)]+\\)\\}\\}')}}
          with_validate: {{validate_pattern|default('\\{\{\\w+\\|validate\\([^)]+\\)\\}\\}')}}
      
      # Schema compliance
      schema_compliance:
        enabled: {{schema_compliance_enabled|default(true)}}
        validate_against: {{validation_schema|default('markdown-exec-code-block-template')}}
        required_fields:
          - language
          - security_level
          - timeout
        optional_fields:
          - dependencies
          - environment_variables
          - working_directory
    
    # During-execution validation
    during_execution:
      enabled: {{during_exec_enabled|default(true)}}
      checks:
        - resource_monitoring
        - security_monitoring
        - output_validation
        - progress_tracking
      
      # Resource monitoring
      resource_monitoring:
        enabled: {{resource_monitoring_enabled|default(true)}}
        check_interval_ms: {{resource_check_interval|default(100)}}
        
        # CPU monitoring
        cpu_monitoring:
          enabled: {{cpu_monitoring_enabled|default(true)}}
          max_percent: {{max_cpu_percent|default(80)}}
          max_time_seconds: {{max_cpu_time_seconds|default(30)}}
          action_on_exceed: {{cpu_exceed_action|enum('warn', 'terminate', 'log')}}
        
        # Memory monitoring
        memory_monitoring:
          enabled: {{memory_monitoring_enabled|default(true)}}
          max_rss_mb: {{max_memory_rss_mb|default(100)}}
          max_vms_mb: {{max_memory_vms_mb|default(200)}}
          action_on_exceed: {{memory_exceed_action|enum('warn', 'terminate', 'log')}}
        
        # Disk I/O monitoring
        disk_io_monitoring:
          enabled: {{disk_io_monitoring_enabled|default(true)}}
          max_read_bytes: {{max_disk_read_bytes|default(10485760)}}
          max_write_bytes: {{max_disk_write_bytes|default(10485760)}}
          action_on_exceed: {{disk_exceed_action|enum('warn', 'terminate', 'log')}}
        
        # Network monitoring
        network_monitoring:
          enabled: {{network_monitoring_enabled|default(true)}}
          max_bytes_sent: {{max_network_sent_bytes|default(1048576)}}
          max_bytes_received: {{max_network_received_bytes|default(1048576)}}
          max_connections: {{max_network_connections|default(5)}}
          action_on_exceed: {{network_exceed_action|enum('warn', 'terminate', 'log')}}
      
      # Security monitoring
      security_monitoring:
        enabled: {{security_monitoring_enabled|default(true)}}
        monitor_types:
          - filesystem_violations
          - network_violations
          - module_violations
          - syscall_violations
        
        # Violation thresholds
        violation_thresholds:
          filesystem: {{fs_violation_threshold|default(3)}}
          network: {{network_violation_threshold|default(1)}}
          module: {{module_violation_threshold|default(5)}}
          syscall: {{syscall_violation_threshold|default(3)}}
        
        # Action on threshold
        threshold_action: {{security_threshold_action|enum('block', 'terminate', 'log', 'alert')}}
      
      # Output validation
      output_validation:
        enabled: {{output_validation_enabled|default(true)}}
        validate_real_time: {{real_time_validation|default(false)}}
        max_output_size: {{max_output_size_bytes|default(1048576)}}
        
        # Output format validation
        format_validation:
          enabled: {{format_validation_enabled|default(true)}}
          expected_format: {{expected_output_format|enum('raw', 'json', 'table', 'markdown')}}
          
          # JSON-specific validation
          json_validation:
            enabled: {{json_validation_enabled|default(true)}}
            validate_schema: {{json_schema_validation|default(true)}}
            schema_file: {{json_schema_file|default('')}}
            allow_partial: {{json_allow_partial|default(false)}}
          
          # Table-specific validation
          table_validation:
            enabled: {{table_validation_enabled|default(true)}}
            expected_columns: {{expected_table_columns|default([])}}
            validate_row_count: {{validate_row_count|default(true)}}
            min_rows: {{min_table_rows|default(1)}}
            max_rows: {{max_table_rows|default(1000)}}
      
      # Progress tracking
      progress_tracking:
        enabled: {{progress_tracking_enabled|default(false)}}
        update_interval_ms: {{progress_update_interval|default(1000)}}
        track_metrics:
          - cpu_usage
          - memory_usage
          - output_size
          - execution_time
    
    # Post-execution validation
    post_execution:
      enabled: {{post_exec_enabled|default(true)}}
      checks:
        - exit_code_validation
        - output_validation
        - result_schema_validation
        - performance_validation
        - security_audit
      
      # Exit code validation
      exit_code_validation:
        enabled: {{exit_code_validation_enabled|default(true)}}
        expected_exit_code: {{expected_exit_code|default(0)}}
        allow_non_zero: {{allow_non_zero_exit|default(false)}}
        acceptable_exit_codes: {{acceptable_exit_codes|default([0])}}
        
        # Exit code mapping
        exit_code_meanings:
          0: "Success"
          1: "General error"
          2: "Misuse of shell builtins"
          126: "Command invoked cannot execute"
          127: "Command not found"
          128: "Invalid exit argument"
          130: "Script terminated by Control-C"
      
      # Output validation
      output_validation:
        enabled: {{post_output_validation_enabled|default(true)}}
        
        # Content validation
        content_validation:
          enabled: {{content_validation_enabled|default(true)}}
          must_contain: {{output_must_contain|default([])}}
          must_not_contain: {{output_must_not_contain|default([])}}
          pattern_match: {{output_pattern_match|default('')}}
          
          # Size validation
          size_validation:
            enabled: {{size_validation_enabled|default(true)}}
            min_size: {{min_output_size|default(1)}}
            max_size: {{max_output_size|default(10485760)}}
            size_unit: {{size_unit|enum('bytes', 'kb', 'mb')}}
        
        # Format validation
        format_validation:
          enabled: {{post_format_validation_enabled|default(true)}}
          expected_format: {{post_expected_format|enum('raw', 'json', 'table', 'markdown')}}
          
          # JSON validation
          json_validation:
            enabled: {{post_json_validation_enabled|default(true)}}
            validate_schema: {{post_json_schema_validation|default(true)}}
            schema_definition: {{json_schema_definition|default('')}}
            required_fields: {{json_required_fields|default([])}}
            optional_fields: {{json_optional_fields|default([])}}
            allow_extra_fields: {{json_allow_extra|default(false)}}
          
          # Table validation
          table_validation:
            enabled: {{post_table_validation_enabled|default(true)}}
            expected_headers: {{expected_table_headers|default([])}}
            validate_data_types: {{validate_table_data_types|default(true)}}
            column_types: {{table_column_types|default({})}}
      
      # Result schema validation
      result_schema_validation:
        enabled: {{result_schema_validation_enabled|default(true)}}
        schema_type: {{result_schema_type|enum('json_schema', 'zod_schema', 'custom')}}
        
        # JSON Schema validation
        json_schema:
          file: {{result_json_schema_file|default('')}}
          definition: {{result_json_schema_def|default({})}}
          strict_validation: {{json_schema_strict|default(true)}}
        
        # Zod schema validation
        zod_schema:
          definition: {{zod_schema_definition|default('')}}
          strict_validation: {{zod_schema_strict|default(true)}}
        
        # Custom validation
        custom_validator:
          command: {{custom_validator_cmd|default('')}}
          timeout: {{custom_validator_timeout|default(5000)}}
          expected_exit_code: {{custom_validator_exit_code|default(0)}}
      
      # Performance validation
      performance_validation:
        enabled: {{performance_validation_enabled|default(true)}}
        
        # Duration validation
        duration_validation:
          enabled: {{duration_validation_enabled|default(true)}}
          max_duration_ms: {{max_duration_ms|default(10000)}}
          min_duration_ms: {{min_duration_ms|default(0)}}
          warn_on_slow: {{warn_on_slow|default(true)}}
          slow_threshold_ms: {{slow_threshold_ms|default(5000)}}
        
        # Resource usage validation
        resource_usage_validation:
          enabled: {{resource_usage_validation_enabled|default(true)}}
          max_cpu_percent: {{max_cpu_percent|default(80)}}
          max_memory_mb: {{max_memory_mb|default(100)}}
          max_disk_io_mb: {{max_disk_io_mb|default(10)}}
          warn_on_high_usage: {{warn_on_high_usage|default(true)}}
      
      # Security audit
      security_audit:
        enabled: {{security_audit_enabled|default(true)}}
        audit_types:
          - filesystem_access_log
          - network_access_log
          - module_load_log
          - syscall_log
          - privilege_changes
        
        # Audit thresholds
        audit_thresholds:
          suspicious_activity: {{suspicious_activity_threshold|default(3)}}
          critical_violations: {{critical_violations_threshold|default(1)}}
        
        # Audit actions
        audit_actions:
          log_all: {{audit_log_all|default(false)}}
          alert_on_violation: {{alert_on_violation|default(true)}}
          terminate_on_critical: {{terminate_on_critical|default(true)}}

# Validation result reporting
reporting:
  # Report format
  format: {{report_format|enum('json', 'yaml', 'markdown', 'text')}}
  
  # Report sections
  include_sections:
    - validation_summary
    - detailed_results
    - performance_metrics
    - security_audit
    - recommendations
  
  # Validation summary
  validation_summary:
    show_status: {{show_validation_status|default(true)}}
    show_score: {{show_validation_score|default(true)}}
    show_critical_issues: {{show_critical_issues|default(true)}}
  
  # Detailed results
  detailed_results:
    show_all_checks: {{show_all_checks|default(false)}}
    show_failed_only: {{show_failed_only|default(false)}}
    include_error_details: {{include_error_details|default(true)}}
  
  # Performance metrics
  performance_metrics:
    show_resource_usage: {{show_resource_usage|default(true)}}
    show_duration: {{show_duration|default(true)}}
    show_benchmarks: {{show_benchmarks|default(false)}}
  
  # Recommendations
  recommendations:
    generate_recommendations: {{generate_recommendations|default(true)}}
    include_security_tips: {{include_security_tips|default(true)}}
    include_performance_tips: {{include_performance_tips|default(true)}}

# YASK Integration Metadata
_yask:
  template_version: "1.0"
  document_type: "validation-configuration"
  requirements_traceability:
    - requirement: "markdown-exec-requirements.md#validation-requirements"
      design: "markdown-exec-design.md#validation-architecture"
      tasks: "markdown-exec-tasks.md#validation-implementation"
  cross_references:
    - "#[[file:markdown-exec-code-block-template.md]]"
    - "#[[file:markdown-exec-security-config-template.md]]"
    - "#[[file:markdown-exec-event-schema-template.md]]"
```

## Zod-like Validation Schemas

### TypeScript Schema Definitions

```typescript
import { z } from 'zod';

// Base validation schemas
const SyntaxValidationSchema = z.object({
  enabled: z.boolean().default(true),
  strict_mode: z.boolean().default(false),
  language_specific: z.object({
    python: z.object({
      check_imports: z.boolean().default(true),
      check_syntax: z.boolean().default(true),
      max_line_length: z.number().int().positive().default(100),
      require_type_hints: z.boolean().default(false)
    }).default({}),
    javascript: z.object({
      check_syntax: z.boolean().default(true),
      check_semicolons: z.boolean().default(false),
      max_line_length: z.number().int().positive().default(100),
      es_version: z.enum(['es5', 'es6', 'es2015', 'es2017', 'es2020', 'es2022']).default('es2020')
    }).default({}),
    typescript: z.object({
      check_syntax: z.boolean().default(true),
      check_types: z.boolean().default(true),
      strict_mode: z.boolean().default(true),
      max_line_length: z.number().int().positive().default(100)
    }).default({}),
    bash: z.object({
      check_syntax: z.boolean().default(true),
      shellcheck_enabled: z.boolean().default(true),
      strict_mode: z.boolean().default(false)
    }).default({})
  }).default({})
});

const SecurityScanSchema = z.object({
  enabled: z.boolean().default(true),
  scan_types: z.array(z.enum([
    'dangerous_functions',
    'unsafe_imports',
    'filesystem_access',
    'network_operations',
    'code_injection_patterns',
    'privilege_escalation'
  ])).default(['dangerous_functions', 'unsafe_imports']),
  dangerous_functions: z.object({
    python: z.array(z.string()).default(['eval', 'exec', 'compile', '__import__']),
    javascript: z.array(z.string()).default(['eval', 'Function', 'setTimeout', 'setInterval']),
    bash: z.array(z.string()).default(['eval', 'exec', 'source'])
  }).default({}),
  unsafe_imports: z.object({
    python: z.array(z.string()).default(['os.system', 'subprocess.call', 'subprocess.Popen']),
    javascript: z.array(z.string()).default(['child_process', 'fs.promises'])
  }).default({}),
  severity_levels: z.object({
    critical: z.number().int().min(1).default(1),
    high: z.number().int().min(1).default(3),
    medium: z.number().int().min(1).default(5),
    low: z.number().int().min(1).default(10)
  }).default({}),
  violation_action: z.enum(['block', 'warn', 'log']).default('block')
});

const PlaceholderValidationSchema = z.object({
  enabled: z.boolean().default(true),
  required_placeholders: z.array(z.string()).default([]),
  optional_placeholders: z.array(z.string()).default([]),
  validate_defaults: z.boolean().default(true),
  patterns: z.object({
    variable: z.string().default('\\{\\{\\w+\\}\\}'),
    with_default: z.string().default('\\{\\{\\w+\\|[^}]+\\}\\}'),
    with_type: z.string().default('\\{\\{\\w+\\|type\\([^)]+\\)\\}\\}'),
    with_validate: z.string().default('\\{\\{\\w+\\|validate\\([^)]+\\)\\}\\}')
  }).default({})
});

const ResourceMonitoringSchema = z.object({
  enabled: z.boolean().default(true),
  check_interval_ms: z.number().int().min(10).default(100),
  cpu_monitoring: z.object({
    enabled: z.boolean().default(true),
    max_percent: z.number().min(0).max(100).default(80),
    max_time_seconds: z.number().min(0).default(30),
    action_on_exceed: z.enum(['warn', 'terminate', 'log']).default('warn')
  }).default({}),
  memory_monitoring: z.object({
    enabled: z.boolean().default(true),
    max_rss_mb: z.number().min(0).default(100),
    max_vms_mb: z.number().min(0).default(200),
    action_on_exceed: z.enum(['warn', 'terminate', 'log']).default('warn')
  }).default({}),
  disk_io_monitoring: z.object({
    enabled: z.boolean().default(true),
    max_read_bytes: z.number().int().min(0).default(10485760),
    max_write_bytes: z.number().int().min(0).default(10485760),
    action_on_exceed: z.enum(['warn', 'terminate', 'log']).default('warn')
  }).default({}),
  network_monitoring: z.object({
    enabled: z.boolean().default(true),
    max_bytes_sent: z.number().int().min(0).default(1048576),
    max_bytes_received: z.number().int().min(0).default(1048576),
    max_connections: z.number().int().min(0).default(5),
    action_on_exceed: z.enum(['warn', 'terminate', 'log']).default('warn')
  }).default({})
});

const OutputValidationSchema = z.object({
  enabled: z.boolean().default(true),
  validate_real_time: z.boolean().default(false),
  max_output_size: z.number().int().min(1024).default(1048576),
  format_validation: z.object({
    enabled: z.boolean().default(true),
    expected_format: z.enum(['raw', 'json', 'table', 'markdown']).default('raw'),
    json_validation: z.object({
      enabled: z.boolean().default(true),
      validate_schema: z.boolean().default(true),
      schema_file: z.string().default(''),
      allow_partial: z.boolean().default(false)
    }).default({}),
    table_validation: z.object({
      enabled: z.boolean().default(true),
      expected_columns: z.array(z.string()).default([]),
      validate_row_count: z.boolean().default(true),
      min_rows: z.number().int().min(0).default(1),
      max_rows: z.number().int().min(1).default(1000)
    }).default({})
  }).default({})
});

const ExitCodeValidationSchema = z.object({
  enabled: z.boolean().default(true),
  expected_exit_code: z.number().int().min(0).default(0),
  allow_non_zero: z.boolean().default(false),
  acceptable_exit_codes: z.array(z.number().int().min(0)).default([0]),
  exit_code_meanings: z.record(z.number().int().min(0), z.string()).default({
    0: 'Success',
    1: 'General error',
    2: 'Misuse of shell builtins',
    126: 'Command invoked cannot execute',
    127: 'Command not found'
  })
});

const ContentValidationSchema = z.object({
  enabled: z.boolean().default(true),
  must_contain: z.array(z.string()).default([]),
  must_not_contain: z.array(z.string()).default([]),
  pattern_match: z.string().default(''),
  size_validation: z.object({
    enabled: z.boolean().default(true),
    min_size: z.number().int().min(0).default(1),
    max_size: z.number().int().min(1).default(10485760),
    size_unit: z.enum(['bytes', 'kb', 'mb']).default('bytes')
  }).default({})
});

const JsonValidationSchema = z.object({
  enabled: z.boolean().default(true),
  validate_schema: z.boolean().default(true),
  schema_definition: z.any().optional(),
  required_fields: z.array(z.string()).default([]),
  optional_fields: z.array(z.string()).default([]),
  allow_extra_fields: z.boolean().default(false)
});

const TableValidationSchema = z.object({
  enabled: z.boolean().default(true),
  expected_headers: z.array(z.string()).default([]),
  validate_data_types: z.boolean().default(true),
  column_types: z.record(z.string(), z.enum(['string', 'number', 'boolean', 'date'])).default({})
});

const PostOutputValidationSchema = z.object({
  enabled: z.boolean().default(true),
  content_validation: ContentValidationSchema.default({}),
  format_validation: z.object({
    enabled: z.boolean().default(true),
    expected_format: z.enum(['raw', 'json', 'table', 'markdown']).default('raw'),
    json_validation: JsonValidationSchema.default({}),
    table_validation: TableValidationSchema.default({})
  }).default({})
});

const ResultSchemaValidationSchema = z.object({
  enabled: z.boolean().default(true),
  schema_type: z.enum(['json_schema', 'zod_schema', 'custom']).default('json_schema'),
  json_schema: z.object({
    file: z.string().default(''),
    definition: z.any().optional(),
    strict_validation: z.boolean().default(true)
  }).default({}),
  zod_schema: z.object({
    definition: z.string().default(''),
    strict_validation: z.boolean().default(true)
  }).default({}),
  custom_validator: z.object({
    command: z.string().default(''),
    timeout: z.number().int().positive().default(5000),
    expected_exit_code: z.number().int().min(0).default(0)
  }).default({})
});

const DurationValidationSchema = z.object({
  enabled: z.boolean().default(true),
  max_duration_ms: z.number().int().positive().default(10000),
  min_duration_ms: z.number().int().min(0).default(0),
  warn_on_slow: z.boolean().default(true),
  slow_threshold_ms: z.number().int().positive().default(5000)
});

const ResourceUsageValidationSchema = z.object({
  enabled: z.boolean().default(true),
  max_cpu_percent: z.number().min(0).max(100).default(80),
  max_memory_mb: z.number().min(0).default(100),
  max_disk_io_mb: z.number().min(0).default(10),
  warn_on_high_usage: z.boolean().default(true)
});

const PerformanceValidationSchema = z.object({
  enabled: z.boolean().default(true),
  duration_validation: DurationValidationSchema.default({}),
  resource_usage_validation: ResourceUsageValidationSchema.default({})
});

const SecurityAuditSchema = z.object({
  enabled: z.boolean().default(true),
  audit_types: z.array(z.enum([
    'filesystem_access_log',
    'network_access_log',
    'module_load_log',
    'syscall_log',
    'privilege_changes'
  ])).default(['filesystem_access_log', 'network_access_log']),
  audit_thresholds: z.object({
    suspicious_activity: z.number().int().min(1).default(3),
    critical_violations: z.number().int().min(1).default(1)
  }).default({}),
  audit_actions: z.object({
    log_all: z.boolean().default(false),
    alert_on_violation: z.boolean().default(true),
    terminate_on_critical: z.boolean().default(true)
  }).default({})
});

// Main validation policy schema
const ValidationPolicySchema = z.object({
  level: z.enum(['basic', 'standard', 'strict', 'comprehensive']).default('standard'),
  stages: z.object({
    pre_execution: z.object({
      enabled: z.boolean().default(true),
      checks: z.array(z.enum([
        'syntax_validation',
        'security_scan',
        'dependency_check',
        'placeholder_validation',
        'schema_compliance'
      ])).default(['syntax_validation', 'security_scan']),
      syntax_validation: SyntaxValidationSchema.default({}),
      security_scan: SecurityScanSchema.default({}),
      dependency_check: z.object({
        enabled: z.boolean().default(true),
        check_types: z.array(z.enum([
          'availability',
          'version_compatibility',
          'security_vulnerabilities',
          'license_compliance'
        ])).default(['availability']),
        package_managers: z.object({
          python: z.string().default('pip'),
          javascript: z.string().default('npm'),
          typescript: z.string().default('npm')
        }).default({}),
        version_constraints: z.object({
          allow_prerelease: z.boolean().default(false),
          allow_git_urls: z.boolean().default(false),
          max_age_days: z.number().int().positive().default(365)
        }).default({})
      }).default({}),
      placeholder_validation: PlaceholderValidationSchema.default({}),
      schema_compliance: z.object({
        enabled: z.boolean().default(true),
        validate_against: z.string().default('markdown-exec-code-block-template'),
        required_fields: z.array(z.string()).default(['language', 'security_level', 'timeout']),
        optional_fields: z.array(z.string()).default(['dependencies', 'environment_variables'])
      }).default({})
    }).default({}),
    during_execution: z.object({
      enabled: z.boolean().default(true),
      checks: z.array(z.enum([
        'resource_monitoring',
        'security_monitoring',
        'output_validation',
        'progress_tracking'
      ])).default(['resource_monitoring', 'security_monitoring']),
      resource_monitoring: ResourceMonitoringSchema.default({}),
      security_monitoring: z.object({
        enabled: z.boolean().default(true),
        monitor_types: z.array(z.enum([
          'filesystem_violations',
          'network_violations',
          'module_violations',
          'syscall_violations'
        ])).default(['filesystem_violations', 'network_violations']),
        violation_thresholds: z.object({
          filesystem: z.number().int().min(1).default(3),
          network: z.number().int().min(1).default(1),
          module: z.number().int().min(1).default(5),
          syscall: z.number().int().min(1).default(3)
        }).default({}),
        threshold_action: z.enum(['block', 'terminate', 'log', 'alert']).default('block')
      }).default({}),
      output_validation: OutputValidationSchema.default({}),
      progress_tracking: z.object({
        enabled: z.boolean().default(false),
        update_interval_ms: z.number().int().positive().default(1000),
        track_metrics: z.array(z.string()).default(['cpu_usage', 'memory_usage'])
      }).default({})
    }).default({}),
    post_execution: z.object({
      enabled: z.boolean().default(true),
      checks: z.array(z.enum([
        'exit_code_validation',
        'output_validation',
        'result_schema_validation',
        'performance_validation',
        'security_audit'
      ])).default(['exit_code_validation', 'output_validation']),
      exit_code_validation: ExitCodeValidationSchema.default({}),
      output_validation: PostOutputValidationSchema.default({}),
      result_schema_validation: ResultSchemaValidationSchema.default({}),
      performance_validation: PerformanceValidationSchema.default({}),
      security_audit: SecurityAuditSchema.default({})
    }).default({})
  }).default({})
});

// Type exports
export type ValidationPolicy = z.infer<typeof ValidationPolicySchema>;
export type SyntaxValidationConfig = z.infer<typeof SyntaxValidationSchema>;
export type SecurityScanConfig = z.infer<typeof SecurityScanSchema>;
export type ResourceMonitoringConfig = z.infer<typeof ResourceMonitoringSchema>;
export type OutputValidationConfig = z.infer<typeof OutputValidationSchema>;

// Validation function
export function validatePolicy(policy: unknown): ValidationPolicy {
  return ValidationPolicySchema.parse(policy);
}
```

## Adaptation Rules

### Rule 1: Validation Level Auto-Selection
```
ANALYZE code_block FOR:
  - security_level == "critical" → validation_level = "comprehensive"
  - security_level == "high" → validation_level = "strict"
  - security_level == "medium" → validation_level = "standard"
  - security_level == "low" → validation_level = "basic"
  
  - contains_sensitive_data → validation_level = max(validation_level, "strict")
  - network_operations_enabled → validation_level = max(validation_level, "strict")
  - external_dependencies → validation_level = max(validation_level, "standard")
```

### Rule 2: Security Scan Rule Generation
```
FOR each language:
  LOAD dangerous_functions[language]
  LOAD unsafe_imports[language]
  ANALYZE code_block FOR pattern matches
  GENERATE security_rules[]
  CALCULATE risk_score = count(matches) * severity_weights
```

### Rule 3: Performance Threshold Calculation
```
CALCULATE thresholds BASED ON:
  - code_complexity (lines of code, cyclomatic complexity)
  - language_overhead (python: 1.0, js: 0.8, bash: 0.5)
  - security_level_multiplier (low: 1.0, medium: 1.2, high: 1.5, critical: 2.0)
  - resource_constraints (available_cpu, available_memory)
  
max_duration_ms = base_duration * complexity_factor * security_multiplier
max_memory_mb = base_memory * complexity_factor * security_multiplier
max_cpu_percent = base_cpu * security_multiplier
```

### Rule 4: Output Validation Rule Generation
```
IF expected_output_format == "json":
  GENERATE json_schema_validation
  PARSE expected_output_schema
  EXTRACT required_fields[]
  EXTRACT field_types{}
  
ELIF expected_output_format == "table":
  GENERATE table_validation
  EXTRACT expected_headers[]
  INFER column_types FROM sample_data
  
ELIF expected_output_format == "markdown":
  GENERATE markdown_validation
  VALIDATE markdown_syntax
  CHECK for proper_formatting
```

## Validation Examples

### Example 1: Python Data Processing Validation
```yaml
validation_policy:
  level: "standard"
  stages:
    pre_execution:
      syntax_validation:
        language_specific:
          python:
            check_imports: true
            check_syntax: true
            require_type_hints: true
      security_scan:
        scan_types: ["dangerous_functions", "unsafe_imports"]
    post_execution:
      exit_code_validation:
        expected_exit_code: 0
      output_validation:
        format_validation:
          expected_format: "json"
          json_validation:
            validate_schema: true
            required_fields: ["status", "data", "timestamp"]
      performance_validation:
        duration_validation:
          max_duration_ms: 5000
```

### Example 2: JavaScript API Validation
```yaml
validation_policy:
  level: "strict"
  stages:
    pre_execution:
      syntax_validation:
        language_specific:
          javascript:
            check_syntax: true
            es_version: "es2020"
      security_scan:
        scan_types: ["network_operations", "dangerous_functions"]
    during_execution:
      resource_monitoring:
        network_monitoring:
          enabled: true
          max_bytes_sent: 1048576
          max_connections: 3
    post_execution:
      exit_code_validation:
        expected_exit_code: 0
      output_validation:
        content_validation:
          must_contain: ["success", "data"]
          must_not_contain: ["error", "exception"]
```

### Example 3: Bash System Check Validation
```yaml
validation_policy:
  level: "comprehensive"
  stages:
    pre_execution:
      syntax_validation:
        language_specific:
          bash:
            check_syntax: true
            shellcheck_enabled: true
            strict_mode: true
      security_scan:
        scan_types: ["filesystem_access", "privilege_escalation"]
    post_execution:
      exit_code_validation:
        expected_exit_code: 0
      output_validation:
        format_validation:
          expected_format: "raw"
        content_validation:
          pattern_match: "System\\s+Information:"
```

## YASK Integration

### Requirements Traceability
```
_Requirements: markdown-exec-requirements.md#validation-requirements
_Design: markdown-exec-design.md#validation-architecture
_Tasks: markdown-exec-tasks.md#validation-implementation
```

### Cross-Reference Format
```markdown
See code execution template: #[[file:markdown-exec-code-block-template.md]]
See security configuration: #[[file:markdown-exec-security-config-template.md]]
See event schema: #[[file:markdown-exec-event-schema-template.md]]
```

### Template Variables
- `{{validation_level}}` - Overall validation strictness
- `{{security_scan_enabled}}` - Whether security scanning is active
- `{{max_duration_ms}}` - Maximum allowed execution time
- `{{expected_exit_code}}` - Expected process exit code
- `{{expected_output_format}}` - Expected output format (json/table/raw/markdown)
- `{{required_fields}}` - Required fields in output
- `{{max_cpu_percent}}` - Maximum CPU usage percentage
- `{{max_memory_mb}}` - Maximum memory usage in MB