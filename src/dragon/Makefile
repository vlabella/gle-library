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

all: dragon.eps dragon.pdf dragon.png

dragon.eps: dragon.gle
	gle -device EPS -cairo dragon.gle

dragon.pdf: dragon.gle
	gle -device PDF -cairo dragon.gle

dragon.png: dragon.gle
	gle -device PNG -cairo -DPI 150 dragon.gle

clean:
	-$(RM) dragon.eps dragon.pdf dragon.png
	-$(RMDIR) .gle