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

all: bayesiannet.eps bayesiannet.pdf bayesiannet.png

bayesiannet.eps: bayesiannet.gle
	gle -device EPS -cairo  bayesiannet.gle

eps: bayesiannet.eps

bayesiannet.pdf: bayesiannet.gle
	gle -device PDF -cairo  bayesiannet.gle

pdf: bayesiannet.pdf

bayesiannet.png: bayesiannet.gle
	gle -device PNG -cairo -DPI 150 bayesiannet.gle

png: bayesiannet.png

clean:
	-$(RM) bayesiannet.eps bayesiannet.pdf bayesiannet.png
	-$(RMDIR) .gle