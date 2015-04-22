#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
#set -o xtrace

aws iam upload-server-certificate \
  --path "/cloudfront/" \
  --server-certificate-name "webmaker.org-2015-04-21" \
  --certificate-body "file://webmaker_org.crt" \
  --private-key "file://webmaker_org.key" \
  --certificate-chain "file://DigiCertCA.crt"
