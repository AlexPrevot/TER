from distutils.core import setup, Extension

module1 = Extension('myModule',
                    sources = ['algogen.cpp', 'path.cpp', 'geneticalgorithm.cpp', 'generator.cpp', 'crosser.cpp', 'timer.cpp'],
		    extra_compile_args=['/openmp'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])