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

all: utitle.eps utitle.pdf utitle.png

utitle.eps: utitle.gle
	gle -device EPS -cairo  utitle.gle

eps: utitle.eps

utitle.pdf: utitle.gle
	gle -device PDF -cairo  utitle.gle

pdf: utitle.pdf

utitle.png: utitle.gle
	gle -device PNG -cairo -DPI 150 utitle.gle

png: utitle.png

clean:
	-$(RM) utitle.eps utitle.pdf utitle.png
	-$(RMDIR) .gle