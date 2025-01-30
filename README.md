# Getting up-to-speed with Python: Workshop Materials

This page contains the complementary material for the "Getting up to speed with Python" workshop. The material is designed to be used in the hands-on part of the workshop and is not supposed to be used as an stand-alone source of instructions. 

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


---
**NOTE**

- To inherit packages from the global python environment, use `--system-site-packages` during environment creation.

  **Example:** `python3 -m venv myvenv --system-site-packages`

---

## Package and environment management with conda <a name="conda"></a>

### 1. Get started
These are the options for Conda installation (Anaconda is not required for the workshop):[https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

You may have to perform some further steps to activate Conda. Consult [https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)

Remove the defaults channel, and add the conda-forge channel (unless already present):
```
conda config --remove channels defaults
conda config --add channels conda-forge
```
List current channels:
```
conda config --show channels
````

### 2. Set up a new virtual environment
Create a Conda environment. Specify Python version
```
conda create --name my-own-test-env python=3.11 
```
Activate the environment:
```
conda activate my-own-test-env 
```
Do you now see an indication that `my-own-test-env` is active?

The new environment will be located inside a folder in a default location (It is possible to override the default location). To look up the location, you can use
```
conda info
```
Look under `active env location`. Python should already be in there -- verify this with e.g. `where python`. Do you have the expected version of Python?

### 3. Install a package
If you haven't already, activate the environment first.

Install a package with Conda: 
```
conda install pandas
```

### 4. Use Pip within a Conda environment
Do we have Pip inside the environment?
```
where pip
```
Is the `pip` executable inside the Conda environment folder? If not, install it:
```
conda install pip
```
Install a package with pip:
```
pip install scikit-learn
````
Both Pandas and Scikit-learn depend on Numpy. Did Pip reinstall Numpy, or did it find that Numpy was already installed when we installed Pandas?

Note that Scikit-learn is also available from Conda, but we want to try out Pip here.

### 5. Document an environment
List the primary dependencies:
```
conda env export --from-history
```
Was scikit-learn listed?

Also try these:
```
conda env export
conda list
conda list --explicit
```
These document the environment in various level of detail.

### 6. Reproduce an environment
List all dependencies, including version number, and write the output to a yaml file:
```
conda env export > environment.yml
```
(This level of detail may be too high for sharing across systems)

Deactivate the environment:
```
conda deactivate
```
Recreate the environment based on the yaml file:
```
conda env create --name test-my-yml --file environment.yml
```

Activate the new environment, and verify that packages were installed.

## Package and environment management with poetry <a name="poetry"></a>

### 1. Install poetry

Poetry requires python 3.9 or higher. Refer to [this earlier section](#1-check-your-python-version). For the final demonstration of this part of the workshop, python 3.10 (or higher) is required (optional).

Once you have the right python version, it is recommended to install poetry using `pipx`.

See [here](https://pipx.pypa.io/stable/installation/) on how to install `pipx`.

Once `pipx` is installed, see [here](https://python-poetry.org/docs/#installing-with-pipx) on how to use it to install `poetry`



### 2. Setting up a poetry environment

1. **Create a new directory for the project:**


See [here](#2-setting-up-a-virtual-environment-10-minutes) 
Create a directory `my_poetry_project` (ideally, within this repo), and `cd` into it .


2. **Create a poetry ("virtual") environment:**

```bash
poetry init 
```
This will create an isolated poetry project in the current (working) directory called `my_poetry_proj`.

This will ask you a series of questions to set up the project. You can skip this by using the `-n` flag:

You can in principle add packages, but due to a current "bug" (change in PyPi search results), this is not working as expected.

*Note: you can alternatively, create a new directory with poetry directly, which will skip the interactive setup, and set some defaults in the configuration files*

```bash
poetry new my_poetry_proj
```

This will create a `pyproject.toml` file, which is the configuration file for poetry.

By default, poetry will assume you are creating a package. For clarity, and to avoid potential any errors (unless your codebase is is set up as a valid python package),

add the following to the `pyproject.toml`:
```toml
package-mode = false
```

3. **Activate the virtual environment (and run python script):**


```bash
poetry shell
```

From here, you can run a python script:

```bash
python path/to/python_workshop/scripts/pd_data.py
```

Alternatively, you can do the above to in one step:

```bash
poetry run python path/to/python_workshop/scripts/pd_data.py
```

*Note: the above two lines will not work, because we are missing the packages*

### 3. Installing and Using Packages

1. **Installing a package inside your environment:**

*Note: requires a poetry environment to be activated*

```bash
poetry add {package name} 
```

Specifically, we will add `numpy` and `pandas`:

```bash
poetry add numpy 
poetry add pandas
```

Or in one line:

```bash
poetry add numpy pandas
```

This will update the `pyproject.toml` and `poetry.lock` (or create the latter if it does not exist)

Now, we will be able to successfully run the python script:

```bash
python path/to/python_workshop/scripts/pd_data.py
```


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

We will see how this works by installing dependencies and running a microservice from another repo (to be done together)

*Note: in the example, we will most likely have to add `package-mode = false` to the `pyproject.toml` file, as the microservice is not a valid python package.*


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

### 6. Additional

1. **Poetry just for package managment**

It is possible to just use poetry for package management, but set up the virtual environmet with something else (e.g. conda), or not use a virtual environment at all.
In this case, you would run:

```bash
poetry config virtualenvs.create false
```
All the above commands are relevant, with the exception of `poetry shell`


2. **Poetry subfolder in VS Code**

VS Code “python: select interpreter” will automatically detect poetry environments in the working directory

If elsewhere (e.g. subfolder), need to manually specify the path

```bash
poetry env info -p {in directory containing poetry configs}
```

Paste path from above into the “Enter interpreter path”


## VS Code <a name="vscode"></a>

### Install extensions

In this workshop, we will explore several extensions that enhance the functionality of VS Code for Python development. Click on each link for installation instructions: 

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Black formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) 
- [Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler) 

*Note: You can technically run python code without any of these extensions, but they have useful features.*

*Note: The "Black formatter" and "Pylint" depend on the "Python" extension. "Jupyter" will allow you to run code in an "interactive window". "Data Wrangler" will allow you to inspect pandas dataframes in a spreadsheet view.*

### Install libraries 

How to install required libraries for this setup (ideally in an virtual environment):
```bash
pip install jupyter
pip install ipykernel
```

Additional to convert a python file (.py) to jupyter notebook (.ipynb)
```bash
pip install nbconvert
```
In order to run python codes interactively, you need a VS Code version from 2024.

See [here](https://code.visualstudio.com/docs/python/jupyter-support-py) for full details

You also need the jupyter extension (see above)

### Hands-on VS Code
#### Basics 

1. **General layout**
    - Welcome page 
    - Open folder 
    - File system explorer 
    - Other tabs located on the left panel


2. **Python files**
    - Create a new python file  
    - Add the following code to the file 
    
    ```Python
    import numpy as np
    import matplotlib.pyplot as plt
    random_numbers = np.random.rand(100)
    mean_value = np.mean(random_numbers)
    print("Random numbers:", random_numbers)
    print("Mean value:", mean_value)

    # Create a plot
    plt.figure(figsize=(10, 6))
    plt.plot(random_numbers, marker='o', linestyle='-', color='b', label='Random Numbers')
    plt.axhline(y=mean_value, color='r', linestyle='--', label=f'Mean Value: {mean_value:.2f}')
    plt.title('Plot of 100 Random Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

   ```
   - Save the file with this name: `demo-script.py`


3. **Select python interpreter/environment**

    - Click on:
    `
    Manage (cog wheel) -> Command Palette ->  "Python: Select Interpreter" -> {choose desired environment/interpreter}
    `
    - Or with keyboard shortcut 
    `
    Ctrl + shift + P "> "Python: Select Interpreter" -> {choose desired environment/interpreter}
    `

4. **Run python script** 
    - Open a new terminal and run 
    ```
    python demo-script.py
    ```
    - Do we have any alternative to run python code interactively? 


#### Formatting, linting and debugging 

1. **Formatting Python in VS Code**

    - There are lots of formatters in python, that are available in VS Code. We will be using `black` in this workshop.

      `Right click (anywhere in open file) -> Format Document with -> Black Formatter`

    - We will see how this changes `scripts/fizz_buzz.py`

    - If you want to the formatter to be "activated" when saving a file at the workspace level, 
      Select:

      `Command Palette -> Preferences: Open Workspace Settings (JSON)`. 

    - This will open / create `.vscode/settings.json`. This should be edited to:

    ```json
    {
        "[python]": {
          "editor.formatOnSave": true,
          "python.formatting.provider": "ms-python.black-formatter"
        }
    }
    ```
      - See official [documentation](https://code.visualstudio.com/docs/python/formatting) for more details

2. **Linting python in VS Code**

    - Checks code for semantic and stylistic problems.

    - To open tab with list of “problems” press: `Ctrl + shift + M`: 

    - Note: Unlike a formatter, in VS Code, this is by default activated  for *all* python files. Need to manually turn it off if not desired.

3. **Debugging in VS Code**

The basic options are:

1. Continue (F5): 
    - Continue running the code until the next breakpoint, or to the end of the script, or until an error occurs.
2. Step Over (F10): 
    - Run the next line of code, but do not go into functions (see next option)
3. Step Into (F11)
    - Run the next line of code, and go into functions
4. Step out (Shift+F11)
    - Complete the current function (that you have "stepped into")

Run the debugger on a python file (e.g. `scripts/code_debug.py`) and it will continue until there is an error.

Can set a "breakpoint" where you want the code to stop, to inspect objects (called "variables" in the debugger: "locals" and "globals").

We will go over examples of the options above with the `scripts/code_debug.py`

#### Version (source) control in VS Code
1. **Initiate a Git repo**
    - Select a desired directory for the demo 
    - To initialize the repo click on the `Source control` tab and then `Initialize Repository`

2. **Add/commit** 
    - Open a new text file and save it in the same directory 
    - On VS Code Click on the `Source control` tab, add and commit 

3. **Push a local repo to GitHub**
    - Click on `publish Branch`
    - Potentially authenticate your GitHub with VS Code 
    - Approve the creation of the repo on GitHub 
    - Check the result on GitHub 

4. **Clone from a GitHub repo**
    - Close VS Code and delete the directory you made in step 1 
    - On GitHub, go to the repo you made in step 3 and copy the `HTTPS` of the repo
    - on VS Code open another folder to clone the repo into 
    - Press `Ctrl + shift + p` -> type `Git:Clone` -> select `Clone from GitHub`-> paste `the HTTPS of the repo`

5. **Git Graph** 
    - Use Git Graph to keep track of the project's histoy 



#### Jupyter in VS Code

1. **`.ipynb` files**
    - Markdown formatting 
    - Integrated text/code/output 
    - Running chunk by chunk 
    - Updating outputs independently 
    - Generating html or pdf render

2. **Running "cells" in interactive mode**

    - In a standard `.py` file, you can create cells by adding `# %%` at the beginning of a line.
    e.g.
    ```python
    # %%
    x = 5
    y = 3
    print(x + y)
    ```

    - Markdown cells can be defined with `# %% [markdown]` at the beginning of a line.
    e.g.
    ```python
    # %% [markdown]
    """
    Add any desired text (in quotation marks) that you want displayed in the rendered jupyter file
    """
    ```

3. **Some useful shortcuts:**

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

4. **Convert python to jupyter file (minor)**

    - In a python file that has "cells":

      `Right click (anywhere in the file view) -> Export current python file as jupyter notebook`

    - Then, to render the juptyer notebook as an HTML file, do:

    ```bash
    jupyter nbconvert --to html --execute <name of jupyter file>.ipynb
    ```

    - or simply Click on the `...` on top of the notebook and select `Export as html`

5. **Variable view**

    - To replicate the "global environment" window in RStudio, you can use the "Data Wrangler" extension.

    - This lets you inspect a pandas dataframe in a spreadheet view, that can be opened as a separate window.

    - Assuming you have a pandas dataframe in an "interactive window", you will see a new button. 


#### Using your own virtual environments for Jupyter in VS Code
1. Open an empty source folder in VS Code.
2. Download the notebook from <a href="https://github.com/ArashAh/python_workshop/blob/main/scripts/Python_script_jupyter.ipynb" download>this link</a> (Right click --> Save link as...)
3. Copy the downloaded notebook to the source folder and open it in VS Code.
4. **Setup a virtual environment** for the notebook. 
     - Click on "Select Kernel" at the top right.
     - Choose "Python Environments" > "+ Create Python Environment" > "Venv".
     - Select an available Python installation.
     - A new .venv folder will appear in your explorer.
5. **Run the notebook**
     - Click "Run All"
     - If prompted, install the `ipykernel` package.
     - You will see a `ModuleNotFoundError`, open the VS Code terminal and run `pip install matplotlib`
     - Click "Run All" again to execute all cells.


## Production tools - HPC servers <a name="hpc"></a>
We will demonstrate a simple python job submitted with Slurm on the Fox HPC cluster. If you have access to Fox and want to follow along, you can download the scripts needed: 

```
wget https://raw.githubusercontent.com/ArashAh/python_workshop/refs/heads/main/scripts/pandas_plots.py
wget https://raw.githubusercontent.com/ArashAh/python_workshop/refs/heads/main/scripts/run_pandas_plots.slurm
wget https://raw.githubusercontent.com/ArashAh/python_workshop/refs/heads/main/scripts/weather_data.csv
```

For running on other HPC systems you will need to edit the module names and the account name in the run_pandas_plots.slurm script, to match the names for your HPC.  
