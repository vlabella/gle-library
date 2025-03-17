all: let-multi-dim.eps let-multi-dim.pdf let-multi-dim.png

let-multi-dim.eps: let-multi-dim.gle
	gle /device EPS /cairo let-multi-dim.gle

let-multi-dim.pdf: let-multi-dim.gle
	gle /device PDF /cairo let-multi-dim.gle

let-multi-dim.png: let-multi-dim.gle
	gle /device PNG /cairo /DPI 150 let-multi-dim.gle

clean:
	-del let-multi-dim.eps let-multi-dim.pdf let-multi-dim.png
	-rmdir /SQ .gle