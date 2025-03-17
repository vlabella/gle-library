all: sarppepo.eps sarppepo.pdf sarppepo.png

sarppepo.eps: sarppepo.gle
	gle /device EPS /cairo sarppepo.gle

sarppepo.pdf: sarppepo.gle
	gle /device PDF /cairo sarppepo.gle

sarppepo.png: sarppepo.gle
	gle /device PNG /cairo /DPI 150 sarppepo.gle

clean:
	-del sarppepo.eps sarppepo.pdf sarppepo.png
	-rmdir /SQ .gle