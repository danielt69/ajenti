from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title=_('Dashboard'),
    icon='dashboard',
    dependencies=[
        PluginDependency('main')
    ],
)


def init():
    import dash
    import api
    import welcome
