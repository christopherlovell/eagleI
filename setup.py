import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eagleIO",
    version="0.0.1",
    author="Christopher Lovell",
    author_email="c.lovell@herts.ac.uk",
    description="Read EAGLE HDF5 files with multithreading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/christopherlovell/eagleIO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


