from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ACCESS_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJ4R1AzWWx5cTkzZFBSRTczckdySnNScmNrQ04iLCJ0eXAiOiJTQ0lTUEFDRV9VU0VSIiwiaXNzIjoiaHR0cHM6Ly9zY2lzcGFjZS5jb20iLCJpYXQiOjE3NjA5MDgzODUsImV4cCI6MTc2OTU0ODM4NX0.Uan7ieY41_i_NbPOKhJAyXLVzUeXpf-zncvCrvagnBhq4Dnc_-uTJAQcHMWfuV94b2NtJQxZ5W-ivm7wmpSUVIiExr5yuLMD_wgGwMkzI6QAXirfIWJ7HwcmajgK77yrVBvjZ36JpSTAsCYptI_3-EUiuxcujhFxllYCNt_VCo962A7Dzook0f58WQW7eTLbhPTlTHoKiL0jOLfobP9a0xnM_kDqvUfrtkLFeSkVwfxQ8x5Gij_EXlpV2HnIrPuM_w01bjZGH0T3wrMDRCel3FLjV86aSwJ9nEPuSUY-NiD4w9Ry1zMub4kCYme0sXO3L41GimjsVEfuMUzK_OZsBg"
SESSION_ID = "02zjkl7rx9jp9jeas8m99pyo22x5353r"

def token_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://scispace.com/")
        
        token_script = f"""
        localStorage.setItem('access_token', '{ACCESS_TOKEN}');
        localStorage.setItem('sessionid', '{SESSION_ID}');
        document.cookie = 'access_token={ACCESS_TOKEN}; domain=.scispace.com; path=/';
        document.cookie = 'sessionid={SESSION_ID}; domain=.scispace.com; path=/';
        console.log('✅ Tokens set');
        """
        
        driver.execute_script(token_script)
        print("✅ Token login completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    token_login()
