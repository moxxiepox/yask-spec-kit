---
date: '2025-12-28'
  description: "// Base schemas
const UserContextSchema = z.object({
  user_id: z.string().uuid().optional(),
\
    \  session_id: z.string().uuid().optional(),
  permissions: z.array(z.string()).default([])
\
    });"
  status: active
    title: Markdown-Exec Event Schema Template
  version: 6.0.0
tags:
  - system/yask
  - yask/documentation
  - yask/status/active
  - directory/active-projects
  - type/documentation
  - status/active

---

# Markdown-Exec Event Schema Template

## Template Structure

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Markdown-Exec Execution Event",
  "description": "Schema for tracking markdown-exec code block execution events",
  "type": "object",
  "required": ["event_id", "timestamp", "event_type", "execution_context"],
  "properties": {
    "event_id": {
      "description": "Unique identifier for this event",
      "type": "string",
      "format": "uuid",
      "example": "{{uuid}}"
    },
    "timestamp": {
      "description": "Event occurrence timestamp in ISO 8601 format",
      "type": "string",
      "format": "date-time",
      "example": "{{timestamp_iso8601}}"
    },
    "event_type": {
      "description": "Type of execution event",
      "type": "string",
      "enum": [
        "execution_started",
        "execution_completed",
        "execution_failed",
        "security_violation",
        "resource_limit_exceeded",
        "timeout_occurred",
        "validation_failed",
        "cache_hit",
        "cache_miss",
        "dependency_installation_started",
        "dependency_installation_completed",
        "dependency_installation_failed"
      ]
    },
    "execution_context": {
      "description": "Context information for the execution",
      "type": "object",
      "required": ["execution_id", "code_block_id", "language", "security_level"],
      "properties": {
        "execution_id": {
          "description": "Unique identifier for this execution instance",
          "type": "string",
          "format": "uuid",
          "example": "{{execution_uuid}}"
        },
        "code_block_id": {
          "description": "Identifier for the code block being executed",
          "type": "string",
          "example": "{{code_block_identifier}}"
        },
        "language": {
          "description": "Programming language of the code block",
          "type": "string",
          "enum": ["python", "javascript", "typescript", "bash", "sh"],
          "example": "{{language}}"
        },
        "security_level": {
          "description": "Security classification for this execution",
          "type": "string",
          "enum": ["low", "medium", "high", "critical"],
          "example": "{{security_level}}"
        },
        "execution_mode": {
          "description": "How the code block is being executed",
          "type": "string",
          "enum": ["inline", "block", "interactive"],
          "example": "{{execution_mode}}"
        },
        "source_document": {
          "description": "Document containing the code block",
          "type": "object",
          "properties": {
            "file_path": {
              "type": "string",
              "example": "{{source_file_path}}"
            },
            "document_id": {
              "type": "string",
              "example": "{{document_id}}"
            },
            "section": {
              "type": "string",
              "example": "{{section_identifier}}"
            }
          }
        },
        "user_context": {
          "description": "Information about the user triggering execution",
          "type": "object",
          "properties": {
            "user_id": {
              "type": "string",
              "example": "{{user_id}}"
            },
            "session_id": {
              "type": "string",
              "example": "{{session_id}}"
            },
            "permissions": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "example": ["{{permission1}}", "{{permission2}}"]
            }
          }
        }
      }
    },
    "code_block_metadata": {
      "description": "Metadata about the code block being executed",
      "type": "object",
      "properties": {
        "line_number": {
          "description": "Line number where the code block starts",
          "type": "integer",
          "example": {{line_number}}
        },
        "code_hash": {
          "description": "SHA256 hash of the code content",
          "type": "string",
          "example": "{{code_sha256_hash}}"
        },
        "code_size": {
          "description": "Size of the code in bytes",
          "type": "integer",
          "example": {{code_size_bytes}}
        },
        "dependencies": {
          "description": "Declared dependencies for this code block",
          "type": "array",
          "items": {
            "type": "string"
          },
          "example": ["{{dependency1}}", "{{dependency2}}"]
        },
        "timeout_configured": {
          "description": "Configured timeout in milliseconds",
          "type": "integer",
          "example": {{configured_timeout_ms}}
        },
        "expected_output": {
          "description": "Expected output pattern or validation rules",
          "type": "object",
          "properties": {
            "format": {
              "type": "string",
              "enum": ["raw", "json", "table", "markdown"]
            },
            "validation_schema": {
              "type": "string"
            },
            "exit_code": {
              "type": "integer"
            }
          }
        }
      }
    },
    "execution_metrics": {
      "description": "Performance and resource usage metrics",
      "type": "object",
      "properties": {
        "start_time": {
          "description": "Execution start timestamp",
          "type": "string",
          "format": "date-time",
          "example": "{{start_time_iso8601}}"
        },
        "end_time": {
          "description": "Execution end timestamp",
          "type": "string",
          "format": "date-time",
          "example": "{{end_time_iso8601}}"
        },
        "duration_ms": {
          "description": "Total execution time in milliseconds",
          "type": "integer",
          "example": {{duration_milliseconds}}
        },
        "cpu_usage": {
          "description": "CPU usage statistics",
          "type": "object",
          "properties": {
            "percent": {
              "description": "Average CPU usage percentage",
              "type": "number",
              "example": {{cpu_percent}}
            },
            "peak_percent": {
              "description": "Peak CPU usage percentage",
              "type": "number",
              "example": {{peak_cpu_percent}}
            },
            "time_seconds": {
              "description": "CPU time used in seconds",
              "type": "number",
              "example": {{cpu_time_seconds}}
            }
          }
        },
        "memory_usage": {
          "description": "Memory usage statistics",
          "type": "object",
          "properties": {
            "peak_rss_mb": {
              "description": "Peak resident set size in MB",
              "type": "number",
              "example": {{peak_memory_mb}}
            },
            "peak_vms_mb": {
              "description": "Peak virtual memory size in MB",
              "type": "number",
              "example": {{peak_vms_mb}}
            },
            "current_rss_mb": {
              "description": "Current resident set size in MB",
              "type": "number",
              "example": {{current_memory_mb}}
            }
          }
        },
        "disk_io": {
          "description": "Disk I/O statistics",
          "type": "object",
          "properties": {
            "read_bytes": {
              "description": "Bytes read from disk",
              "type": "integer",
              "example": {{disk_read_bytes}}
            },
            "write_bytes": {
              "description": "Bytes written to disk",
              "type": "integer",
              "example": {{disk_write_bytes}}
            },
            "read_count": {
              "description": "Number of read operations",
              "type": "integer",
              "example": {{disk_read_count}}
            },
            "write_count": {
              "description": "Number of write operations",
              "type": "integer",
              "example": {{disk_write_count}}
            }
          }
        },
        "network_io": {
          "description": "Network I/O statistics (if enabled)",
          "type": "object",
          "properties": {
            "bytes_sent": {
              "description": "Bytes sent over network",
              "type": "integer",
              "example": {{network_bytes_sent}}
            },
            "bytes_received": {
              "description": "Bytes received over network",
              "type": "integer",
              "example": {{network_bytes_received}}
            },
            "connections": {
              "description": "Number of network connections",
              "type": "integer",
              "example": {{network_connection_count}}
            }
          }
        }
      }
    },
    "execution_result": {
      "description": "Result of the code execution",
      "type": "object",
      "properties": {
        "exit_code": {
          "description": "Process exit code",
          "type": "integer",
          "example": {{exit_code}}
        },
        "stdout": {
          "description": "Standard output content",
          "type": "string",
          "example": "{{stdout_content}}"
        },
        "stderr": {
          "description": "Standard error content",
          "type": "string",
          "example": "{{stderr_content}}"
        },
        "output_truncated": {
          "description": "Whether output was truncated due to size limits",
          "type": "boolean",
          "example": {{output_truncated}}
        },
        "output_size": {
          "description": "Size of output in bytes",
          "type": "integer",
          "example": {{output_size_bytes}}
        },
        "validation_result": {
          "description": "Result of output validation",
          "type": "object",
          "properties": {
            "passed": {
              "type": "boolean",
              "example": {{validation_passed}}
            },
            "errors": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "example": ["{{validation_error1}}", "{{validation_error2}}"]
            },
            "warnings": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "example": ["{{validation_warning1}}"]
            }
          }
        }
      }
    },
    "security_events": {
      "description": "Security-related events detected during execution",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "event_type": {
            "description": "Type of security event",
            "type": "string",
            "enum": [
              "filesystem_violation",
              "network_violation",
              "module_violation",
              "syscall_violation",
              "resource_exceeded",
              "privilege_escalation_attempt"
            ]
          },
          "severity": {
            "description": "Severity of the security event",
            "type": "string",
            "enum": ["low", "medium", "high", "critical"]
          },
          "timestamp": {
            "description": "When the event occurred",
            "type": "string",
            "format": "date-time"
          },
          "details": {
            "description": "Detailed information about the event",
            "type": "object",
            "properties": {
              "violated_policy": {
                "type": "string"
              },
              "attempted_action": {
                "type": "string"
              },
              "resource": {
                "type": "string"
              },
              "blocked": {
                "type": "boolean"
              }
            }
          }
        }
      }
    },
    "cache_information": {
      "description": "Cache-related information for this execution",
      "type": "object",
      "properties": {
        "cache_hit": {
          "description": "Whether this execution used cached results",
          "type": "boolean",
          "example": {{cache_hit}}
        },
        "cache_key": {
          "description": "Cache key used for this execution",
          "type": "string",
          "example": "{{cache_key_hash}}"
        },
        "cache_ttl": {
          "description": "Time-to-live for cache entry in seconds",
          "type": "integer",
          "example": {{cache_ttl_seconds}}
        },
        "cached_result_age": {
          "description": "Age of cached result in seconds",
          "type": "integer",
          "example": {{cached_result_age_seconds}}
        }
      }
    },
    "error_information": {
      "description": "Error details for failed executions",
      "type": "object",
      "properties": {
        "error_type": {
          "description": "Type of error that occurred",
          "type": "string",
          "enum": [
            "timeout",
            "memory_limit",
            "cpu_limit",
            "security_violation",
            "dependency_error",
            "syntax_error",
            "runtime_error",
            "validation_error",
            "system_error"
          ]
        },
        "error_message": {
          "description": "Human-readable error message",
          "type": "string",
          "example": "{{error_message}}"
        },
        "error_details": {
          "description": "Technical details about the error",
          "type": "object",
          "properties": {
            "stack_trace": {
              "type": "string"
            },
            "exception_type": {
              "type": "string"
            },
            "line_number": {
              "type": "integer"
            },
            "file_path": {
              "type": "string"
            }
          }
        },
        "recovery_action": {
          "description": "Action taken to recover from error",
          "type": "string",
          "enum": ["retry", "fallback", "terminate", "alert"]
        }
      }
    },
    "dependency_information": {
      "description": "Information about dependency installation",
      "type": "object",
      "properties": {
        "dependencies_installed": {
          "description": "Whether dependencies were installed",
          "type": "boolean",
          "example": {{dependencies_installed}}
        },
        "installation_duration_ms": {
          "description": "Time taken to install dependencies",
          "type": "integer",
          "example": {{installation_duration_ms}}
        },
        "installed_packages": {
          "description": "List of packages that were installed",
          "type": "array",
          "items": {
            "type": "string"
          },
          "example": ["{{package1}}", "{{package2}}"]
        },
        "installation_errors": {
          "description": "Errors encountered during installation",
          "type": "array",
          "items": {
            "type": "string"
          },
          "example": ["{{install_error1}}"]
        }
      }
    }
  }
}
```

## Event Type Definitions

### 1. Execution Started Event
```json
{
  "event_id": "{{uuid}}",
  "timestamp": "{{timestamp_iso8601}}",
  "event_type": "execution_started",
  "execution_context": {
    "execution_id": "{{execution_uuid}}",
    "code_block_id": "{{code_block_identifier}}",
    "language": "{{language}}",
    "security_level": "{{security_level}}",
    "execution_mode": "{{execution_mode}}",
    "source_document": {
      "file_path": "{{source_file_path}}",
      "document_id": "{{document_id}}",
      "section": "{{section_identifier}}"
    },
    "user_context": {
      "user_id": "{{user_id}}",
      "session_id": "{{session_id}}",
      "permissions": ["{{permission1}}", "{{permission2}}"]
    }
  },
  "code_block_metadata": {
    "line_number": {{line_number}},
    "code_hash": "{{code_sha256_hash}}",
    "code_size": {{code_size_bytes}},
    "dependencies": ["{{dependency1}}", "{{dependency2}}"],
    "timeout_configured": {{configured_timeout_ms}}
  },
  "cache_information": {
    "cache_hit": {{cache_hit}},
    "cache_key": "{{cache_key_hash}}"
  }
}
```

### 2. Execution Completed Event
```json
{
  "event_id": "{{uuid}}",
  "timestamp": "{{timestamp_iso8601}}",
  "event_type": "execution_completed",
  "execution_context": {
    "execution_id": "{{execution_uuid}}",
    "code_block_id": "{{code_block_identifier}}",
    "language": "{{language}}",
    "security_level": "{{security_level}}"
  },
  "execution_metrics": {
    "start_time": "{{start_time_iso8601}}",
    "end_time": "{{end_time_iso8601}}",
    "duration_ms": {{duration_milliseconds}},
    "cpu_usage": {
      "percent": {{cpu_percent}},
      "peak_percent": {{peak_cpu_percent}},
      "time_seconds": {{cpu_time_seconds}}
    },
    "memory_usage": {
      "peak_rss_mb": {{peak_memory_mb}},
      "peak_vms_mb": {{peak_vms_mb}},
      "current_rss_mb": {{current_memory_mb}}
    }
  },
  "execution_result": {
    "exit_code": {{exit_code}},
    "stdout": "{{stdout_content}}",
    "stderr": "{{stderr_content}}",
    "output_truncated": {{output_truncated}},
    "output_size": {{output_size_bytes}},
    "validation_result": {
      "passed": {{validation_passed}},
      "errors": ["{{validation_error1}}", "{{validation_error2}}"],
      "warnings": ["{{validation_warning1}}"]
    }
  },
  "security_events": [
    {
      "event_type": "{{security_event_type}}",
      "severity": "{{security_severity}}",
      "timestamp": "{{security_event_timestamp}}",
      "details": {
        "violated_policy": "{{violated_policy}}",
        "attempted_action": "{{attempted_action}}",
        "resource": "{{resource}}",
        "blocked": {{blocked}}
      }
    }
  ]
}
```

### 3. Security Violation Event
```json
{
  "event_id": "{{uuid}}",
  "timestamp": "{{timestamp_iso8601}}",
  "event_type": "security_violation",
  "execution_context": {
    "execution_id": "{{execution_uuid}}",
    "code_block_id": "{{code_block_identifier}}",
    "language": "{{language}}",
    "security_level": "{{security_level}}",
    "user_context": {
      "user_id": "{{user_id}}",
      "session_id": "{{session_id}}"
    }
  },
  "security_events": [
    {
      "event_type": "{{violation_type}}",
      "severity": "{{violation_severity}}",
      "timestamp": "{{violation_timestamp}}",
      "details": {
        "violated_policy": "{{violated_policy}}",
        "attempted_action": "{{attempted_action}}",
        "resource": "{{violated_resource}}",
        "blocked": {{blocked}},
        "violation_count": {{violation_count}}
      }
    }
  ],
  "execution_metrics": {
    "duration_ms": {{duration_before_violation}}
  },
  "error_information": {
    "error_type": "security_violation",
    "error_message": "{{security_error_message}}",
    "recovery_action": "{{recovery_action}}"
  }
}
```

### 4. Resource Limit Exceeded Event
```json
{
  "event_id": "{{uuid}}",
  "timestamp": "{{timestamp_iso8601}}",
  "event_type": "resource_limit_exceeded",
  "execution_context": {
    "execution_id": "{{execution_uuid}}",
    "code_block_id": "{{code_block_identifier}}",
    "language": "{{language}}"
  },
  "execution_metrics": {
    "start_time": "{{start_time_iso8601}}",
    "duration_ms": {{duration_before_limit}},
    "cpu_usage": {
      "percent": {{cpu_percent_at_limit}},
      "peak_percent": {{peak_cpu_percent}}
    },
    "memory_usage": {
      "peak_rss_mb": {{memory_at_limit_mb}},
      "limit_mb": {{configured_limit_mb}}
    }
  },
  "error_information": {
    "error_type": "{{limit_type}}",
    "error_message": "{{limit_error_message}}",
    "error_details": {
      "limit_exceeded": "{{exceeded_limit}}",
      "current_value": {{current_value}},
      "limit_value": {{limit_value}}
    },
    "recovery_action": "{{limit_recovery_action}}"
  }
}
```

## Zod-like Validation Schema

### TypeScript Schema Definition
```typescript
import { z } from 'zod';

