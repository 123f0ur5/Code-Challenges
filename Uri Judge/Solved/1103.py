import datetime

while True:
    ih, im, fh, fm = map(int, input().split())

    if ih == im == fh == fm == 0:
        break
    
    x = datetime.timedelta(hours=ih,minutes=im)
    y = datetime.timedelta(hours=fh,minutes=fm)

    print(int((y - x).seconds/60))