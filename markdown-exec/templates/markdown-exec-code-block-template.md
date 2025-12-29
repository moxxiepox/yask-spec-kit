---
date: '2025-12-28'
  description: '<!-- Expected Output -->
  
  
    [expected output pattern or validation rules]'
  status: active
    title: Markdown-Exec Code Block Template
  version: 6.0.0
tags:
  - system/yask
  - yask/documentation
  - yask/status/active
  - directory/active-projects
  - type/documentation
  - status/active

---

# Markdown-Exec Code Block Template

## Template Structure

```markdown
<!-- MARKDOWN-EXEC-CODE-BLOCK -->
<!-- Language: [python|javascript|bash|typescript] -->
<!-- Execution Mode: [inline|block|interactive] -->
<!-- Security Level: [low|medium|high|critical] -->
<!-- Timeout: [milliseconds] -->
<!-- Max Output: [bytes] -->
<!-- Working Directory: [path] -->
<!-- Environment Variables: [key=value pairs] -->
<!-- Dependencies: [package list] -->
<!-- Validation Schema: [schema reference] -->
<!-- Error Handling: [continue|stop|retry] -->
<!-- Output Format: [raw|json|table|markdown] -->

```[language]
[executable code with placeholders]
```

<!-- Expected Output -->
```
[expected output pattern or validation rules]
```

<!-- Validation Rules -->
- Output must match expected pattern
- Exit code must be 0
- Execution time under [timeout]ms
- No security violations detected
- Resource usage within limits

<!-- Usage Example -->
```markdown
```python exec="true" 
import json
import sys

def process_data(data):
    return {"processed": True, "input": data}

result = process_data("{{input_data}}")
print(json.dumps(result))
```
```
```

## Language-Specific Templates

### Python Template
```python exec="true" timeout="5000" security="medium"
import json
import sys
import os
from typing import Dict, Any

def main():
    # Configuration
    config = {
        "input": "{{input_value}}",
        "mode": "{{execution_mode|default('process')}}",
        "verbose": {{verbose|default('False')}}
    }
    
    # Processing logic
    try:
        result = process_function(config)
        print(json.dumps(result))
        sys.exit(0)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

def process_function(config: Dict[str, Any]) -> Dict[str, Any]:
    # Implementation placeholder
    return {"status": "success", "data": config}

if __name__ == "__main__":
    main()
```

### JavaScript/TypeScript Template
```javascript exec="true" timeout="3000" security="medium"
const fs = require('fs');
const path = require('path');

interface Config {
  input: string;
  mode: string;
  verbose: boolean;
}

interface Result {
  status: string;
  data: any;
  timestamp: number;
}

async function main(): Promise<void> {
  const config: Config = {
    input: "{{input_value}}",
    mode: "{{execution_mode|default('process')}}",
    verbose: {{verbose|default('false')}}
  };

  try {
    const result: Result = await processFunction(config);
    console.log(JSON.stringify(result));
    process.exit(0);
  } catch (error) {
    console.error(JSON.stringify({ error: error.message }));
    process.exit(1);
  }
}

async function processFunction(config: Config): Promise<Result> {
  // Implementation placeholder
  return {
    status: "success",
    data: config,
    timestamp: Date.now()
  };
}

main().catch(error => {
  console.error(JSON.stringify({ error: error.message }));
  process.exit(1);
});
```

### Bash Template
```bash exec="true" timeout="2000" security="low"
#!/bin/bash

# Configuration
INPUT_VALUE="{{input_value}}"
EXECUTION_MODE="{{execution_mode|default('process')}}"
VERBOSE="{{verbose|default('false')}}"

# Error handling
set -euo pipefail

echo "Starting execution with mode: $EXECUTION_MODE"

# Main processing
process_function() {
    local input="$1"
    local mode="$2"
    
    # Implementation placeholder
    result=$(jq -n \
        --arg status "success" \
        --arg data "$input" \
        --arg mode "$mode" \
        '{status: $status, data: $data, mode: $mode}')
    
    echo "$result"
}

# Execute and output
result=$(process_function "$INPUT_VALUE" "$EXECUTION_MODE")
echo "$result"
exit 0
```

## Placeholder System

### Variable Placeholders
- `{{variable_name}}` - Required variable
- `{{variable_name|default('value')}}` - Optional with default
- `{{variable_name|type('int')}}` - Type-constrained variable
- `{{variable_name|validate('regex')}}` - Validated variable

