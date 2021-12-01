#!/bin/bash
poetry config virtualenvs.create false
poetry env use system
poetry install

jupyter notebook --generate-config
echo 'c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"' >> /home/vscode/.jupyter/jupyter_notebook_config.py
which jupyter
jupyter nbextension install --py jupytext --user
jupyter nbextension enable jupytext --user --py
