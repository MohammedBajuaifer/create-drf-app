import os
import platform
import pathlib

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
    current_dir_path = os.path.dirname(script_path)
    templates_path = os.path.join(current_dir_path, "templates")
    return os.path.join(templates_path, template_name)
    

def activate_venv(path):

    # set current directory
    os.chdir(path)
    print("🔨 setting up your virutal environment")
    os.system("python -m venv venv")
    os.getcwd()

    env_activate_script = ""
    if OS == "Windows":
        env_activate_script = "Scripts"

    activate_file = os.path.join(path, "venv", env_activate_script, "activate")
    print("🔨 downloading packages")
    os.system(f"{activate_file} && pip install -r requirements.txt")


@app.command("")
def start(template_name):
    template_path = get_template_path(template_name)
    path = cookiecutter(template_path)

    activate_venv(path)
    print("🎉🎉 your DRF project is ready! 🚀🚀")
    folder_name = pathlib.PurePath(path)
    
    if OS == "Windows":
        activate_file = os.path.join("venv", "Scripts", "activate")
        

    print("\nTo start the project run the following commands:\n")
    print(f"cd {folder_name.name}; {activate_file}\n")
    print("python manage.py makemigrations")
    print("python manage.py migrate")
    print("python manage.py runserver")