import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="kitten",
    version="0.0.1",
    author="Chris Rehn",
    author_email="chris@rehn.me",
    description="Tiny tool to manage multiple servers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hoffa/kitten",
    packages=setuptools.find_packages(),
    scripts=["bin/kitten"],
    install_requires=["boto3>=1.7.0", "fabric>=2.1.0"],
    license="MIT",
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ),
)
