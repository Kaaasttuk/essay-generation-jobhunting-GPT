from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
from django.http import HttpResponse

def main(request):
    return render(request, "main.html")

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

def chatbot(request):
    
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key

        selected_option = request.POST['selected_option']
        if f"{selected_option}" == "gakuchika":
            company_name = request.POST['company_name']
            question = request.POST['question']
            word_limit = request.POST['word_limit']
            episode = request.POST['episode']
            other = request.POST['other']
            if len(other)>3:
                other_input = f"、入れたい内容に{other}があります。" 
            else:
                other_input = "す。"

            prompt = f"非常に優秀な大学生のあなたは就職活動中で、{company_name}の新卒採用に応募しています。書類選考の{question}という質問に答えてください。何を頑張ったか、なぜそれを頑張る必要があったか、どのような困難があり、どう具体的にそれを解決し目標を達成したかという順番で書いてください。頑張ったことは{episode}で{other_input}端的な日本語{word_limit}字以内でお願いします。"
        elif f"{selected_option}" == "PR":
            company_name2 = request.POST['company_name2']
            question2 = request.POST['question2']
            word_limit2 = request.POST['word_limit2']
            strength2 = request.POST['strength2']
            episode2 = request.POST['episode2']
            other2 = request.POST['other2']
            if len(other2)>3:
                other_input = f"入れたい内容に、{other2}があります。" 
            else:
                other_input = ""

            prompt = f"非常に優秀な大学生のあなたは就職活動中で、{company_name2}の新卒採用に応募しています。書類選考の{question2}という質問に答えてください。私の強みは{strength2}です、その根拠となるエピソードは{episode2}です。{other_input}強みが伝わるように、日本語{word_limit2}字以内でお願いします。"
        elif f"{selected_option}" == "motivation":
            company_name3 = request.POST['company_name3']
            question3 = request.POST['question3']
            word_limit3 = request.POST['word_limit3']
            vision3 = request.POST['vision3']
            other3 = request.POST['other3']
            if len(other3)>3:
                other_input = f"入れたい内容に、{other3}があります。" 
            else:
                other_input = ""
            
         

            prompt = f"非常に優秀な大学生のあなたは就職活動中で、{company_name3}の新卒採用に応募しています。書類選考の{question3}という質問に答えてください。将来の夢や大きなビジョン、そう思うきっかけになった経験、そのために応募先の会社で何を学びたいか、のような構成で端的に書いてください。将来のビジョンは{vision3}です。{other_input}日本語{word_limit3}字以内でお願いします。"
        elif f"{selected_option}" == "one-word":
            company_name4 = request.POST['company_name4']
            other4 = request.POST['other4']
            if len(other4)>3:
                other_input = f"あなたは{other4}というエピソードを持っています。" 
            else:
                other_input = ""

            prompt = f"{other_input}こんなあなたを興味深く短く表すと"
        elif f"{selected_option}" == "other-type":
            company_name5 = request.POST['company_name5']
            question5 = request.POST['question5']
            word_limit5 = request.POST['word_limit5']
            other5 = request.POST['other5']
            if len(other5)>3:
                other_input = f"入れたい内容に、{other5}があります。" 
            else:
                other_input = ""

            prompt = f"非常に優秀な大学生のあなたは就職活動中です。{question5}という質問に答えてください。{other_input}日本語{word_limit5}字以内でお願いします。"



        # prompt = user_input
        
        print(prompt)

        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt= prompt, 
            max_tokens=610,
            stop=".",
            #↑ GPT will start response from "."
            temperature=0.4,
        )
        print(response)

        chatbot_response = response["choices"][0]["text"]
        clean_chatbot_response = chatbot_response.replace("\n\n", "")
    return HttpResponse(clean_chatbot_response)
    # return render(request, "main.html", {"response":chatbot_response})