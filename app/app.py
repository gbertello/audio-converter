import os
from .file import File, FileDSStore, FileFLAC


class App:
  def __init__(self, origin_path="", destination_path=""):
    self.origin_path = origin_path
    self.destination_path = destination_path

  def main(self):
    for filename in self.get_filenames():
      extension = self.get_extension(filename)
      if extension in ["jpg", "ape", "cue", "log", "txt", "wav"] or extension == os.path.basename(filename):
        f = File(filename, self.origin_path, self.destination_path)
      elif extension == "flac":
        f = FileFLAC(filename, self.origin_path, self.destination_path)
      elif extension == "DS_Store":
        f = FileDSStore(filename, self.origin_path, self.destination_path)
      else:
        raise Exception("Unknown extension %s" % extension)
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
