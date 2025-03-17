all: colormapcontour.eps colormapcontour.pdf colormapcontour.png

colormapcontour.eps: colormapcontour.gle
	gle /device EPS /cairo colormapcontour.gle

colormapcontour.pdf: colormapcontour.gle
	gle /device PDF /cairo colormapcontour.gle

colormapcontour.png: colormapcontour.gle
	gle /device PNG /cairo /DPI 150 colormapcontour.gle

clean:
	-del colormapcontour.eps colormapcontour.pdf colormapcontour.png
	-rmdir /SQ .gle