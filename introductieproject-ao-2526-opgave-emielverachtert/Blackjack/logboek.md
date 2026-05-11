## 03 April 2026 (1 hour)

Ik ben gestart met het volgen van de tutorial en heb de stappen stap voor stap uitgevoerd. Al snel merkte ik een eerste fout op: *“font not initialized”*. Deze fout kwam ook voor in de tutorial zelf. Daar werd een oplossing gegeven door `pygame.init()` bovenaan bij de variabelen te plaatsen. Hierdoor worden alle pygame-modules geïnitialiseerd, wat nodig is voor de onderdelen die later in de code gebruikt worden.

Na deze eerste fout volgde een tweede fout: *“KeyboardInterrupt”*. In het begin was het voor mij niet duidelijk wat deze fout betekende en hoe ik die moest oplossen. Daarom heb ik dit opgezocht. Ik ontdekte dat deze melding betekent dat het programma handmatig wordt gestopt door de gebruiker. Omdat mijn programma gebruikmaakt van een game loop, blijft het oneindig draaien.

De conclusie is dus dat dit geen echte fout is, maar dat ik het spelvenster gewoon moet laten openstaan in plaats van het programma zelf te stoppen.

## 04 MEI 2026 (  2 Hours  20 minute ) (filmpje 50:00)

vandaag werk ik verder aan mijn project , het eerste wat mij opvalt is dat het al even geleden is dat ik dit project open gehad heb.Hierdoorweet ik niet zo goed meer waar ik preceis mee bezig was hierdoor ondervindt ik ook waarom een logboek handig kan zijn. Dus lees ik even mijn logboek en  spoel ik de video een beetje terug en kijk ik ook naar de code die ik al geschreven heb.

Zonet heb ik mijn code nog eens bekeken en ben ik weer mee, nu valt het me ook op dat ik nog wat moeite heb met het begrip van een git repo / reposittory en hoe ik deze met dit project correct gebruik. Hiervoor heb ik mijn Lector Daan gecontacteerd.

voor nu werk ik verder aan het project en heb ik ervoor gezorgd dat  De dealerkaarten worden getekend, maar dat de eerste kaart verborgen blijft, (dit wordt aangetoond door middel van vraagtekens (???) )  tot reveal op True staat.

Er valt mij nu ook op dat normaal in echte blackjack de eerste kaart zichtbaar is en de 
tweede kaart verborgen. Ik ben benieuwd of dit in de verdere tutorial aangepast gaat worden , zo niet is dit al een idee om in mijn verdere uitbreiding aan te passen.

## 06 MEI 2026 ( 1 Hours 30 minutes  ) (Einde tutorial)

Ik werk verder aan de game, Nu probeer ik om de scores van mezelf en de dealer op het scherm te krijgen. Een eerste fout dat ik opmerk is dat bij de dealer de score 0 komt te staan, gellukig is hier in de tutorial al een oplossing voor.
Tijdens het volgen van de tutorial kreeg ik af en toe errors deze errors waren vrij gemakkelijk op te lossen. De error ging vaak over een typfout wat zeer belangerijk is want anders werken bepaalde functies niet.
Ondertussen ben ik aan het einde van de tutorial geraakt.


## 08 MEI 2026 ( 3 hours )

Om te bepalen welke uitbreidingen zinvol zijn, speel ik de game eerst opnieuw door en zoek ik online naar bestaande blackjack implementaties.Ik doe dit bewust als eerste stap omdat ik een goed beeld wilde hebben van wat er al bestaat  en wat er eventueel beter kan aan mijn eige versie. 

Als eerste uitbreiding koos ik ervoor om de game visueel aantrekkelijker maken en extra functionaliteit toevoegen. hiervoor wilde ik een start menu maken de reden waarom ik een start menu wilde maken is omdat een game zonder menu je direct in het spel gooit , wat niet gebruiksvriendelijk is. door het menu te maken krijgt de speler controle.

ik starte met het kijken van een tutorial hierin leerde ik hoe ik een menu opbouwde met draw_menu() en draw_game(). en hier buttons aan toe voegde.


Problemen en Oplossingen:

Dubbele functiedefinitie
Bij het implementeren van de tutorial definieer ik per ongeluk een tweede draw_game() functie, terwijl er al één bestond. Python overschrijft de eerste definitie met de tweede, waardoor functionaliteit verloren gaat. De oplossing is beide functies samen te voegen tot één, waarbij de menu-knop altijd zichtbaar is en boven de if not active: conditie geplaatst wordt.

