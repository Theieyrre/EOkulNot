import pandas as pd
from io import StringIO

s = StringIO(
    """111	YİĞİT ENES AKTUTAN	93	96			100	100	100	100	96,3333	Öğrenci Not Bilgisi
             114	ABDURRAHMAN ERTOP	76	51			85	85	85	85	70,6667	Öğrenci Not Bilgisi
             123	HAMZA KARA	47	10			55	55	55	55	37,3333	Öğrenci Not Bilgisi
             124	MUZAFFER EFE GÜMÜŞ	54	50			75	75	75	75	59,6667	Öğrenci Not Bilgisi
             154	EYMEN KOÇ	74	50	100		90	90	90	95	73	Öğrenci Not Bilgisi
             166	TARIK SAMİ DEMİR	68	87	100		95	95	95	97,50	84,1667	Öğrenci Not Bilgisi
             204	HİDAYET ONUR	70	49	100		95	95	95	97,50	72,1667	Öğrenci Not Bilgisi
             209	ENES HAKKI ERTUĞ	95	96			100	100	100	100	97	Öğrenci Not Bilgisi
             234	İBRAHİM ALİ AKTAŞ	82	50	100		90	90	90	95	75,6667	Öğrenci Not Bilgisi
             235	NURİ ERBİL	68	58			85	85	85	85	70,3333	Öğrenci Not Bilgisi
             242	ENES KAAN ŞOLPAN	87	71			85	85	85	85	81	Öğrenci Not Bilgisi
             306	SELİM ENES KOCAMAN	98	96			100	100	100	100	98	Öğrenci Not Bilgisi
             350	SÜLEYMAN ŞAKALAK	76	61			85	85	85	85	74	Öğrenci Not Bilgisi
             373	MEHMET EMİN YÜCE	49	48	100		55	55	55	77,50	58,1667	Öğrenci Not Bilgisi
             385	YUSUF PİRİNÇ	82	94			100	100	100	100	92	Öğrenci Not Bilgisi
             388	ENES BUĞRA GÜLAÇAN	93	98			100	100	100	100	97	Öğrenci Not Bilgisi
             391	MUHAMMED EMİN SARIBAŞ	81	66	100		90	90	90	95	80,6667	Öğrenci Not Bilgisi
             394	MUHAMMED ALİ SERÇE	49	54			80	80	80	80	61	Öğrenci Not Bilgisi
             407	MUHAMMED NUR ACUZ	79	43			90	90	90	90	70,6667	Öğrenci Not Bilgisi
             410	MUSTAFA ÖZEN	63	40			65	65	65	65	56	Öğrenci Not Bilgisi
             442	MERT ORAK	57	31	100		65	65	65	82,50	56,8333	Öğrenci Not Bilgisi
             707	ABDURRAHMAN AYDIN	92	90			100	100	100	100	94	Öğrenci Not Bilgisi
             712	MUHAMMED FURKAN VAROL	95	86			100	100	100	100	93,6667	Öğrenci Not Bilgisi
             730	MUHAMMED SAİD SAATCİOĞLU	80	79			95	95	95	95	84,6667	Öğrenci Not Bilgisi
             732	MUHAMMED FATİH ERTÜRK	82	58			85	85	85	85	75	Öğrenci Not Bilgisi
             734	MUSTAFA MUSAB ÖZCAN	55	43			65	65	65	65	54,3333	Öğrenci Not Bilgisi
             742	UMUT ALİ DEMİR	78	70			95	95	95	95	81	Öğrenci Not Bilgisi
             980	MUHAMMED TAHA REZAEI								 	 	Öğrenci Not Bilgisi"""
)

df = pd.read_csv(
    s,
    sep="\t",
)
print(df.head(5))
