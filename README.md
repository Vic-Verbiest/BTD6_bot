# Bloons Tower Defence 6 Bot

## Doelstellingen
### hoofd doel
Het is de bedoeling om de AI aant te leren hoe je het populaire spelletje Boons Tower Defence 6 moet spelen. Hierbij hoort het plaatsen van apjes en het upgraden van de aapjes die eerder geplaatst sijn.
### supdoel
zonder enige data, buiten een array die aantoont hoe de map in elkaar zit, een level op de moeilijkheidsgraad hard te laten verslaan.

## Analyse
### Mouse inpout
Om het spel te spelen ordt er gebruik gemaakt van de muis. Dit wil zeggen dat het programa controle moet krijgen over de muis wanneer dit nodig is. Hiervoor heb ik de python library 'mouse' grbruikt. Vie deze library kan het programma de muis besturen aan de hand van X en Y coördinaten an de linker muisknop indrukken wanneer nodig.
### Data extraction
Om het mogelijk te maken het spelletje te spelen zijn er eental gegevens belangrijk om te spelen. Aangezien het programma geen ogen heeft om het scherm te kunnen lezen, moeten we een andere manier vinden om het geld, levens en de huidige ronde als informatie mee te geven aan het programma. Dit gebeurd via pytesseract. dit is een optical character recognition tool ide text en getallen uit afbeelding kan herkennen en als string door geeft aan het programma.
### AI model
Het AI model is het brein achter het volledige project. Ik heb gekozen voor een Deep Q-Netwerk. Dit berekent de beste actie voor de staat waar het spel zich in bevindt. terweil het programma bij leert op basis van de vooraf genomen stappen om in de toekomst betere keuzes te kunne maken.
### training
Aangezien ik zelf geen data in aan het programma wou geven, moest het programma alles zelf leren om het spel te leren gebruiken en zo juiste keuzes maken die er voor zorgen dat het spel dichter bij zijn eind toestand komt.

## resultaat
### plaatsen en upgraden
Het programma is goed in staat om apen te plaatsen en te upgraden met behulp van de mouse library. Wanneer de snelheid van bewegen te hoog wordt ingeselt, kan het zijn dat plaatsen niet mogelijk is maar dit is gemakkelijk te verhelpen door de snelheid te verlagen.
### data extractioen
Het lezen van data is meestal geen probleem. Soms worden er woorde ingelezen bij de levens, geld, of rondes maar hier is  rekening mee gehouden in de code. Om te kijken of de game over is zijn er wel problemen. soms denkt het programma dat het spe gedaan is door voorbijgaande ballonen als tekst te beschouwen.
### AI model
De AI heeft veel vordering gebekt tijden het leren. Ondanks het de vooruitgang is hi er noch niet ingeslaagt om de gewenste ronde voorbij te gaan. Met extra leer tijd zou dit misschien wel mogelijk zijn geweest.
### algemeen
het programma heeft geleert om apen te plaatsen en upgraden in starategische plaatsen. Het kan gemakkelijk tot ronde 28 overleven maar daarna wordt het lastig. in ronde 29 komen metalen ballonen voor die enkel een aantal speciale apen en upgrades kunnen tegen houden. Dit is het zelfde probleem voor camo ballonen. In ronde 40 is er een MOAB. Dit is te vergelijken met een boss-battle in een ander spel waarbij de AI ook nog even zou kunnen vast ziten moest hij hier ooit geraakt zijn.

## Uitbreiding
### meerder uitdagingen
Op elke map heb je verschillende uitdagingen. Zo kan je niet enkel de moeillijkheidsgraad aanpasses, maar zijn er ook uitdagingen waar een slectie van apen niet is toegestaan of waar je moeilijkere rondes meot tegen houden.
### meerdere mappen
Er zijn verschillende mappen. Ik heb op dit moment de informatie van 1 map in het programma gestoken maar op dit vlak kan er heel veel verbetering worden geboekt.
### gebruik van powers
bij het upgraden van sommige apen krijg je een power. deze kan je gebruiken tijden het spelen wanneer je er op klinkt maar deze actie is niet geprogrammeerd in de huidige versie van het project.
### verschilende hero's
Er zijn verschillende hero's in het spel waaruit vrij gekozen kan worden. Er kan maar 1 tegelijkertijd op het speelveld staan waardoor er verschillende strategiën kunnen ontstaan. In de huidige versie van het programma is er een vaste hero gekozen.
### implementeren van water
Ik heb de  eerste map gekozen in de game. Het toeval heeft besloten dat er op deze map geen water is en dus ook geen boten kunnen geplaatst worden. Dit is een deel van de code die eenvoudiger is gamaakt maar wanneer er wordt uitgbrijd naar meerdere mappen is dit een essentieel stuk.

## Conclusie
Het hoofddoel is berijkt. het prgramma kan apen plaatsen en upgraden om rondes te overleven. Daarnaast is het subdoel niet geslaagt. Ookal heeft de Ai veel bijgeleerd over het plaatsen en upgraden van apen op strategische plaatsen is het er noch niet in geslaagt om tot ronde 80 (mode: hard) te overleven.

## Bibliographie