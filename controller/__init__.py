from os.path import dirname, sep, basename, isfile
import glob

modules = glob.glob(dirname(__file__) + sep + "*_controller.py")

__all__ = [ basename(f)[:-3] for f in modules if isfile(f) ]

from . import *