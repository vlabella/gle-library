all: bitmap.eps bitmap.pdf bitmap.png

bitmap.eps: bitmap.gle
	gle /device EPS /cairo bitmap.gle

bitmap.pdf: bitmap.gle
	gle /device PDF /cairo bitmap.gle

bitmap.png: bitmap.gle
	gle /device PNG /cairo /DPI 150 bitmap.gle

clean:
	-del bitmap.eps bitmap.pdf bitmap.png
	-rmdir /SQ .gle