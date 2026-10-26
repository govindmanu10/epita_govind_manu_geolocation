EPITA Engineering Tools — Session 2 Lab Report
Name:Govind Manu (`govind.manu`)
Assigned Group: Group 6
Domain & Provider: Geolocation & IP Ops

Environment & `uv` Mechanics
Virtual Environment Isolation: `uv run` dynamically configures and runs commands inside the isolated virtual environment context without needing manual activation (`source .venv/bin/activate`). `sys.executable` targets the local `.venv` binary and `sys.prefix` differs from `sys.base_prefix`, confirming full environment encapsulation.
Git Hygiene: Configured `.gitignore` to omit `.venv/`, `.env`, `dist/`, and `__pycache__/`

Live API Connection & 12-Factor Hygiene
Secret Security: Storing tokens in environment variables (`.env`) instead of hardcoding them into configuration files (`config.json`) prevents credential leaks in source control and separates configuration from code logic
Endpoint Integrated:`GET https://ipinfo.io/json` with Bearer token authentication.

Dependency Hygiene & SemVer
Dependency Locking:`uv.lock` uses cryptographic SHA-256 hashes to guarantee reproducible builds and guard against supply-chain tampering.
SemVer Constraints:`pyproject.toml` handles version declarations while `uv.lock` ensures exact version pinning.

Package Deployment
CLI Entrypoint: `epita-govind-manu-cli = "epita_govind_manu_geolocation.cli:main"`
Distribution Formats: Wheels (`.whl`) are pre-compiled and faster/safer to install compared to Source Distributions (`.tar.gz`) which require local compilation.

Part 5: Professional Debugging Challenge
Diagnosis: `record["volume"]` and `record["weight"]` were parsed as string data types directly from the CSV split operation, causing a `TypeError` during multiplication.
The Fix: Explicitly cast values to `float` inside `parse_api_record()`.
Validated Output:`Aggregate Result: {'successful_entries': 3, 'total_volume': 650.0, 'avg_volume': 216.66666666666666, 'high_impact_count': 1}`