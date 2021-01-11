from cx_Freeze import setup, Executable

setup(
    name="LabyrintheAuto",
    version="1.0",
    description="génération de labyrinthe aléatoire de taille variable",
    executables=[Executable("Main.py")],
    options={'build_exe': {'include_files': ["Labyrinthe.py", "Case.py", "Traducteur.py", "CONST.py", "Pathfinder.py"]}},
)
