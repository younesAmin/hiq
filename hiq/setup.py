from setuptools import setup
import os

here = os.path.dirname(os.path.realpath(__file__))

VERSION = (
    "1.0.1a"
    if "PKG_VERSION" not in os.environ or not os.environ["PKG_VERSION"]
    else os.environ["PKG_VERSION"]
)
DESCRIPTION = "HiQ - A Modern Observability System"

packages = [
    "hiq",
]


def read_file(filename: str):
    try:
        lines = []
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines if not line.startswith('#')]
        return lines
    except:
        pass

LONG_DESCRIPTION = read_file(f"{here}/README.rst")


setup(
    name="hiq-python",
    version=VERSION,
    author="Henry Fuheng Wu; Kathan Patel",
    author_email="<fuheng.wu@oracle.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=read_file(f"{here}/requirements.txt"),
    keywords=[
        "hiq",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=packages,
    package_dir={"": "src"},
    package_data={"hiq": ["data/*.pk"]},
    url="https://github.com/oracle-samples/hiq",
)
