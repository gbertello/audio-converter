#!/usr/bin/env python3

import os
import shutil
import subprocess

if os.path.exists('test/to convert/music'):
  shutil.rmtree('test/to convert/music/')

shutil.copytree('test/data/music', 'test/to convert/music')

subprocess.call(['./convert.py'])

if len(os.listdir('test/converted/music/')) == 8:
  print("OK")
else:
  print("KO")

shutil.rmtree('test/converted/music/')
