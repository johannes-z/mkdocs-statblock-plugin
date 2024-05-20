from setuptools import setup, find_packages

setup(
    name="mkdocs-statblock-plugin",
    version="0.1",
    description="MkDocs plugin to format YAML within statblock superfences as HTML",
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.0.4',
        'pyyaml',
    ],
    entry_points={
        'mkdocs.plugins': [
            'statblock = mkdocs_statblock_plugin.mkdocs_statblock_plugin:StatBlockPlugin'
        ]
    }
)
