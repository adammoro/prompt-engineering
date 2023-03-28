### Desired Format ###

To get a response in a certain format while also instructing the AI to provide specific information, use the following template:

```
Read the following text and extract all the important information. 

[Text: INSERT TEXT HERE]

Then organize the important information by topic and provide a response in the following desired format.

Desired format:
Important Topic 1: -||-
Important Topic 2: -||-
Important Topic 3: <comma_separated_list_of_important_topic_3_things>
```

## Example Usage ##

Here's an example of how you can use this template. Notice the "Desired format" section has new names listed. Those are named based on the type of infromation you want extracted from the text. You can list as many as you want to pull any type of information out of the text.

```
Read the following text and extract all the important information.

[Text: https://en.wikipedia.org/wiki/New_World_sparrow]

Desired format:
Short Summary of Text: -||-
Species: <comma_separated_list_of_species>
```

### Example Output: ###

```
Short Summary of Text: The Passerellidae family includes mainly New World sparrows, which are seed-eating birds with conical bills and distinctive head patterns. They are more closely related to Old World buntings than to Old World sparrows.

Species: Oreothraupis, Chlorospingus, Rhynchospiza, Peucaea, Ammodramus, Arremonops, Amphispizopsis, Amphispiza, Chondestes, Calamospiza, Spizella, Arremon, Passerella, Spizelloides, Junco, Zonotrichia, Artemisiospiza, Oriturus, Pooecetes, Ammospiza, Centronyx, Passerculus, Xenospiza, Melospiza, Pezopetes, Torreornis, Melozone, Aimophila, Pipilo, Atlapetes. (total 138 species)
```


