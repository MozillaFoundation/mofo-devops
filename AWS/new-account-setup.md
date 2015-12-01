# AWS New Account Setup

## Creating the account

Before you create a new AWS account, make sure you have access to devops@mozillafoundation.org email address.

* Head to the [sign-up page](https://)
* Fill in the information as follows:
  * **Full Name** - C/O Jon Buckley
  * **Company Name** - Mozilla Foundation
  * **Country** - US
  * **Address** - 331 E. Evelyn Ave
  * **City** - Mountain View
  * **State** - CA
  * **Postal Code** - 94041
  * **Phone Number** - +1 416 400 5662 (must be your phone number for account verification step)

* Fill in your credit card details
* Select the correct AWS Support tier, probably Business

## Setting Billing Defaults

* Sign-in to the console with your root account
* Click your AWS account name on the top-left corner then "Billing and Cost Management"
* Click "Cost Explorer" then "Enable" button
* If this is a parent account:
  * Click "Consolidated Billing" then "Enable" button
* If this is a child account:
  * Send a "Consolidated Billing" request from the parent account to this account
  * Accept the "Consolidated Billing" request
  * Remove the saved credit card from Payment Methods
* Click "Account Settings" then:
  * Update the **Phone Number** to +1 650 903 0800 (MV office)
  * Designate alternate contacts for:
    * Billing
      * **Full Name** - Alexei Skrynnikov
      * **Title** - Accountant
      * **Email Address** - alexei@mozillafoundation.org
      * **Phone Number** - +1 647 991 1579
    * Operations
      * **Full Name** - Jon Buckley
      * **Title** - Developer/Operations
      * **Email Address** - jon@mozillafoundation.org
      * **Phone Number** - +1 416 400 5662
    * Security
      * **Full Name** - Jon Buckley
      * **Title** - Developer/Operations
      * **Email Address** - jon@mozillafoundation.org
      * **Phone Number** - +1 416 400 5662
  * Enable IAM User Access to Billing Information
* If this is a parent account:
  * Click "Preferences" then:
    * Turn on "Receive PDF Invoice By Email"
    * Turn on "Receive Billing Alerts"

## Setting IAM Defaults

* Visit the IAM Console
* Click "Dashboard" then:
  * Click "Customize" to set the Console sign-in link to something memorable
  * Change the password policy to require a 50 character password minimum (to encourage people to use pass phrases instead)
  * Add the mofo-ops-Administrator role via Cloudformation
  * Click "Activate MFA on your root account" and follow the steps to enable MFA
  * Create a group called "Administrators", and grant that account the AdministratorAccess managed policy
  * Create a user account for yourself, and add it to the "Administrators" group
* Sign out of your root AWS account, hide the MFA device, and never use it again unless you absolutely have to

## Setting up your Administrator user account

* Sign-in to your new Administrator user account
* Go to IAM and enable MFA on your user account
