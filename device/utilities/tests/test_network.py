# Import standard python libraries
import sys, os

# Set system path
ROOT_DIR = os.environ["OPENAG_BRAIN_ROOT"]
sys.path.append(ROOT_DIR)
os.chdir(ROOT_DIR)

# Import connect utility
from device.utilities import network


def test_init() -> None:
    assert True
