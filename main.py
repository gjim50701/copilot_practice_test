import converter_logic

def main():
    try:
        # 1. 呼叫邏輯檔的抓取函數
        rate = converter_logic.get_exchange_rate("TWD")
        
        # 2. 取得使用者輸入
        amount = float(input("請輸入美金金額: "))
        
        # 3. 呼叫邏輯檔的計算函數
        result = converter_logic.convert_currency(amount, rate)
        
        print(f"轉換金額：{result['twd_amount']} TWD")
        print(f"匯率：{result['exchange_rate']}")
        
    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    main()