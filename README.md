# Getting up-to-speed with Python: Workshop Materials

## Package and environment management with pip and venv

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

   ```bash
   mkdir my_project
   cd my_project
   ```

2. **Create a virtual environment:**
The following command creates an isolated Python environment in the "my_venv" directory.
   ```bash
   python3 -m venv my_venv
    ```

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
1. **Installing a package inside your environment:**
   ```bash
   pip install scipy
    ```
2. **Verify the installation:**
   ```bash
   pip list
    ```
3. **Compare with global python environment:**

    Deactivate your virtual environment
   ```bash
   deactivate
   ```
   
    List packages in the global environment
   ```bash
   pip list
   ```
   
4. **Reactivate your virtual environment:**

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

   
5. **Upgrading pip inside the environment:**
   ```bash
   pip install --upgrade pip
   ```
6. **Creating a requirements file:**
   ```bash
   pip freeze > requirements.txt
   ```
   
7. **Recreate your environment somewhere else:**

<table>
  <tr>
    <td>
      <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Badge">
    </td>
    <td>
      <pre>
      <code>
python -m venv new_venv
.\new_venv\Scripts\activate
pip install -r requirements.txt
      </code>
      </pre>
    </td>
  </tr>
</table>
   
<table>
  <tr>
    <td>
      <img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0" alt="macOS Badge">
      <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux Badge">
    </td>
    <td>
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
Deactivate your environment

   ```bash
   deactivate 
   ```

Delete your environment 

| ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) | ```rmdir /s /q new_venv ``` |
|---------------------------------------------------------------------------------------------------------|-----------------------------|

| ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)  | ```rm -rf new_venv ``` |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|


## Package and envirnoment management with conda 

## Package and environment management with poetry 

## VS Code

## Production tools - HPC servers