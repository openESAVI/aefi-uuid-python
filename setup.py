from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'UUID v4 to AEFI (ESAVI)'
LONG_DESCRIPTION = 'Package to generate UUID v5 to AEFI (ESAVI)'

# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="aefi-uuid", 
        version=VERSION,
        author="Alejandro Benavides",
        author_email="<abenavidescr@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'aefi', 'uuid', 'esavi', 'uuidv5'],
        classifiers= [
            "License :: OSI Approved :: Apache Software License",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Healthcare Industry",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
            "Natural Language :: English",
            "Natural Language :: Spanish"
        ]
)