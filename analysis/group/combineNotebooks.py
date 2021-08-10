import nbformat
# SOURCE: https://towardsdatascience.com/how-to-easily-merge-multiple-jupyter-notebooks-into-one-e464a22d2dc4

# Reading the notebooks
guysNotebook = nbformat.read('../Guy/milestone2.ipynb', 4)
jiaQuansNotebook = nbformat.read('../jia_quan/milestone2.ipynb', 4)

# Creating a new notebook
final_notebook = nbformat.v4.new_notebook(metadata=guysNotebook.metadata)

# Concatenating the notebooks
final_notebook.cells = guysNotebook.cells + jiaQuansNotebook.cells

# Saving the new notebook 
nbformat.write(final_notebook, 'final_notebook.ipynb')