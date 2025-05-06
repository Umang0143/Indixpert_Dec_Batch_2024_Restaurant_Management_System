import sys
import os

sys.path.append(os.getcwd())

from Src.Authentication.Manage import Menu

ob=Menu()
ob.menu()