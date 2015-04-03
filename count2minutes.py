from datetime import datetime, timedelta
from os import system
a = datetime.today() + timedelta(minutes=2)
continuar = True;
print "Contando..."
c = datetime.today()
while continuar:
    b = datetime.today()
    if b >= a:
        continuar = False
        msg = "Listo, he contado 2 minutos."
        print msg
        system("say "+msg);
    elif b >= c:
        print "contando",b,"  --final:",a
        c = datetime.today() + timedelta(seconds=1)

