from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.2",
    author="ds-fau-ck",
    description="A small package for ANN Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ds-fau-ck/ANN-Implementation.git",
    author_email="chakmakulakirti@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)