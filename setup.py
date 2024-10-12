from setuptools import setup  # type: ignore

setup(
    name="pycout",
    version="1.0.2",
    packages=["pycout"],
    url="http://github.com/ebonnal/pycout",
    license="Apache 2.",
    author="Enzo Bonnal",
    author_email="bonnal.enzo.dev@gmail.com",
    description="C++'s cout for Python ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
