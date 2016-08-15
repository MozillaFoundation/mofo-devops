## How to Setup a Heroku App with Cloudfront

Assuming you have created your heroku app and have the link ready e.g. (appname.herokuapp.com)

### Create Cloudfront Distribution

1. Open cloudfront and hit **Create Distribution**
2. In this case we are going to click **Get Started** on create web distribution.
3. Fill in the blank for **Origin Settings section**.  
    3.1 Origin Domain Name: This should be your heroku URL (appname.herokuapp.com)  
    3.2 Origin Path: This should be your base route for example: **appname.herokuapp.com/home** then this should be **/home**  
    3.3 Origin ID: This will be auto generated.  
    3.4 Origin Custom Headers: Use this to pass custom HTTP Headers from CloudFront to your origin server  
4. Fill in the blank for **Default Cache Behavior Settings**.   
    4.1 Viewer Protocol Policy: Redirect HTTP to HTTPS if you need this to be on HTTPS  
    4.2 Allowed HTTP Methods: Leave it **GET, HEAD** unless you need other METHODS.  
    _NOTE: leave other part as default in this section unless you need something custom_  
5. Fill in the blank for **Distribution Settings**  
    5.1 Alternate Domain Names (CNAMEs): This should be your Route53 domain name for example: appname.mofostaging.net  
    5.2 SSL Certificate: You would probably want **Custom SSL Certificate (example.com):**. Select the one that matches your Route53 domain.   
6. The rest can be left as default, and hit **Create Distribution**

### Create Route53

1. Open Hosted zone
2. Click Create Hosted Zone or open an existing domain in the list.
3. Create new record by clicking on **Create Record Set**
4. On the right sidebar fill in these fields:  
    4.1 Name: this will be your subdomain name (appname.mofostaging.net) would be `appname`  
    4.2 Type: **A - IPv4 address** record in the case of Cloudfront distribution  
    4.3 Alias: **Yes**  
    4.4 Alias Target: This will be cloudfront distribution URL (you can obtain this by going to the list in cloudfront tab and click on your distribution and find it under **Domain Name**).
    4.5 Click **Create**
