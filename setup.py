from setuptools import setup
from Cython.Build import cythonize

setup(
    name="IsolationSplinter",
    ext_modules=cythonize("ghost_pdf.py", compiler_directives={'language_level': "3"}),
    zip_safe=False,
)
