all: entropy.eps entropy.pdf entropy.png

entropy.eps: entropy.gle
	gle /device EPS /cairo entropy.gle

entropy.pdf: entropy.gle
	gle /device PDF /cairo entropy.gle

entropy.png: entropy.gle
	gle /device PNG /cairo /DPI 150 entropy.gle

clean:
	-del entropy.eps entropy.pdf entropy.png
	-rmdir /SQ .gle