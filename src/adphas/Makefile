all: adphas.eps adphas.pdf adphas.png

adphas.eps: adphas.gle
	gle /device EPS /cairo adphas.gle

adphas.pdf: adphas.gle
	gle /device PDF /cairo adphas.gle

adphas.png: adphas.gle
	gle /device PNG /cairo /DPI 150 adphas.gle

clean:
	-del adphas.eps adphas.pdf adphas.png
	-rmdir /SQ .gle