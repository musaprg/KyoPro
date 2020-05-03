#!/bin/bash

set -eu

python main.py < sample.txt > out.txt
diff out.txt answer.txt
