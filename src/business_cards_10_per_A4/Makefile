all: business_cards_10_per_A4.eps business_cards_10_per_A4.pdf business_cards_10_per_A4.png

business_cards_10_per_A4.eps: business_cards_10_per_A4.gle
	gle /device EPS /cairo business_cards_10_per_A4.gle

business_cards_10_per_A4.pdf: business_cards_10_per_A4.gle
	gle /device PDF /cairo business_cards_10_per_A4.gle

business_cards_10_per_A4.png: business_cards_10_per_A4.gle
	gle /device PNG /cairo /DPI 150 business_cards_10_per_A4.gle

clean:
	-del business_cards_10_per_A4.eps business_cards_10_per_A4.pdf business_cards_10_per_A4.png
	-rmdir /SQ .gle