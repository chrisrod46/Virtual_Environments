##  Python Virtual Environments

This is an exercise to ensure you have the required software available to work with virtual environments and our selected plotting library [matplotlib](https://matplotlib.org/).

A program named matplotlib_demo.py is provided along with a `requirements.txt` file.

Create a virtual environment given the requirements and verify that the program executes without errors or warnings.

Finally make a small change to the given program (detailed below) and commit your changes back to your repository.

### Creating a Virtual Environment
Create a virtual environment using the command `python3 -m venv env`.

Activate the virtual environment with the command `source env/bin/activate`. This assumes that the directory `env` is in the current working directory when you issue the command.

Activating the virtual environment will change your prompt to include the string `(env)`.

To deactivate or exit the virtual environment, use the command `deactivate`. You will see your prompt return to what it was prior to having the string `(env)` added to it.

## Example Output
The program shall open three additional windows to display plots.
```
$ ./matplotlib_demo.py
Writing out figure to simple_plot.png
Writing out figure to line_demo_dash_control.png
Writing out figure to timeline.png
$
```

