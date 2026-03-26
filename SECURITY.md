# Security

## Baseline controls
- Do not commit secrets (`.env`, tokens, private keys).
- Keep machine credentials outside version control.
- Treat build/release credentials as high-impact assets.

## Threat model highlights
- If a publishing token is compromised, an attacker could publish misleading artifacts.
- Replay verification and commit provenance reduce risk, but do not replace secret hygiene.

## Hardening requirements
- Enforce branch protections and least-privilege tokens.
- Rotate credentials regularly.
- Prefer signed commits/tags for release artifacts.
- Audit workflows that can publish or mutate public outputs.

## Incident response
1. Revoke compromised token/credential immediately.
2. Freeze automation that can publish artifacts.
3. Publish incident note with affected commit/time range.
4. Re-run deterministic pipeline from trusted commits and republish receipts.
