from pattern.web import *
f = Facebook(license = 'CAAEuAis8fUgBAPAndRmvdkvtBbh6UYilMqXubriSF2ZB1DGx6qP9I30ZAvZBNCIFVWntQLCnsDp1e6a61sDg6ZB2xO2mysEEROcAyKIouoRzfrbEe8dxJ47qdXI6Sc1uSNWp8zL0AcftCSdteAPYQYUzGqsi9hYxL3i6uHl5S84ZColyDRNv2')
me = f.profile()
print me



print len(f.search(me[0],type = FRIENDS))
help (Facebook)