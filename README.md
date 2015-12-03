# mofo-devops
Mozilla Foundation DevOps Plans, Issues, Discussions

## On-Call Emergencies:

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

### The team vault

If you forget, the 1password team vault is "mofos".
