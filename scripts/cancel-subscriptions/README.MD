cancel_subscriptions.py
-----------------------

This script reads in a list of subscription IDs from a CSV file and cancels them using the correct REST APIs. If a sucscription fails to be cancelled for any reason it is output to `{filename}-errors.csv`.

How to run:
-----------
Stripe:
```
source ./venv/bin/activate
pip install -r requirements.txt
python cancel_subscriptions.py --subscription-type stripe --stripe-key {key} --filename {filename}
```

Paypal:
```
source ./venv/bin/activate
pip install -r requirements.txt

# Set Environment Variables for Paypal
export PAYPAL_MODE=sandbox   # sandbox or live
export PAYPAL_CLIENT_ID=your-client-id
export PAYPAL_CLIENT_SECRET=your-client-secret

python cancel_subscriptions.py --subscription-type paypal --filename {filename}
```