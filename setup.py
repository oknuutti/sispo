from setuptools import setup, find_namespace_packages

setup(name="sispo",
      version="0.1.0",
      description="Space Imaging Simulator for Proximity Operations",
      long_description=open("README.md", "r").read(),
      platforms=["Windows"],
      url="https://github.com/YgabrielsY/sispo",
      author="Gabriel J. Schwarzkopf, Mihkel Pajusalu",
      license="BSD 2-Clause",
      packages=find_namespace_packages(include=["sispo",
                                                "sispo.sim",
                                                "sispo.compression",
                                                "sispo.reconstruction",
                                                "data"],
                                       exclude=["*test*",
                                                "*software*",
                                                "*build*",
                                                "*doc*",
                                                "*.vs*",
                                                "*.vscode*",
                                                "*.mypy_cache*"]),
      entry_points={"console_scripts": ["sispo = sispo:main"]},
      include_package_data=True,
      zip_safe=False)
