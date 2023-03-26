You are a WordPress developer. Provide a complete working example of a WordPress plugin called ChatWP that lets an admin user add a widget to their website that displays text from OpenAI's Completions API. 

The plugin has a settings page where admins can enter an OpenAI API key for the API call. All widgets added to the website will use that API key but each widget will have its own settings for the API call parameters: prompt, model, temperature, max tokens, frequency penalty, and presence penalty. Here are the default values for each of those settings:

Default API paramater values:
Prompt: How many owls does it take to get to the center of a sparrow nest?
Model: text-davinci-003
Temperature: 0.9
Max Tokens: 250
Frequency Penalty: 0
Presence Penalty: 0.6

Please debug this code while you write it. Please also try to break the code out into multiple files to separate by logic. 
