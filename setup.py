from setuptools import setup

setup(
    name="footballframe",
    version="0.1.0",
    description="Framework for creating football simulations",
    url="https://github.com/adam42739/football-frame",
    author="Adam Lynch",
    author_email="aclynch@umich.edu",
    license="MIT License",
    packages=["footballframe", "footballframe.stats"],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licesnse :: MIT License",
        "Operating System :: OS Independent",
    ],
)
