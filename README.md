# mofo-devops
Mozilla Foundation DevOps Plans, Issues, Discussions

[![](https://raw.githubusercontent.com/ZenHubIO/support/master/zenhub-badge.png)](https://zenhub.com)

## On-Call Emergencies:

### Reporting an emergency ---- [USE THIS EMAIL TEMPLATE WHEN REPORTING AN EMERGENCY](docs/emergency-template.md)

From a `mozilla.com` or `mozillafoundation.org` email address, send a detailed description of the error to [emergency@mozillafoundation.org](mailto:emergency@mozillafoundation.org) to alert the on-call engineer. **The on-call engineer will respond to issues 24/7 so don't feel bad about reporting issues after hours!**

#### donate.mozilla.org

We have a separate schedule for the on-call rotation of donate.mozilla.org, to route email emergencies directly to the on-call engineer for the donation site, add `[DONATE]` to the subject of your email.

Things to note:

1. Do not email this address unless there is immediate action that needs to be taken by the on-call engineer. This email is not for simply making them aware of an issue they're not responsible for fixing.
2. This email address is **not** meant to be cc'd on email threads, as it will generate a new incident report for every response to the thread. **Please only email it once per incident, that's all that is required**

### Incident response plan

Our Incident response plan for Stripe, Paypal and 1Password can be accessed by employees [at this link](https://docs.google.com/a/mozilla.com/document/d/1AVSqG1WfQNTyvyOQAXwrHjT6JQwRjk0AFnJzUbS7Hxg/edit?usp=sharing)

### Current status of all the things:

http://status.mozillafoundation.org/

### How to find the thing that's alerting:

Most of our applications now reside on Heroku. Some have not been moved over or make sense to keep on EC2. To find the home of an application that's triggering an error, the DNS can often give you clues:

```
dig thimble.webmaker.org

; <<>> DiG 9.8.3-P1 <<>> thimble.webmaker.org

[...]

;; ANSWER SECTION:
thimble.webmaker.org.	296	IN	CNAME	hokkaido-6558.herokussl.com.
[...]
```

You'll see in the above example, thimble is hosted on Heroku. For blog.webmaker.org, you'll see it's a direct IP address, which means it lives in EC2:

```
dig blog.webmaker.org

; <<>> DiG 9.8.3-P1 <<>> blog.webmaker.org
[...]
;; ANSWER SECTION:
blog.webmaker.org.	56	IN	A	23.23.168.90
[...]
```

There are five separate accounts in AWS. You can find the details of these accounts in our 1Password team vault.

### Tech Stack

[Read about the technologies we develop with here on the Foundation engineering team](docs/technology.md)

### Go-live Checklist

[Use the Go-live checklist](docs/go-live.md) when evaluating a new website or new functionality for secure practices.

### Creating new Third-party Service Accounts

Here are the steps for registering a new service:

1. Get approval from Simon
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

### Database Migrations

[Follow the migration checklist](docs/migrations.md)

### VictorOps

Installing the VictorOps app is highly recommended. You can see details of when you're next on-call, what your methods of contact are and set your phone to alert even when the device has notifications muted.

### Zenhub

[See the docs](docs/zenhub.md)

