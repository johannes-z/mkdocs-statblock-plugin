from setuptools import setup, find_packages

setup(
    name="mkdocs-statblock-plugin",
    version="0.1",
    description="MkDocs plugin to format YAML within statblock superfences as HTML",
    url="https://github.com/johannes-z/mkdocs-statblock-plugin.git",
    author="Johannes Zwirchmayr",
    author_email="johannes.zwirchmayr@gmail.com",
    packages=find_packages(),
    install_requires=[
        "mkdocs>=1.6.0",
        "pyyaml",
    ],
    python_requires=">=3.6",
    entry_points={
        "mkdocs.plugins": [
            "statblock = mkdocs_statblock_plugin.mkdocs_statblock_plugin:StatBlockPlugin"
        ]
    },
)
