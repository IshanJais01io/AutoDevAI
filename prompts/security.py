def build_security_prompt():

    return """
Perform a security review.

Look for:

- Hardcoded secrets
- Unsafe APIs
- Injection risks
- Vulnerabilities
"""