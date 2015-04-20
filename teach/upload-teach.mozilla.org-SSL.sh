#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
#set -o xtrace

aws iam upload-server-certificate \
  --path "/cloudfront/" \
  --server-certificate-name "teach.mozilla.org-2015-04-19" \
  --certificate-body "file://teach_mozilla_org.crt" \
  --private-key "file://teach_mozilla_org.key" \
  --certificate-chain "file://DigiCertCA.crt"