// Base schemas
const UserContextSchema = z.object({
  user_id: z.string().uuid().optional(),
  session_id: z.string().uuid().optional(),
  permissions: z.array(z.string()).default([])
});

const SourceDocumentSchema = z.object({
  file_path: z.string().optional(),
  document_id: z.string().optional(),
  section: z.string().optional()
});

const ExecutionContextSchema = z.object({
  execution_id: z.string().uuid(),
  code_block_id: z.string(),
  language: z.enum(['python', 'javascript', 'typescript', 'bash', 'sh']),
  security_level: z.enum(['low', 'medium', 'high', 'critical']),
  execution_mode: z.enum(['inline', 'block', 'interactive']).default('block'),
  source_document: SourceDocumentSchema.optional(),
  user_context: UserContextSchema.optional()
});

const CodeBlockMetadataSchema = z.object({
  line_number: z.number().int().positive().optional(),
  code_hash: z.string().optional(),
  code_size: z.number().int().positive().optional(),
  dependencies: z.array(z.string()).default([]),
  timeout_configured: z.number().int().positive().optional(),
  expected_output: z.object({
    format: z.enum(['raw', 'json', 'table', 'markdown']).optional(),
    validation_schema: z.string().optional(),
    exit_code: z.number().int().optional()
  }).optional()
});