IndexError: list index out of range
Na het samenvoegen run ik de game nog eenss en krijg ik de volgende foutmelding:
IndexError: list index out of range (lijn 243)
Nadat ik lijn 243 bekijk mer ik op dat in de game loop nog steeds buttons[0], buttons[1] en buttons[2] gebruik met de oude indexen. Doordat de menu-knop nu als eerste element aan de lijst toegevoegd wordt, zijn alle indexen met één verschoven. 
Na het aanpassen van de indexen werkt de game opnieuw.
Fout bij de Deal-knop
Na het oplossen van de index-fout merk ik dat de game afsluit wanneer ik op de Deal-knop klik , het tegenovergestelde van wat de bedoeling is. Vermoedelijk zit er een logicafout in de for-loop die de events verwerkt. Dit vereist verder onderzoek.

dit leerde me wel meteen hoe fragiel code kan zijn als je hardcoded indexen gebruikt. 
De volgende keer wil ik liever de knoppen opslaan in een dictionary met een naam als sleutel.

BRONNEN : 
-https://www.youtube.com/watch?v=16DM5Eem0cI
-https://www.youtube.com/watch?v=Y52JsDs4cMQ


## 9 MEI 2026 (  2 hours )
Ik werk verder aan het menu , het probleem was dat de Deal-knop die de game afsloot.
Ik run de game nog eens en ga kijken naar wat de foutmelding precies zegt.
De foutmelding geeft aan dat de fout op lijn 238 zit. Mijn eerste gedacht was dat ik de indexen miss nog niet goed had aangepast maar al snel viel me iets anders op. De menu knop werd wel op het scherm getekend maar stond nooit in button_listt. iK WAS VERGETEN OM DE BUTTON-LISTT.APPEND(menu_btn) toe te voegen. Zonder die regel stond de knop visueel in de game maar bestond hij nog niet voor de event handeing daarom dat ik dus de index fout kreeg.

Ik vond dit interesant  omdat het visueel leek te werken maar onderliggend volledig kapot was . Dit leerde me dat tekenen en logica twee aparte dingen in Pygame zijn. in de toekolst  ga ik er bewusst op letten dat elke knop die ik maak ook aan de lijst toegevoed wordt .

nu runt mijn game zonder errors . Als ik op start game klik krijg ik de volgende opties DEAL HAND of Main menu. dat ziet er al beter uit laat ik gaan kijken wat er gebeurd als ik op beide kloppen klik bv op main menu . oke na het klikken van de main menu button krijg ik terug het start game scherm dat is wat ik wilde. Laat ik ook testen of de game verder nog werkt want het zou kunnen door dat ik aanpassingen gedaan heb dat de game stuk is ... en oef gellukig werkt alles nog hoe dat het zou moeten werken.

De menu knop staat wel heel ongemakkelijk in het midden als ik de game speel , dit stoort me enorm dus laat ik dit oplossen en bijvoorbeeld de button main menu rechtsboven gaan plaatsen. Ik heb de coördinaten aangepast zodat de knop rechtsboven staat wat veel natuurlijker aanvoelt. Kleine UI-aanpassing maar het maakt de game al een stuk aangenamer.



## 10 MEI 2026 (   2 hours )

 Nu speel ik de game nog eens en er valt me iets op de loss counter blijft optellen, ik test of dit bij win counter ook het geval is en merk op dat dit ook bij de win counter blijft optellen dus er is duidelijk iets misgelopen ..

Het probleem was dat add = False die altijd buiten de if moet staan niet buiten de if stond maar binnen. Hierdoor bleef de win / loss counter optellen .. 
Het vinden van deze fout was eig het moeilijkste deel . Omdat de code logish leek maar het gedrag klopte niet. Uiteindelijk heb ik de code regel per regel doorlopen en toen viel me de indentatiefout op .

ik merk op dat het heel belangerijk is zeker in een groter project dat alles correct ingesrpongen staat. Iets waar ik nu zeker op ga letten zodat dit me tijd bespaart met het zoeken naar een probleem .

ik speel de game opnieuw om er zeker van de zijn dat alles correct werkt en ik zie een nieuw probleem , als het spel gedaan is bv ik ben gewonnen dan kan geen nieuw spel starten .. dit was eerder wel het geval als ik op de hit knop duwde starte er een nieuw spel. Maar als ik dan op main menu klik en ik ga terug naar main menu dan krijg ik de optie new hand of deal hand dat is niet wat ik wil. ik denk dat er iets mis loopt . Ik ben er nog niet volledig uit en ga dit in de volgende sessie verder onderzoeken . Als ik er niet snel uitgeraak overweeg ik om de lector te contacteren.


BUGfixes:
-score bleef optellen opgelost door add = False buiten de if te zetten
-calculate_score indentatie probleem opgelost zodat alle kaarten correct worde opgesteld

UI aanpassingen:

-Tiny_font toegevoegd voor main menu tekst
-DEALHAND knop naar beneden verplaatst naar y = 150
- NEW  HAND knop verplaatst naar y = 950 onder scores
- scherm groter gemaakt 







