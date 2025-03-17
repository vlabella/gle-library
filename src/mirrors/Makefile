all: mirrors.eps mirrors.pdf mirrors.png

mirrors.eps: mirrors.gle
	gle /device EPS /cairo mirrors.gle

mirrors.pdf: mirrors.gle
	gle /device PDF /cairo mirrors.gle

mirrors.png: mirrors.gle
	gle /device PNG /cairo /DPI 150 mirrors.gle

clean:
	-del mirrors.eps mirrors.pdf mirrors.png
	-rmdir /SQ .gle