const CpuUsageSchema = z.object({
  percent: z.number().min(0).max(100).optional(),
  peak_percent: z.number().min(0).max(100).optional(),
  time_seconds: z.number().min(0).optional()
});

const MemoryUsageSchema = z.object({
  peak_rss_mb: z.number().min(0).optional(),
  peak_vms_mb: z.number().min(0).optional(),
  current_rss_mb: z.number().min(0).optional()
});

const DiskIoSchema = z.object({
  read_bytes: z.number().int().min(0).optional(),
  write_bytes: z.number().int().min(0).optional(),
  read_count: z.number().int().min(0).optional(),
  write_count: z.number().int().min(0).optional()
});

const NetworkIoSchema = z.object({
  bytes_sent: z.number().int().min(0).optional(),
  bytes_received: z.number().int().min(0).optional(),
  connections: z.number().int().min(0).optional()
});

const ExecutionMetricsSchema = z.object({
  start_time: z.string().datetime().optional(),
  end_time: z.string().datetime().optional(),
  duration_ms: z.number().int().min(0).optional(),
  cpu_usage: CpuUsageSchema.optional(),
  memory_usage: MemoryUsageSchema.optional(),
  disk_io: DiskIoSchema.optional(),
  network_io: NetworkIoSchema.optional()
});

