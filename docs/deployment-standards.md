# Deployment Standards

## Who

Anyone with permissions to merge code in one of our repos can deploy to staging and production. Master is automatically deployed to staging, but production requires doing a manual `promote to prod`.

## When

You should never be afraid of deploying: things break and that's okay! If you never did a rollback and think you will need assistance to do it, avoid deploying when less people are around (end of a work day or after-hours, Fridays, or weekends)... Unless circumstances require it. For example, to fix a crash bug after-hours.

## Failed Deployments and Rollbacks

If Heroku fails to build the app, it will not deploy it. However, if a runtime error is encountered and the app can't start up, a [rollback](https://devcenter.heroku.com/articles/releases#rollback) should be performed.

For static apps deployed on AWS S3 that break, revert the bad commit and re-deploy.

## Notifications

Deployment notifications can be found for most apps in the #mofo-devops channel on the Mozilla Slack workspace
