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
# !endif

all: entropy.eps entropy.pdf entropy.png

entropy.eps: entropy.gle
	gle -device EPS -cairo entropy.gle

entropy.pdf: entropy.gle
	gle -device PDF -cairo entropy.gle

entropy.png: entropy.gle
	gle -device PNG -cairo -DPI 150 entropy.gle

clean:
	-$(RM) entropy.eps entropy.pdf entropy.png
	-$(RMDIR) .gle