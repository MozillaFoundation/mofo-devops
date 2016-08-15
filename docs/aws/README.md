# Amazon Web Services
This folder contains documentation for how we use different AWS services as part of usual workflows in deploying or configuring applications/websites.

## Learn How To
- [Deploy an application with S3 and CloudFront](https://github.com/MozillaFoundation/mofo-devops/blob/master/docs/aws/deploy-s3.md)
- [Deploy an application with Heroku and CloudFront](https://github.com/MozillaFoundation/mofo-devops/blob/master/docs/aws/deploy-heroku.md)


## Where do AWS resources go?

In general, put create new resources in the mofo-projects account. The exception to this rule is if the new resource needs to be in the legacy account (mofo-everything) to access an existing resource in that account (i.e. IAM stored certificates in mofo-everything are only available to resources in that account)
