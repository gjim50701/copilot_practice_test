import requests

def get_exchange_rate():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["rates"]["TWD"]
    except requests.exceptions.RequestException as e:
        print(f"無法取得匯率: {e}")
        return None

def main():
    """
    主程式：將美金金額轉換為台幣。
    
    此函數執行以下步驟：
    1. 提示使用者輸入美金金額
    2. 取得目前的匯率
    3. 計算對應的台幣金額
    4. 顯示轉換結果
    
    Args:
        無
    
    Returns:
        無
    
    Raises:
        ValueError: 當使用者輸入的金額無法轉換為浮點數時
    
    Example:
        >>> main()
        請輸入美金金額: 100
        100.0 美金 = 3100.00 台幣 (匯率: 31.00)
    """
    try:
        usd_amount = float(input("請輸入美金金額: "))
        if usd_amount < 0:
            print("金額不能為負數")
            return
        
        exchange_rate = get_exchange_rate()
        if exchange_rate is None:
            return
        
        twd_amount = usd_amount * exchange_rate
        print(f"{usd_amount} 美金 = {twd_amount:.2f} 台幣 (匯率: {exchange_rate:.2f})")
    except ValueError:
        print("錯誤：請輸入有效的數字金額")

if __name__ == "__main__":
    main()