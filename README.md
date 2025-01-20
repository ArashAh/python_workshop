# Getting up-to-speed with Python: Workshop Materials

- [Package and environment management with pip and venv](#environment)
- [Package and environment management with conda](#conda)
- [Package and environment management with poetry](#poetry)
- [VS Code](#vscode)
- [JupyterLab](#jupyterlab)
- [Production tools - HPC servers](#hpc)

----

## Package and environment management with pip and venv <a name="environment"></a>

### Objectives
- Understand the purpose of virtual environments.
- Learn to create, activate, deactivate, and delete virtual environments.

---
### 1. Check your python version

<table>
  <tr>
    <td>
      <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
      <pre>
      <code>
$ python --version
      </code>
      </pre>
    </td>
    <td>
      <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
      <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
      <pre>
      <code>
$ python3 --version
      </code>
      </pre>
    </td>
  </tr>
</table>


### 2. Setting Up a Virtual Environment (10 minutes)


1. **Create a new directory for the project:**
   
    <table>
      <tr>
        <td>
          <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
          <pre>
          <code>
    md my_project
    cd my_project
          </code>
          </pre>
        </td>
        <td>
          <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
          <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
          <pre>
          <code>
    mkdir my_project
    cd my_project
          </code>
          </pre>
        </td>
      </tr>
    </table>

2. **Create a virtual environment:**
The following command creates an isolated Python environment in the "my_venv" directory.

    <table>
      <tr>
        <td>
          <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
          <pre>
          <code>
    python -m venv my_venv
          </code>
          </pre>
        </td>
        <td>
          <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
          <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
          <pre>
          <code>
    python3 -m venv my_venv
          </code>
          </pre>
        </td>
      </tr>
    </table>

3. **Activate the virtual environment:**

    <table>
      <tr>
        <td>
          <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
          <pre>
          <code>
    .\my_venv\Scripts\activate
          </code>
          </pre>
        </td>
        <td>
          <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
          <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
          <pre>
          <code>
    source my_venv/bin/activate
          </code>
          </pre>
        </td>
      </tr>
    </table>
   
### 3. Installing and Using Packages
1. **Check what packages you already have:**
   ```bash
   pip list
    ```
2. **Installing a package inside your environment:**
   ```bash
   pip install numpy
    ```
3. **Verify the installation:**
   ```bash
   pip list
    ```
4. **Compare with global python environment:**

    Deactivate your virtual environment
   ```bash
   deactivate
   ```
   
    List packages in the global environment
   ```bash
   pip list
   ```
   
5. **Reactivate your virtual environment:**

    <table>
      <tr>
        <td>
          <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
          <pre>
          <code>
    .\my_venv\Scripts\activate
          </code>
          </pre>
        </td>
        <td>
          <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
          <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
          <pre>
          <code>
    source my_venv/bin/activate
          </code>
          </pre>
        </td>
      </tr>
    </table>

   
6. **Upgrading pip inside the environment:**
   ```bash
   pip install --upgrade pip
   ```
7. **Creating a requirements file:**
   ```bash
   pip freeze > requirements.txt
   ```
   
8. **Recreate your environment somewhere else:**

    <table>
      <tr>
        <td>
          <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
          <pre>
          <code>
    python -m venv new_venv
    .\new_venv\Scripts\activate
    pip install -r requirements.txt
          </code>
          </pre>
        </td>
        <td>
          <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
          <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
          <pre>
          <code>
    python3 -m venv new_venv
    source new_venv/bin/activate
    pip install -r requirements.txt
          </code>
          </pre>
        </td>
      </tr>
    </table>
   
### 4. Cleanup

- **Deactivate your environment:**

   ```bash
   deactivate 
   ```

- **Delete your environment: (if needed)** 

<table>
  <tr>
    <td>
      <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
      <pre>
      <code>
rmdir /s /q new_venv
      </code>
      </pre>
    </td>
    <td>
      <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
      <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
      <pre>
      <code>
rm -rf new_venv
      </code>
      </pre>
    </td>
  </tr>
</table>


## Package and environment management with conda <a name="conda"></a>

These are the options for Conda installation (Anaconda is not required for the workshop) [https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

Removing the defaults channel, and (just in case) adding the conda-forge channel:
````
conda config --remove channels defaults
conda config --add channels conda-forge
`````

Example Conda session. Pip is used inside a Conda environment:
```
conda create --name my-own-test-env python=3.11 
conda activate my-own-test-env 
conda install pandas
where pip
conda install pip
pip install scikit-learn
conda list
conda env export --from-history
conda deactivate
```


## Package and environment management with poetry <a name="poetry"></a>

Poetry requires python 3.8 or higher. For the final demonstration of this part of the workshop, python 3.10 (or higher) is required (optional).

Once you have the right python version, it is recommended to install poetry using `pipx`.

See [here](https://pipx.pypa.io/stable/installation/) on how to install `pipx`.

Once `pipx` is installed, see [here](https://python-poetry.org/docs/#installing-with-pipx) on how to use it to install `poetry`

## VS Code <a name="vscode"></a>

### Install extensions

The below lists the following extensions that will be used in the workshop. Click on each link for installation instructions 

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Black formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) (optional)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) (optional)
- [Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) (optional)

*Note: You can technically run python code without any of these extensions, but they have useful features.*

*Note: The "Black formatter" and "Pylint" depend on the "Python" extension. "Jupyter" will allow you to run code in an "interactive window". "Data Wrangler" will allow you to inspect pandas dataframes in a spreadsheet view.*

### Setup for Python interactive window

You need a VS Code version from 2024.

See [here](https://code.visualstudio.com/docs/python/jupyter-support-py) for full details

How to install required libraries for this setup (ideally in an virtual environment):
```bash
pip install jupyter
pip install ipykernel
```

Additional to convert a python file (.py) to jupyter notebook (.ipynb)
```bash
pip install nbconvert
```

You also need the jupyter extension (see above)

### Hands-on VS Code

#### 1. General

1. **General layout**

![Image](https://github.com/user-attachments/assets/9142e0f9-bf8a-47bb-bfc5-1c7ad643ce0c)

2. **Select python interpreter/environment**

Click on:
```
Manage (cog wheel) -> Command Palette -> "> "Python: Select Interpreter" -> {choose desired environment/interpreter}
```
Or with keyboard shortcut 
```
Ctrl + shift + P "> "Python: Select Interpreter" -> {choose desired environment/interpreter}
```

### Formatting and linting

![Image](https://github.com/user-attachments/assets/e6afdc13-f377-4c12-b004-9c1f3fd9b185)

1. **Formatting Python in VS Code**

There are lots of formatters in python, that are available in VS Code. We will be using `black` in this workshop.

![Image](https://github.com/user-attachments/assets/a5a44be0-b319-4b12-b91f-ad5b229a66b1)


`Right click (anywhere in open file) -> Format Document with -> Black Formatter`

We will see how this changes `scripts/fizz_buzz.py`

If you want to the formatter to be "activated" when saving a file at the workspace level, 
Select:

`Command Palette -> Preferences: Open Workspace Settings (JSON)`. 

This will open / create `.vscode/settings.json`. This should be edited to:

```json
{
    "[python]": {
      "editor.formatOnSave": true,
      "python.formatting.provider": "ms-python.black-formatter"
    }
}
```
See official [documentation](https://code.visualstudio.com/docs/python/formatting) for more details

2 **Linting python in VS Code (minor)**

Checks code for semantic and stylistic problems.

![Image](https://github.com/user-attachments/assets/a304dd51-e5b1-479f-bcf2-f1daf3daee34)

`Ctrl + shift + M`: open tab with list of “problems”

Note: Unlike a formatter, in VS Code, this is by default activated  for *all* python files. Need to manually turn it off if not desired.


### 3. Jupyter in VS Code

1. **`.ipynb` files**
- Markdown formatting 
- Integrated text/code/output 
- Running chunk by chunk 
- Updating outputs independently 
- Generating html or pdf render

![Image](https://github.com/user-attachments/assets/38345b7c-4bf0-4efd-b133-7f861515a0d9)


2. **Running "cells" in interactive mode**

In a standard `.py` file, you can create cells by adding `# %%` at the beginning of a line.

e.g.
```python
# %%
x = 5
y = 3
print(x + y)
```

Markdown cells can be defined with `# %% [markdown]` at the beginning of a line.

e.g.
```python
# %% [markdown]
"""
Add any desired text (in quotation marks) that you want displayed in the rendered jupyter file
"""
```

Some useful shortcuts:

* `ctrl + enter` = run current cell
* `shift + enter` = run current cell and jump to next cell
* `[ctrl + shift + ,] A` = insert cell above
* `[ctrl + shift + ,] B` = insert cell below
* `[ctrl + shift + ,] S` = insert cell below current position
* `[ctrl + shift + ,] X` = delete selected cell(s)
* `[ctrl + shift + ,] M` = change code cell to markdown
* `[ctrl + shift + ,] C` = change (markdown) cell to code
* `[ctrl + shift + ,] U` = move selected cell(s) up
* `[ctrl + shift + ,] D` = move selected cell(s) down

3. **Convert python to jupyter file (minor)**

In a python file that has "cells":

` Right click (anywhere in the file view) -> Export current python file as jupyter notebook`

Then, to render the juptyer notebook as an HTML file, do:

```bash
jupyter nbconvert --to html --execute <name of jupyter file>.ipynb
```

4. **Variable view**

To replicate the "global environment" window in RStudio, you can use the "Data Wrangler" extension.

![Image](https://github.com/user-attachments/assets/1f057fcf-81de-4783-9e5c-dc6c63ae54f1)

This lets you inspect a pandas dataframe in a spreadheet view, that can be opened as a separate window.

Assuming you have a pandas dataframe in an "interactive window", you will see a new button:

![Image](https://github.com/user-attachments/assets/7a06a0a0-da1b-4900-9eef-a32be12e3598)


5. **Version control in VS Code**

![Image](https://github.com/user-attachments/assets/139fc806-d5b3-4622-818a-d4f12938392f)


## JupyterLab <a name="jupyterlab"></a>
Create a new virtual environment, activate it, install jupyerlab and start jupyterlab server.
<table>
  <tr>
    <td>
      <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
      <pre>
      <code>
python -m venv jup_venv
.\jup_venv\Scripts\activate
pip install jupyterlab
jupyter lab
      </code>
      </pre>
    </td>
    <td>
      <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
      <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
      <pre>
      <code>
python3 -m venv jup_venv
source jup_venv/bin/activate
pip install jupyterlab
jupyter lab
      </code>
      </pre>
    </td>
  </tr>
</table>

**Download Example notebook**
```
wget https://raw.githubusercontent.com/ArashAh/python_workshop/refs/heads/main/scripts/Python_script_jupyter.ipynb
```

**Extras** (Note: If any of the following commands do not work as expected, please make changes based on earlier exercises.)
```
python -m venv jupyterlab_env
python -m venv kernel_env
source jupyterlab_env/bin/activate
pip install jupyterlab
source kernel_env/bin/activate
pip install ipykernel
python -m ipykernel install --user --name=kernel_env --display-name "Python (kernel_env)"
source jupyterlab_env/bin/activate
jupyter lab

jupyter kernelspec list
jupyter kernelspec uninstall unwanted-kernel
```

## Production tools - HPC servers <a name="hpc"></a>
We will demonstrate a simple python job submitted with Slurm on the Fox HPC cluster. If you have access to Fox and want to follow along, you can download the scripts needed: 

```
wget https://raw.githubusercontent.com/ArashAh/python_workshop/refs/heads/main/scripts/pandas_plots.py
wget https://raw.githubusercontent.com/ArashAh/python_workshop/refs/heads/main/scripts/run_pandas_plots.slurm
wget https://raw.githubusercontent.com/ArashAh/python_workshop/refs/heads/main/scripts/weather_data.csv
```

For running on other HPC systems you will need to edit the module names and the account name in the run_pandas_plots.slurm script, to match the names for your HPC.  
