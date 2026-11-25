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

all: protract.eps protract.pdf protract.png

protract.eps: protract.gle
	gle -device EPS -cairo  protract.gle

eps: protract.eps

protract.pdf: protract.gle
	gle -device PDF -cairo  protract.gle

pdf: protract.pdf

protract.png: protract.gle
	gle -device PNG -cairo -DPI 150 protract.gle

png: protract.png

clean:
	-$(RM) protract.eps protract.pdf protract.png
	-$(RMDIR) .gle