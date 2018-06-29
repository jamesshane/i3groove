#!/bin/env python3

#   Author  :   James Shane

import sys
import argparse
import yaml
import os.path
sys.path.append("..")
import load_json as lj
import config as conf
import install
import replace_theme as rt

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='create-theme by James Shane')
    parser.add_argument('-c','--config', type=str, required=True, help='Load config file')
    parser.add_argument('-t','--theme', type=str, required=True, help='Theme name')
    args = parser.parse_args()

    configuration = {}
    configuration = conf.read_config( args.config)
    print (configuration['json-template'])
    install.install_file_noconfig(configuration['json-template'],args.theme+".json")
    #print (args.config)
    #print (args.theme)

    jfile = lj.load_json(args.theme+".jpg.json")
    back=jfile['pal']['1']
    #print (back)
    fore=jfile['pal']['2']
    #print (fore)

    #jfile = lj.load_json(args.theme+".json")
    rt.replace_theme(args.theme+".json",back,fore)

    exit(0)
