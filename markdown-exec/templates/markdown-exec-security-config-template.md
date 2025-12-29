---
date: '2025-12-28'
  description: "security_policy:
   Overall security level
  level: {{security_level|enum('low',\
    \ 'medium', 'high', 'critical')}}
  
   Execution constraints
  execution:
\
    \    max_runtime: {{max_runtime_ms|default(5000..."
  status: active
    title: Markdown-Exec Security Configuration Template
  version: 6.0.0
tags:
  - system/yask
  - yask/documentation
  - yask/status/active
  - directory/active-projects
  - type/documentation
  - status/active

---

# Markdown-Exec Security Configuration Template

## Template Structure

```yaml
# MARKDOWN-EXEC-SECURITY-CONFIG
# Version: 1.0
# Last Updated: {{timestamp}}
# Applies to: [code_block_id or pattern]

security_policy:
  # Overall security level
  level: {{security_level|enum('low', 'medium', 'high', 'critical')}}
  
  # Execution constraints
  execution:
    max_runtime: {{max_runtime_ms|default(5000)}}
    max_memory: {{max_memory_mb|default(100)}}
    max_cpu_percent: {{max_cpu_percent|default(50)}}
    allow_parallel: {{allow_parallel|default(false)}}
    max_concurrent: {{max_concurrent|default(1)}}
  
  # Filesystem permissions
  filesystem:
    # Access mode: whitelist, blacklist, or readonly
    access_mode: {{filesystem_access|enum('whitelist', 'blacklist', 'readonly', 'none')}}
    
    # Allowed paths (for whitelist mode)
    allowed_paths:
      {{#each allowed_paths}}
      - path: "{{this.path}}"
        permissions: {{this.permissions|enum('read', 'write', 'readwrite')}}
        recursive: {{this.recursive|default(false)}}
      {{/each}}
    
    # Blocked paths (for blacklist mode)
    blocked_paths:
      {{#each blocked_paths}}
      - "{{this}}"
      {{/each}}
    
    # Read-only paths
    readonly_paths:
      {{#each readonly_paths}}
      - "{{this}}"
      {{/each}}
    
    # Temporary file restrictions
    temp_file_restrictions:
      max_size: {{temp_max_size|default(10485760)}}  # 10MB default
      allowed_dirs: {{temp_allowed_dirs|default(['/tmp', './temp'])
      cleanup_on_exit: {{temp_cleanup|default(true)}}
  
  # Network permissions
  network:
    # Overall network access
    enabled: {{network_enabled|default(false)}}
    
    # Allowed protocols
    allowed_protocols:
      {{#each allowed_protocols}}
      - "{{this}}"
      {{/each}}
    
    # Allowed hosts (IP or domain)
    allowed_hosts:
      {{#each allowed_hosts}}
      - "{{this}}"
      {{/each}}
    
    # Allowed ports
    allowed_ports:
      {{#each allowed_ports}}
      - {{this}}
      {{/each}}
    
    # Rate limiting
    rate_limiting:
      max_requests: {{max_requests|default(10)}}
      time_window: {{time_window_seconds|default(60)}}
      burst_size: {{burst_size|default(5)}}
    
    # Timeout for network operations
    timeout: {{network_timeout|default(5000)}}
  
  # Process permissions
  process:
    # Subprocess execution
    allow_subprocess: {{allow_subprocess|default(false)}}
    allowed_commands:
      {{#each allowed_commands}}
      - "{{this}}"
      {{/each}}
    
    # Signal handling
    allowed_signals:
      {{#each allowed_signals}}
      - {{this}}
      {{/each}}
    
    # Resource limits
    resource_limits:
      max_processes: {{max_processes|default(1)}}
      max_threads: {{max_threads|default(10)}}
      max_file_descriptors: {{max_file_descriptors|default(100)}}
  
  # Environment variable restrictions
  environment:
    # Allowed environment variables
    allowed_vars:
      {{#each allowed_env_vars}}
      - "{{this}}"
      {{/each}}
    
    # Blocked environment variables
    blocked_vars:
      {{#each blocked_env_vars}}
      - "{{this}}"
      {{/each}}
    
    # Required environment variables
    required_vars:
      {{#each required_env_vars}}
      - name: "{{this.name}}"
        value: "{{this.value}}"
        {{#if this.secret}}
        secret: true
        {{/if}}
      {{/each}}
    
    # Variable prefix restrictions
    allowed_prefixes:
      {{#each allowed_env_prefixes}}
      - "{{this}}"
      {{/each}}
  
  # Module/package restrictions (language-specific)
  modules:
    # Python-specific
    python:
      allowed_modules:
        {{#each python_allowed_modules}}
        - "{{this}}"
        {{/each}}
      blocked_modules:
        {{#each python_blocked_modules}}
        - "{{this}}"
        {{/each}}
      allowed_imports:
        {{#each python_allowed_imports}}
        - "{{this}}"
        {{/each}}
    
    # Node.js-specific
    javascript:
      allowed_packages:
        {{#each js_allowed_packages}}
        - "{{this}}"
        {{/each}}
      blocked_packages:
        {{#each js_blocked_packages}}
        - "{{this}}"
        {{/each}}
      allowed_builtin_modules:
        {{#each js_allowed_builtin}}
        - "{{this}}"
        {{/each}}
  
  # System call filtering (advanced)
  system_calls:
    # Filter mode: whitelist, blacklist, or audit
    filter_mode: {{syscall_filter|enum('whitelist', 'blacklist', 'audit', 'none')}}
    
    # Allowed system calls (whitelist mode)
    allowed_calls:
      {{#each allowed_syscalls}}
      - "{{this}}"
      {{/each}}
    
    # Blocked system calls (blacklist mode)
    blocked_calls:
      {{#each blocked_syscalls}}
      - "{{this}}"
      {{/each}}
  
  # Security monitoring
  monitoring:
    # Enable security event logging
    log_security_events: {{log_security_events|default(true)}}
    
    # Alert on violations
    alert_on_violation: {{alert_on_violation|default(true)}}
    
    # Violation thresholds
    violation_thresholds:
      filesystem: {{fs_violation_threshold|default(3)}}
      network: {{network_violation_threshold|default(1)}}
      process: {{process_violation_threshold|default(2)}}
      memory: {{memory_violation_threshold|default(5)}}
    
    # Action on threshold exceeded
    threshold_action: {{threshold_action|enum('block', 'terminate', 'log', 'alert')}}
  
  # Container/isolation settings
  isolation:
    # Use container/isolation technology
    use_isolation: {{use_isolation|default(true)}}
    
    # Isolation type
    type: {{isolation_type|enum('chroot', 'docker', 'firejail', 'nsjail', 'none')}}
    
    # Container image (if applicable)
    container_image: "{{container_image|default('alpine:latest')}}"
    
    # Drop capabilities
    drop_capabilities:
      {{#each drop_capabilities}}
      - "{{this}}"
      {{/each}}
    
    # Read-only filesystem
    readonly_root: {{readonly_root|default(true)}}
    
    # Disable privileged mode
    no_privileged: {{no_privileged|default(true)}}

# Default policies for different security levels
default_policies:
  low:
    description: "Minimal restrictions, suitable for trusted code"
    filesystem:
      access_mode: "readonly"
      allowed_paths:
        - "/tmp"
        - "./data"
    network:
      enabled: true
      allowed_hosts: ["localhost", "127.0.0.1"]
    process:
      allow_subprocess: true
    modules:
      python:
        blocked_modules: ["os", "subprocess", "sys"]
  
  medium:
    description: "Balanced security for semi-trusted code"
    filesystem:
      access_mode: "whitelist"
      allowed_paths:
        - path: "/tmp"
          permissions: "readwrite"
        - path: "./sandbox"
          permissions: "readwrite"
    network:
      enabled: false
    process:
      allow_subprocess: false
    modules:
      python:
        allowed_modules: ["json", "re", "math", "datetime", "collections"]
  
  high:
    description: "Strict security for untrusted code"
    filesystem:
      access_mode: "none"
    network:
      enabled: false
    process:
      allow_subprocess: false
      max_processes: 1
    modules:
      python:
        allowed_modules: ["json", "math"]
      javascript:
        allowed_builtin_modules: ["fs", "path"]
    isolation:
      use_isolation: true
      type: "firejail"
  
  critical:
    description: "Maximum security for potentially malicious code"
    filesystem:
      access_mode: "none"
    network:
      enabled: false
    process:
      allow_subprocess: false
      max_processes: 1
      max_threads: 1
    modules:
      python:
        allowed_modules: []
      javascript:
        allowed_builtin_modules: []
    system_calls:
      filter_mode: "whitelist"
      allowed_calls: ["read", "write", "exit", "exit_group"]
    isolation:
      use_isolation: true
      type: "nsjail"
      readonly_root: true
      no_privileged: true

# Audit logging configuration
audit:
  enabled: {{audit_enabled|default(true)}}
  log_level: {{audit_log_level|enum('debug', 'info', 'warning', 'error')}}
  log_file: "{{audit_log_file|default('./logs/security-audit.log')}}"
  
  # What to log
  log_events:
    - execution_start
    - execution_complete
    - security_violation
    - resource_limit_exceeded
    - filesystem_access
    - network_access
    - process_spawn
    - module_load
  
  # Log format
  format: {{log_format|enum('json', 'text')}}
  
  # Retention policy
  retention:
    max_size: {{log_max_size|default(104857600)}}  # 100MB
    max_files: {{log_max_files|default(10)}}
    compress: {{log_compress|default(true)}}

# Compliance settings
compliance:
  # Standards to comply with
  standards:
    {{#each compliance_standards}}
    - "{{this}}"
    {{/each}}
  
  # Data protection
  data_protection:
    encrypt_sensitive_data: {{encrypt_sensitive|default(true)}}
    mask_logs: {{mask_logs|default(true)}}
    secure_delete: {{secure_delete|default(true)}}
  
  # Audit requirements
  audit_requirements:
    log_all_access: {{log_all_access|default(true)}}
    immutable_logs: {{immutable_logs|default(false)}}
    tamper_detection: {{tamper_detection|default(true)}}

# YASK Integration Metadata
_yask:
  template_version: "1.0"
  document_type: "security-configuration"
  requirements_traceability:
    - requirement: "markdown-exec-requirements.md#security-sandboxing"
      design: "markdown-exec-design.md#security-architecture"
      tasks: "markdown-exec-tasks.md#security-implementation"
  cross_references:
    - "#[[file:markdown-exec-code-block-template.md]]"
    - "#[[file:markdown-exec-event-schema.md]]"
    - "#[[file:markdown-exec-validation.md]]"
```

## Adaptation Rules

### Rule 1: Security Level Auto-Detection
```
ANALYZE code_block FOR:
  - file_system_operations → level = "high" or "critical"
  - network_operations → level = "critical"
  - subprocess_spawning → level = "high"
  - sensitive_data_access → level = "high"
  - pure_computation → level = "low" or "medium"
```

### Rule 2: Permission Matrix Generation
```
FOR each security_level:
  LOAD default_policy[security_level]
  MERGE with custom_permissions IF specified
  VALIDATE against compliance_requirements
  GENERATE final_security_config
```

### Rule 3: Filesystem Access Calculation
```
IF access_mode == "whitelist":
  allowed_paths = explicit_allowed_paths + default_allowed_paths[security_level]
  blocked_paths = []
ELSE IF access_mode == "blacklist":
  allowed_paths = ["*"]
  blocked_paths = explicit_blocked_paths + default_blocked_paths[security_level]
ELSE IF access_mode == "readonly":
  allowed_paths = explicit_paths
  blocked_paths = []
  SET all permissions to "read"
```

### Rule 4: Network Access Determination
```
IF code_contains_network_operations:
  IF security_level IN ["low", "medium"] AND network_explicitly_enabled:
    allowed_hosts = explicit_allowed_hosts + ["localhost", "127.0.0.1"]
    rate_limiting = default_rate_limits[security_level]
  ELSE:
    network_enabled = false
    allowed_hosts = []
```

## Permission Matrix Examples

### Matrix 1: Development Environment
```yaml
security_level: "low"
filesystem:
  access_mode: "readonly"
  allowed_paths:
    - "/project"
    - "/tmp"
network:
  enabled: true
  allowed_hosts: ["localhost", "api.internal.com"]
process:
  allow_subprocess: true
  allowed_commands: ["git", "npm", "pip"]
```

### Matrix 2: Data Processing
```yaml
security_level: "medium"
filesystem:
  access_mode: "whitelist"
  allowed_paths:
    - path: "/data/input"
      permissions: "read"
    - path: "/data/output"
      permissions: "readwrite"
    - path: "/tmp"
      permissions: "readwrite"
network:
  enabled: false
process:
  allow_subprocess: false
modules:
  python:
    allowed_modules: ["pandas", "numpy", "json", "csv"]
```

### Matrix 3: Untrusted Code
```yaml
security_level: "critical"
filesystem:
  access_mode: "none"
network:
  enabled: false
process:
  allow_subprocess: false
  max_processes: 1
  max_threads: 1
isolation:
  use_isolation: true
  type: "nsjail"
  readonly_root: true
system_calls:
  filter_mode: "whitelist"
  allowed_calls: ["read", "write", "exit", "exit_group", "brk"]
```

## YASK Integration

### Requirements Traceability
```
_Requirements: markdown-exec-requirements.md#security-requirements
_Design: markdown-exec-design.md#security-architecture
_Tasks: markdown-exec-tasks.md#security-implementation
```

### Cross-Reference Format
```markdown
See code execution template: #[[file:markdown-exec-code-block-template.md]]
See event tracking: #[[file:markdown-exec-event-schema.md]]
See validation rules: #[[file:markdown-exec-validation.md]]
```

### Template Variables
- `{{security_level}}` - Overall security classification
- `{{max_runtime_ms}}` - Maximum execution time in milliseconds
- `{{allowed_paths}}` - List of permitted filesystem paths
- `{{network_enabled}}` - Whether network access is permitted
- `{{allowed_modules}}` - Permitted importable modules/packages
- `{{isolation_type}}` - Container/isolation technology to use