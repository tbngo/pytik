from setuptools import find_packages, setup

setup(
    name="pytik",
    packages=find_packages(include=["pytik"]),
    version="0.1.2",
    author="The Ngo",
    author_email="thengocu@gmail.com",
    description="Python metadata scrapper for TikTok",
    url="https://github.com/thengo1/pytik",
    project_urls={
        "Read the Docs": "https://pytik.readthedocs.io/en/latest",
    },
    license="MIT",
    install_requires=["selenium", "chromedriver-py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
