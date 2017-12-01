# Latest from Network-Pulse Slack Bot

## What?

This bot publishes new Pulse entries on Slack. It runs on Zapier (credentials in 1Password). You can find a running example on Mozilla's "mofo-pulse-latest" Slack channel.

## Zapier's Configuration

This bot needs 3 steps:

### Poll for entries

- Select `Webhooks`,
- Select `Retrieve Poll`,
- Edit options. `URL` is `https://api.mozillapulse.org/api/pulse/entries/?ordering=-id`, `Key` is `results` and `Deduplication Key ` is `id`,

### Run Python

- Select `code`,
- Select `Run Python`
- Edit options. `Input Data` is `related_creators` and `{{27723444__related_creators}}`.

```python
from collections import defaultdict

# check for empty input
if !input_data['related_creators']:
    return [{"Creators": ''}]

# Input_data is a string ("id: 2\n name: Puppy\n") so we need to prepare it.
related_creators = input_data['related_creators'].split('\n')

# Create a default dict: we will have multiple creators so we need to regroup them under the same "name" key.
dd = defaultdict(list)

for x in related_creators:
    # If you have multiple creators, zapier will add an empty line, because why not.
    if x != '':
        k, v = x.split(': ', 1)
        dd[k].append(v)

creators = ', '.join(dd['name'])

# Must return a dict to be used in the slack template.
return [{"Creators": creators}]
```

## Send Channel Message

- Select `Slack`,
- Select `Send Channel Message`,
- Select or connect an account,
- Edit options: `Channel` is `mofo-pulse-latest`, `Message` is `*{{27723444__title}}* > {{27723444__description}} _Published By: {{28765781__Creators}}_ :point_right: {{27723444__content_url}}`, `Attach Image by URL` is `{{27723444__thumbnail}}`. You can customize the rest :)
