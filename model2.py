# GPT モデルによる小説の生成モデル
import openai

def generate_story(keywords, max_tokens=150):
    openai.api_key = 'your API Key'  # あなたのAPIキーを設定

    prompt = f"Create a story based on these keywords: {', '.join(keywords)}."

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7
    )

    story = response.choices[0].text.strip()
    return story

# 以下モデル単体での出力
""" keywords = ["wizard", "forest", "adventure"]
print(generate_story(keywords)) """
