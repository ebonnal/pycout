from setuptools import setup  # type: ignore

setup(
    name="pycout",
    version="1.0.1",
    packages=["pycout"],
    url="http://github.com/EnzoBnl/pycout",
    license="Apache 2.",
    author="Enzo Bonnal",
    author_email="enzobonnal@gmail.com",
    description="""C++'s `cout << "Hello" << " World !" << endl;` in Python.""",
)
