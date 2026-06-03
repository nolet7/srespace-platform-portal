# Security and Access

## Access Model

The local portal uses GitHub OAuth for user authentication. In an enterprise deployment, this pattern can be extended to OIDC providers such as Authentik, Okta, Azure AD, or Google Workspace.

## Identity Controls

| Control | Purpose |
|---|---|
| OAuth login | User authentication |
| Backstage user entity | Identity mapping |
| Group entity | Ownership and authorization grouping |
| Repository ownership | Source control accountability |
| Token scoping | Reduce blast radius |

## Secret Handling

Secrets must not be committed to Git.

Ignored local files include:

    .env
    .env.*
    .venv-techdocs/
    .techdocs/
    node_modules/

## GitHub Token Guidance

Use the minimum permissions required for catalog discovery and repository reads. Rotate tokens immediately if exposed.

## Production Recommendations

- Use enterprise OIDC instead of local-only GitHub OAuth
- Store secrets in Vault or a cloud secrets manager
- Enforce branch protection
- Require pull request review
- Enable secret scanning
- Use signed commits where possible
- Apply least privilege to tokens
- Separate production and development configs
