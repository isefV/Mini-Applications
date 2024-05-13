import os
import pathlib
import patoolib

# os.system(f'cd C:\\Program Files\\WinRAR')
dir_path = f"{pathlib.Path().resolve()}"

for folder in pathlib.Path(dir_path).iterdir():
    patoolib.create_archive(f"{dir_path}{folder.name}.rar",(f".\\Mangas\\{folder.name}",))
