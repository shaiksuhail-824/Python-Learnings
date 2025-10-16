import qrcode
user_url=input("Enter the URL to generate QR code: ")
phonepe_url=f'upi://pay?pa={user_url}&pn=recipent%20name&mc=1234'
paytm_url=f'upi://pay?pa={user_url}&pn=recipent%20name&mc=1234'
phonepe_qr=qrcode.make(phonepe_url)#make qr code
paytm_qr=qrcode.make(paytm_url) 
phonepe_qr.show()#show the qrcode
paytm_qr.show()


