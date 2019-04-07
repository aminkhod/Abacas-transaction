from cx_Freeze import setup, Executable

base = None    

executables = [Executable("transaction _PO.py", base=base)]

packages = ['idna','pandas','numpy',]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
