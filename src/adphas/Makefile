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

all: adphas.eps adphas.pdf adphas.png

adphas.eps: adphas.gle
	gle -device EPS -cairo adphas.gle

adphas.pdf: adphas.gle
	gle -device PDF -cairo adphas.gle

adphas.png: adphas.gle
	gle -device PNG -cairo -DPI 150 adphas.gle

clean:
	-$(RM) adphas.eps adphas.pdf adphas.png
	-$(RMDIR) .gle