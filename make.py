#!/usr/bin/env python
# -*- coding: utf-8 -*-
import posixpath
import boto3
import argparse
import getpass
import os
import shutil
from subprocess import call

REPO = '798432293470.dkr.ecr.eu-west-1.amazonaws.com'
PROJECT = os.path.split(os.getcwd())[-1]

parser = argparse.ArgumentParser(prog='make')
parser.add_argument('-c', '--command',
                    choices=['build', 'run', 'push'], help='The command to execute')
args = parser.parse_args()


def build(args, cache=False):
    if cache:
        call(['docker', 'build', '-t', PROJECT, '.'])
    else:
        call(['docker', 'build', '--no-cache', '-t', PROJECT, '.'])
    call(['docker', 'tag', PROJECT, '{}/{}:{}'.format(REPO, PROJECT, 'latest')])


def run(args):
    build(args, True)
    call(['docker', 'run', '-p', '5000:5000',
          '{}/{}:{}'.format(REPO, PROJECT, 'latest')])


def push(args):
    build(args, True)
    call(['docker', 'push', '{}/{}:{}'.format(REPO, PROJECT, 'latest')])


locals()[args.command](args)
