from setuptools import setup, find_packages

setup(
    name = "autoinsights",
    version = "0.1",
    author = "Akash Das",
    author_email = "akashdpro@gmail.com",
    description = "An automatic dataset exploration and visualization package",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/Akashdtech/autoinsights",
    packages = find_packages(),
    install_requires = [
        "pandas>=1.0.0",
        "matplotlib>=3.0.0",
        "seaborn>=0.11.0"
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
