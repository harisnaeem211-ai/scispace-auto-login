from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("🚀 Starting SciSpace Token Login...")

# Tumhare REAL tokens
ACCESS_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJ4R1AzWWx5cTkzZFBSRTczckdySnNScmNrQ04iLCJ0eXAiOiJTQ0lTUEFDRV9VU0VSIiwiaXNzIjoiaHR0cHM6Ly9zY2lzcGFjZS5jb20iLCJpYXQiOjE3NjA5MDgzODUsImV4cCI6MTc2OTU0ODM4NX0.Uan7ieY41_i_NbPOKhJAyXLVzUeXpf-zncvCrvagnBhq4Dnc_-uTJAQcHMWfuV94b2NtJQxZ5W-ivm7wmpSUVIiExr5yuLMD_wgGwMkzI6QAXirfIWJ7HwcmajgK77yrVBvjZ36JpSTAsCYptI_3-EUiuxcujhFxllYCNt_VCo962A7Dzook0f58WQW7eTLbhPTlTHoKiL0jOLfobP9a0xnM_kDqvUfrtkLFeSkVwfxQ8x5Gij_EXlpV2HnIrPuM_w01bjZGH0T3wrMDRCel3FLjV86aSwJ9nEPuSUY-NiD4w9Ry1zMub4kCYme0sXO3L41GimjsVEfuMUzK_OZsBg"
SESSION_ID = "02zjkl7rx9jp9jeas8m99pyo22x5353r"

try:
    # Chrome setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    print("✅ Browser started")
    
    # SciSpace login page par jao
    driver.get("https://scispace.com/login")
    print("✅ Login page loaded")
    
    # JavaScript se tokens set karo
    token_script = f"""
    // Clear existing data
    localStorage.clear();
    
    // Set tokens in localStorage
    localStorage.setItem('access_token', '{ACCESS_TOKEN}');
    localStorage.setItem('sessionid', '{SESSION_ID}');
    
    // Set cookies
    document.cookie = 'access_token={ACCESS_TOKEN}; domain=.scispace.com; path=/; max-age=8640000';
    document.cookie = 'sessionid={SESSION_ID}; domain=.scispace.com; path=/; max-age=8640000';
    
    console.log('🔑 Tokens set successfully');
    
    // Validate token
    fetch('https://scispace.com/api/auth/validate', {{
        method: 'GET',
        headers: {{
            'Authorization': 'Bearer {ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        }},
        credentials: 'include'
    }})
    .then(response => response.json())
    .then(data => {{
        console.log('Token validation:', data);
        if(data.auth_status === 'success') {{
            console.log('✅ Token valid! Redirecting...');
            window.location.href = 'https://scispace.com/';
        }} else {{
            console.log('❌ Token invalid');
        }}
    }});
    """
    
    driver.execute_script(token_script)
    print("🔑 Tokens injected")
    
    # Wait for redirect
    time.sleep(5)
    
    # Check current URL
    current_url = driver.current_url
    print(f"📊 Current URL: {current_url}")
    
    if "scispace.com" in current_url and "login" not in current_url:
        print("🎉 TOKEN LOGIN SUCCESSFUL!")
    else:
        print("❌ Login failed - trying credential login...")
        
        # Fallback: Email/password login
        login_script = """
        // Auto fill credentials
        const emailField = document.querySelector('input[name="email"]');
        const passwordField = document.querySelector('input[name="password"]');
        const loginButton = document.querySelector('button[data-test-id="auth_log-in"]');
        
        if(emailField && passwordField && loginButton) {
            emailField.value = 'aldjekej21@gmail.com';
            passwordField.value = 'scispace@7675';
            
            // Trigger events
            emailField.dispatchEvent(new Event('input', {bubbles: true}));
            passwordField.dispatchEvent(new Event('input', {bubbles: true}));
            
            // Auto click login
            setTimeout(() => {
                loginButton.click();
            }, 2000);
            
            console.log('🔑 Credentials filled');
        }
        """
        
        driver.execute_script(login_script)
        print("🔑 Credentials filled")
    
    # Take screenshot
    driver.save_screenshot("result.png")
    print("📸 Screenshot saved")
    
    driver.quit()
    print("✅ Script completed!")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
