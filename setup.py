import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dappi",
    version="1.0.2",
    description="Parse messages from discord server exports into csv files",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Andrew-Pynch/discord-message-scraper/tree/main/dappy",
    author="Andrew Pynch",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["beautifulsoup4"],
    entry_points={
        "console_scripts": [
            "dappi=dappi.__main__:main",
        ]
    },
)