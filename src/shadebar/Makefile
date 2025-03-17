all: shadebar.eps shadebar.pdf shadebar.png

shadebar.eps: shadebar.gle
	gle /device EPS /cairo shadebar.gle

shadebar.pdf: shadebar.gle
	gle /device PDF /cairo shadebar.gle

shadebar.png: shadebar.gle
	gle /device PNG /cairo /DPI 150 shadebar.gle

clean:
	-del shadebar.eps shadebar.pdf shadebar.png
	-rmdir /SQ .gle