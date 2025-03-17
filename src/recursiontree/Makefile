all: recursiontree.eps recursiontree.pdf recursiontree.png

recursiontree.eps: recursiontree.gle
	gle /device EPS /cairo recursiontree.gle

recursiontree.pdf: recursiontree.gle
	gle /device PDF /cairo recursiontree.gle

recursiontree.png: recursiontree.gle
	gle /device PNG /cairo /DPI 150 recursiontree.gle

clean:
	-del recursiontree.eps recursiontree.pdf recursiontree.png
	-rmdir /SQ .gle