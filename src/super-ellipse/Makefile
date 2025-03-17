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

all: super-ellipse.eps super-ellipse.pdf super-ellipse.png

super-ellipse.eps: super-ellipse.gle
	gle -device EPS -cairo super-ellipse.gle

super-ellipse.pdf: super-ellipse.gle
	gle -device PDF -cairo super-ellipse.gle

super-ellipse.png: super-ellipse.gle
	gle -device PNG -cairo -DPI 150 super-ellipse.gle

clean:
	-$(RM) super-ellipse.eps super-ellipse.pdf super-ellipse.png
	-$(RMDIR) .gle