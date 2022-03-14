#!/usr/bin/env bash

pip install --upgrade pip
pip install spacy tqdm spacytextblob vaderSentiment networkx
python -m spacy download en_core_web_sm

cd cds-lang
cd cds-language
git config --global user.name "sarah-hvid"