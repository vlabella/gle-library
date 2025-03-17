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

all: arrowdesign.eps arrowdesign.pdf arrowdesign.png

arrowdesign.eps: arrowdesign.gle
	gle -device EPS -cairo arrowdesign.gle

arrowdesign.pdf: arrowdesign.gle
	gle -device PDF -cairo arrowdesign.gle

arrowdesign.png: arrowdesign.gle
	gle -device PNG -cairo -DPI 150 arrowdesign.gle

clean:
	-$(RM) arrowdesign.eps arrowdesign.pdf arrowdesign.png
	-$(RMDIR) .gle