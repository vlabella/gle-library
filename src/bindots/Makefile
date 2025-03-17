all: bindots.eps bindots.pdf bindots.png

bindots.eps: bindots.gle
	gle /device EPS /cairo bindots.gle

bindots.pdf: bindots.gle
	gle /device PDF /cairo bindots.gle

bindots.png: bindots.gle
	gle /device PNG /cairo /DPI 150 bindots.gle

clean:
	-del bindots.eps bindots.pdf bindots.png
	-rmdir /SQ .gle