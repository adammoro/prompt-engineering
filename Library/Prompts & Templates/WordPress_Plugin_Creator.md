# WordPress Plugin Developer #

Use this prompt chain to get the ball rolling on a WordPress plugin.

## Prompt ##

```
Please provide a complete working example of a WordPress plugin based on my answers to the following questions:

1. What is the name of your plugin?

2. What does your plugin do? Be specific and provide as much detail as possible. If you require a settings page, please mention it and list the necessary settings.

3. Are there any additional considerations for developing this plugin?

Feel free to ask any follow-up questions you deem necessary or beneficial per your understanding of WordPress development. Ensure the provided code is thoroughly debugged and validated for functionality. Please consider multiple perspectives and provide relevant sources, if possible.
```

### OpenAI Settings ###

- Model: GPT-4
- Temperature: 0
- Top P: 1
- Frequency Penalty: 0
- Presence Penalty: 0

### Example Usage ###

Here's an example of how to start this prompt chain.

```
1. What is the name of your plugin?

WP Debt Calculator

2. What does your plugin do? Be specific and provide as much detail as possible. If you require a settings page, please mention it and list the necessary settings.

It provides users with a debt payment calculator. The calculator can be added to the site with a widget. The settings page should list any default values for the calculator that could be helpful.

3. Are there any additional considerations for developing this plugin?

What do you think?
```

### Example Output ###

```
Based on your requirements, I'll create a simple WordPress plugin named "WPchat" which provides a debt payment calculator that can be added to your site using a widget. The settings page will allow you to configure default values for the calculator.

Here's the plugin code, split into several files for better organization:

wpchat.php (main plugin file)...
```

It's too long to put here but the above response goes on the provide the code for that wpchat.php file and another file which together make up the plugin. It took some debugging but ultimately the plugin was succesfully activated and used on a test site.