const ValidationResultSchema = z.object({
  passed: z.boolean(),
  errors: z.array(z.string()).default([]),
  warnings: z.array(z.string()).default([])
});

const ExecutionResultSchema = z.object({
  exit_code: z.number().int().optional(),
  stdout: z.string().default(''),
  stderr: z.string().default(''),
  output_truncated: z.boolean().default(false),
  output_size: z.number().int().min(0).optional(),
  validation_result: ValidationResultSchema.optional()
});

const SecurityEventDetailsSchema = z.object({
  violated_policy: z.string().optional(),
  attempted_action: z.string().optional(),
  resource: z.string().optional(),
  blocked: z.boolean().default(true)
});

const SecurityEventSchema = z.object({
  event_type: z.enum([
    'filesystem_violation',
    'network_violation',
    'module_violation',
    'syscall_violation',
    'resource_exceeded',
    'privilege_escalation_attempt'
  ]),
  severity: z.enum(['low', 'medium', 'high', 'critical']),
  timestamp: z.string().datetime(),
  details: SecurityEventDetailsSchema
});

const CacheInformationSchema = z.object({
  cache_hit: z.boolean().optional(),
  cache_key: z.string().optional(),
  cache_ttl: z.number().int().min(0).optional(),
  cached_result_age: z.number().int().min(0).optional()
});

