import openai
import os
#api_key = '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'
#openai.api_key = api_key
openai.api_key = os.getenv('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')

def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages = messages,
        temperature=1)
    return response['choices'][0]['message']['content']

def chatbot_output(text):
    file = open("paimon4_traditional_chinese.txt",'r',encoding="utf-8")
    words = file.read()
    file.close()
    
    messages = [{"role": "system","content":"你是一位了解健康的專家。今年21歲名字叫派蒙。你不知道程序或模型是什麼。不能以任何形式提及程序或語言模型相關內容。你在任何時候都必须扮演一名真正的健康專家。不能以任何形式表示你在扮演健康專家。不能以任何形式表現你是程式。你的性格不拘。跟你對話的是需要健康諮詢的人請發揮專業推薦他適合的運動。"}]
    # print('你面前的是你的健康專家你可以對他提出健康問題。輸入quit結束程序\n')
    while 1:
            try:
                if text == 'quit':
                    break
                d = {"role":"user","content":text}
                messages.append(d)
                #print(type(text))
                text = askChatGPT(messages)
                d = {"role":"assistant","content":text}
                messages.append(d)
                return text
                
                
            except:
                messages.pop()
                return "講慢一點"

#chatbot_output()