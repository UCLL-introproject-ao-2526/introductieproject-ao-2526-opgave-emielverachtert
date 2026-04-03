## 03 April 2026 (minute 30:49)

Ik ben gestart met het volgen van de tutorial en heb de stappen stap voor stap uitgevoerd. Al snel merkte ik een eerste fout op: *“font not initialized”*. Deze fout kwam ook voor in de tutorial zelf. Daar werd een oplossing gegeven door `pygame.init()` bovenaan bij de variabelen te plaatsen. Hierdoor worden alle pygame-modules geïnitialiseerd, wat nodig is voor de onderdelen die later in de code gebruikt worden.

Na deze eerste fout volgde een tweede fout: *“KeyboardInterrupt”*. In het begin was het voor mij niet duidelijk wat deze fout betekende en hoe ik die moest oplossen. Daarom heb ik dit opgezocht. Ik ontdekte dat deze melding betekent dat het programma handmatig wordt gestopt door de gebruiker. Omdat mijn programma gebruikmaakt van een game loop, blijft het oneindig draaien.

De conclusie is dus dat dit geen echte fout is, maar dat ik het spelvenster gewoon moet laten openstaan in plaats van het programma zelf te stoppen.
