from setuptools import setup, find_packages
import sys

with open("README-PYPI.md",encoding="utf-8") as f:
    long_description = f.read()

data_files = []
if sys.platform == "win32":
    data_files = [('Scripts', ['scripts/upgrade-pip-select.exe','scripts/upgrade-pip-auto.exe'])]

with open("README.md",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "auto-upgrade-pip",
    version = "0.1.0",
    install_requires = ["toml","requests","geoip2"],
    python_requires = ">=3.6",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "",
    long_description = long_description,
    license = "MIT",
    url = "https://github.com/xystudio889/auto-upgrade-pip",
    data_files = data_files,
    include_package_data = True
)
