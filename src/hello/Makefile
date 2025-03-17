all: hello.eps hello.pdf hello.png

hello.eps: hello.gle
	gle /device EPS /cairo hello.gle

hello.pdf: hello.gle
	gle /device PDF /cairo hello.gle

hello.png: hello.gle
	gle /device PNG /cairo /DPI 150 hello.gle

clean:
	-del hello.eps hello.pdf hello.png
	-rmdir /SQ .gle