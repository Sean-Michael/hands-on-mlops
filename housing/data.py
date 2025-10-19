'''
FILE: data.py
AUTHOR: Sean-Michael Riesterer
DATE: 10-18-2025
VERSION: 0.0.1
DESCRIPTION: Utility for gathering and preparing housing data for model training.
'''

import sys
import argparse
import pandas as pd
import numpy as np
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
    if VERBOSE: print(f"{Colors.CYAN}[log]: {msg}{Colors.RESET}")

def warn(msg):
    print(f"{Colors.YELLOW}[WARN]: {msg}{Colors.RESET}")

def err(msg):
    print(f"{Colors.RED}[ERROR]: {msg}{Colors.RESET}")

def ok(msg):
    print(f"{Colors.GREEN}[SUCCESS]: {msg}{Colors.RESET}")

def parse_args():
    global VERBOSE
    global DATA_PATH

    parser = argparse.ArgumentParser(
        description='Utility for gathering and preparing housing data for model training.'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging output'
    )

    args = parser.parse_args()

    if args.verbose:
        VERBOSE = True
        log("Using verbose output, log messages enabled.")
    return args

    ''' 
    TODO: 
    parser.add_argument(
        '-f', '--file',
        type=str,
        default=DATA_PATH,
        metavar='PATH',
        help=f"Path to housing data file (default: {DATA_PATH})"
    )
    DATA_PATH = args.file
    path = Path(DATA_PATH)

    if path.is_file():
        ok(f"Using data file: {DATA_PATH}")
    else:
        err(f"Path {DATA_PATH} not found, creating...")
        Path("datasets").mkdir(parents=True, exist_ok=True)
    '''


'''
Data Processing Steps:
-[x] Extract Data from source as PD Dataframe
-[ ] Split training/test data
-[ ] Normalize?
'''

def load_housing_data(tb_path):
    tarball_path = Path(tb_path)
    if not tarball_path.is_file():
        log(f"Path {tarball_path} not found, creating...")
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

def shuffle_and_split_data(data, test_ratio, rng):
    shuffled_indices = rng.permutation(len(data))
    test_set_size = int(test_ratio * len(data))
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == "__main__":
    parse_args()
    housing_full = load_housing_data(DATA_PATH)
    #log(f'housing_full={housing_full}')
    rng = np.random.default_rng(seed=42)
    train_set, test_set = shuffle_and_split_data(housing_full, 0.2, rng)
    log(f'len(train_set)={len(train_set)}')
    log(f'len(test_set)={len(test_set)}')