## 03 April 2026 (1 uur)

Ik ben gestart met het volgen van de tutorial en heb de stappen stap voor stap uitgevoerd. Al snel merkte ik een eerste fout op: font not initialized. Deze fout kwam ook voor in de tutorial zelf. Daar werd een oplossing gegeven door pygame.init() bovenaan bij de variabelen te plaatsen. Hierdoor worden alle pygame-modules geïnitialiseerd, wat nodig is voor de onderdelen die later in de code gebruikt worden.

Na deze eerste fout volgde een tweede fout: KeyboardInterrupt. In het begin was het voor mij niet duidelijk wat deze fout betekende en hoe ik die moest oplossen. Daarom heb ik dit opgezocht. Ik ontdekte dat deze melding betekent dat het programma handmatig wordt gestopt door de gebruiker. Omdat mijn programma gebruikmaakt van een game loop, blijft het oneindig draaien.

De conclusie is dus dat dit geen echte fout is, maar dat ik het spelvenster gewoon moet laten openstaan in plaats van het programma zelf te stoppen.

## 04 MEI 2026 (2 uur 20 minuten ) (filmpje 50:00)

vandaag werk ik verder aan mijn project, het eerste wat mij opvalt is dat het al even geleden is dat ik dit project open gehad heb. Hierdoor weet ik niet zo goed meer waar ik precies mee bezig was hierdoor ondervindt ik ook waarom een logboek handig kan zijn. Dus lees ik even mijn logboek en spoel ik de video een beetje terug en kijk ik ook naar de code die ik al geschreven heb.

Zonet heb ik mijn code nog eens bekeken en ben ik weer mee, nu valt het me ook op dat ik nog wat moeite heb met het begrip van een git repo/reposittory en hoe ik deze met dit project correct gebruik. Hiervoor heb ik mijn Lector Daan gecontacteerd.

Voor nu werk ik verder aan het project en heb ik ervoor gezorgd dat De dealerkaarten worden getekend, maar dat de eerste kaart verborgen blijft, (dit wordt aangetoond door middel van vraagtekens (???) )tot reveal op True staat.

Er valt mij nu ook op dat normaal in echte blackjack de eerste kaart zichtbaar is en de tweede kaart verborgen. Ik ben benieuwd of dit in de verdere tutorial aangepast gaat worden, zo niet is dit al een idee om in mijn verdere uitbreiding aan te passen.

## 06 MEI 2026 (1 uur 30 minuten ) (Einde tutorial)

Ik werk verder aan de game, Nu probeer ik om de scores van mezelf en de dealer op het scherm te krijgen. Een eerste fout dat ik opmerk is dat bij de dealer de score 0 komt te staan, gelukkig is hier in de tutorial al een oplossing voor.

Tijdens het volgen van de tutorial kreeg ik af en toe errors deze errors waren vrij gemakkelijk op te lossen. De error ging vaak over een typefout wat zeer belangrijk is want anders werken bepaalde functies niet.

Ondertussen ben ik aan het einde van de tutorial geraakt.

## 08 MEI 2026 (3 uur)

Om te bepalen welke uitbreidingen zinvol zijn, speel ik de game eerst opnieuw door en zoek ik online naar bestaande blackjack implementaties.Ik doe dit bewust als eerste stap omdat ik een goed beeld wilde hebben van wat er al bestaat en wat er eventueel beter kan aan mijn eigen versie.

Als eerste uitbreiding koos ik ervoor om de game visueel aantrekkelijker te maken en extra functionaliteit toe te voegen. Hiervoor wilde ik een start menu maken de reden waarom ik een start menu wilde maken is omdat een game zonder menu je direct in het spel gooit, wat niet gebruiksvriendelijk is. Door het menu te maken krijgt de speler controle.

Ik start met het kijken van een tutorial hierin leerde ik hoe ik een menu opbouw met draw_menu() en draw_game(). En ik hier buttons aan toe voegde.

Problemen en Oplossingen:

Dubbele functiedefinitie

