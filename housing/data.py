'''
FILE: data.py
AUTHOR: Sean-Michael Riesterer
DATE: 10-18-2025
VERSION: 0.0.1
DESCRIPTION: Utility for gathering and preparing housing data for model training.
'''

import sys
import pandas as pd
import tarfile
import urllib.request
from pathlib import Path

VERBOSE = False
DATA_PATH = "datasets/housing.tgz"

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def log(msg):
    if VERBOSE: print(f"{Colors.CYAN}[info]: {msg}{Colors.RESET}")

def warn(msg):
    print(f"{Colors.YELLOW}[WARN]: {msg}{Colors.RESET}")

def err(msg):
    print(f"{Colors.RED}[ERROR]: {msg}{Colors.RESET}")

def ok(msg):
    print(f"{Colors.GREEN}[SUCCESS]: {msg}{Colors.RESET}")


'''
Data Processing Steps:
-[ ] Extract Data from source
-[ ] Split training/test data
-[ ] Normalize?
'''

def load_housing_data(tarball_path):
    if not tarball_path.is_file():
        print(f"Path {tarball_path} not found, creating...")
        Path("datasets").mkdir(parents=True, exist_ok=True)

def parse_args(args):
    global VERBOSE
    global DATA_PATH
    if len(args) > 1:
        log(f"parse_args.args={args}")
        if any(flag in args for flag in ['-v', '--v', '--verbose']):
            VERBOSE = True
            log("Using verbose output, log messages enabled.")
    else:
        warn(f"No data path provided, using default {DATA_PATH}")


if __name__ == "__main__":
    parse_args(sys.argv)
    #load_housing_data(DATA_PATH)