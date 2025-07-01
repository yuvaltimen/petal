from setuptools import setup, find_packages

setup(
    name="petal",
    version="0.1.0",
    author="Yuval Timen",
    author_email="yuvaltimen@gmail.com",
    description="Composable ETL Logic Layer",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