Bij het implementeren van de tutorial definieer ik per ongeluk een tweede draw_game() functie, terwijl er al één bestond. Python overschrijft de eerste definitie met de tweede, waardoor functionaliteit verloren gaat. De oplossing is beide functies samen te voegen tot één, waarbij de menu-knop altijd zichtbaar is en boven de if not active: conditie geplaatst wordt.

IndexError: list index out of range

Na het samenvoegen run ik de game nog eens en krijg ik de volgende foutmelding:

IndexError: list index out of range (lijn 243)

Nadat ik lijn 243 bekijk merk ik op dat in de game loop nog steeds buttons [0] , buttons [1] en buttons [2] gebruik met de oude indexen. Doordat de menu-knop nu als eerste element aan de lijst toegevoegd wordt, zijn alle indexen met één verschoven.

Na het aanpassen van de indexen werkt de game opnieuw.

Fout bij de deal-knop

Na het oplossen van de index-fout merk ik dat de game afsluit wanneer ik op de deal-knop klik, het tegenovergestelde van wat de bedoeling is. Vermoedelijk zit er een logicafout in de for-loop die de events verwerkt. Dit vereist verder onderzoek.

Dit leerde me wel meteen hoe fragiel code kan zijn als je hardcoded indexen gebruikt.

De volgende keer wil ik liever de knoppen opslaan in een dictionary met een naam als sleutel.

BRONNEN:

-https://www.youtube.com/watch?v=16DM5Eem0cI

-https://www.youtube.com/watch?v=Y52JsDs4cMQ


## 9 MEI 2026 (2 uur)

Ik werk verder aan het menu, het probleem was dat de Deal-knop die de game afsloot.

Ik run de game nog eens en ga kijken naar wat de foutmelding precies zegt.

De foutmelding geeft aan dat de fout op lijn 238 zit. Mijn eerste gedacht was dat ik de indexen miss nog niet goed had aangepast maar al snel viel me iets anders op. het menu knop werd wel op het scherm getekend maar stond nooit in button_listt. Ik was vergeten om de button-list.append(menu_btn) toe te voegen. Zonder die regel stond de knop visueel in de game maar bestond hij nog niet voor de event handeing daarom dat ik dus de index fout kreeg.

Ik vond dit interessant omdat het visueel leek te werken maar onderliggend volledig kapot was. Dit leerde me dat tekenen en logica twee aparte dingen in Pygame zijn. in de toekomst ga ik er bewust op letten dat elke knop die ik maak ook aan de lijst toegevoegd wordt.

Nu runt mijn game zonder errors. Als ik op start game klik krijg ik de volgende opties DEAL HAND of Main menu. Dat ziet er al beter uit laat ik gaan kijken wat er gebeurd als ik op beide kloppen klik. Na het klikken op de main menu button krijg ik terug het start game scherm, dat is wat ik wilde. Laat ik ook testen of de game verder nog werkt want het zou kunnen door dat ik aanpassingen gedaan heb dat de game stuk is... en oef gelukkig werkt alles nog hoe het zou moeten werken.

De menu knop staat wel heel ongemakkelijk in het midden als ik de game speel, dit stoort me enorm dus laat ik dit oplossen en bijvoorbeeld de button main menu rechtsboven gaan plaatsen. Ik heb de coördinaten aangepast zodat de knop rechtsboven staat wat veel natuurlijker aanvoelt. Kleine UI-aanpassing, maar het maakt de game al een stuk aangenamer om te spelen.


## 10 MEI 2026 (3 uur)

Nu speel ik de game nog eens en er valt me iets op. De loss counter blijft optellen, ik ga testen of dit bij de win counter ook het geval is en merk op dat dit ook bij de win counter blijft optellen dus er is duidelijk iets misgelopen ..

Het probleem was dat add=False die altijd buiten de if moet staan niet buiten de if stond maar er binnen. Hierdoor bleef de win/loss counter optellen ..

Het vinden van deze fout was het moeilijkste deel. Omdat de code logisch leek maar het gedrag klopte niet. Uiteindelijk heb ik de code regel per regel doorlopen en toen viel me de indentatiefout op.

ik merk op dat het heel belangrijk is zeker in een groter project dat alles correct ingesprongen staat. Iets waar ik nu zeker op ga letten zodat dit me tijd bespaart met het zoeken naar een probleem.

