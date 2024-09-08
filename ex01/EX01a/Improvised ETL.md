# Improvised ETL

## Description

This program converts a leaked JSON file that contains personal information into a CSV format required by a government service to help block compromised credit cards. The JSON data contains personal information, and the goal is to extract only the `name` and `creditcard` fields, where credit card numbers are not null or empty. The service requires a CSV file with exactly two columns: `name` and `creditcard`. The generated file will be named according to the date it was created, following the format `YYYYMMDD.csv`.

## Solution

### Executables

Executables for both Linux and Windows are provided to make running the program straightforward on either platform. These executables were created using **PyInstaller**, which converts Python scripts into standalone executables. PyInstaller was run in Windows to create the Windows executable (`improvisedETL.exe`) and in Rocky Linux (the VM provided by RLES) to create the Linux executable (`improvisedETL`). The `tkinter` module was required to be included to create a standalone executable.

### Script

The source code will be included in the repository, allowing you to see how the conversion from JSON to CSV is performed. You can run the script directly in Python if you prefer, without using the provided executables. This method requires Python to be installed on your system. Ensure to have all necessary dependencies, such as `tkinter` for Linux users.

## Prerequisites

* **Linux**
  - Ensure the `tkinter` module is installed.
    ```bash
    pip install tk
    ```

* **Windows**
  - You may need to set up a virtual environment (venv) to run the Python script properly.

## Running the Executables

1. **Get the appropriate executable**
   - `improvisedETL`: For Linux systems.
   - `improvisedETL.exe`: For Windows systems.

2. **Place the executable** in the same directory as the `data.json` file containing the leaked data.

3. **Run the executable**.

4. The program will generate a CSV file in the same directory as `data.json` with the name formatted as `YYYYMMDD.csv`, where `YYYYMMDD` is the date the program runs.

## Running the Script

In case you need to modify and execute the script directly, make sure the file has the right permissions and proceed to execute it.

* **Linux**
  1. Change executable permissions:
     ```bash
     chmod +x improvisedETL.py
     ```
  2. Run the script:
     ```bash
     ./improvisedETL.py
     ```

* **Windows**
  1. If necessary, set up a virtual environment ([Python venv documentation](https://docs.python.org/3/library/venv.html)).
  2. Run the script using `python`, or the command you use to run Python on your machine:
     ```bash
     python improvisedETL.py
     ```

## Notes on PyInstaller

1. **Install PyInstaller module**
   ```bash
   pip install pyinstaller
   ```
2. **Create asingle executable**
   ```bash
   pyinstaller --onefile improvisedETL.py
   ```
3. **The executable will usually be placed in the `dist` folder**
   ```bash
   cd ./build
   ```
4.	Check [PyInstaller](https://pyinstaller.org/en/stable/installation.html) to get more documentation


