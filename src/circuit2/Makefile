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
!endif

install-includes:
	$(INSTALL_INCLUDES)

all: circuit2.eps circuit2.pdf circuit2.png

circuit2.eps: circuit2.gle
	gle -device EPS -cairo circuit2.gle

circuit2.pdf: circuit2.gle
	gle -device PDF -cairo circuit2.gle

circuit2.png: circuit2.gle
	gle -device PNG -cairo -DPI 150 circuit2.gle

clean:
	-$(RM) circuit2.eps circuit2.pdf circuit2.png
	-$(RMDIR) .gle