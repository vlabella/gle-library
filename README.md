# gle-library

GLE Library - Library of example figures and include files for [GLE](http://glx.sourceforge.io).  The example figures are displayed in a categorized list on the website [here](https://glx.sourceforge.io/examples/). The include files come bundled with the GLE distribution and displayed on the website [here](https://glx.sourceforge.io/library/).  

This repository makes both the examples and include files available for users to modify and/or update outside of the GLE release schedule.  Instructions for contributing examples and include files are below. 

## Installation Instructions

Installation of include files is only needed if they get updated prior to the next release of GLE. The installation command below copies all the .gle files from /include to the /gleinc folder at the root of your GLE installation:

* windows: `C:\Program Files\GLE\gleinc`.
* Linux: `/usr/share/gle/gleinc`.

To install the new include files

 * Windows: `cd src & nmake install-includes`
 * Linux & macOS `cd src ; make install-includes`

## Using Include Files in GLE Figures

The include folder contains several user contributed include files of custom routines.  They can be included individually in GLE scripts.  In addition, a file `gle-include.gle` can be included that includes all the include files in the library.

## Building all figures

To build all the figures from the source code

* Windows: `cd src & nmake`
* Linux & macOS `cd src ; make`

To clean the build, i.e. delete all the files created during the build

* Windows: `cd src & nmake clean`
* Linux & macOS `cd src ; make clean`

## Contributing Figures

Contributions of figures and include files are always appreciated. The contributed files will have the same license as this repository.  By submitting your files to this repository you accept the license of this repository.

To contribute figures to the library:

1. Create a fork of the repository.

2. Create a folder in the `src` folder with a unique name, preferably the same name as the figure.  Each figure must be in its own folder.  For multiple figures create unique folders for each one.

3. Put all the files needed to create the figure in that folder.  Do not put any of the GLE output files such as PNG, EPS etc.  Just put the source files that GLE needs to create the figure.

4. If the GLE figure uses an include file that that maybe useful to others place it in the `include` folder, otherwise place it in the same folder as the figure.

5. Create a `config.yaml` file in the same folder as the figure with the following content. Replace the `<>` with the requested information. Optional information should be left blank if not used.

```yaml
author: <optional authors name>
author_email: <optional authors email>
cairo: <true or false>
category: <id of category see scripts/categories.yaml>
description: <optional description of figure>
filename: <gle filename>
name: <name of the figure>
notes: <optional notes about the figure>
```

6. Add and commit everything and then submit a pull request to the main branch.

7. Once the pull request is accepted the new figure will appear on the site.  It may take a few days as this has to be done manually by the maintainer.

## Contributing Include Files

Place new include files that others may find useful in the `include` folder.  Submit a pull request.  They will appear on the site and in the next release of GLE.

## Generating the Makefile

The Makefiles are automatically generated upon any git push or pull.  So there is no need to regenerate it prior to submitting a pull request.  The python script that does this is `scripts/gen_makefiles.py`.  It can be run to regenerate the Makefiles on your local machine if desired. The command is:

```
cd scripts
python gen_makefile.py
```

## Generating the Global Include File `gle-library.gle`

The global include file `gle-library.gle` is automatically generated upon any git push or pull.  So there is no need to regenerate it prior to submitting a pull request.  The python script that does this is `scripts/gen_include.py`.  It can be run to regenerate the global include file on your local machine if desired. The command is:

```
cd scripts
python gen_include.py
```

## Adding Categories

Consult the `scripts/categories.yaml` file for the list of categories.  These mirror the ones on the GLE website.  Add new category with the following information
and submit a pull request if desired.

```yaml
- id: <unique_one_word_id>
  name:        <name to appear on the site
  order:       <number indicating order on website>
  description: <description of category for website>
```