const ErrorDetailsSchema = z.object({
  stack_trace: z.string().optional(),
  exception_type: z.string().optional(),
  line_number: z.number().int().positive().optional(),
  file_path: z.string().optional()
});

const ErrorInformationSchema = z.object({
  error_type: z.enum([
    'timeout',
    'memory_limit',
    'cpu_limit',
    'security_violation',
    'dependency_error',
    'syntax_error',
    'runtime_error',
    'validation_error',
    'system_error'
  ]),
  error_message: z.string(),
  error_details: ErrorDetailsSchema.optional(),
  recovery_action: z.enum(['retry', 'fallback', 'terminate', 'alert']).optional()
});

const DependencyInformationSchema = z.object({
  dependencies_installed: z.boolean().optional(),
  installation_duration_ms: z.number().int().min(0).optional(),
  installed_packages: z.array(z.string()).default([]),
  installation_errors: z.array(z.string()).default([])
});

// Main event schema
const MarkdownExecEventSchema = z.object({
  event_id: z.string().uuid(),
  timestamp: z.string().datetime(),
  event_type: z.enum([
    'execution_started',
    'execution_completed',
    'execution_failed',
    'security_violation',
    'resource_limit_exceeded',
    'timeout_occurred',
    'validation_failed',
    'cache_hit',
    'cache_miss',
    'dependency_installation_started',
    'dependency_installation_completed',
    'dependency_installation_failed'
  ]),
  execution_context: ExecutionContextSchema,
  code_block_metadata: CodeBlockMetadataSchema.optional(),
  execution_metrics: ExecutionMetricsSchema.optional(),
  execution_result: ExecutionResultSchema.optional(),
  security_events: z.array(SecurityEventSchema).default([]),
  cache_information: CacheInformationSchema.optional(),
  error_information: ErrorInformationSchema.optional(),
  dependency_information: DependencyInformationSchema.optional()
});

