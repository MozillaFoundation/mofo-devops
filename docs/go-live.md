# Mozilla Foundation Go-Live Checklist

Make use of this checklist when evaluating a new website or feature for secure practices. Note that all items may not apply to the code being deployed.

- [ ] Conduct an RRA
- [ ] Perform  a Security Review
  - [ ] Does user generated content get displayed in-browser safely?
  - [ ] Does user generated content get stored in any way - is it done safely?
  - [ ] Is PII handled according to Mozilla's Privacy Policy?
  - [ ] If password information is stored, is it done using best practices? (bcrypt/scrypt + salt)
  - [ ] Does the site implement recommended security headers for HTTP requests? (HSTS, XFO, CSP, XCTO, etc)
  - [ ] Do POST/PUT/DELETE requests implement some form of Cross Site Request Forgery protection?
  - [ ] Does it have dependencies with known security vulnerabilities? (nsp, OWASP dependency-check)
- [ ] Does the system/site have adequate automated testing?
- [ ] Is there a contributors.json file present in the source repository, does it provide contact information in the event of an emergency?
- [ ] If automatically deployed, who can trigger deploys? Should deployment permission be limited? (branch/merge protection)
- [ ] Data Storage
  - [ ] Automatic Backups
  - [ ] Not publicly accessible AND/OR Strong Access credentials
- [ ] [node] Is it using an up-to-date LTS version of node?  
- [ ] Logs & Monitoring
  - [ ] Does this app require uptime monitoring? (pingdom)
  - [ ] Does this app need to be hooked into logentries
  - [ ] Does this app require log analysis (for alerting devs of runtime errors)