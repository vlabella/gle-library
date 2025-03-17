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

all: flux_linkage_space_vector_diagram.eps flux_linkage_space_vector_diagram.pdf flux_linkage_space_vector_diagram.png

flux_linkage_space_vector_diagram.eps: flux_linkage_space_vector_diagram.gle
	gle -device EPS -cairo flux_linkage_space_vector_diagram.gle

flux_linkage_space_vector_diagram.pdf: flux_linkage_space_vector_diagram.gle
	gle -device PDF -cairo flux_linkage_space_vector_diagram.gle

flux_linkage_space_vector_diagram.png: flux_linkage_space_vector_diagram.gle
	gle -device PNG -cairo -DPI 150 flux_linkage_space_vector_diagram.gle

clean:
	-$(RM) flux_linkage_space_vector_diagram.eps flux_linkage_space_vector_diagram.pdf flux_linkage_space_vector_diagram.png
	-$(RMDIR) .gle