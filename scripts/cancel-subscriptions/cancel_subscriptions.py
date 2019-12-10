import sys
from csv import DictReader, DictWriter
import stripe

failed_subscriptions = []

# Cancels all subscriptions specified in the CSV "filename"
def cancel_all_subscriptions(filename):
    print(f'Loading subscription ids from {filename}')
    subscription_ids = load_subscription_ids(filename)

    print(f'Cancelling {len(subscription_ids)} subscriptions...')
    for subscription_id in subscription_ids:
        cancel_subscription_by_id(subscription_id)

    if len(failed_subscriptions) > 0:
        print(f'{len(failed_subscriptions)} failed to cancel, outputting to {filename}-errors.csv')
        write_errors(failed_subscriptions, f'{filename}-errors.csv')
        exit(1)

    print('Successfully cancelled all subscriptions!')
    exit(0)

# Cancel the given subscription using its ID
def cancel_subscription_by_id(subscription_id):
    try:
        canceled = stripe.Subscription.delete(subscription_id)
    except stripe.error.StripeError as e:
        failed_subscriptions.append(subscription_id)
    except Exception as e:
        failed_subscriptions.append(subscription_id)

    if not canceled or canceled.status != 'canceled':
        failed_subscriptions.append(subscription_id)

# Open the CSV file and read in all the subscription IDs
def load_subscription_ids(filename):
    with open(filename, 'rb') as csv_file:
        reader = DictReader(csv_file)
        subscription_ids = []

        for row in reader:
            subscription_ids.append(row['subscription_id']

        return subscription_ids

# output any failed subscription cancellations to errors.csv
def write_errors(subscription_ids, filename):
    field_name = 'subscription_id'

    with open(filename, 'w') as csv_file:
        writer = DictWriter(csv_file, fieldname=[field_name])
        writer.writeheader()

        for subscription_id in subscription_ids:
            writer.writerow({field_name: subscription_id})

if __name__ == '__main__':
    if not sys.argv[1] or not sys.argv[2]:
        print('You must provide a path to a CSV file containing subscription IDs')
        exit(1)

    # Configure Stripe, the first script argument is the Stripe API key
    stripe.api_key = sys.argv[1]
    stripe.max_network_retries = 3

    # Start cancelling subscriptions using the CSV file specified as the second script parameter
    cancel_all_subscriptions(sys.argv[2])
