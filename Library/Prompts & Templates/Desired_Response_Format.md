### Formatted Output ###

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

You can adjust the above format template to call out specific information to extract. For example:

```
Read the following text and extract all the important information.

[Text: New World sparrows are a group of mainly New World passerine birds, forming the family Passerellidae. They are seed-eating birds with conical bills, brown or gray in color, and many species have distinctive head patterns.

Although they share the name sparrow, New World sparrows are more closely related to Old World buntings than they are to the Old World sparrows (family Passeridae). New World sparrows are also similar in both appearance and habit to finches, with which they sometimes used to be classified.

Taxonomy
The genera now assigned to the family Passerellidae were previously included with the buntings in the family Emberizidae. A phylogenetic analysis of nuclear and mitochondrial DNA sequences published in 2015 found that the Passerellidae formed a monophyletic group that had an uncertain relationship to the Emberizidae. Emberizidae was therefore split and the family Passerellidae resurrected.[4][5] It had originally been introduced, as the subfamily Passerellinae, by the German ornithologist Jean Cabanis in 1851.

The International Ornithological Congress (IOC) recognizes 138 species in the family, distributed among these 30 genera. For more detail, see list of New World sparrow species.

Passerellidae

Genus Oreothraupis
Genus Chlorospingus
Genus Rhynchospiza
Genus Peucaea
Genus Ammodramus
Genus Arremonops
Genus Amphispizopsis
Genus Amphispiza
Genus Chondestes
Genus Calamospiza
Genus Spizella
Genus Arremon
Genus Passerella
Genus Spizelloides
Genus Junco
Genus Zonotrichia
Genus Artemisiospiza
Genus Oriturus
Genus Pooecetes
Genus Ammospiza
Genus Centronyx
Genus Passerculus
Genus Xenospiza
Genus Melospiza
Genus Pezopetes
Genus Torreornis
Genus Melozone
Genus Aimophila
Genus Pipilo
Genus Atlapetes
]

Desired format:
Short Summary of Text: -||-
Species: <comma_separated_list_of_species>
```


