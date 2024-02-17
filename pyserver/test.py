import google.generativeai as genai


genai.configure(api_key='AIzaSyAl0Hg1SyWCt6878-ipeNl-pusgptpAdiY')

model = genai.GenerativeModel('gemini-pro')



response = model.generate_content("write a nodejs function to create a database schema which consists of 3 tables - user_data, purchasses, sale_data ")

print(response.text)