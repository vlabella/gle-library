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

all: maungazoom.eps maungazoom.pdf maungazoom.png

maungazoom.eps: maungazoom.gle
	gle -device EPS -cairo maungazoom.gle

maungazoom.pdf: maungazoom.gle
	gle -device PDF -cairo maungazoom.gle

maungazoom.png: maungazoom.gle
	gle -device PNG -cairo -DPI 150 maungazoom.gle

clean:
	-$(RM) maungazoom.eps maungazoom.pdf maungazoom.png
	-$(RMDIR) .gle