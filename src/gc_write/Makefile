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

all: gc_write.eps gc_write.pdf gc_write.png

gc_write.eps: gc_write.gle
	gle -device EPS -cairo gc_write.gle

gc_write.pdf: gc_write.gle
	gle -device PDF -cairo gc_write.gle

gc_write.png: gc_write.gle
	gle -device PNG -cairo -DPI 150 gc_write.gle

clean:
	-$(RM) gc_write.eps gc_write.pdf gc_write.png
	-$(RMDIR) .gle