#
# gle-library makefile runs on MS nmake.exe or GNU make
#
# -- automatically generated - do not modify all changes maybe lost
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

all: jitter.eps jitter.pdf jitter.png

jitter.eps: jitter.gle
	gle -device EPS -cairo jitter.gle

jitter.pdf: jitter.gle
	gle -device PDF -cairo jitter.gle

jitter.png: jitter.gle
	gle -device PNG -cairo -DPI 150 jitter.gle

clean:
	-$(RM) jitter.eps jitter.pdf jitter.png
	-$(RMDIR) .gle