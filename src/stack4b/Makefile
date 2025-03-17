all: stack4b.eps stack4b.pdf stack4b.png

stack4b.eps: stack4b.gle
	gle /device EPS /cairo stack4b.gle

stack4b.pdf: stack4b.gle
	gle /device PDF /cairo stack4b.gle

stack4b.png: stack4b.gle
	gle /device PNG /cairo /DPI 150 stack4b.gle

clean:
	-del stack4b.eps stack4b.pdf stack4b.png
	-rmdir /SQ .gle