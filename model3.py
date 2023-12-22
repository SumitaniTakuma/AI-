# 小説作成コード
# gpt-author

from transformers import pipeline, TextGenerationPipeline, GPT2LMHeadModel, AutoTokenizer

model_name = "aspis/gpt2-genre-story-generation"

model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
generator = TextGenerationPipeline(model=model, tokenizer=tokenizer)

input_prompt = "<BOS> <adventure>"
story = generator(input_prompt, max_length=200, do_sample=True,
            repetition_penalty=1.5, temperature=1.2, 
            top_p=0.95, top_k=50)

print(story)