from setuptools import setup, find_packages
import sys
from auto_upgrade_pip import __version__

with open("README-PYPI.md",encoding="utf-8") as f:
    long_description = f.read()

data_files = []
if sys.platform == "win32":
    data_files = [('Scripts', ['scripts/upgrade-pip.exe'])]

setup(
    name = "auto-upgrade-pip",
    version = __version__,
    install_requires = [],
    python_requires = ">=3.6",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "Fast to upgrade your pip packages.",
    long_description = open("README.md",encoding="utf-8").read(),
    license = "MIT",
    url = "https://github.com/xystudio889/auto-upgrade-pip",
    data_files = data_files,
    include_package_data = True
)
