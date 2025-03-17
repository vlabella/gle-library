all: color-markers-3d.eps color-markers-3d.pdf color-markers-3d.png

color-markers-3d.eps: color-markers-3d.gle
	gle /device EPS /cairo color-markers-3d.gle

color-markers-3d.pdf: color-markers-3d.gle
	gle /device PDF /cairo color-markers-3d.gle

color-markers-3d.png: color-markers-3d.gle
	gle /device PNG /cairo /DPI 150 color-markers-3d.gle

clean:
	-del color-markers-3d.eps color-markers-3d.pdf color-markers-3d.png
	-rmdir /SQ .gle