### Environment Placeholders
- `{{env.HOME}}` - Environment variable
- `{{config.setting}}` - Configuration value
- `{{context.path}}` - Context variable
- `{{timestamp}}` - Auto-generated timestamp
- `{{uuid}}` - Auto-generated UUID

### Dynamic Placeholders
- `{{file.content('path')}}` - File content injection
- `{{command.output('cmd')}}` - Command output injection
- `{{api.response('endpoint')}}` - API response injection
- `{{template.render('name')}}` - Template rendering

## Adaptation Rules

### Rule 1: Language Detection
```
IF code_block starts with "```python" THEN use Python template
IF code_block starts with "```javascript" or "```typescript" THEN use JS/TS template
IF code_block starts with "```bash" or "```sh" THEN use Bash template
ELSE use generic template with language inference
```

### Rule 2: Security Level Assignment
```
IF code contains file system operations THEN security = "high"
IF code contains network operations THEN security = "critical"
IF code contains only data processing THEN security = "medium"
IF code contains only calculations THEN security = "low"
```

### Rule 3: Timeout Calculation
```
timeout = base_timeout + (complexity_factor * line_count) + network_delay
base_timeout: 1000ms for simple, 5000ms for complex
complexity_factor: 10ms per line for simple, 50ms per line for complex
network_delay: 2000ms if network operations detected
```

### Rule 4: Dependency Detection
```
FOR each import/require statement:
  IF package not in standard library THEN add to dependencies
  IF version specified THEN include version constraint
  IF package requires compilation THEN mark as "build-dependency"
```

## Validation Schema Integration

### Zod-like Schema Definition
```typescript
const codeBlockSchema = z.object({
  language: z.enum(['python', 'javascript', 'typescript', 'bash']),
  executionMode: z.enum(['inline', 'block', 'interactive']),
  securityLevel: z.enum(['low', 'medium', 'high', 'critical']),
  timeout: z.number().min(100).max(60000),
  maxOutput: z.number().min(1024).max(10485760),
  workingDirectory: z.string().optional(),
  environmentVariables: z.record(z.string()).optional(),
  dependencies: z.array(z.string()).optional(),
  validationSchema: z.string().optional(),
  errorHandling: z.enum(['continue', 'stop', 'retry']),
  outputFormat: z.enum(['raw', 'json', 'table', 'markdown']),
  code: z.string().min(1),
  expectedOutput: z.string().optional(),
  validationRules: z.array(z.string()).optional()
});
```

## YASK Integration

### Requirements Traceability
```
_Requirements: markdown-exec-requirements.md#code-execution_
_Design: markdown-exec-design.md#security-sandboxing_
_Tasks: markdown-exec-tasks.md#implementation_
```

### Cross-Reference Format
```markdown
See security configuration: #[[file:markdown-exec-security-config.md]]
See event schema: #[[file:markdown-exec-event-schema.md]]
See validation rules: #[[file:markdown-exec-validation.md]]
```

## Usage Examples

### Example 1: Data Processing
```python exec="true" security="medium" timeout="3000"
import json

def analyze_data(data):
    return {
        "count": len(data),
        "unique": len(set(data)),
        "summary": {
            "min": min(data) if data else None,
            "max": max(data) if data else None
        }
    }

sample_data = [1, 2, 3, 4, 5, 3, 2, 1]
result = analyze_data(sample_data)
print(json.dumps(result, indent=2))
```

### Example 2: File Analysis
```javascript exec="true" security="high" timeout="5000"
const fs = require('fs');
const path = require('path');

function analyzeDirectory(dirPath) {
  const stats = {
    totalFiles: 0,
    totalSize: 0,
    extensions: {}
  };
  
  function scan(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        scan(fullPath);
      } else {
        stats.totalFiles++;
        const ext = path.extname(entry.name);
        stats.extensions[ext] = (stats.extensions[ext] || 0) + 1;
      }
    }
  }
  
  scan(dirPath);
  return stats;
}

const result = analyzeDirectory('./src');
console.log(JSON.stringify(result, null, 2));
```

### Example 3: System Check
```bash exec="true" security="low" timeout="2000"
#!/bin/bash

echo "System Information:"
echo "==================="
echo "Date: $(date)"
echo "User: $(whoami)"
echo "Directory: $(pwd)"
echo "Files in current directory: $(ls -1 | wc -l)"

echo ""
echo "Environment Variables:"
echo "====================="
env | grep -E "(PATH|HOME|USER)" | sort
```