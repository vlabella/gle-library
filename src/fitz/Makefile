#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# -- automatically generated - do not modify all changes maybe lost
#
# NMAKE code here \
!ifndef 0 # \
MV=move # \
RM=del /Q # \
RMDIR=rmdir /S /Q # \
CP=copy # \
MAKE=nmake /nologo # \
SEP=\ # \
CSEP=& # \
INSTALL_INCLUDES=copy ..\include\*.gle "C:\Program Files\gle-graphics\gleinc" # \
!else
# Make code here
MV=mv -f
RM=rm -f
RMDIR=rm -r
CP=cp -f
MAKE=make
SEP=/
CSEP=;
INSTALL_INCLUDES=sudo cp ../include/*.gle /usr/share/gle-graphics/gleinc
# \
!endif

all: fitz.eps fitz.pdf fitz.png

fitz.eps: fitz.gle
	gle -device EPS -cairo  fitz.gle

eps: fitz.eps

fitz.pdf: fitz.gle
	gle -device PDF -cairo  fitz.gle

pdf: fitz.pdf

fitz.png: fitz.gle
	gle -device PNG -cairo -DPI 150 fitz.gle

png: fitz.png

clean:
	-$(RM) fitz.eps fitz.pdf fitz.png
	-$(RMDIR) .gle