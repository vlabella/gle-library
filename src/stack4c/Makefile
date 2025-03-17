all: stack4c.eps stack4c.pdf stack4c.png

stack4c.eps: stack4c.gle
	gle /device EPS /cairo stack4c.gle

stack4c.pdf: stack4c.gle
	gle /device PDF /cairo stack4c.gle

stack4c.png: stack4c.gle
	gle /device PNG /cairo /DPI 150 stack4c.gle

clean:
	-del stack4c.eps stack4c.pdf stack4c.png
	-rmdir /SQ .gle