ik speel de game opnieuw om er zeker van de zijn dat alles correct werkt en ik zie een nieuw probleem, als het spel gedaan is bv ik ben gewonnen dan kan ik geen nieuw spel starten .. dit was eerder wel het geval als ik op de hit knop duwde start er een nieuw spel. Maar als ik dan op main menu klik en ik ga terug naar main menu dan krijg ik de optie new hand of deal hand dat is niet wat ik wil. ik denk dat er iets mis loopt. Ik ben er nog niet volledig uit en ga dit in de volgende sessie verder onderzoeken. Als ik er niet snel uitgeraak overweeg ik om de lector te contacteren.

BUGfixes:

-score bleef optellen opgelost door add=False buiten de if te zetten
-calculate_score indentatie probleem opgelost zodat alle kaarten correct worden opgesteld

UI aanpassingen:

-Tiny_font toegevoegd voor main menu tekst
-DEALHAND knop naar beneden verplaatst naar y=150
- NEW HAND knop verplaatst naar y=950 onder scores
- scherm groter gemaakt


## 11 MEI 2026 (3 uur

Ik ga verder met het oplossen van het vorige probleem.

Het probleem was dat als het spel gedaan was dat ik geen nieuw spel kon starten de button was verdwenen.

Ik ben eerst gaan kijken naar de event handling in de game loop omdat ik vermoede dat de knoppen niet correct reageerde op de spelstatus. ik dacht dat het probleem in draw_game()zat. Dat de verkeerde buttons getoond werden maar na verder onderzoek zag ik dat het probleem dieper zat. de variabele active werd niet correct gereset wanneer ik vanuit het menu terugkeerde naar de game.

De oplossing zat in twee delen, om een nieuw spel te kunnen spelen moesten alle spelvariabelen volledig gereset worden. Als de speler op de main menu knop klikt moet active op False gezet worden zodat als je terug gaat naar het start scherm het juiste scherm getoond wordt met enkel de deal hand knop.

Het moeilijkste was niet het fixen zelf maar begrijpen welke variabelen precies de spelstatus bepaalden. Er waren meerdere variabelen die samen de toestand van de game bepaalde.Als er 1 hiervan niet gereset werd gedroeg de game zich onvoorspelbaar.

Nu dat ik wat functionaliteit heb toegevoegd zou het leuk zijn dat er een muziekje op de achtergrond speelt. Hiervoor heb ik even gegoogeld hoe ik muziek kan toevoegen in pygame. Ik heb gebruik gemaakt van de functie pygame.mixer.init() dit is de audio-engine van pygame. ik heb er voor gekozen om een muziekje uit de pixabay website te downloaden zodat deze niet copyright is en ik deze mag gebruiken. Vervolgens heb ik deze in dezelfde map als mijn project bestanden gezet zodat ik deze kon gebruiken.

Dit was niet zo moeilijk maar toch geeft het een leuke speel ervaring voor de speler.

Het ziet er al tof uit maar als ik met de button terug naar main menu ga wil ik ook dat er een quit button komt te staan. Zodat je vanaf het main menu ervoor kunt kiezen om de game af te sluiten.

Hiervoor heb ik de knop getekend In draw_menu() ik heb gekozen om deze de kleur rood te geven en een lagere positie zodat deze knop onder de start game button staat. En ervoor gezorgd dat de tekst QUIT GAME erop komt.

Ik kreeg een attributen error dit kwam doordat ik de twee buttons als een tuple behandelde wat dus een error gaf. De oplossing hiervoor was om de twee knoppen als losse objecten te behandelen en ervoor gezorgd dat ik in de aanroep ook de quit_btn aanroep. Als laatste moest ik ervoor zorgen dat de knop quit game ook effectief de game afsloot dit heb ik gedaan door de actie run=False te koppelen.

Tijdens deze sessie merkte ik ook op dat er veel aanpassingen nodig zijn aan de UI als ik een nieuwe functie maak en dat ik er dan voor moet zorgen dat de andere functies ook aangepast worden.

## 14 MEI 2026 (3 uur)

