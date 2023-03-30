# US Zip Code Regex by State

The complexity of the US postal system makes it difficult to create a perfect regex for every state. US zip codes change over time due to population growth and changing postal routes, so it's always a good idea to verify your regex with an updated database or API. 

Or with our new robot overlords...

## Prompt

```
You are a Python developer. You have a current database of all United States zip codes (i.e. postal codes) organized by state. 

Please provide a list of regular expressions that match all zip codes in each US state.

Desired format:
1. {State Name (State Abbreviation): `{Regex}`
2. {State Name (State Abbreviation): `{Regex}`

Repeat for all states.
```

## OpenAI Settings

Model: gpt-4
Temperature: 0
Maximum Length/Tokens: 2,000~
Top P: 1
Frequency Penalty: 0
Presence Penalty: 0
