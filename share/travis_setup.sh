#!/bin/bash
set -evx

mkdir ~/.dashcore

# safety check
if [ ! -f ~/.argocore/.argo.conf ]; then
  cp share/argo.conf.example ~/.argocore/argo.conf
fi
