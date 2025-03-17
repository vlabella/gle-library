all: polargrid.eps polargrid.pdf polargrid.png

polargrid.eps: polargrid.gle
	gle /device EPS /cairo polargrid.gle

polargrid.pdf: polargrid.gle
	gle /device PDF /cairo polargrid.gle

polargrid.png: polargrid.gle
	gle /device PNG /cairo /DPI 150 polargrid.gle

clean:
	-del polargrid.eps polargrid.pdf polargrid.png
	-rmdir /SQ .gle