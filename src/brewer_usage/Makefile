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

all: brewerusage.eps brewerusage.pdf brewerusage.png

brewerusage.eps: brewerusage.gle
	gle -device EPS  brewerusage.gle

eps: brewerusage.eps

brewerusage.pdf: brewerusage.gle
	gle -device PDF  brewerusage.gle

pdf: brewerusage.pdf

brewerusage.png: brewerusage.gle
	gle -device PNG -DPI 150 brewerusage.gle

png: brewerusage.png

clean:
	-$(RM) brewerusage.eps brewerusage.pdf brewerusage.png
	-$(RMDIR) .gle