#!bin/bash

PYTHON=$(which python)

if [ -z "$PYTHON" ]; then
	PYTHON=$(which python3)
fi

if [ -z "$PYTHON" ]; then
	echo "You don't have Python installed!"
	exit 1
fi

sudo $PYTHON -B launch.py