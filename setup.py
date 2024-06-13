from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'GB program'
LONG_DESCRIPTION = 'Pacakge for grain boundary construction in a hexagonal system'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="GB", 
        version=VERSION,
        author="Davydov N. Geondzhian A., Aksenov D.",
        author_email="Nikita.Davydov@skoltech.ru",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy', 'siman'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'GB', 'grain boundary', 'grain', 'grainboundary'],
        classifiers= [
            "Development Status :: Pre-Alpha",
            "Intended Audience :: Academic",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS 14.4.1 ",
            "Operating System :: Microsoft :: Windows",
        ]
)