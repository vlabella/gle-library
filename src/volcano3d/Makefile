all: volcano3d.eps volcano3d.pdf volcano3d.png

volcano3d.eps: volcano3d.gle
	gle /device EPS /cairo volcano3d.gle

volcano3d.pdf: volcano3d.gle
	gle /device PDF /cairo volcano3d.gle

volcano3d.png: volcano3d.gle
	gle /device PNG /cairo /DPI 150 volcano3d.gle

clean:
	-del volcano3d.eps volcano3d.pdf volcano3d.png
	-rmdir /SQ .gle