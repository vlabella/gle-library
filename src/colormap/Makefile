all: colormap.eps colormap.pdf colormap.png

colormap.eps: colormap.gle
	gle /device EPS /cairo colormap.gle

colormap.pdf: colormap.gle
	gle /device PDF /cairo colormap.gle

colormap.png: colormap.gle
	gle /device PNG /cairo /DPI 150 colormap.gle

clean:
	-del colormap.eps colormap.pdf colormap.png
	-rmdir /SQ .gle