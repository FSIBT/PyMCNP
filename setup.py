from setuptools import setup
import os

setup(
    name="mcnptools",
    use_scm_version={"write_to": "mcnptools/version.py"},
    description="MCNP tools",
    url="https://github.com/mauricioAyllon/MCNP-tools",
    author="Mauricio Ayllon Unzueta",
    author_email="mauri.ayllon12@gmail.com",
    packages=["mcnptools"],
    scripts=["MCNPtools-parse-ptrac"],
    package_data={"mcnptools": [os.path.join("mcnptools", "data", "*txt"),]},
)
