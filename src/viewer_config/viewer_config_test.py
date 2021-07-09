import unittest
import pickle

from bark.runtime.commons.parameters import ParameterServer

from src.viewer_config.viewer_config import dump_viewer_default_params


def pickle_unpickle(object):
    d = pickle.dumps(object)
    return pickle.loads(d)


class ViewerTests(unittest.TestCase):
    def test_dump_defaults(self):
        dump_viewer_default_params("/tmp/")

if __name__ == '__main__':
    unittest.main()
