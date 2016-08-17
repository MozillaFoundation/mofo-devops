## How to purchase a new domain

Don't publicly share domain names before we purchase them, the last thing we need is a domain squatter snatching it up before we can.

### Set up a Hosted Zone in AWS for the new domain

1. Open the AWS console, log in, and assume the role for working in the mofo-projects account
2. Open Route 53 and select "Hosted Zones" in the left hand menu area to bring up the list of existing zones.
3. Click the "Create Hosted Zone" button on the top left, just above the table of Hosted Zones.
4.  Fill in the form
    1. **Domain Name** - enter the domain name of the new zones
    2. **Comment** - optionally enter in a comment or description for the new Zone
    3. **Type** - 99.99% of the time we'll be using "Public Hosted Zone"
5. Copy the values in the NS record set of the new Hosted Zone record

### Purchase the Domain

1. [File an IT request](https://bugzilla.mozilla.org/enter_bug.cgi?product=mozilla.org&format=itrequest) (requires a valid session using a mozilla employee account)
    1. Select the urgency, based on the situation. No rush, or within the next week are the best options in most cases.
    2. Select "Report a problem with a Mozilla website, or to request a change or push"
    3. Enter a bug summary - i.e. "Purchase furrykittens.net"
    4. Describe the reason for the domain purchase, provide a relevant link if possible.
    5. Provide the NS record set values that were created in the new Hosted Zone you set up.
    6. Submit and reward yourself with an ice cold beverage of your choice.