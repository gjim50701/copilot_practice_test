def convert_currency(usd_amount, exchange_rate):
    """
    將美金金額轉換為台幣。
    
    此函數執行以下步驟：
    1. 接收美金金額和匯率作為參數
    2. 計算對應的台幣金額
    3. 返回轉換結果和當前匯率
    
    Args:
        usd_amount (float): 美金金額
        exchange_rate (float): 美金對台幣的匯率
    
    Returns:
        dict: 包含轉換後金額和匯率的字典
            - 'twd_amount' (float): 對應的台幣金額
            - 'exchange_rate' (float): 當前匯率
    
    Raises:
        ValueError: 當輸入的金額或匯率無法轉換為浮點數時
    
    Example:
        >>> convert_currency(100, 31)
        {'twd_amount': 3100.0, 'exchange_rate': 31}
    """
    if usd_amount < 0:
        raise ValueError("金額不能為負數")
    
    if exchange_rate <= 0:
        raise ValueError("匯率必須大於零")
    
    twd_amount = usd_amount * exchange_rate
    
    return {
        'twd_amount': twd_amount,
        'exchange_rate': exchange_rate
    }

# 建立一個函數 get_exchange_rate(target_currency)
# 使用 requests 從 https://api.exchangerate-api.com/v4/latest/USD 抓取匯率
import requests
def get_exchange_rate(target_currency):
    """
    從匯率 API 抓取指定貨幣的匯率。
    
    此函數執行以下步驟：
    1. 發送 GET 請求到匯率 API
    2. 解析 JSON 回應以取得指定貨幣的匯率
    3. 返回匯率值
    
    Args:
        target_currency (str): 目標貨幣的代碼（例如 "TWD"）
    
    Returns:
        float: 指定貨幣的匯率
    
    Raises:
        requests.exceptions.RequestException: 當 HTTP 請求失敗時
        KeyError: 當回應中不包含指定貨幣的匯率時
    
    Example:
        >>> get_exchange_rate("TWD")
        31.0
    """
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if target_currency not in data["rates"]:
            raise KeyError(f"無法找到 {target_currency} 的匯率")
        
        return data["rates"][target_currency]
    except requests.exceptions.RequestException as e:
        print(f"無法取得匯率: {e}")
        return None