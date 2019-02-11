'VisiData: a curses interface for exploring and arranging tabular data'

__version__ = '1.6-dev'
__version_info__ = 'VisiData v' + __version__
__author__ = 'Saul Pwanson <vd@saul.pw>'
__status__ = 'Production/Stable'
__copyright__ = 'Copyright (c) 2016-2019 ' + __author__

from .vdtui import *
from .vdtui.textsheet import TextSheet
from .helpers import *
from .asyncthread import *
from .input import *
from .movement import *
from .path import *
from .errors import *
from .urlcache import *
from .zscroll import *
from ._types import *
from .selection import *
from .loaders.tsv import *
from .data import *
from .clipboard import *
from .utils import *
from .slide import *
from .search import *
from .expr import *

from .pyobj import *
from .metasheets import *
from .join import *
from .describe import *
from .aggregators import *
from .pivot import *
from .freqtbl import *
from .tidydata import *
from .cmdlog import *
from .freeze import *
from .regex import *
from .canvas import *
from .graph import *
from .motd import *
from .transpose import *
from .diff import *
from .shell import *
import visidata.sort

from .vimkeys import *

from .loaders.csv import *
from .loaders.json import *
from .loaders.zip import *
from .loaders.xlsx import *
from .loaders.hdf5 import *
from .loaders.sqlite import *
from .loaders.fixed_width import *
from .loaders.postgres import *
from .loaders.shp import *
from .loaders.mbtiles import *
from .loaders.http import *
from .loaders.html import *
from .loaders.markdown import *
from .loaders.pcap import *
from .loaders.png import *
from .loaders.ttf import *
from .loaders.sas import *
from .loaders.spss import *
from .loaders.xml import *
from .loaders.yaml import *
from .loaders._pandas import *
from .loaders.graphviz import *

from .plugins import *

from .colors import *   # ColorsSheet

from math import *


addGlobals(globals())
