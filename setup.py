from setuptools import setup, find_packages

setup(
    name="make_xml_4_igv",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pathlib",
        "typing"
    ],
    author="Hanzhou Wang",
    author_email="wangh5@uthscsa.edu",
    description="A package to generate IGV session files from CSV",
    license="MIT", # or other licenses you prefer
    keywords="igv xml bioinformatics",
    url="https://github.com/yourusername/make_xml_4_igv",  # If you host your code on GitHub or another site
)
