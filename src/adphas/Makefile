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

all: adphas.eps adphas.pdf adphas.png

adphas.eps: adphas.gle
	gle -device EPS -cairo  adphas.gle

eps: adphas.eps

adphas.pdf: adphas.gle
	gle -device PDF -cairo  adphas.gle

pdf: adphas.pdf

adphas.png: adphas.gle
	gle -device PNG -cairo -DPI 150 adphas.gle

png: adphas.png

clean:
	-$(RM) adphas.eps adphas.pdf adphas.png
	-$(RMDIR) .gle