// Type export
export type MarkdownExecEvent = z.infer<typeof MarkdownExecEventSchema>;

// Validation function
export function validateEvent(event: unknown): MarkdownExecEvent {
  return MarkdownExecEventSchema.parse(event);
}

// Event creation helpers
export function createExecutionStartedEvent(
  context: ExecutionContext,
  metadata: CodeBlockMetadata,
  cacheInfo?: CacheInformation
): MarkdownExecEvent {
  return validateEvent({
    event_id: crypto.randomUUID(),
    timestamp: new Date().toISOString(),
    event_type: 'execution_started',
    execution_context: context,
    code_block_metadata: metadata,
    cache_information: cacheInfo
  });
}

export function createExecutionCompletedEvent(
  context: ExecutionContext,
  metrics: ExecutionMetrics,
  result: ExecutionResult,
  securityEvents: SecurityEvent[] = []
): MarkdownExecEvent {
  return validateEvent({
    event_id: crypto.randomUUID(),
    timestamp: new Date().toISOString(),
    event_type: 'execution_completed',
    execution_context: context,
    execution_metrics: metrics,
    execution_result: result,
    security_events: securityEvents
  });
}
```

## Adaptation Rules

### Rule 1: Event Type Determination
```
IF execution_status == "started" THEN event_type = "execution_started"
IF execution_status == "completed" AND exit_code == 0 THEN event_type = "execution_completed"
IF execution_status == "completed" AND exit_code != 0 THEN event_type = "execution_failed"
IF security_violation_detected THEN event_type = "security_violation"
IF resource_limit_exceeded THEN event_type = "resource_limit_exceeded"
IF timeout_occurred THEN event_type = "timeout_occurred"
IF validation_failed THEN event_type = "validation_failed"
IF cache_lookup AND cache_exists THEN event_type = "cache_hit"
IF cache_lookup AND NOT cache_exists THEN event_type = "cache_miss"
```

### Rule 2: Security Event Classification
```
FOR each security_event:
  IF filesystem_access_violation THEN severity = "high"
  IF network_access_violation THEN severity = "critical"
  IF module_import_violation THEN severity = "medium"
  IF syscall_violation THEN severity = "high"
  IF resource_exceeded THEN severity = "medium"
  IF privilege_escalation THEN severity = "critical"
  
  IF severity == "critical" THEN alert_immediately = true
  IF violation_count > threshold THEN escalate = true
