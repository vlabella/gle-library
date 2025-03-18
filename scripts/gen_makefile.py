#
# -- gen_makefile.py - generates a makefile for the gle-library to build all the samples in the src folder
#
# must run in scripts folder
# creates Makefile in ../src folder
# creates Makefile for each image in ../src folder
# these makefiles gets shipped with distribution so only needed when
# new figures have been added to the library
#
import os
import platform
from enum import Enum
import pathlib
import glob
from datetime import datetime
import yaml

config_filename   = "config.yaml"
makefile_filename = "Makefile"
png_dpi           = 150
formats           = {'EPS':'eps','PDF':'pdf','PNG':'png'}

#
# -- makefile preamble for platform independance
#
preamble="""#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# automatically generated - do not modify all changes maybe lost
#
# NMAKE code here \\
!ifndef 0 # \\
MV=move # \\
RM=del # \\
RMDIR=rmdir /S /Q # \\
CP=copy # \\
MAKE=nmake /nologo # \\
SEP=\\ # \\
CSEP=& # \\
INSTALL_INCLUDES=copy ..\\include\\*.gle "C:\\Program Files\\gle\\gleinc" # \\
!else
# Make code here
MV=mv -f
RM=rm -f
RMDIR=rm -r
CP=cp -f
MAKE=make
SEP=/
CSEP=;
INSTALL_INCLUDES=sudo cp ../include/*.gle /usr/share/gle/gleinc
# \
!endif

install-includes:
\t$(INSTALL_INCLUDES)

"""

class OS(Enum):
    WINDOWS = 1
    MACOS = 2
    LINUX = 3

this_os = OS.LINUX
os_type = platform.system()
if os_type == "Windows":
    this_os = OS.WINDOWS
elif os_type == "Linux":
    this_os = OS.LINUX
elif os_type == "Darwin":
    this_os = OS.MACOS
else:
    print(f"Unknown operating system: {os_type} - assuming Linux")

def load_yaml_to_dict(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
       print(f"Error while loading YAML file: {e}")
    except IOError as e:
       print(f"Unable to open file. {e}")

def my_walk(top, topdown=True, onerror=None, followlinks=False, maxdepth=None):
    # adds max depth parameter
    islink, join, isdir = os.path.islink, os.path.join, os.path.isdir
    try:
        names = os.listdir(top)
    except(OSError, err):
        if onerror is not None:
            onerror(err)
        return

    dirs, nondirs = [], []
    for name in names:
        if isdir(join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    if topdown:
        yield top, dirs, nondirs

    if maxdepth is None or maxdepth > 1:
        for name in dirs:
            new_path = join(top, name)
            if followlinks or not islink(new_path):
                for x in walk(new_path, topdown, onerror, followlinks, None if maxdepth is None else maxdepth-1):
                    yield x
    if not topdown:
        yield top, dirs, nondirs

def generate_makefile(root_dir,dpi,formats):
    root_makefile_content = []
    num_makefiles         = 0
    figures               = []
    for subdir, dirs, files in my_walk(root_dir,maxdepth=1):
        for dir_name in dirs:
            makefile_content = []
            config = load_yaml_to_dict(os.path.join(subdir,dir_name,config_filename))
            gle_file = config['filename']
            figures.append(dir_name)
            base_name = os.path.splitext(gle_file)[0]
            targets = {}
            target_files = []

            for device, ext in formats.items():
                item = {}
                item['target'] = f"{base_name}.{ext}"
                target_files.append(item['target'])
                item['device'] = device
                item['options'] = f"-cairo -DPI {dpi}" if device == "PNG" else "-cairo"
                targets[device] = item

            makefile_content.append(f"all: {' '.join(target_files)}")
            makefile_content.append(f"")
            for device, item in targets.items():
                makefile_content.append(f"{item['target']}: {gle_file}")
                makefile_content.append(f"\tgle -device {item['device']} {item['options']} {gle_file}")
                makefile_content.append(f"")
            makefile_content.append(f"clean:")
            makefile_content.append(f"\t-$(RM) {' '.join(target_files)}")
            makefile_content.append(f"\t-$(RMDIR) .gle")
            num_makefiles += 1
            with open(os.path.join(subdir,dir_name,makefile_filename), "w") as f:
                f.write(preamble)
                f.write("\n".join(makefile_content))

    print(f"{num_makefiles} Makefiles generated successfully.")
    return figures

figs = generate_makefile(os.path.join("..","src"),png_dpi,formats)
# make global makefile

makefile_content = []

makefile_content.append(f"all:")
for fig in figs:
    makefile_content.append(f"\tcd {fig} $(CSEP) $(MAKE)")
makefile_content.append(f"")
makefile_content.append(f"clean:")
for fig in figs:
    makefile_content.append(f"\tcd {fig} $(CSEP) $(MAKE) clean")

with open(os.path.join("..","src",makefile_filename), "w") as f:
    f.write(preamble)
    f.write("\n".join(makefile_content))

