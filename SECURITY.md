# Security Policy

Thank you for helping keep OpenCuttle and its users secure.

OpenCuttle is an orchestration layer that may connect:
- local models
- external agent systems
- subprocesses
- HTTP services
- WebSocket services
- MCP/A2A-compatible systems
- recursive sub-buses

Because OpenCuttle sits between systems and may coordinate execution, memory, and routing, responsible security reporting is extremely important.

---

## Supported versions

OpenCuttle is in early development.

At this stage, security support is provided for:
- the latest development branch
- the latest tagged release, once releases begin

As the project matures, this table will be updated.

| Version | Supported |
|---------|-----------|
| main    | Yes       |
| pre-1.0 latest release | Yes |
| older releases | No |

---

## Reporting a vulnerability

If you believe you have found a security vulnerability, please report it **privately**.

### Preferred reporting methods

1. **GitHub private vulnerability reporting**, if enabled for this repository
2. Email the maintainer directly at: `YOUR_SECURITY_EMAIL`
3. If neither is available, open a minimal issue asking for a private contact channel, **without disclosing exploit details publicly**

### Please do not
- open a public GitHub issue with exploit details
- open a public pull request containing a vulnerability demonstration
- publish proof-of-concept details before a fix is available or coordinated disclosure has been agreed

---

## What to include in a report

Please include as much of the following as possible:

- affected version, branch, or commit
- component involved
- vulnerability type
- clear reproduction steps
- expected impact
- any logs, traces, or payloads needed to reproduce
- suggested mitigation, if you have one

Useful examples:
- adapter trust boundary bypass
- unintended file access
- unsafe subprocess behavior
- policy bypass
- memory isolation failure
- credential leakage
- privilege escalation across nodes
- remote execution paths not properly constrained
- trace or log data leaking secrets

---

## Scope

Security issues may include, but are not limited to:

- remote code execution
- arbitrary file access
- sandbox or permission bypass
- credential or token leakage
- unsafe default trust boundaries
- insecure routing or escalation behavior
- memory scope isolation failures
- adapter vulnerabilities
- unsafe deserialization
- denial of service
- injection vulnerabilities
- replay or impersonation vulnerabilities
- insecure defaults in orchestration policies

---

## Response goals

We will try to:
- acknowledge the report promptly
- validate and triage the issue
- communicate next steps
- coordinate a fix and disclosure timeline when appropriate

Response times may vary depending on severity and maintainer availability, especially during early development.

---

## Disclosure policy

We prefer coordinated disclosure.

Our general approach is:
1. receive the report privately
2. validate and assess impact
3. develop and test a fix
4. prepare release notes or advisory text if needed
5. disclose publicly after mitigation is available, when appropriate

---

## Security principles

OpenCuttle is being built with these security goals:

- **local-first by default**
- **explicit trust boundaries**
- **least privilege where possible**
- **clear adapter permissions**
- **memory isolation by scope**
- **observable routing decisions**
- **minimal hidden behavior**
- **secure-by-default configuration over convenience hacks**

---

## User guidance

If you run OpenCuttle, please treat adapters and connected nodes according to their trust level.

Recommended practices:
- do not grant broad file or network access unless necessary
- isolate high-risk adapters
- keep secrets out of logs
- use separate environments for sensitive testing
- prefer local-only policies when evaluating new nodes
- review adapter configuration carefully
- update to supported versions when fixes are released

---

## Hardening areas planned

The following areas are planned or evolving:
- adapter permission model
- better secret handling
- stronger manifest validation
- clearer trust boundaries for external nodes
- signed node manifests
- improved audit and replay controls

---

## Out of scope

Please do not use the public issue tracker for:
- exploit payloads
- leaked credentials
- sensitive environment details
- private infrastructure information
- proof-of-concept attacks against third-party systems

---

## Credits

We appreciate responsible disclosure and will credit reporters when appropriate and desired.
