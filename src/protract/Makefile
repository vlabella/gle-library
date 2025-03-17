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

all: protract.eps protract.pdf protract.png

protract.eps: protract.gle
	gle -device EPS -cairo protract.gle

protract.pdf: protract.gle
	gle -device PDF -cairo protract.gle

protract.png: protract.gle
	gle -device PNG -cairo -DPI 150 protract.gle

clean:
	-$(RM) protract.eps protract.pdf protract.png
	-$(RMDIR) .gle