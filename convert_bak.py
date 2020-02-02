#!/usr/bin/env python3

import os
import shutil
import subprocess

ORIGIN_DIRNAME = "test/to convert/"
DESTINATION_DIRNAME = "test/converted/"

def get_filenames(path):
  return [os.path.join(root, name)
          for root, dirs, files in os.walk(path)
          for name in files]

filenames = get_filenames(ORIGIN_DIRNAME)

def get_substituted_filename(filename, path, path2):
  return os.path.join(path2, filename[len(path):])

for filename in sorted(filenames):
  if filename.endswith(".flac"):
    filename2 = get_substituted_filename(filename, ORIGIN_DIRNAME, DESTINATION_DIRNAME)
    filename2 = ".".join(filename2.split(".")[0:-1]) + ".m4a"
    os.makedirs(os.path.dirname(filename2), exist_ok=True)
    cmd = ["ffmpeg",  "-y", "-i", filename, "-acodec", "alac", filename2]
    subprocess.call(cmd)
    os.remove(filename)
    print("%s converted" % os.path.basename(filename))
  elif filename.split(".")[-1] in ["jpg", "ape", "cue", "log", "txt", "wav"] or "." not in os.path.basename(filename) or len(os.path.basename(filename).split(".")[-1]) > 10:
    filename2 = get_substituted_filename(filename, ORIGIN_DIRNAME, DESTINATION_DIRNAME)
    os.makedirs(os.path.dirname(filename2), exist_ok=True)
    shutil.move(filename, filename2)
    print("%s moved" % os.path.basename(filename))
  elif filename.endswith(".DS_Store"):
    os.remove(filename)
    print("%s deleted" % os.path.basename(filename))
  else:
    raise Exception("Unknown extension %s" % filename.split(".")[-1])

  dirname = os.path.dirname(filename)
  while os.listdir(dirname) == [] and dirname.rstrip("/") != ORIGIN_DIRNAME.rstrip("/"):
    os.rmdir(dirname)
    print("%s cleaned" % os.path.basename(dirname))
    dirname = os.path.dirname(dirname)
 
dirnames = [os.path.join(root, dir)
            for root, dirs, files in os.walk(ORIGIN_DIRNAME)
            for dir in dirs]

for dirname in sorted(dirnames):
  while os.listdir(dirname) == [] and dirname.rstrip("/") != ORIGIN_DIRNAME.rstrip("/"):
    os.rmdir(dirname)
    print("%s cleaned" % os.path.basename(dirname))
    dirname = os.path.dirname(dirname)