Ik heb er nu voor gezorgd dat mijn game aangenamer is voor de speler, ik heb een menu gemaakt waar de speler kan kiezen om het spel te starten of om te stoppen.

Ook heb ik de UI aantrekkelijker gemaakt door kleuraanpassingen te doen en om een muziekje toe te voegen als de game opgestart wordt.

Ik werkte voordien altijd op een extern monitort, nu dat ik de game enkel op mijn laptop speel merk ik dat het speel scherm er niet op past. Ik wil dit gaan aanpassen zodat de game op elk scherm speelbaar is. Ik weet niet zo goed hoe ik hieraan begin dus begin ik met het zoeken naar informatie waarmee ik nadien aan de slag kan gaan.

Ik begin met het importeren van os en volg een paar stappen van de tutorial. Met Deze code zorgt ik ervoor dat Pygame-venster bijna full-screen is, maar met een kleine marge aan de randen. Ik gebruikt de resolutie van het huidige scherm om de grootte dynamisch aan te passen. Ik merk echter dat dit nog niet de beste optie is omdat mijn buttons zicht niet automatisch aanpassen, hiervoor moet ik dus iets aanpassen. Ik heb voor de buttons een vaste positie gekozen wat nu niet meer klopt.Ook denk ik eraan dat dit waarschijnlijk ook het probleem gaat zijn met mijn kaarten en fonts. Ik ga dit verder onderzoeken en stel hierbij een vraag aan chatgpt.

Ik stel de volgende prompt aan chatgpt en krijg de volgende oplossingen aangeboden:

Mijn promt:

Ik heb mijn Pygame-venster bijna full-screen gemaakt. Door gebruik te maken van de resolutie van het huidige scherm, kan de grootte van het venster dynamisch worden aangepast.

Mijn Buttons hebben nog vaste posities, waardoor sommige knoppen buiten het scherm vallen bij andere resoluties.

Welke mogelijke oplossingen kan ik toepassen zodat de knoppen altijd correct op het scherm worden weergegeven, ongeacht de schermgrootte?

Een mogelijke oplossing die ik krijg is het gebruik maken van relatieve posities en schaalfactoren. Om hier meer over te weten ga ik dit eens opzoeken, zo krijg ik een beter inzicht over relatieve posities en schaalfactoren.

## 17 MEI 2026 (3 uur)

Responsive Design toepassen in Pygame Blackjack

tijdens deze sessie heb ik mijn game aangepast zodat de UI correct werkt op verschillende schermresoluties.

Mijn game had overal vaste posities uitgedrukt in pixels voor buttons, kaarten en tekst. Hierdoor vielen deze elementen buiten het scherm of zagen ze er niet goed uit.

Om dit op telossen heb ik als eerste ervoor gezord dat ik schaalvariabelen gedefinieerd heb.

Ik heb een basisresolutie van 600x1100 vastgelegd en de huidige schermgrootte vergeleken met die basisresolutie. Zo kreeg ik twee schaalfactoren, SX voor horizontaal en SY voor verticaal, die ik overal in mijn code kon gebruiken.

Daarna heb ik hulpfuncties geschreven, de functie s(x,y,w, h) schaalt een volledige rechthoek terwijl sx(x) en sy(y) individuele coördinaten schalen.vervolges heb ik de fonts eme laten schalen zodat tekst groter en kleiner wordt afhankelijk van de schermgrootte.

Dan heb ik alle functies aangepast en alle vaste getallen werden vervangen door geschaalde waarden. Daarna heb ik de buttons aangepast

Hier liep ik tegen een specifiek probleem aan. De HIT ME en STAND knoppen werden veel te breed omdat SX op een breed scherm alles horizontaal uitrekte. Een knop die in de basisresolutie 300 pixels breed was werd op mijn scherm meer dan 700 pixels breed. De oplossing was om knoppen een vaste breedte te geven zonder SX en alleen SY te gebruiken voor de hoogte. De tekst centreer ik nu via text.get_rect(center=... ) zodat die altijd netjes in het midden van de knop staat.

