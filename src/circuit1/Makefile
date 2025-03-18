#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# automatically generated - do not modify all changes maybe lost
#
# NMAKE code here \
!ifndef 0 # \
MV=move # \
RM=del # \
RMDIR=rmdir /S /Q # \
CP=copy # \
MAKE=nmake /nologo # \
SEP=\ # \
CSEP=& # \
INSTALL_INCLUDES=copy ..\include\*.gle "C:\Program Files\gle\gleinc" # \
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
# !endif

all: circuit1.eps circuit1.pdf circuit1.png

circuit1.eps: circuit1.gle
	gle -device EPS -cairo circuit1.gle

circuit1.pdf: circuit1.gle
	gle -device PDF -cairo circuit1.gle

circuit1.png: circuit1.gle
	gle -device PNG -cairo -DPI 150 circuit1.gle

clean:
	-$(RM) circuit1.eps circuit1.pdf circuit1.png
	-$(RMDIR) .gle