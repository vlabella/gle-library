all: rt-y-is-x.eps rt-y-is-x.pdf rt-y-is-x.png

rt-y-is-x.eps: rt-y-is-x.gle
	gle /device EPS /cairo rt-y-is-x.gle

rt-y-is-x.pdf: rt-y-is-x.gle
	gle /device PDF /cairo rt-y-is-x.gle

rt-y-is-x.png: rt-y-is-x.gle
	gle /device PNG /cairo /DPI 150 rt-y-is-x.gle

clean:
	-del rt-y-is-x.eps rt-y-is-x.pdf rt-y-is-x.png
	-rmdir /SQ .gle