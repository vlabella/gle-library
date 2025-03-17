all: polarcircle.eps polarcircle.pdf polarcircle.png

polarcircle.eps: polarcircle.gle
	gle /device EPS /cairo polarcircle.gle

polarcircle.pdf: polarcircle.gle
	gle /device PDF /cairo polarcircle.gle

polarcircle.png: polarcircle.gle
	gle /device PNG /cairo /DPI 150 polarcircle.gle

clean:
	-del polarcircle.eps polarcircle.pdf polarcircle.png
	-rmdir /SQ .gle