import os
import shutil
import subprocess


class File:
  def __init__(self, filename="", path="", path2=""):
    self.filename = filename
    self.path = path
    self.path2 = path2
    self.filename2 = ""
    self.cmd = ""

  def create_directory(self):
    os.makedirs(os.path.dirname(self.filename2), exist_ok=True)


class FileCopy(File):
  def process(self):
    self.set_filename2()
    self.create_directory()
    self.copy_file()
    self.print_log()

  def copy_file(self):
    shutil.copy(self.filename, self.filename2)
  
  def set_filename2(self):
    self.filename2 = os.path.join(self.path2, self.filename[len(self.path):])

  def print_log(self):
    print("%s moved" % os.path.basename(self.filename))


class FileDelete(File):
  def process(self):
    self.print_log()

  def print_log(self):
    print("%s deleted" % os.path.basename(self.filename))

  
class FileLossless(File):
  def __init__(self, filename="", path="", path2=""):
    self.filename = filename
    self.path = path
    self.path2 = path2
    self.filename2 = ""
    self.cmd = ""
    
  def process(self):
    self.set_filename2()
    self.create_directory()
    self.set_ffmpeg_cmd()
    self.run_cmd()
    self.print_log()

  def set_filename2(self):
    self.filename2 = os.path.join(self.path2, self.filename[len(self.path):])
    self.filename2 = ".".join(self.filename2.split(".")[0:-1]) + ".m4a"

  def set_ffmpeg_cmd(self):
    self.cmd = ["ffmpeg",  "-y", "-i", self.filename, "-acodec", "alac", self.filename2]

  def run_cmd(self):
    subprocess.call(self.cmd)

  def print_log(self):
    print("%s converted lossless" % os.path.basename(self.filename))


class FileMP3(File):
  def process(self):
    self.set_filename2()
    self.create_directory()
    self.set_ffmpeg_cmd()
    self.run_cmd()
    self.print_log()

  def set_filename2(self):
    self.filename2 = os.path.join(self.path2, self.filename[len(self.path):])
    self.filename2 = ".".join(self.filename2.split(".")[0:-1]) + ".mp3"

  def set_ffmpeg_cmd(self):
    self.cmd = ["ffmpeg",  "-y", "-i", self.filename, "-acodec", "libmp3lame", self.filename2]

  def run_cmd(self):
    subprocess.call(self.cmd)

  def print_log(self):
    print("%s converted mp3" % os.path.basename(self.filename))
