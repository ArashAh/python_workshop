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

### 1. Install poetry

Poetry requires python 3.8 or higher. Refer to [this earlier section](#1-check-your-python-version). For the final demonstration of this part of the workshop, python 3.10 (or higher) is required (optional).

Once you have the right python version, it is recommended to install poetry using `pipx`.

See [here](https://pipx.pypa.io/stable/installation/) on how to install `pipx`.

Once `pipx` is installed, see [here](https://python-poetry.org/docs/#installing-with-pipx) on how to use it to install `poetry`



### 2. Setting up a poetry environment

1. **Create a new directory for the project:**


See [here](#2-setting-up-a-virtual-environment-10-minutes) 
Once you have a directory created, `cd` into it.


2. **Create a poetry ("virtual") environment:**

```bash
poetry init my_poetry_proj
```
This will create an isolated poetry project in the current (working) directory called `my_poetry_proj`.

This will ask you a series of questions to set up the project. You can skip this by using the `-n` flag:


3. **Activate the virtual environment (and run python script):**


```bash
poetry shell
```

From here, you can run a python script:

```bash
python {your python script}.py
```

Alternatively, you can do the above to in one step:

```bash
poetry run python {your python script}.py
```
   
It is possible to just use poetry for package management, but set up the virtual environmet with something else (e.g. conda), or not use a virtual environment at all.
In this case, you would run:

```bash
poetry config virtualenvs.create false
```
All the previous (and below) commands are relevant, with the exception of `poetry shell`


### 3. Installing and Using Packages

1. **Installing a package inside your environment:**

*Note: requires a poetry environment to be activated*

```bash
poetry add {package name} 
```
This will update the `pyproject.toml` and `poetry.lock` files

2. **Check what packages you already have:**

You can check the `pyproject.toml` or `poetry.lock` files.

Alternatively, you can run the following command:

```bash
poetry show
```

And for even more detail, add the `--tree` flag:

```bash
poetry show --tree
```

3. **Update dependencies**

You can update all dependencies by running:

```bash
poetry update
```

Or, for a specific package:

```bash
poetry update {package name 1} {package name 2} ...
```


### 4. **Recreate your environment somewhere else:**

To recreate your environment, share your `pyproject.toml` and `poetry.lock` files with someone else. They can then run the following commands:

Note: the user needs to install the correct python and poetry versions (which can be seen in the `pyproject.toml` file)

Then, the user can run
```bash
poetry shell
```

to activate the poetry environment ("project"). The packages can be installed with

```bash
poetry install
```



   
### 5. Cleanup

- **Deactivate your environment:**

You can either run

```bash
exit
```
or
```bash
deactivate
```


- **Delete your environment: (if needed)** 

Within the directory that is defined as a poetry project, first list the available environments

```bash
poetry env list
```

Then, delete chosen environment with

```bash
poetry env remove {environment name}
```


## VS Code <a name="vscode"></a>

### Extensions

- [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Black formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) (optional)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) (optional)
- [Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) (optional)

### Python interactive window

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
