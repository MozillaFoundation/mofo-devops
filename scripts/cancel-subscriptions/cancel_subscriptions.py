import sys
import argparse
from csv import DictReader, DictWriter
import stripe
from paypalrestsdk import (
    BillingAgreement,
    ResourceNotFound
)

parser = argparse.ArgumentParser()

parser.add_argument(
    '--subscription-type',
    help='The type of subscriptions being cancelled',
    choices=['stripe', 'paypal'],
    required=True,
    dest='type'
)
parser.add_argument(
    '--csv-filename',
    help='The file where subscriptions are listed',
    required=True,
    dest='filename'
)
parser.add_argument(
    '--stripe-key',
    help='Stripe API key. must be specified if type is "stripe"',
    dest='stripe_key'

)

args = parser.parse_args()

failed_transactions = []

# Cancels all subscriptions specified in the CSV "filename"
def cancel_all_subscriptions(filename):
    print(f'Loading ids from {filename}')
    ids = load_ids(filename)

    # use the selected cancellation strategy
    cancellation_strategy = cancel_stripe_subscription if args.type == 'stripe' else cancel_paypal_billing_agreement

    print(f'Cancelling {len(ids)} subscriptions...')
    for id in ids:
        cancellation_strategy(id)

    if len(failed_transactions) > 0:
        print(f'{len(failed_transactions)} failed to cancel, outputting to {args.type}-errors.csv')
        write_errors(failed_transactions, f'{args.type}-errors.csv')
        exit(1)

    print('Successfully cancelled all subscriptions!')
    exit(0)

# Cancel the given Stripe subscription using its ID
def cancel_stripe_subscription(subscription_id):
    try:
        canceled = stripe.Subscription.delete(subscription_id)

        if not canceled or canceled.status != 'canceled':
            failed_transactions.append(subscription_id)

    except (stripe.error.StripeError, Exception) as e:
        failed_transactions.append(subscription_id)
        print(f'Failed to cancel subscription f{subscription_id}. Error: {e}')

# Cancel the given Paypal Billing Agreement using its ID
def cancel_paypal_billing_agreement(billing_agreement_id):
    try:
        billing_agreement = BillingAgreement.find(billing_agreement_id)
        cancel_note = {'note': 'MZLA migration'}

        if not billing_agreement.cancel(cancel_note):
            failed_transactions.append(billing_agreement_id)
            print(f'Failed to cancel Billing Agreement {billing_agreement_id}. Error: ${billing_agreement.error}')

    except ResourceNotFound as error:
        failed_transactions.append(billing_agreement_id)
        print(f'Failed to find Billing Agreement ${billing_agreement_id}.')

# Open the CSV file and read in all the ids
def load_ids(filename):
    ids = []

    with open(filename, 'r') as csv_file:
        reader = DictReader(csv_file)
        row_name = ''

        if args.type == 'stripe':
            row_name = 'PMT Subscription ID'
        else:
            row_name = 'Reference Txn ID'

        for row in reader:
            ids.append(row[row_name])

    return ids

# output any failed subscription cancellations to errors.csv
def write_errors(ids, filename):
    field_name = 'ids'

    with open(filename, 'w') as csv_file:
        writer = DictWriter(csv_file, fieldnames=[field_name])
        writer.writeheader()

        for id in ids:
            writer.writerow({field_name: id})

if __name__ == '__main__':

    if args.type == 'stripe':
        if not args.stripe_key:
            print('please provide a Stripe API key with --stripe-key')
            exit(1)

        # Configure Stripe, the first script argument is the Stripe API key
        stripe.api_key = args.stripe_key
        stripe.max_network_retries = 3

    # Start cancelling subscriptions using the CSV file specified as the second script parameter
    cancel_all_subscriptions(args.filename)
