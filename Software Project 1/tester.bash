#!/bin/bash

echo "Testing..."
for test_in in Tests/*.inp; do
    test_dir=${test_in%.inp}
    test_exp=$test_dir.exp
    test_out=$test_dir.opt
    time python3 ${1:-MP1_ANCHETA.py} < $test_in | tail -n +2 > $test_out
    if diff $test_out $test_exp; then
        echo "Test ${test_dir##*/} Accepted"
    fi
done