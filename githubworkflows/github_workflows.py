# -*- coding: utf-8 -*-
"""github/workflows.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W9_YwIZSfgH2rZ5J1egXpz05PV53KacQ
"""

# .github/workflows/tests.py
name: Tests
on: push
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v1
      with:
        python-version: 3.8
        architecture: x64
    - run: make setup
    - run: make check
    - run: bash <(curl -s https://codecov.io/bash)