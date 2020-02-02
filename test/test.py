#!/usr/bin/env python3

import sys
sys.path.append('..')

import os
import shutil
from app.app import App


class Test:
  data_path = 'test/data/music'
  origin_path = 'test/to convert/music/'
  destination_path = 'test/converted/music'

  def test_can_convert_audio_files(self):
    self.clean_test_directory()
    self.copy_test_data()
    self.run_main_program()
    self.check_created_files()
    self.clean_test_directory()

  def clean_test_directory(self):
    if os.path.exists(self.origin_path):
      shutil.rmtree(self.origin_path)
    if os.path.exists(self.destination_path):
      shutil.rmtree(self.destination_path)

  def copy_test_data(self):
    shutil.copytree(self.data_path, self.origin_path)

  def run_main_program(self):
    App(self.origin_path, self.destination_path).main()

  def check_created_files(self):
    assert len(os.listdir(self.destination_path)) == 8
    
