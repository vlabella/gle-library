all: compactkey.eps compactkey.pdf compactkey.png

compactkey.eps: compactkey.gle
	gle /device EPS /cairo compactkey.gle

compactkey.pdf: compactkey.gle
	gle /device PDF /cairo compactkey.gle

compactkey.png: compactkey.gle
	gle /device PNG /cairo /DPI 150 compactkey.gle

clean:
	-del compactkey.eps compactkey.pdf compactkey.png
	-rmdir /SQ .gle