```

### Rule 3: Performance Metrics Collection
```
FOR each execution:
  COLLECT cpu_usage_samples[] every 100ms
  CALCULATE cpu_percent = average(cpu_usage_samples)
  CALCULATE peak_cpu_percent = max(cpu_usage_samples)
  
  COLLECT memory_usage_samples[] every 100ms
  CALCULATE peak_memory_mb = max(memory_usage_samples)
  
  IF disk_io_enabled:
    COLLECT disk_read_bytes, disk_write_bytes
    COLLECT disk_read_count, disk_write_count
  
  IF network_enabled:
    COLLECT network_bytes_sent, network_bytes_received
    COLLECT network_connection_count
```

### Rule 4: Cache Key Generation
```
CALCULATE cache_key_components:
  - code_hash (SHA256 of code content)
  - language
  - security_level
  - input_data_hash (if applicable)
  - dependency_versions[] (if applicable)
  
GENERATE cache_key = SHA256(concatenate(cache_key_components))
DETERMINE cache_ttl based on security_level:
  low: 3600 seconds (1 hour)
  medium: 1800 seconds (30 minutes)
  high: 300 seconds (5 minutes)
  critical: 60 seconds (1 minute)
```

## YASK Integration

### Requirements Traceability
```
_Requirements: markdown-exec-requirements.md#event-tracking
_Design: markdown-exec-design.md#telemetry-architecture
_Tasks: markdown-exec-tasks.md#event-implementation
```

### Cross-Reference Format
```markdown
See code execution template: #[[file:markdown-exec-code-block-template.md]]
See security configuration: #[[file:markdown-exec-security-config-template.md]]
See validation rules: #[[file:markdown-exec-validation-template.md]]
```

### Template Variables
- `{{uuid}}` - Auto-generated unique identifier
- `{{timestamp_iso8601}}` - ISO 8601 formatted timestamp
- `{{execution_uuid}}` - Execution instance identifier
- `{{code_block_identifier}}` - Code block reference
- `{{language}}` - Programming language
- `{{security_level}}` - Security classification
- `{{execution_mode}}` - Execution mode (inline/block/interactive)
- `{{duration_milliseconds}}` - Execution duration
- `{{exit_code}}` - Process exit code
- `{{cache_hit}}` - Cache hit indicator