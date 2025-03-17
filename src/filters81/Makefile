all: filters81.eps filters81.pdf filters81.png

filters81.eps: filters81.gle
	gle /device EPS /cairo filters81.gle

filters81.pdf: filters81.gle
	gle /device PDF /cairo filters81.gle

filters81.png: filters81.gle
	gle /device PNG /cairo /DPI 150 filters81.gle

clean:
	-del filters81.eps filters81.pdf filters81.png
	-rmdir /SQ .gle