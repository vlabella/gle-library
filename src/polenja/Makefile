all: polenja.eps polenja.pdf polenja.png

polenja.eps: polenja.gle
	gle /device EPS /cairo polenja.gle

polenja.pdf: polenja.gle
	gle /device PDF /cairo polenja.gle

polenja.png: polenja.gle
	gle /device PNG /cairo /DPI 150 polenja.gle

clean:
	-del polenja.eps polenja.pdf polenja.png
	-rmdir /SQ .gle