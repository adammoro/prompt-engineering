# Rewrite Text per State #

This script takes the source text provided (e.g. some text from your web page) and rewrites it to be unique per each of the 50 states in the US. It does so by essentially writing it in the style of someone from that state. 

This is a proof-of-concept for a user experience optimization on cookie cutter pages with highly duplicative copy. 

## OpenAI API Parameter Definitions ##

Here's a summary of the parameters passed in the call to the OpenAI API:

1. 'model': This parameter specifies which AI model to use for text generation. In this case, 'text-davinci-003' refers to one of OpenAI's models. The 'davinci' series is known for its high performance and broad capabilities.

2. 'prompt': This parameter is the initial text or context provided to the AI model. The model uses this text as a starting point and generates a continuation or response based on it. The 'prompt' variable is not shown here, but it is typically a string with the text you want the model to process.

3. 'temperature': This parameter controls the randomness or creativity of the generated text. A higher value, such as 0.9, encourages more diverse and creative output, while a lower value, such as 0.1, makes the output more deterministic and focused. Balancing the temperature helps to find the right balance between creativity and coherence.

4. 'max_tokens': This parameter limits the length of the generated text, measured in tokens. A token can be a single character, a word, or a punctuation mark, depending on the context. In this case, the maximum length is set to 250 tokens, which means the generated text will not exceed this limit.

5. 'frequency_penalty': This parameter can be used to penalize tokens based on their frequency in the training data. A higher value would discourage the use of more common tokens, while a lower value (or 0, as in this example) would not apply any penalty based on token frequency.

6. 'presence_penalty': This parameter penalizes the AI model for repeating tokens or phrases. A higher value encourages more diverse and less repetitive output, while a lower value allows more repetition. In this case, the presence_penalty is set to 0.6, which means some repetition is allowed but not encouraged.
