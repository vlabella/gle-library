all: heatmap.eps heatmap.pdf heatmap.png

heatmap.eps: heatmap.gle
	gle /device EPS /cairo heatmap.gle

heatmap.pdf: heatmap.gle
	gle /device PDF /cairo heatmap.gle

heatmap.png: heatmap.gle
	gle /device PNG /cairo /DPI 150 heatmap.gle

clean:
	-del heatmap.eps heatmap.pdf heatmap.png
	-rmdir /SQ .gle