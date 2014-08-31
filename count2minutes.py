from datetime import datetime, timedelta
from os import system
a = datetime.today() + timedelta(minutes=5)
continuar = True;
print "Contando..."
while continuar:
    b = datetime.today()
    if b > a:
        continuar = False
        msg = "Listo, he contado 2 minutos."
        print msg
        system("say "+msg);
    else:
        print b


