all: stack2.eps stack2.pdf stack2.png

stack2.eps: stack2.gle
	gle /device EPS /cairo stack2.gle

stack2.pdf: stack2.gle
	gle /device PDF /cairo stack2.gle

stack2.png: stack2.gle
	gle /device PNG /cairo /DPI 150 stack2.gle

clean:
	-del stack2.eps stack2.pdf stack2.png
	-rmdir /SQ .gle