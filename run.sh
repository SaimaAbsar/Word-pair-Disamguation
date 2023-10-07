#!/bin/sh

input_dir=$1 
output_dir=$2
pip3 install -r requirements.txt 
python3 main.py $input_dir $output_dir
