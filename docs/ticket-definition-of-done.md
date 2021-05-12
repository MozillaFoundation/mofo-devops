# Definition of done for Github/Zenhub issues & tickets

Make use of this checklist when creating/working on a ticket and before marking it as "Done".

(Feel free to remove items that are not applicable.)


**Before creating ticket**:

- [ ] Business requirements are verified (make sure the suggested solution will meet stakeholder’s needs)

**Ticket-Creation**:

- [ ] Make sure you have acceptance criteria in the ticket (in a checklist)
- [ ] List of all tasks that need to be completed to meet the acceptance criteria
- [ ] Ticket structured well

**Pre-Merge**:
- [ ] Code follows our code style guide [documentation WIP]
- [ ] Code is documented according to our documentation standards [Need to create]
- [ ] Unit Test Coverage [need to create coverage target and tooling]
- [ ] Integration Test Coverage [need to create guide]
- [ ] Any technical debt is documented (todo/fixme => needs an issue linked in comments)
- [ ] Any follow-up tasks are created before a PR is merged
- [ ] Code peer-reviewed by at least one other developer

**If the work had design-dev handoff, also signed off by a designer**:
- [ ] Code has error handling with clear error messages
- [ ] Incomplete features are hidden behind feature flags (for features without Update or Delete DB migrations)
- [ ] Secrets (github actions + heroku) are up to date for CI, review apps, and staging

**Post-Merge, Pre-Production Deploy**:
- [ ] Code is deployed to Staging
- [ ] Code is manually verified to work on staging (rare, but important)
- [ ] Test management commands that may need to be run
- [ ] Release scripts are up to date (rare, but important)

**Production Deploy**:
- [ ] Production deploy successful
- [ ] Notify Stakeholders
