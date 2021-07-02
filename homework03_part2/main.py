#!/usr/bin/env python
class FileLineReader:
  def __init__(self, file_path):
    self.file_path = file_path

  def __iter__(self):
    def _gen():
      with open(self.file_path, 'r') as fo:
        for line in fo:
          yield line

    return _gen()


class PersonReader:
  def __init__(self, flr:FileLineReader):
    self.flr = flr        
        
  def __iter__(self):
    pass


class FemaleReader:
  def __init__(self, pr:PersonReader):
    self.pr = pr
        
  def __iter__(self):
    pass


if __name__ == '__main__':
  # Line reader
  fr = FileLineReader('homework3_part2.csv')
  print("=== Line reader ===")
  for line in fr:
    print(line.strip())

  # Person reader
  print("\n=== Person reader ===")
  pr = PersonReader(fr)
  for p in pr:
    print(p)

  # Female reader
  print("\n=== Female reader ===")
  fr = FemaleReader(pr)
  for p in fr:
    print(p)
