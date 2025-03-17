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

all: polenja.eps polenja.pdf polenja.png

polenja.eps: polenja.gle
	gle -device EPS -cairo polenja.gle

polenja.pdf: polenja.gle
	gle -device PDF -cairo polenja.gle

polenja.png: polenja.gle
	gle -device PNG -cairo -DPI 150 polenja.gle

clean:
	-$(RM) polenja.eps polenja.pdf polenja.png
	-$(RMDIR) .gle