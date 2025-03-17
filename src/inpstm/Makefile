all: inpstm.eps inpstm.pdf inpstm.png

inpstm.eps: inpstm.gle
	gle /device EPS /cairo inpstm.gle

inpstm.pdf: inpstm.gle
	gle /device PDF /cairo inpstm.gle

inpstm.png: inpstm.gle
	gle /device PNG /cairo /DPI 150 inpstm.gle

clean:
	-del inpstm.eps inpstm.pdf inpstm.png
	-rmdir /SQ .gle