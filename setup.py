from setuptools import find_packages, setup

setup(
    name="pytik",
    packages=find_packages(include=["pytik"]),
    version="0.1.1",
    author="The Ngo",
    author_email="thengocu@gmail.com",
    description="Python metadata scrapper for TikTok",
    license="MIT",
    install_requires=["selenium", "webdriver-manager"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
