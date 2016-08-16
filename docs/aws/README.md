# Amazon Web Services
This folder contains documentation for how we use different AWS services as part of usual workflows in deploying or configuring applications/websites.

## Learn How To
- [Deploy an application with S3 and CloudFront](https://github.com/MozillaFoundation/mofo-devops/blob/master/docs/aws/deploy-s3.md)
- [Deploy an application with Heroku and CloudFront](https://github.com/MozillaFoundation/mofo-devops/blob/master/docs/aws/deploy-heroku.md)


## Where do AWS resources go?

In general, put create new resources in the mofo-projects account. The exception to this rule is if the new resource needs to be in the legacy account (mofo-everything) to access an existing resource in that account (i.e. IAM stored certificates in mofo-everything are only available to resources in that account)


## Useful Tools

- [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
    - Interface with your AWS resources using a terminal emulator!
- [aws-shell](https://github.com/awslabs/aws-shell)
    - Interactive shell for working with AWS. Autocomplete commands and resources, inline documentation. What more could you want.
- [Assume AWS Role](https://www.npmjs.com/package/assume-aws-role)
    - A helper script for assuming new AWS Roles for when working with multiple accounts.
- [Logentries](https://logentries.com)
    - Log aggregation service. Lets you view, search and analyze server logs in real time. Use for debugging issues in staging and production.