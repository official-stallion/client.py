#!/bin/sh

echo "Rolling in ..."

python3 setup.py sdist

twine upload dist/*
