import requests
import json

def fetch():
    try:
        # 价格
        price_url = "https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT"
        price = float(requests.get(price_url, timeout=10).json()['data'][0]['last'])
        
        # 资金费率
        funding_url = "https://www.okx.com/api/v5/public/funding-rate?instId=BTC-USDT-SWAP"
        funding_rate = float(requests.get(funding_url, timeout=10).json()['data'][0]['fundingRate'])
        
        # OI
        oi_url = "https://www.okx.com/api/v5/public/open-interest?instId=BTC-USDT-SWAP"
        oi = float(requests.get(oi_url, timeout=10).json()['data'][0]['oi'])
        
        data = {
            "price": price,
            "funding_rate": funding_rate,
            "oi": oi,
            "timestamp": requests.get("https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT", timeout=5).json()['data'][0]['ts']
        }
        
        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
            
        print("Data fetched successfully:", data)
        
    except Exception as e:
        print("Error:", e)
        # 写入错误标记，防止旧数据被覆盖
        try:
            with open("data.json", "r") as f:
                old = json.load(f)
            old["error"] = str(e)
            with open("data.json", "w") as f:
                json.dump(old, f, indent=2)
        except:
            pass

if __name__ == "__main__":
    fetch()
