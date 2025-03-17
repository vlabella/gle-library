all: stacks.eps stacks.pdf stacks.png

stacks.eps: stacks.gle
	gle /device EPS /cairo stacks.gle

stacks.pdf: stacks.gle
	gle /device PDF /cairo stacks.gle

stacks.png: stacks.gle
	gle /device PNG /cairo /DPI 150 stacks.gle

clean:
	-del stacks.eps stacks.pdf stacks.png
	-rmdir /SQ .gle