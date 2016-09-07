## Monitoring for certificate expiration

A simple mechanism has been put in place to give us daily checks on the expiration time of our certificates. Here's how to add a new check for a host:

1. Using the credentials in the vault log into the [healthchecks account](https://healthchecks.io)
2. Create a new check, give it a meaningful name and tags
3. For a 30 day check, set the check period to two days and the grace period to twelve hours. For a 3 day check, set the period to one day and the grace period to 6 hours
4. Go to the integrations page, and turn off notifications on Pagerduty if the check is for 30 days.
5. Make note of the unique healthcheck endpoint that is generated.
6. Go to [the Heroku app](https://dashboard.heroku.com/apps/mofo-cron) (Ask Chris for access if required)
7. Open up the Heroku Scheduler Add-on and create a new daily task.
8. Fill in the variables in this command, given the nature of the check you set up: `test $(node_modules/.bin/ssl-date-checker changecopyright.org -f json | jq '.expires') -gt $30_OR_3 && curl -fsS --retry 3 $HEALTHCHECK_ENDPOINT`
