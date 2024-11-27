# Getting up-to-speed with Python: Workshop Materials

- [Package and environment management with pip and venv](#environment)
- [Package and environment management with conda](#conda)
- [Package and environment management with poetry](#poetry)
- [VS Code](#vscode)
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

## Package and environment management with poetry <a name="poetry"></a>

Poetry requires python 3.8 or higher. For the final demonstration of this part of the workshop, python 3.10 (or higher) is required (optional).

Once you have the right python version, it is recommended to install poetry using `pipx`.

See [here](https://pipx.pypa.io/stable/installation/) on how to install `pipx`.

Once `pipx` is installed, see [here](https://python-poetry.org/docs/#installing-with-pipx) on how to use it to install `poetry`

## VS Code <a name="vscode"></a>

### Extensions

- [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [Juptyer](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
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

## Production tools - HPC servers <a name="hpc"></a>