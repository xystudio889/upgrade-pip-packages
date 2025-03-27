from setuptools import setup, find_packages

with open("README-PYPI.md",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "auto-upgrade-pip",
    version = "0.1.0.dev0",
    packages = find_packages(),
    install_requires = ["toml","requests"],
    python_requires = ">=3.6",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "",
    long_description = long_description,
    license = "MIT",
    url = "https://github.com/xystudio889/",
)
