import os
import platform
from re import L

import typer
from cookiecutter.main import cookiecutter

OS = platform.system()

app = typer.Typer()

@app.callback()
def callback():
    """
    DRF scaffold
    """

def get_template_path(template_name):
    script_path = os.path.abspath(__file__)
    module_path = os.path.dirname(script_path)
    project_path = os.path.dirname(module_path)
    cookiecutters_path = os.path.join(project_path, "templates")
    return os.path.join(cookiecutters_path, template_name)
    

def activate_venv():

    parent = os.getcwd()
    os.system("python -m venv env")

    env_activate_script = ""
    if OS == "Windows":
        env_activate_script = "Scripts"


    activate_file = os.path.join(parent, "env", env_activate_script, "activate")
    os.system(f"{activate_file} && pip install -r requirements.txt")

@app.command()
def main(template_name):
    cookiecutter("https://github.com/MohammedBajuaifer/drf-starter-templates.git")

    activate_venv()

