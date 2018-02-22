from setuptools import setup, find_packages

setup(name="hello",
      version="0.1",
      description="hello",
      author="Kontrol SAS",
      packages=find_packages(),
      include_package_data=True,
      setup_requires=["cffi"],
      cffi_modules=["build_hello.py:ffibuilder"],
      install_requires=["cffi"],
      )
