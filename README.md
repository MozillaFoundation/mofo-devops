# mofo-devops
Mozilla Foundation DevOps Plans, Issues, Discussions

## On-Call Emergencies:

### On-Call at MoFo

If one of our service goes down, an alert will be sent to the on-call engineer using VictorOps.

**Keep in mind that on-call is provided as best-effort.**

#### Manually reporting an emergency

The fastest way to alert the on-call engineer is to post a message in the `mofo-devops` channel following this template:

`@here [SERVICE or WEBISTE] is having [DESCRIPTION OF THE ISSUE] since [TIME]`. Feel free to add screenshots or anything that you find relevant to the problem.

### Incident response plan

Our Incident response plan for Stripe, Paypal and 1Password can be accessed by employees [at this link](https://docs.google.com/a/mozilla.com/document/d/1AVSqG1WfQNTyvyOQAXwrHjT6JQwRjk0AFnJzUbS7Hxg/edit?usp=sharing)

### Current status of all the things:

http://status.mozillafoundation.org/

### Tech Stack

[Read about the technologies we develop with here on the Foundation engineering team](docs/technology.md)

### Go-live Checklist

[Use the Go-live checklist](docs/go-live.md) when evaluating a new website or new functionality for secure practices.

### Creating new Third-party Service Accounts

Here are the steps for registering a new service:

1. Get approval from Anil
2. If it stores *any* user data, launch a vendor security review
3. Create the master *and* billing account to use our devops email address.
4. Enter the credentials in our Team Vault (see below)
5. If we pay for the service, to ensure that accounting gets the billing receipts, make sure they show up in gmail with any of the following filters:
  * `"billing"`
  * `"invoice"`
  * `"has:attachment"`
  * `"statement"`
  * `"receipt"`

### Deployment

[Read about deployment standards and practices that we follow](docs/deployment-standards.md)

### The Team Vault

If you forget, the 1password team vault is "mofos".
