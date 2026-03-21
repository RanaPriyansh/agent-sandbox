# Thielon Agent Sandbox

[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github)](https://github.com/thielon-apps/thielon-agent-sandbox)
[![License](https://img.shields.io/github/license/thielon-apps/thielon-agent-sandbox)](https://github.com/thielon-apps/thielon-agent-sandbox/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/thielon-apps/thielon-agent-sandbox)](https://github.com/thielon-apps/thielon-agent-sandbox/commits/main)

Secure execution environment for untrusted agent code. Run agents in isolation with resource limits, network restrictions, and capability-based security.

## Features

- **WASM Sandbox**: Run agent code in WebAssembly for isolation
- **Container Sandbox**: Docker-based isolation for full-featured agents
- **Resource Limits**: CPU, memory, time, network quotas
- **Capability Security**: Grant/revoke permissions (file, network, API access)
- **Audit Logging**: Complete audit trail of all operations
- **Multi-tenant**: Host multiple untrusted agents safely

## Quick Start

```python
from thielon_sandbox import Sandbox

# Create sandbox with limits
sandbox = Sandbox(
    max_cpu=0.5,  # 50% of a core
    max_memory="256MB",
    allow_network=False,
    allow_filesystem=False
)

# Run agent code
result = sandbox.run(agent_code, input_data={"task": "analyze market"})
print(result.output)
```

## Why

Agents are powerful and potentially dangerous. This sandbox:
- Prevents malicious agents from harming host system
- Enforces fair resource allocation (no DoS)
- Provides audit trail for compliance (EU AI Act)
- Enables multi-tenant agent hosting

## License

MIT
