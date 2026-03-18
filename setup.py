from setuptools import setup, find_packages
from auto_upgrade_pip import __version__

with open("README-PYPI.md",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "auto-upgrade-pip",
    packages=find_packages(),
    version = __version__,
    install_requires = [],
    python_requires = ">=3.6",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "Fast to upgrade your pip packages.",
    long_description = open("README.md",encoding="utf-8").read(),
    license = "MIT",
    entry_points={
        "console_scripts": [
            "pip-upgrade = auto_upgrade_pip.__main__:main",
        ]
    }, 
    url = "https://github.com/xystudio889/auto-upgrade-pip",
    include_package_data = True
)
