#!/bin/sh

echo "Rolling in ..."

python3 -m build

twine upload dist/*
