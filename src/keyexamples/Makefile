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

all: keyexamples.eps keyexamples.pdf keyexamples.png

keyexamples.eps: keyexamples.gle
	gle -device EPS -cairo keyexamples.gle

keyexamples.pdf: keyexamples.gle
	gle -device PDF -cairo keyexamples.gle

keyexamples.png: keyexamples.gle
	gle -device PNG -cairo -DPI 150 keyexamples.gle

clean:
	-$(RM) keyexamples.eps keyexamples.pdf keyexamples.png
	-$(RMDIR) .gle