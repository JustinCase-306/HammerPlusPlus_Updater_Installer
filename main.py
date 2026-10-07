import os
import shutil
from pathlib import Path
import zipfile
from colorama import init, Fore

init(autoreset=True)

# files to delete, input folder path
bin_delete = ["hammerplusplus.exe", "hlmvplusplus.dll", "hlmvplusplus.exe"]
bin_folder = Path(input(Fore.LIGHTYELLOW_EX + "Please paste your Portal 2's bin folder path here: ").strip('"'))

print(Fore.LIGHTYELLOW_EX + "Cleaning up old files...")

# clean old files
for file in bin_delete:
    full_path = bin_folder / file
    if full_path.exists():
        full_path.unlink()
        print(Fore.LIGHTYELLOW_EX + "\nFile deleted: " + file)
    else:
        print(Fore.LIGHTRED_EX + "\nError: File not found or invalid path: " + file)


print(Fore.LIGHTYELLOW_EX + "\nSuccessfully cleaned up old files. Continue...")

# zip file path
zip_file = Path(input(Fore.LIGHTYELLOW_EX + "\nPlease paste your hammerplusplus_portal2_build[...] .zip path here: ").strip('"'))

# extract zip file
with zipfile.ZipFile(zip_file, "r") as zip_archive:
    zip_archive.extractall(bin_folder)
    build = zip_archive.namelist()[0]
    print(Fore.LIGHTYELLOW_EX + "\nSuccessfully extracted zip file in bin folder: " + str(zip_file))

# move all files to the bin folder
hammer_build = Path(build).parts[0]
hammer_bin_folder = bin_folder / hammer_build / hammer_build / "bin"

for file in hammer_bin_folder.iterdir():
    if file.is_file():
        shutil.move(file, bin_folder)
    elif file.is_dir():
        if not (bin_folder / file.name).exists():
            shutil.move(file, bin_folder)
        else: print(Fore.LIGHTRED_EX + "\nError: hammerplusplus already exists. Continue...")
    else:
        print(Fore.LIGHTRED_EX + "\nError: please check your .zip archive or try re-downloading it.")


print(Fore.LIGHTYELLOW_EX + "\nSuccessfully moved files.")



