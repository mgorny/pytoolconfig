"""Source for setup.cfg configuration files via ini config."""
from pathlib import Path
from typing import Optional, Tuple

from pytoolconfig.universal_config import UniversalConfig
from pytoolconfig.utils import min_py_version

from .ini import IniConfig


class SetupConfig(IniConfig):
    """Source for setup.cfg configuration files via ini config."""

    name: str = "setup.cfg"
    description = """
    Setuptools allows using configuration files (usually setup.cfg) to define a
    package’s metadata and other options that are normally supplied to the setup()
    function (declarative config)."""

    def __init__(self, working_directory: Path, base_table: str):
        super().__init__(working_directory, "setup.cfg", base_table)
