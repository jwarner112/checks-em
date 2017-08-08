#! /bin/bash

if [[ "$EUID" != "0" ]]; then
    echo "This script requires superuser privilege. Please re-run as superuser."
    exit;
fi

echo "========================================"
echo "Installing..."
pip install --upgrade .

echo "Verifying..."
echo "Hello, world" > test.txt
openssl dgst -md5 test.txt > test.txt.md5
checksem md5 test.txt test.txt.md5
rm test.txt test.txt.md5

echo "If above reads 'MISMATCH!' instead of 'OK!', an error has occurred."
echo "========================================"
