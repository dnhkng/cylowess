'''
Setup file for cylowess.pyx, a faster lowess smoother in Cython.
'''
try:
    from distutils.core import setup
    from distutils.extension import Extension
    import numpy as np
#    from Cython.Distutils import build_ext # uncomment for development

    setup(
        name='cylowess',
#        cmdclass = {'build_ext' : build_ext}, # uncomment for development
        include_dirs = [np.get_include()],
        ext_modules = [Extension('cylowess', ['cylowess.c'])]
        )
except:
    pass
