import sys
import segno
url = sys.argv[1]
segno.make(url, error="m").save("qr.png", scale=30, border=4)
