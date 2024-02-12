from setuptools import setup
import find_complet

setup(
    name="my_paquet_LM",
    version="0.1",
    description='Un paquet pour gérer les bibliothéques',
    packages=['TD1_gestion_arguements\my_package_LM'],
    scripts=["my_package_LM\\find_complet.py"],
)