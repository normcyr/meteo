import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meteo",
    version="0.0.1",
    author="Normand Cyr",
    author_email="normand.cyr@gmail.com",
    description="Petit programme pour appeler OpenWeatherMap et obtenir la météo actuelle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/normcyr/meteo",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyyaml',
        'requests',
          ],
)
