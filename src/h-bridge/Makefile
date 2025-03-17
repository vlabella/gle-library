all: h-bridge.eps h-bridge.pdf h-bridge.png

h-bridge.eps: h-bridge.gle
	gle /device EPS /cairo h-bridge.gle

h-bridge.pdf: h-bridge.gle
	gle /device PDF /cairo h-bridge.gle

h-bridge.png: h-bridge.gle
	gle /device PNG /cairo /DPI 150 h-bridge.gle

clean:
	-del h-bridge.eps h-bridge.pdf h-bridge.png
	-rmdir /SQ .gle