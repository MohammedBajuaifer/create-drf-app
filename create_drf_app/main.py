import typer


app = typer.Typer()

@app.callback()
def callback():
    """
    DRF scaffold
    """

@app.command()
def main(name):
    # clone repo
    # activate virtaulenv
    # download requirements
    ...
