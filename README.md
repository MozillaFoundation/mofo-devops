# mofo-devops
Mozilla Foundation DevOps Plans, Issues, Discussions

[![](https://raw.githubusercontent.com/ZenHubIO/support/master/zenhub-badge.png)](https://zenhub.com)

## On-Call Emergencies:

### Reporting an emergency

From a `mozilla.com` or `mozillafoundation.org` email address, send a detailed description of the error to [emergency@mozillafoundation.org](mailto:emergency@mozillafoundation.org) to alert the on-call engineer. **The on-call engineer will respond to issues 24/7 so don't feel bad about reporting issues after hours!**

### Current status of all the things:

http://stats.pingdom.com/58vz4fvae745

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

### The Team Vault

If you forget, the 1password team vault is "mofos".

### Pager Duty

Installing the Pager Duty app is highly recommended. You can see details of when you're next on-call, what your methods of contact are and set your phone to alert even when the device has notifications muted. You can do this in settings of pager duty.

### Zenhub

[See the docs](docs/zenhub.md)

