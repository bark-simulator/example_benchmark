import os

from bark.runtime.viewer.matplotlib_viewer import MPViewer
from bark.runtime.commons.parameters import ParameterServer


def dump_viewer_default_params(dir):
    params = ParameterServer()
    miqp_behavior = MPViewer(params)

    params.Save(filename=os.path.join(dir, "mp_viewer_params.json"))
    params.Save(filename=os.path.join(dir, "mp_viewer_description.json"),
                print_description=True)
