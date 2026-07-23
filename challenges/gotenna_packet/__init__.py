import sys

sys.modules.setdefault("gotenna_packet", sys.modules[__name__])

from .gotenna_packet import *
