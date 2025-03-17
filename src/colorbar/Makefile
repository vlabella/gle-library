all: colorbar.eps colorbar.pdf colorbar.png

colorbar.eps: colorbar.gle
	gle /device EPS /cairo colorbar.gle

colorbar.pdf: colorbar.gle
	gle /device PDF /cairo colorbar.gle

colorbar.png: colorbar.gle
	gle /device PNG /cairo /DPI 150 colorbar.gle

clean:
	-del colorbar.eps colorbar.pdf colorbar.png
	-rmdir /SQ .gle