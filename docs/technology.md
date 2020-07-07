When starting a new project, use the technologies listed on this page. In cases where your project might require something not listed here, [file an issue](https://github.com/MozillaFoundation/mofo-devops/issues/new) to begin a discussion on the topic.

Where possible, we develop apps for deployment on Heroku. Static sites will be hosted on S3 and served through CloudFront.

## Platforms/Languages

* Django 2.2 LTS (Python 3.x)
* NodeJS LTS (JavaScript)

## Developers' tooling

Try to use `Docker`, `pip-tools`, and `Invoke` when setting up a new Python codebase: it helps standardise dev environments across projects.

## Preferred Add-ons

* [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
* [Heroku Redis](https://elements.heroku.com/addons/heroku-redis)

In most cases, if it's a Heroku Add-on and your app needs it, we can probably use it, but [file an issue](https://github.com/MozillaFoundation/mofo-devops/issues/new) just to make sure.

There are a few exceptions:
1. Logging - We have a separate account we can use for log aggregation and monitoring with Scalyr. 
2. Pingdom - We have a pingdom account.
3. VictorOps - We use VictorOps to manage on-call alerts for applications. 

If the app requires any of the above three services, [file an issue](https://github.com/MozillaFoundation/mofo-devops/issues/new) to get it set up! 

## Continuous Integration

Our CI of choice is [Travis CI](https://travis-ci.org/).
