### SSL Certificate Management

This guide contains information about generating keys and Certificate Signing Requests (CSRs), submitting them to Digicert, approving them, and deploying them to AWS or Heroku.

### Obtaining a new certificate

1. Grab [the helper script](https://github.com/MozillaFoundation/mofo-devops/blob/master/scripts/generate-ssl-cert) from this repo.
2. run `./generate-ssl-cert fuzzykittens.org`.
3. grab the CSR: `cat fuzzykittens.org/fuzzy_kittens_org.csr`.
4. Log into Digicert, and go the the "Request Cert" page.
5. Select "SSL Certificate" as product type, if not already selected.
6. Paste the CSR into the text area provided.
7. The Common Name should automatically populate. Make sure it's correct.
8. If you need other hostnames for the cert, such as "www.fuzzykittens.org" enter it under the "Other Hostnames (SANs)" section.
9. Select Mozilla Foundation as the Organization.
10. Only select Extended Validation if required. If you don't know, Ask Chris or Simon.
11. Select Apache as the Server Platform.
12. Select 1 Year for Validity period.
13. Select auto-renew, it's helpful
14. Under "Order Access", find Chris De Cairos and check the box.
15. Don't worry about the input area for additional emails about renewals.
16. Add in any relevant comments (links, explainations etc.) to the "Comments to Administrator" field 
17. Agree to the TOS presented at the bottom of the form. Or don't. depends how badly you need that cert!
18. Submit the Certificate Request.
19. Chris, and possibly you (TBD), will receive an email asking to confirm the request. It should contain a link to the request on the Digicert website, where you should select the approval button.
20. The signed certificate for the domain will be emailed to you! extract the contents of the attachment to the same directory we created the key and CSR in.

### Install the certificate

#### On AWS

1. Ensure you've configured the [AWS cli](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)for your machine
2. Install & configure the [assume-aws-role](https://www.npmjs.com/package/assume-aws-role) helper
3. Grab the [helper script](https://github.com/MozillaFoundation/mofo-devops/blob/master/scripts/iam-upload-cert)
4. Navigate to the directory where your certificate and secret is.
5. Assume the role of the account you need the certificate to reside in. `assume-aws-role mofo-projects 123456`
6. Execute the helper script & follow the instructions: `/path/to/helper/iam-upload-cert`
7. It will give you the Certificate ID that you can use to configure resources in the account that need it (i.e. load balancers or Cloudfront Distributions)

#### On Heroku

1. Enable the SNI beta! `heroku labs:enable http-sni -a fuzzy-kittens`
2. Add the cert: `heroku _certs:add /path/to/cert/fuzzy_kittens.crt /path/to/cert/fuzzy_kittens.key --type sni`
3. Select the domain to configure with a heroku SSL domain (see on screen display from the Heroku CLI)
4. Grab the Heroku SSL domain (should look like `www.fuzzykittens.org.herokudns.com`)
5. Update the Hosted Zone in AWS for that domain with a CNAME record that resolves to that Heroku domain.
