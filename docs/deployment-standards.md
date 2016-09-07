# Deployment Standards

## Who

As detailed in the [Mofo Standards documentation about Github Flow](https://github.com/MozillaFoundation/mofo-standards#github-flow), anyone with permissions to merge code in one of our repos can deploy to staging. For production deployments, you'll need to ask someone on the DevOps team (Chris, Ali, or Gideon) to deploy or ask them to grant you permissions to deploy.

## When

Deployment should never happen:

1. At the end of a work day or after-hours
2. On a Friday
3. On a weekend

... Unless circumstances require it. For example, to fix a crash bug after-hours.

## Failed Deployments and Rollbacks

If Heroku fails to build the app, it will not deploy it. However, if a runtime error is encountered and the app can't start up, a [rollback](https://devcenter.heroku.com/articles/releases#rollback) should be performed.

For static apps deployed on AWS S3 that break, revert the bad commit and re-deploy.

## Notifications

Deployment notifications can be found for most apps in the 'Github Feed' Mattermost channel on https://chat.mozillafoundation.org/mozilla 

If you'd like deployment notifications for an application to be added to that channel, or another channel, contact 'cade' on Mattermost with your request.
