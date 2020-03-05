import json
import os
from .file import FileDelete, FileLossless, FileMP3, FileCopy


class App:
  def __init__(self, origin_path="", destination_path="", rules_path=""):
    self.origin_path = origin_path
    self.destination_path = destination_path
    self.rules_path = rules_path
    self.rules = json.load(open(self.rules_path, 'r'))

  def main(self):
    for filename in self.get_filenames():
      extension = self.get_extension(filename)
      if extension == filename:
        if "NONE" not in self.rules.keys():
          raise Exception("Define default behavior")
        action = self.rules["NONE"].lower()
      else:
        if extension.lower() not in self.rules.keys():
          raise Exception("Unknown extension %s" % extension)
        action = self.rules[extension.lower()].lower()
      if action == "copy":
        f = FileCopy(filename, self.origin_path, self.destination_path)
      elif action == "lossless":
        f = FileLossless(filename, self.origin_path, self.destination_path)
      elif action == "delete":
        f = FileDelete(filename, self.origin_path, self.destination_path)
      elif action == "mp3":
        f = FileMP3(filename, self.origin_path, self.destination_path)
      else:
        raise Exception("Unknown action %s" % action)
      f.process()
  
    for dirname in self.get_dirnames():
      self.clean_directories(dirname)

  def get_filenames(self):
    return sorted([os.path.join(root, name)
                  for root, dirs, files in os.walk(self.origin_path)
                  for name in files])

  def get_dirnames(self):
    return sorted([os.path.join(root, dir)
                  for root, dirs, files in os.walk(self.origin_path)
                  for dir in dirs])

  def clean_directories(self, dirname):
    while os.listdir(dirname) == [] and dirname.rstrip("/") != self.origin_path.rstrip("/"):
      os.rmdir(dirname)
      print("%s cleaned" % os.path.basename(dirname))
      dirname = os.path.dirname(dirname)

  def get_extension(self, filename):
    return filename.split(".")[-1]
