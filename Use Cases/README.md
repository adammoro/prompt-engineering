# Use Cases #

This is an assortment of scripts that connect to AI service APIs and automate prompting. This automation can be useful for the purpose of generating responses at scale, crafting advanced multi-shot prompts with conditional logic, and so much more.

## OpenAI API Parameters ##

Here's a summary of the parameters passed in a call to the OpenAI API:

1. 'model': Specifies the OpenAI model to use (e.g., 'text-davinci-003').
2. 'prompt': The input text or context for the model to generate a response.
3. 'temperature': Controls the randomness or creativity of the generated text.
4. 'max_tokens': Limits the length of the generated text, measured in tokens.
5. 'frequency_penalty': Penalizes tokens based on their frequency in the training data.
6. 'presence_penalty': Penalizes the model for repeating tokens or phrases.
