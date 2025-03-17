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

all: circuit4.eps circuit4.pdf circuit4.png

circuit4.eps: circuit4.gle
	gle -device EPS -cairo circuit4.gle

circuit4.pdf: circuit4.gle
	gle -device PDF -cairo circuit4.gle

circuit4.png: circuit4.gle
	gle -device PNG -cairo -DPI 150 circuit4.gle

clean:
	-$(RM) circuit4.eps circuit4.pdf circuit4.png
	-$(RMDIR) .gle