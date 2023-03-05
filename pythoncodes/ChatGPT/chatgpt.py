import openai

# Set your API key
openai.api_key = "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"
# Use the GPT-3 model
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="请你介绍一下python在linux中的用途",
    max_tokens=1024,
    temperature=0.5
)
# Print the generated text
print(completion.choices[0].text)


