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

all: playtennis_dt.eps playtennis_dt.pdf playtennis_dt.png

playtennis_dt.eps: playtennis_dt.gle
	gle -device EPS -cairo playtennis_dt.gle

playtennis_dt.pdf: playtennis_dt.gle
	gle -device PDF -cairo playtennis_dt.gle

playtennis_dt.png: playtennis_dt.gle
	gle -device PNG -cairo -DPI 150 playtennis_dt.gle

clean:
	-$(RM) playtennis_dt.eps playtennis_dt.pdf playtennis_dt.png
	-$(RMDIR) .gle