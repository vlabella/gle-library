all: stack1.eps stack1.pdf stack1.png

stack1.eps: stack1.gle
	gle /device EPS /cairo stack1.gle

stack1.pdf: stack1.gle
	gle /device PDF /cairo stack1.gle

stack1.png: stack1.gle
	gle /device PNG /cairo /DPI 150 stack1.gle

clean:
	-del stack1.eps stack1.pdf stack1.png
	-rmdir /SQ .gle