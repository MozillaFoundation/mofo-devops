# Setup an Application using Simple Storage Service (S3)
This document explains how to setup an application that does not need a server to be running i.e. is a static application, for e.g. static websites.

## Services Used
- S3
- CloudFront
- Route 53

## Steps

### Setting up the S3 Bucket
1. __Role__: Switch to the appropriate role in which the content for the application needs to exist in.
2. __Create Bucket__: Click on the "Create Bucket" button in S3, give your bucket a name and select "US Standard" as the region.
3. __Upload Content__: Click on "Upload" and drag and drop your files into the bucket.
4. __Setup Hosting__: Next you need to setup hosting for the application. Here's how you do it:
  1. Select the "Properties" tab and expand the "Static Website Hosting" section.
  2. Select "Enable website hosting" and type in your application entry-point (Index Document) and the default error page you would like to show (set it to the same value of the Index Document if you don't have a custom error page).
  3. Click "Save". You should now see an "Endpoint" url that you can access your bucket's contents at. However, this url won't be accessible until you setup permissions for the bucket as described in the next step.
5. __Permissions__: Adequate permissions need to be set on the bucket to enable access to it. The steps for this are:
  1. Expand the "Permissions" section in the "Properties" tab.
  2. Select "Add Bucket Policy" and click on the "AWS Policy Generator" link in the bottom-left corner. This will open a new window/tab with the Policy Generator page.
  3. In the Policy Generator page:
    1. Select the "Policy Type" as "S3 Bucket Policy". 
    2. Set the "Principal" based on who you would like to allow access to the bucket. Set it to "*" (without quotes) to allow access to everyone.
    3. For the "Action", you will need to at least select the "GetObject" permission. If you want to allow uploads to the S3 bucket from anywhere outside AWS, you should also enable the "PutObject" permission. _CAUTION: Do not set the "Principal" as "*" if you are enabling the "PutObject" option. If you need to allow uploading content to the bucket, only allow the "GetObject" action on the bucket, create an IAM user, generate a policy that allows "PutObject" for that user, and use its secret key to upload content._
    4. For the "ARN" set it to your bucket ARN which will look something like `arn:aws:s3:::<bucket_name>/*`
    5. Click on "Add Statement" and then "Generate Policy". A JSON document is created for you. Copy the text from there.
  4. Paste the JSON permission object into the text area back in the "Add Bucket Policy" dialog in the previous page and click "Save".
  5. Verify that you can now access the bucket's content by using the url seen in the "Static Website Hosting" section.
6. Your S3 bucket should now be setup correctly.

### Setting up a CloudFront distribution
Once you have your S3 bucket set up, you need to add a CloudFront CDN to serve the bucket's content effectively. The steps for doing so are as follows:

1. __Role__: Before proceeding, make sure you switch to the appropriate role so that the CloudFront distribution being created is in the same account which contains the SSL certificate you would like to use.
2. __Create distribution__: Select "Create Distribution" from the CloudFront page and then select "Get Started" under the "Web" section as the delivery method.
3. __Configuration__: Fill out the fields as follows:
  1. The "Origin Domain Name" will be the publicly accessible url for the S3 bucket created above.
  2. If the "Origin Protocol Policy" exists, set it to "HTTP Only".
  3. Set the "Viewer Protocol Policy" to "Redirect HTTP to HTTPS" so that SSL is always used.
  4. If you are setting up a custom domain for the application, add it to the "Alternate Domain Names" text field.
  5. For the basic configuration, the rest of the fields can be left as their default values. Otherwise, you will need to customize some of the other fields (for example, if you do some kind of query string parsing in your application, you might want to enable the "Forward Query Strings" option).
4. __Verification__: Select "Create distribution" to finish the process. The process of creating the distribution can take up to 20 minutes. Once it is completed, verify that you can access contents through CloudFront by accessing the domain name as seen in the "General" tab when you click on your distribution from the list.

### Setting up a custom domain using Route 53
This step is only needed if you need to set a custom domain to access the contents of you website instead of using the CloudFront distribution's url. The assumption here is that the domain name is already in possession by Mozilla.

1. __Navigate__: Head to Route 53 and select "Hosted Zones" from the sidebar.
2. __Create domain__: If your domain does not exist in the list, select "Create Hosted Zone", type in your domain name and click "Create". If your domain already exists in the list, click on it and skip to step 4.
3. __Setup Name Servers__: Click on your domain and then select "Create Record Set". Leave the "Name" blank and select "Name Server" as the type. Set the name server values in the "Values" field. Click "Create".
4. __Connect CloudFront__: Select "Create Record Set". If your custom domain is actually a subdomain, type that into the "Name" field. Select the type as "Alias", check "Yes" for the "Alias" option and then type in the CloudFront distribution's url into the "Alias Target" field. Click on "Create" to complete the process.
5. __Verification__: You should now be able to access your S3 bucket contents through your custom domain name.
