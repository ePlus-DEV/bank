# BankHub roadmap — Personal first, SaaS ready

## Product principles
1. Copy-first: account number and recipient name immediately visible on mobile.
2. Public-only information: no credentials, OTPs or banking secrets.
3. Static-first: GitHub Pages for the initial personal profile.
4. Provider-neutral: VietQR is an optional QR adapter, not a payment processor.
5. Progressive enhancement: the page must remain readable when QR provider fails.

## Phase 1 — Personal MVP
- [x] Responsive profile and copy buttons
- [x] Category filter and search
- [x] Light/dark preference
- [x] VietQR display for enabled accounts
- [ ] Extract styles, JS and data into separate files
- [ ] Validate account data and add unit/browser tests
- [ ] Accessibility and performance audit
- [ ] Configure Pages and optional bank.eplus.dev DNS

## Phase 2 — Personal Pro
- [ ] Profile avatar, description and theme tokens
- [ ] Shareable per-account URLs and metadata
- [ ] Amount and transfer message QR generator
- [ ] Download QR, social preview, print layout
- [ ] Configuration schema and import/export

## Phase 3 — Multi-user SaaS
- [ ] Separate public profile app and authenticated dashboard
- [ ] Auth, roles, sessions, rate limits, anti-abuse
- [ ] Database schema: users, profiles, receiving_accounts, themes, audit_logs
- [ ] API adapter to replace static JSON without rewriting UI
- [ ] Per-user slug routes, ownership validation and moderation
- [ ] Privacy policy, retention, deletion and backups

## Phase 4 — Platform
- [ ] Custom domains and domain verification
- [ ] Privacy-respecting aggregate analytics
- [ ] Optional paid themes and features
- [ ] Admin operations and incident response

## Suggested static structure
```
index.html
assets/css/main.css
assets/js/app.js
assets/js/accounts.js
assets/js/clipboard.js
assets/js/vietqr.js
data/profile.json
data/accounts.json
docs/ROADMAP.md
tests/
.github/workflows/deploy.yml
README.md
```

## SaaS migration notes
GitHub Pages serves static files; it cannot securely provide login, private account editing, or a database. When multi-user functionality is introduced, add an authenticated backend and DB, keep the public frontend static where practical, and publish only user-approved account fields. Avoid collecting financial credentials. Payment confirmation requires a legitimate provider integration and is out of scope for the static MVP.