Ik kreeg ook een UnboundLocalError omdat ik overal dezelfde variabelenaam tekst gebruikte. De oplossing was om elke tekstvariabele een unieke naam te geven zoals menu_text, deal_text, hit_text enzovoort.

ik heb geleerd dat je bij responsive design een onderscheid moet maken tussen elementen die mee mogen schalen zoals kaarten en posities en elementen die beter een vaste grootte hebben zoals buttons. Ik leerde ook dat de volgorde van de code belangrijk is en dat de schaalvariabelen na het aanmaken van het scherm komen anders werkt screen.get_size() niet goed.

Ik merk ook dat het veel beter was geweest om responsive design vanaf het begin in te bouwen in plaats van achteraf alles aan te passen. Ik heb vandaag heel veel tijd gestoken in het omzetten van vaste getallen die ik eerder had ingevoerd. Als ik een volgend project start ga ik dit meteen correct aanpakken.

## 22 MEI 2026 (3 u)

Nu ga ik mijn project mooi afwerken. Ik ga ervoor zorgen dat alle buttons en tekst correct staan en dat de algemene lay-out er verzorgd uitziet. Nadien speel ik het spel nog eens volledig door om er zeker van te zijn dat alles correct werkt. Ik begin met het startscherm en het valt me meteen op dat de titel nog niet mooi gecentreerd staat, dus pas ik dit als eerste aan.

Ik wou de titel centreren maar gaf eerst vaste coördinaten mee. Al snel besefte ik dat dit niet werkt op andere schermformaten, omdat ik eerder al een responsive design had toegepast. Het probleem was dus dat een hardcoded x-waarde er op mijn scherm goed uitzag, maar op een ander scherm volledig verschoven zou staan. De oplossing was om 'screen.get_size() [0] /2' te gebruiken, zodat het midden altijd dynamisch berekend wordt op basis van de huidige schermbreedte.

Daarna merk ik dat het speelveld mijn tweede monitor ook bedekt, wat uiteraard niet de bedoeling is. Ik probeer dit op te lossen via 'pygame.display.Info()', maar al snel blijkt dat 'info.current_w' de gecombineerde breedte van alle schermen samen teruggeeft in plaats van enkel het main scherm. Ik probeer dan met 'min(info.current_w, ... )' de breedte te beperken, maar dit geeft niet het gewenste resultaat. Uiteindelijk kies ik voor een andere aanpak: ik verwijder de overbodige schermconfiguratie en voeg 'screen=pygame.display.set_mode((0, 0), pygame.NOFRAME)' toe. Dit zorgt ervoor dat het venster correct op één scherm blijft zonder een vaste resolutie hard te coderen. Een nuttige les: pygame geeft bij multi-monitor set-ups de totale breedte terug, niet de breedte van één enkel scherm.

Nu dat ik op het einde van de opdracht zit stuur ik een mail naar mijn Lector om feedback te vragen.

## 01/06 2026

Feedback mail Reflexie:

Het eerste feedback puntje dat ik gekregen heb is dat mijn variabele namen beter kunnen en dat deze niet duidelijk zijn.

Hiermee ben ik het zeker eens want het is belangrijk dat als ik later of iemand anders in de toekomst aan mijn code werkt het duidelijk is, en daarom ga ik dit ook aanpassen.

ik kijk de variabelen namen na en probeer deze te veranderen naar namen die duidelijk zijn waardoor je als je de naam leest meteen weet waarover dit gaat. Vervolgens pas ik gap aan door card_spacing.

Ook lees ik feedback over een typefout, hier heb ik een spelling extentie geinstalleert die me helpt om de spelling van mijn commentaar te verbeteren.

Een verdere feedback op mijn code was dat ik diep aan het nesten ben.

Dit is iets wat beter zou kunnen door meerdere condities in 1 statement te zetten.

Dit heb ik toegepast op mijn code en condities samengevoegd met and.

Wat ik ook nog beter had kunnen doen is een aparte functie maken zodat code niet dubbel staat dit ga ik zeker  meenemen in een volgend project.

ook schaalde ik enkel verticaal wat natuurlijk niet zinvol is omdat ik juist alles probeer mee te schalen en de breedte van btn niet. Dit heb ik opgelost door btn_w ook te schalen.