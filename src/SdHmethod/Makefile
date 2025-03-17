all: SdHmethod.eps SdHmethod.pdf SdHmethod.png

SdHmethod.eps: SdHmethod.gle
	gle /device EPS /cairo SdHmethod.gle

SdHmethod.pdf: SdHmethod.gle
	gle /device PDF /cairo SdHmethod.gle

SdHmethod.png: SdHmethod.gle
	gle /device PNG /cairo /DPI 150 SdHmethod.gle

clean:
	-del SdHmethod.eps SdHmethod.pdf SdHmethod.png
	-rmdir /SQ .gle