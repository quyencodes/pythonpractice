# Class is the template, object is an instance of the class/template
class Student:
  # define a bunch of attributes about a student
  def __init__(self, name, major, gpa, is_on_probation):
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation

  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False
