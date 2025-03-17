all: lines.eps lines.pdf lines.png

lines.eps: lines.gle
	gle /device EPS /cairo lines.gle

lines.pdf: lines.gle
	gle /device PDF /cairo lines.gle

lines.png: lines.gle
	gle /device PNG /cairo /DPI 150 lines.gle

clean:
	-del lines.eps lines.pdf lines.png
	-rmdir /SQ .gle