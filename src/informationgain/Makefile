all: informationgain.eps informationgain.pdf informationgain.png

informationgain.eps: informationgain.gle
	gle /device EPS /cairo informationgain.gle

informationgain.pdf: informationgain.gle
	gle /device PDF /cairo informationgain.gle

informationgain.png: informationgain.gle
	gle /device PNG /cairo /DPI 150 informationgain.gle

clean:
	-del informationgain.eps informationgain.pdf informationgain.png
	-rmdir /SQ .gle