#!/bin/bash

# Execute the verifier and generate the mandated platform CTRF report output.
pytest /task/tests/test_outputs.py -rA --json-ctrf=/logs/verifier/ctrf.json

# Record the status outcomes accurately to the system log pathway.
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
