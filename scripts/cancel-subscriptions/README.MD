cancel_subscriptions.py
-----------------------

This script reads in a list of subscription IDs from a CSV file and cancels them. If a sucscription failes to be cancelled for any reason it is output to `{filename}-errors.csv`.

How to run:
-----------
`python cancel_subscriptions.py {STRIPE_API_KEY} {CSV_FILENAME}`
