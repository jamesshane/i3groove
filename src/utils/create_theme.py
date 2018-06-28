#!/bin/env python3

#   Author  :   James Shane

import sys
import argparse
sys.path.append("..")
import load_json as lj

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='create-theme by James Shane')
    parser.add_argument('-c','--config', type=str, required=True, help='Load config file')
    parser.add_argument('-t','--theme', type=str, required=True, help='Theme name')
    args = parser.parse_args()

    jfile = lj.load_json("amy1.jpg.json")
    back=jfile['pal']['1']
    print (back)
    fore=jfile['pal']['2']
    print (fore)
    exit(0)
