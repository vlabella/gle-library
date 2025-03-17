all: fitz.eps fitz.pdf fitz.png

fitz.eps: fitz.gle
	gle /device EPS /cairo fitz.gle

fitz.pdf: fitz.gle
	gle /device PDF /cairo fitz.gle

fitz.png: fitz.gle
	gle /device PNG /cairo /DPI 150 fitz.gle

clean:
	-del fitz.eps fitz.pdf fitz.png
	-rmdir /SQ .gle