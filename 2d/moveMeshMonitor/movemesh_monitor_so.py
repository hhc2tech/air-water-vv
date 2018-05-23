"""
Split operator module for two-phase flow
"""

import os
from proteus.default_so import *
from proteus import Context

# Create context from main module
name_so = os.path.basename(__file__)
if '_so.py' in name_so[-6:]:
    name = name_so[:-6]
elif '_so.pyc' in name_so[-7:]:
    name = name_so[:-7]
else:
    raise NameError, 'Split operator module must end with "_so.py"'

case = __import__(name)
Context.setFromModule(case)
ct = Context.get()

# List of p/n files
pnList = []

# moving mesh
if ct.movingDomain:
    pnList += [("moveMesh_p", "moveMesh_n")]

needEBQ_GLOBAL = False
needEBQ = False

tnList = ct.tnList

from proteus.Archiver import ArchiveFlags
archiveFlag = ArchiveFlags.EVERY_USER_STEP