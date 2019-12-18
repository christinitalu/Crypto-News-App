from django.shortcuts import render

def home(request):
    import requests
    import json

    #取得價格資料
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,EOS,BCH&tsyms=USD")
    price = json.loads(price_request.content)


    # 取得 Crypto 新聞
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)


    return render(request,'home.html',{'api':api,'price':price})

def prices(request):
    if request.method == "POST":
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)


        return render(request,'prices.html',{'quote':quote,'crypto':crypto})
    else:
        notfound = "Enter a crypto currency symbol into the form above... "
        return render(request,'prices.html',{'notfound':notfound})
