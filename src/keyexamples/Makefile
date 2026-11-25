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

all: keyexamples.eps keyexamples.pdf keyexamples.png

keyexamples.eps: keyexamples.gle
	gle -device EPS  keyexamples.gle

eps: keyexamples.eps

keyexamples.pdf: keyexamples.gle
	gle -device PDF  keyexamples.gle

pdf: keyexamples.pdf

keyexamples.png: keyexamples.gle
	gle -device PNG -DPI 150 keyexamples.gle

png: keyexamples.png

clean:
	-$(RM) keyexamples.eps keyexamples.pdf keyexamples.png
	-$(RMDIR) .gle