import sys

from setuptools import setup


setup(
    name="patho_ids",
    version="0.2",
    packages=["patho_ids"],
    include_package_data=True,
    install_requires=["pandas", "google-cloud-vision"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux  ",
    ],
    entry_points="""
        [console_scripts]
        patho_ids=patho_ids.ocr:main
    """,
)
