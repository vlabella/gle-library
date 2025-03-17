all: color_sample.eps color_sample.pdf color_sample.png

color_sample.eps: color_sample.gle
	gle /device EPS /cairo color_sample.gle

color_sample.pdf: color_sample.gle
	gle /device PDF /cairo color_sample.gle

color_sample.png: color_sample.gle
	gle /device PNG /cairo /DPI 150 color_sample.gle

clean:
	-del color_sample.eps color_sample.pdf color_sample.png
	-rmdir /SQ .gle