all: shapes.eps shapes.pdf shapes.png

shapes.eps: shapes.gle
	gle /device EPS /cairo shapes.gle

shapes.pdf: shapes.gle
	gle /device PDF /cairo shapes.gle

shapes.png: shapes.gle
	gle /device PNG /cairo /DPI 150 shapes.gle

clean:
	-del shapes.eps shapes.pdf shapes.png
	-rmdir /SQ .gle