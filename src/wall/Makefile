all: wall.eps wall.pdf wall.png

wall.eps: wall.gle
	gle /device EPS /cairo wall.gle

wall.pdf: wall.gle
	gle /device PDF /cairo wall.gle

wall.png: wall.gle
	gle /device PNG /cairo /DPI 150 wall.gle

clean:
	-del wall.eps wall.pdf wall.png
	-rmdir /SQ .gle