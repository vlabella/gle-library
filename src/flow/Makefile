all: flow.eps flow.pdf flow.png

flow.eps: flow.gle
	gle /device EPS /cairo flow.gle

flow.pdf: flow.gle
	gle /device PDF /cairo flow.gle

flow.png: flow.gle
	gle /device PNG /cairo /DPI 150 flow.gle

clean:
	-del flow.eps flow.pdf flow.png
	-rmdir /SQ .gle