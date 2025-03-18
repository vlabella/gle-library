# gle-library

GLE Library - Library of example figures and include files for [GLE](http://glx.sourceforge.io).  The example figures are displayed in a categorized list on the website [here](https://glx.sourceforge.io/examples/).

The include files come bundled with the GLE distribution and displayed on the website [here](https://glx.sourceforge.io/library/).  This repository makes both the examples and include files available for users to modify and/or update outside of the GLE release schedule.  Instructions for contributing examples and include files are below. 

## Installation Instructions

Installation of include files is only needed if they get updated prior to the next release of GLE. The installation command below copies all the .gle files from /include to the /gleinc folder at the root of your GLE installation:

* windows: `C:\Program Files\GLE\gleinc`.
* Linux: `/usr/share/gle/gleinc`.

To install the new include files

 `cd src`
 `make install-includes` or `nmake install-includes`

## Building all figures

To build all the figures from the source code

  `cd src`
  `make` or `nmake`

To clean the build

  `cd src`
  `make clean` or `nmake clean`

## Contributing Figures

To contribute figures to the library:

1. Clone the repository.

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

6. Regenerate the Makefile. See instructions below

7. Add and commit everything and then submit a pull request.

8. Once the pull request is accepted the new figure will appear on the site.  It may take a few days as this has to be done manually by the maintainer.

## Contributing Include Files

Place new include files that others may find useful in the `include` folder.  Submit a pull request.  They will appear on the site and in the next release of GLE.

## Generating the Makefile

The Makefile will need to be regenerated if new figures are added. To generate the Makefile run

```
cd scripts
python gen_makefile.pl
```

## Adding categories

Consult the `scripts/categories.yaml` file for hte list of categories.  These mirror the ones on the GLE website.  Add new category and submit a pull request if desired.