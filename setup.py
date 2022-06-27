"""
Lab setup 

"""
from setuptools import setup

setup(
    name="vTest",
    version="1.0.0",
    description="Automated vTest",
    packages=['vTest'],
    
    install_requires=[
        "click",
        "questionary"
    		],
    
    entry_points={
        'console_scripts': ['vTest=vTest.__main__:main']
                },

)

