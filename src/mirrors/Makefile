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

all: mirrors.eps mirrors.pdf mirrors.png

mirrors.eps: mirrors.gle
	gle -device EPS -cairo mirrors.gle

mirrors.pdf: mirrors.gle
	gle -device PDF -cairo mirrors.gle

mirrors.png: mirrors.gle
	gle -device PNG -cairo -DPI 150 mirrors.gle

clean:
	-$(RM) mirrors.eps mirrors.pdf mirrors.png
	-$(RMDIR) .gle