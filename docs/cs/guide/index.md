# Příručka Audiovisual Core

Název
: Příručka Audiovisual Core

Datum vydání verze
: 2023-02-24

Datum vytvoření
: 2013-10-15

Součást TDWG Standardu
: <http://www.tdwg.org/standards/638>

Tato verze
: <http://rs.tdwg.org/ac/doc/guide/2023-02-24>

Poslední verze
: <http://rs.tdwg.org/ac/doc/guide/>

Předchozí verze
: <http://rs.tdwg.org/ac/doc/guide/2013-10-15>

Abstrakt
: Audiovisual Core je soubor slovníků určených k reprezentaci metadat pro multimediální zdroje a sbírky týkající se biologické rozmanitosti. Tento nenormativní dokument poskytuje některé základní informace o cílech a použití normy.

Přispěvatelé
: [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) ([University of Massachusetts at Boston, USA](http://www.wikidata.org/entity/Q15144)), [Vijay Barve](https://orcid.org/0000-0002-4852-2567) (), [Mihail Carausu](https://orcid.org/0000-0002-8234-0599) ([Danish Biodiversity Information Facility (DanBIF), Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [Vishwas Chavan](https://orcid.org/0000-0002-3425-6499) ([Global Biodiversity Information Facility, Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [José Cuadra](http://www.wikidata.org/entity/Q51883873) (), [Chris Freeland](https://orcid.org/0000-0002-2541-5822) ([Missouri Botanical Garden, St. Louis, USA](http://www.wikidata.org/entity/Q1852803)), [Gregor Hagedorn](https://orcid.org/0000-0001-7023-7386) ([JKI, Federal Research Institute for Cultivated Plants, Berlin, Germany](http://www.wikidata.org/entity/Q832099)), [Patrick Leary](https://orcid.org/0000-0001-5172-8577) (), [Dimitry Mozzherin](https://orcid.org/0000-0003-1593-1417) ([Encyclopedia of Life, Woods Hole, USA](http://www.wikidata.org/entity/Q82486)), [Annette Olson](https://orcid.org/0000-0002-0772-0022) ([American Association for the Advancement of Science](http://www.wikidata.org/entity/Q40358)), [Greg Riccardi](https://orcid.org/0000-0002-3850-9983) ([Florida State University, Tallahassee, USA](http://www.wikidata.org/entity/Q861548)), [Ivan Teage](https://orcid.org/0000-0003-4176-2274) ()

Tvůrce
: GBIF/TDWG Pracovní skupina pro multimediální zdroje a Skupina pro údržbu audiovizuálního jádra

Bibliografická citace
: GBIF/TDWG Multimedia Resources Task Group and Audiovisual Core Maintenance Group. 2023. Příručka Audiovisual Core. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/guide/2023-02-24>

## 1. Úvod

Audiovisual Core Multimedia Resources Metadata Schema (Audiovisual Core) je datový standard pro výměnu dat popisujících multimediální zdroje a sbírky týkající se biologické rozmanitosti, který vytvořila společná pracovní skupina GBIF/TDWG pro metadata multimediálních zdrojů (MRTG).  Norma se skládá ze čtyř dokumentů.  Tento dokument je průvodcem po cílech a použití normy. Dokument Úvod do Audiovisual
Core poskytuje stručný úvod do Audiovisual Core Standard. Podrobné informace o struktuře Audiovisual Core naleznete v dokumentu [Audiovisual Core Structure](structure).  Podrobnosti o termínech najdete v dokumentu [Seznam termínů Audiovisual Core](terms).

Zkratky a názvy institucí a projektů jsou uvedeny ve slovníku v
příloze I.

### 1.1 Status obsahu tohoto dokumentu

Všechny části tohoto dokumentu jsou nenormativní.

## 2 Shrnutí

Audiovisual Core Multimedia Resources Metadata schema („schéma AC“ nebo
jednoduše „AC“) je soubor slovníků metadat pro popis
multimediálních zdrojů a sbírek souvisejících s biologickou rozmanitostí. Specifikace
je nezávislá na tom, jak mohou být tyto slovníky
zobrazeny pro strojové využití.

Multimediální zdroje jsou digitální nebo fyzické artefakty, které obvykle
obsahují více než jen text. Mezi ně patří obrázky, umělecká díla, kresby,
fotografie, zvukové záznamy, videa, animace, prezentační materiály a
interaktivní online média, včetně např. identifikačních nástrojů. Multimediální
sbírka je souborem takovýchto objektů, ať už kurátorských
či nikoli, a ať už elektronicky přístupných či nikoli. Pro účely
tohoto dokumentu považujeme soubor multimediálních zdrojů sám o sobě
za ‘multimediální zdroj’. Kdykoli se diskuse nebo specifikace může
vztahovat pouze na sbírku nebo pouze na jeden mediální zdroj, výslovně to uvádíme.

Multimediální popisy jsou digitální záznamy, které dokumentují základní
multimediální zdroje nebo sbírky. AC se zaměřuje na
multimediální zdroje související s biologickou rozmanitostí. Sdílí terminologii a
zájmy s mnoha známými a důležitými standardy pro popis
přístupu k zdrojům, jako jsou Dublin Core (DC), Darwin Core (DwC),
Adobe Extensible Metadata Platform (XMP), International Press and
Telecommunications Council (IPTC), Metadata Working Group (MWG)
schema, Natural Collections Schema (NCD) a další. V případě
přesné shody s použitím těchto standardů přijímá AC jejich
identifikátory a definice. Mnohé sbírky multimédií o biologické rozmanitosti
již obsahují popisy svých médií vyjádřené v DwC nebo DC. Použitím
těchto slovníků tam, kde je to vhodné, chce AC zejména usnadnit
opětovné použití stávajících popisů v těchto sbírkách,
v případě potřeby doplněných o další termíny.

Tato příručka doprovází normativní části standardu AC,
které jsou obsaženy ve dvou dokumentech: v dokumentu popisujícím strukturu dokumentu <sup id="cit-1">[\[1\]](#fn-1)</sup>
a v dokumentu se seznamem termínů <sup id="cit-2">[\[2\]](#fn-2)</sup>. Seznam termínů
dokumentuje řadu termínů, z nichž každý je identifikován jedinečným
identifikátorem URI (Uniform Resource Identifier), spolu s normativními definicemi.
Kromě toho může skupina Audiovisual Core Maintenance Group vyvinout doporučené reprezentace pro popisy AC v několika důležitých formátech, včetně RDF <sup id="cit-3">[\[3\]](#fn-3)</sup>, XML
Schema <sup id="cit-4">[\[4\]](#fn-4)</sup> a Comma Separated Values (CSV) <sup id="cit-5">[\[5\]](#fn-5)</sup>.

Obrázek 1 níže doplňuje část obrázku 2 nenormativní
části dokumentu NCD <sup id="cit-6">[\[6\]](#fn-6)</sup>. Ukazuje řadu druhů
zdrojů zaměřených na data o biologické rozmanitosti a ilustruje typické uživatelské
komunity, standardy dat a metadat a síťové služby, které
podporují vyhledávání, analýzu a integraci dat. Z údajů NCD jsme extrahovali
zdroje a vztahy mezi nimi, které
jsme doplnili o tři typy, které nespadají do hlavní působnosti NCD. Jedná se o:
Pozorování, ekologické modely a zaměření této práce, multimediální
zdroje. Aplikace využívající každý z těchto druhů zdrojů nacházejí
uplatnění, nebo někdy vyžadují použití multimediálních zdrojů k
jejich dokumentaci. Například Biological Heritage Library je projekt,
který poskytuje naskenované obrázky starší literatury v mnohem větším rozsahu,
než kolik může poskytnout digitalizovaných verzí založených na optickém rozpoznávání znaků,
a tyto obrázky zůstávají k dispozici jako zdroje pro jakékoli
následné odvozené produkty. Digitálně zpracovaná historická literatura je tedy
dokumentována pomocí obrázků stránek. Většina vědecké literatury je samozřejmě také ilustrována fotografiemi, grafy nebo jinými artefakty, které spadají do působnosti Audiovisual Core. Dokonce i poskytovatelé zdrojů „molekulární DNA“ někdy nabízejí původní data ve formě digitálních obrazů na mikročipech.

![](assets/images/guide_fig_1.png)

Obrázek 1. Vztahy multimediálních zdrojů k primárním typům
zdrojů biologické rozmanitosti

## 3 termíny Audiovisual Core

Záznam Audiovisual Core je popis multimediálního zdroje pomocí termínů Audiovisual Core. AC specifikuje dva druhy termínů:
_termíny na úrovni záznamu_ a _termíny na úrovni přístupu._ Termíny na úrovni záznamu se vztahují
k popisovanému mediálnímu zdroji. Téměř všechny termíny jsou termíny na úrovni záznamu. Jeden z těchto termínů, _serviceAccessPoint_, hraje zvláštní roli při
vyhledávání zdroje, který záznam popisuje. Multimediální
zdroj může mít více než jeden serviceAccessPoint, z nichž každý je
popsán hodnotami jednoho nebo více termínů přístupové úrovně. Termíny na úrovni přístupu
poskytují informace, jako je webová adresa, na které lze získat digitální
zobrazení zdroje, velikost takového
získaného objektu atd.

Záznam Audiovisual Core je tedy soubor termínů, který je v souladu s
normativními dokumenty, obsahuje alespoň čtyři povinné termíny
popsané níže a poskytuje metadata popisující jeden
multimediální zdroj (případně včetně sbírky). Obvykle obsahuje identifikátor, který mohl být zdroji přidělen externí autoritou nebo poskytovatelem záznamu metadat.

Každý termín Audiovisual Core má prostý textový název, URI a prostý textový
normativní definici. Termíny mohou také obsahovat pokyny k použití, které vysvětlují, jak se termín používá v kontextu Audiovisual Core, a poznámky, které poskytují další informace a příklady.  URI pro termíny odpovídají schématu http URI.
Neformálně lze toto pochopit takto: http URI má syntaxi
http URL, ale neočekává se, že jeho zadání do webového
prohlížeče povede k vrácení jakýchkoli informací do prohlížeče,
a pokud ano, vrácené informace nemusí mít žádný význam.

Protože adresy URL jsou poměrně dlouhé, dokumenty AC se řídí standardní
praxí zavádění krátké předpony sestávající z „kvalifikátoru jmenného prostoru“
odděleného dvojtečkou od mnemotechnického názvu úzce souvisejícího s
názvem termínu. Jmenný prostor termínů převzatých z jiných slovníků je stejný jako jmenný prostor původních termínů. Jmenný prostor termínů denovo AC je
http://rs.tdwg.org/ac/terms/. V tabulce termínů má každý termínový záznam
řádek s názvem termínu. V souladu s praxí Darwin Core term
list <sup id="cit-7">[\[7\]](#fn-7)</sup> je název tohoto termínu v případě vypůjčených termínů obecně
„nekvalifikovaným názvem“, před kterým je uvedena široce přijímaná předpona označující
zkratku pro jmenný prostor, zatímco u termínů AC denovo není taková
předpona před termínem uvedena. Implementátorům, kteří potřebují předponu jmenného prostoru pro jmenný prostor AC, se doporučuje používat "ac", kdykoli je to možné. Výsledek
se nazývá kvalifikovaný název. Například normativní wiki
dokumentace pro vypůjčený termín dcterms:identifier má URI
http://purl.org/dc/terms/identifier. V tomto dokumentu budeme dodržovat zavedenou
konvenci kvalifikovaných názvů. Ve
skutečnosti se většina URI pro termíny převzaté z externích slovníků
(asi polovina z nich) ve skutečnosti odkazuje na něco v příslušné
dokumentaci pro daný externí standard. Někdy to není přesné,
protože dokumentace je ve formátu PDF a několik (různých\!)
URI mohou zřejmě směřovat na stejné místo.

Příklady z termínového seznamu jsou uvedeny
níže.

<table>
	<tbody>
		<tr>
			<td>Název termínu:</td>
			<td>dcterms:type</td>
		</tr>
		<tr>
			<td>Normativní URI:</td>
			<td><a href="http://purl.org/dc/terms/type" rel="nofollow">http://purl.org/dc/terms/type</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>Typ</td>
		</tr>
		<tr>
			<td></td>
			<td>Vrstva:&nbsp;1 —&nbsp;Požadováno:&nbsp;Ano —&nbsp;Opakovatelné:&nbsp;Ne</td>
		</tr>
		<tr>
			<td>Definice:</td>
			<td>Povaha nebo druh zdroje.</td>
		</tr>
		<tr>
			<td>Použití:</td>
			<td>Úplný URI, nejlépe z typu URI specifikovaného ve slovníku typů DCMI, <a href="http://dublincore.org/documents/dcmi-type-vocabulary/#section-7-dcmi-type-vocabulary" rel="nofollow">http://dublincore.org/documents/dcmi-type-vocabulary/#section-7-dcmi-type-vocabulary</a>. Doporučené termíny jsou ty URI, jejichž označení jsou Collection, StillImage, Sound, MovingImage, InteractiveResource nebo Text (např. . Doporučujeme také úplné URI adresy ac:PanAndZoomImage, ac:3DStillImage a ac: 3DMovingImage. Hodnoty NESMÍ být řetězcem, ale URI s úplným jmenným prostorem (např. z řízeného slovníku. Implementátoři a komunity praxe mohou určit, zda je nutné používat konkrétní řízené slovníky. Pokud je zdroj sbírkou, tato položka neurčuje, jaké typy objektů může obsahovat. V souladu s doporučeními DC na adrese <a href="http://purl.org/dc/dcmitype/Text" rel="nofollow">http://purl.org/dc/dcmitype/Text</a> by obrázky textu měly mít tuto URI.</td>
		</tr>
		<tr>
			<td>Poznámky:</td>
			<td>V souladu s doporučeními DC pro typ textu <a href="http://purl.org/dc/terms/DCMIType" rel="nofollow">http://purl.org/dc/terms/DCMIType</a> by obrázky textu měly být uvedeny jako http://purl.org/dc/dcmitype/Text, pokud jsou uvedeny jako URI. Viz také heslo dc:type v dokumentu Audiovisual Core term list (Seznam základních audiovizuálních termínů) a viz DCMI FAQ on DC and DCTERMS Namespaces (Často kladené otázky týkající se jmenných prostorů DC a DCTERMS), <a href="https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md" rel="nofollow">https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, kde se diskutuje o důvodech pro použití termínů ve dvou jmenných prostorech. Obvyklým postupem je použít stejný štítek, pokud jsou k dispozici oba. Štítky nemají žádný vliv na vyhledávání informací a slouží pouze jako doporučení. Je nutné zadat alespoň jeden z údajů dc:type a dcterms:type, ale pokud je to možné, zadání obou údajů může zvýšit užitečnost metadat. Hodnoty každého z nich by měly označovat stejný typ, ale v případě nejednoznačnosti má přednost dcterms:type.</td>
		</tr>
	</tbody>
</table>

<table>
	<tbody>
		<tr>
			<td>Název termínu:</td>
			<td>ac:reviewerLiteral</td>
		</tr>
		<tr>
			<td>Normativní URI:</td>
			<td><a href="http://rs.tdwg.org/ac/terms/reviewerLiteral" rel="nofollow">http://rs.tdwg.org/ac/terms/reviewerLiteral</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>Recenzent</td>
		</tr>
		<tr>
			<td></td>
			<td>Vrstva:&nbsp;2 —&nbsp;Požadováno:&nbsp;Ne —&nbsp;Opakovatelné:&nbsp;Ano</td>
		</tr>
		<tr>
			<td>Definice:</td>
			<td>Řetězec obsahující jméno recenzenta. Pokud je přítomen, pak je zdroj recenzován, i když komentáře recenzenta chybí nebo jsou prázdné. Jeho přítomnost udává, zda odborník na dané téma, o kterém se píše v médiích, recenzoval daný mediální příspěvek nebo sbírku a schválil popis jeho metadat; musí být uvedeno jméno nebo doslovný výraz „anonymní“ (= anonymně recenzováno).</td>
		</tr>
		<tr>
			<td>Poznámky:</td>
			<td>Poskytovatel tvrdí, že tuto recenzi přijímá jako kompetentní. Viz také ac:reviewer a část Jmenné prostory, předpony a názvy termínů v dokumentu Audiovisual Core Term List, kde se diskutuje o důvodech pro oddělení termínů, které používají hodnoty URI, od termínů, které používají textové hodnoty, pokud jsou možné obě varianty. Obvyklým postupem je použít stejný štítek, pokud jsou k dispozici oba. Štítky nemají žádný vliv na vyhledávání informací a slouží pouze jako doporučení.</td>
		</tr>
	</tbody>
</table>

Hlavní kvalifikátory jmenného prostoru pro termínové URI v tomto dokumentu jsou

- **dcterms:** a **dc:** Slovník DCMI dokumentovaný na adrese
  http://dublincore.org/documents/dcmi-terms

- **dwc:** Slovník Darwin Core popsaný na adrese
  http://rs.tdwg.org/dwc/index.htm

- **Iptc4ampExt:** Geografická rozšíření IPTC s jmenným prostorem
  http://iptc.org/std/Iptc4xmpExt/2008-02-29/ zdokumentovaná v
  http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf

- **ac:** Termíny v jmenném prostoru http://rs.tdwg.org/ac/terms které nepocházejí
  z jiných řízených slovníků.  Normativní definice těchto dokumentů lze nalézt v [dokumentu Seznam termínů Audiovisual Core](termlist.md)

- **xmp:** Slovníky Adobe XMP s jmenným prostorem
  http://ns.adobe.com/xap/1.0/, dokumentované v oddíle 8.4 dokumentu
  https://wwwimages2.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2016-08/XMPSpecificationPart1.pdf

- **xmpRights:** Slovník práv Adobe XMP s jmenným prostorem
  http://ns.adobe.com/xap/1.0/rights, dokumentovaný v oddíle 8.5 na adrese
  https://wwwimages2.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2016-08/XMPSpecificationPart1.pdf

- **photoshop:** Další vlastnosti Adobe XMP s jmenným prostorem http://ns.adobe.com/photoshop/1.0/ jsou dokumentovány na adrese http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2014-12/XMPSpecificationPart2.pdf

- **exif:** slovník formátu Exchangeable Image File Format asociace Camera and Imaging Products Association s jmenným prostorem http://ns.adobe.com/exif/1.0/ zdokumentovaný v http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf

## 4 Motivace a odůvodnění

Existuje mnoho cenných multimediálních zdrojů, které neobsahují žádné informace uložené v databázích. Někteří mohou mít webovou prezentaci, jiní nikoli. I ty, které jsou
dostupné online, nemusí být pro vyhledávače dostatečně zjistitelné,
nebo se mohou ztratit v záplavě obrázků z nespolehlivých zdrojů. Stručný
popisný záznam, jak je definován standardem Audiovisual Core, může sloužit jako
„vizitka“ multimediálního zdroje a poskytovat dostatek
informací k identifikaci a vyhledání mediálních zdrojů výzkumníky,
agregátory, rozhodovacími činiteli, pedagogy nebo širokou veřejností.

Standard umožňuje agregaci popisů multimediálních zdrojů
z mnoha zdrojů a usnadňuje vyhledávání zdrojů, včetně
vytváření vztahů mezi multimediálními zdroji na několika
místech. Záznamy AC lze také použít jako pomůcku pro procesy správy multimediálních
zdrojů, což umožňuje instituci udělat krok
zpět a zjistit, které sbírky nejvíce potřebují konzervaci nebo by
měly vyšší prioritu pro katalogizaci na úrovni jednotlivých položek.

Mezi důležité využití identifikované pracovní skupinou, které jsou usnadněny
metadaty, patří:

1. Objevování;

2. Hodnocení vhodnosti použití před načtením zdroje
   (zejména relevantní pro offline zdroje);

3. Použití záznamů metadat jako potenciálního důkazu výskytu taxonu nebo
   jiných biologických závěrů, jako jsou důkazy o interakcích druhů, stanovištích a fenotypových variacích;

4. Identifikační pomůcky;

5. Snížení zátěže poskytovatelů a producentů multimediálních zdrojů při
   shromažďování a poskytování zdrojů od široké škály
   producentů a správců, zejména těch, kteří mají malé nebo žádné znalosti
   v oblasti IT nebo podpory.

Aby byly překážky použití co nejmenší, jsou pouze čtyři
vlastnosti záznamu Audiovisual Core považovány za povinné:

1. Identifikátor (dcterms:identifier): libovolný kód, který je jedinečný
   pro daný zdroj, přičemž zdrojem může být poskytovatel,
   sbírka nebo mediální položka. Zatímco identifikátor musí být globálně
   jedinečný pro poskytovatele a sbírky (např. URI), identifikátory pro
   mediální položky mohou být jedinečné pouze v kontextu sbírky nebo
   poskytovatele. Ve skutečnosti standard důrazně doporučuje, ale nevyžaduje
   identifikátor pro mediální položky, ačkoli jej vyžaduje pro
   poskytovatele nebo sbírku.

2. Typ (dcterms:type): Lze použít jakýkoli termín typu dcmi z
   http://dublincore.org/documents/dcmi-type-vocabulary/#section-7-dcmi-type-vocabulary.
   Doporučené termíny jsou Collection (sbírka), StillImage (statický obrázek), Sound (zvuk), MovingImage (pohyblivý obrázek),
   InteractiveResource (interaktivní zdroj) a Text.

3. Jazyk metadat (ac:MetadataLanguage): Jazyk popisu a
   dalších metadat (ale ne nutně samotného obrázku)

4. Prohlášení o autorských právech (dcterms:rights): Informace o právech držených
   v rámci daného zdroje a nad ním. Úplné znění čitelného prohlášení o autorských právech,
   jak vyžadují vnitrostátní právní předpisy držitele autorských práv. U
   sbírek se to vztahuje na všechny obsažené objekty, pokud
   objekt sám nemá jiné prohlášení. Pokud je to možné, doporučuje se také
   uvedení vlastníka autorských práv pomocí xmpRights:Owner

Kromě toho se důrazně doporučuje uvést stručný název zdroje
pomocí dcterms:title

## 5 Stávající normy

Audiovisual Core má v úmyslu poskytovat metadata, která popisují buď samotné mediální
zdroje, nebo jejich sbírky. Existuje několik
známých nebo nově vznikajících standardů, které se těmito otázkami zabývají, takže
by se dalo položit otázku: proč je prostě nepoužít? Ve skutečnosti AC dělá přesně to v
přibližně polovině svých 80 prvků, z nichž téměř všechny jsou volitelné. Jak je
uvedeno výše, většina povinných termínů pochází z externích
řízených slovníků. Všechny existující řízené slovníky,
zejména široce používaný Dublin Core, však nabízejí velmi málo možností
poskytovat metadata obsahu mediálních zdrojů, která jsou specificky
biologicky relevantní. Použití samotného Dublin Core by
ztěžovalo vyhledávání mediálních zdrojů s vysokou přesností. Jedním z důsledků použití pouze Dublin Core by tedy bylo, že dotazy nebudou dostatečně selektivní. Naproti tomu standard Darwin Core TDWG <sup id="cit-8">[\[8\]](#fn-8)</sup>
některé z těchto otázek více podporuje, ale málo se zabývá důležitými
otázkami práv duševního vlastnictví nebo způsoby vyjádření vztahů
mezi alternativními verzemi mediálních zdrojů (např. verzemi s různým rozlišením). Na druhou stranu ani jeden z těchto kontrolovaných slovníků nemá
mechanismy pro zachycení technických metadat, jako jsou EXIF, které
samotné zobrazovací systémy nebo nástroje pro vkládání metadat, jako je Adobe
Photoshop(tm) a open source editor obrázků GIMP, mohou vkládat do
mediálních souborů a streamů. Abychom tento problém vyřešili a podpořili výše uvedené cíle,
mělo by být Audiovisual Core považováno za syntézu DC,
DwC a, tam kde jsou tyto formáty nedostatečné, některých progresivních standardů metadat,
které výrobci kamer v současné době plánují
podporovat v samotných kamerách, podobně jako nyní používají EXIF <sup id="cit-9">[\[9\]](#fn-9)</sup>.
Pokud některá z těchto norem postačuje, jsou termíny a definice metadat AC
termíny a definicemi těchto norem. V některých případech jsme zjistili, že žádný z
těchto návrhů neřeší problémy, které podle našich zkušeností trápí širokou
škálu přispěvatelů obrázků, zejména těch, kteří mají omezený přístup k
sofistikovaným IT pracovníkům nebo digitálním knihovníkům. Schéma AC lze považovat za rozšíření sjednocení malých podskupin několika přijatých standardů (spolu s rámcem, který zajišťuje, že použití metadat z těchto standardů mohou lidé i stroje chápat jako odkaz na stejný zdroj). Jinými slovy, velkou část AC lze
považovat za obal kolem DwC, DC, XMP a IPTC <sup id="cit-10">[\[10\]](#fn-10)</sup>.

Vzhledem k tomu, že drtivá většina polí metadat AC je volitelná,
poskytovatel zdrojů, který již může poskytovat metadata Dublin Core, by
v podstatě nemohl poskytovat nic jiného než to, plus vhodný globálně jedinečný
identifikátor, který by propojil všechna metadata se stejným objektem. Podobně
poskytovatel, který popisuje obsah obrázku výhradně pomocí termínů Darwin Core, nemusí
dělat o moc víc. Oba tito poskytovatelé by však zjistili, že
služby s přidanou hodnotou, jako jsou indexovače metadat a agregátory mezipaměti,
by byly méně pravděpodobné, že by uchovávaly odkazy na své mediální zdroje a
metadata, než kdyby měly bohatší metadata. To poskytovatelům dává jasnou strategii,
jak zvýšit užitečnost svých multimediálních zdrojů s
malým nebo žádným dopadem na jejich služby IT kyberinfrastruktury. Možná budou
potřebovat pouze aktualizovat přiřazení mezi svými interními názvy polí a
metadatovými termíny specifikovanými AC, jakmile budou mít k dispozici personál, který to provede.
Jakmile bude k dispozici více zdrojů pro zaznamenávání dalších metadat a jakmile
vzniknou mechanismy komunitních anotací, které to podpoří, budou moci přidávat
další metadata tempem, které si samy určí podle svých zdrojů. Pokud
sběratelé metadat sledují (volitelnou) vlastnost Metadata Date
(xmp:MetadataDate), mohou být aktualizovaná metadata automaticky načtena
těmito službami s přidanou hodnotou a více dotazů vrátí metadata poskytovatele
a odkazy na jeho mediální zdroje.

## 6 Časté obavy týkající se jiných standardů pro informace o biologické rozmanitosti

Audiovisual Core považuje sbírky multimediálních zdrojů samotné
za druh zdroje. Mnoho typů sbírek lze popsat v
navrhovaném standardu TDWG Natural History Collections (NCD). Pokud
poskytovatel chce pouze umožnit vyhledávání multimediální sbírky
bez ohledu na vyhledávání a přístup k jejímu obsahu (kromě
podsbírek), často nebude mít význam, zda jsou poskytována metadata NCD nebo AC,
nebo obojí. To platí tím spíše, pokud mají NCD
CollectionIdentifier a Audiovisual Core Identifier stejnou
hodnotu. Zatímco typy Audiovisual Core Collection jsou bohatší než typy NCD,
zůstává otevřenou otázkou, zda je rozmanitost Audiovisual Core v tomto případě
užitečná.

Existuje značné překrývání s používáním termínů Darwin Core, zejména pokud jde o
taxonomické, geografické a časové pokrytí dat
popisovaných záznamem metadat. Pro většinu těchto metadat používáme termíny DwC a celý slovník geolokace Darwin Core
je zahrnut jako reference. GPS souřadnice, které jsou stále častěji součástí
obrazových dat pořízených fotoaparáty, lze snadno přiřadit k „doslovným“
lokálním termínům Darwin Core.

## 7 Problémy, které nejsou zdůrazněny v jiných standardech pro informace o biologické rozmanitosti

Některé z zde zmíněných problémů se týkají také bibliografických
metadat, jako je Dublin Core. Tyto otázky však nejsou výslovně
podrobně řešeny ve stávajících standardech TDWG pro biologickou rozmanitost a některé z nich
nejsou dostatečně řešeny ani v DC. Některé z těchto obav jsou uvedeny níže.

**Velikost**: Jednotlivé multimediální zdroje, jako jsou obrázky a zejména
videa a zvuky, jsou ve srovnání se záznamy o vzorcích, pozorovacími
údaji nebo popisy druhů velmi velké. Hlavním důsledkem toho je, že
multimediální metadata musí podporovat případy použití, ve kterých lidé nebo softwaroví
agenti mohou, aniž by museli načítat zdroj, pokusit se posoudit vhodnost
podkladového mediálního zdroje pro požadované použití, obvykle pomocí
vyhledávání založeného na podrobném kontrolovaném slovníku. Bez
náhodného vyhledávání v přirozeném jazyce však není možné, ani při
použití DC a DwC, aby poskytovatel metadat odpověděl na požadavek typu
„Poskytněte mi velikosti a přístupové body URL pro statické obrázky
_Dictyophora indusiata_, které mají k dispozici španělská metadata“.

**Práva duševního vlastnictví**: DwC popisuje fyzické objekty, jejichž vlastnictví se obecně řídí majetkovými zákony, které nejsou považovány za součást souboru práv duševního vlastnictví. Některé připravované normy týkající se vědecké literatury se těmito otázkami zabývají, ale málokdy jsou otázky týkající se povolení k reprodukci publikací tak rozmanité jako v případě multimédií, která byla v minulosti považována za kreativní umělecká díla, nikoli nutně za fakta.

**Původ**: U všech vědeckých údajů je samozřejmě důležité vědět, jak a kdy mohly být údaje od svého původního shromáždění změněny.
To je zvláště důležité pro média, která jsou běžně upravována pro ten či onen účel. Pokud se to provede neopatrně, může to zničit část užitečnosti upraveného objektu. Žádné normy TDWG ani navrhované normy se nezdají být velmi robustní, pokud jde o provenienci, včetně Audiovisual Core, který poskytuje pouze vlastnost Derived From (odvozeno z) za účelem poskytnutí odkazu na jiný zdroj. To je do jisté míry podobné termínu NCD DerivedCollection, který identifikuje záznam kolekce jako vytvořený dotazem na jinou kolekci. To však zjevně neidentifikuje zdrojovou sbírku ani dotaz. Budoucí verze Audiovisual Core přidá další termíny týkající se původu.

## 8 Popisy multimediálních zdrojů

Termín multimediální zdroje zahrnuje širokou škálu objektů, které jsou zajímavé pro biology a komunity, s nimiž spolupracují v oblasti výzkumu, vzdělávání a veřejných služeb. Některé příklady multimédií jsou známé. To zahrnuje:

- Statické snímky z fotoaparátů, skenerů nebo lékařských a průmyslových zobrazovacích zařízení

- Filmy se zvukem nebo bez zvuku

- Zvukové nahrávky

V některých z výše uvedených případů mohou tyto zdroje existovat v elektronické nebo neelektronické podobě nebo v obou. Elektronická forma může být analogová nebo digitální, přičemž digitální forma je vhodnější pro ukládání a výměnu s počítači. Digitální forma může být digitální od počátku, tj. původně zachycena jako digitální objekt, nebo může být vytvořena z nedigitálního objektu. Stejně jako v případě záznamů o biologických vzorcích, publikací, terénních poznámek, experimentálních dat a dalších artefaktů vědecké praxe existuje velké množství takového materiálu, který dosud nebyl digitalizován, ale který může být k dispozici, i když s většími náklady a nepohodlím než digitální zdroje. Tyto analogové (včetně papírových) zdroje stále vyžadují popisná metadata, aby se usnadnilo jejich vyhledávání a ověřila se jejich vhodnost pro použití. Stejně důležité je, že některá metadata mají sama o sobě vědecký a vzdělávací význam, i když daný objekt není snadno přístupný. Jedním z takových použití je důkaz o výskytu georeferencovaného taxonu.

Metadata Audiovisual Core mohou také popisovat zdroje, které nejsou tak často považovány za multimediální objekty. To zahrnuje:

- Interaktivní softwarové aplikace, buď na webu, nebo dostupné
  pro samostatné použití

- Taxonomické identifikační klíče

- Sbírky multimediálních zdrojů

- Webové stránky, které nespadají do žádné z výše uvedených kategorií

## 9 záznamy Audiovisual Core

Normativní specifikace záznamů audiovizuálních základních metadat je nezávislá
na způsobu, jakým jsou tyto záznamy převáděny do elektronické podoby.
MRTG má v úmyslu zveřejnit specifikace pro takové zobrazení reprezentované
v XML omezeném XML schématem a reprezentované v
prostém textu jako hodnoty oddělené čárkami (CSV). [Části 4.4 až 4.5 specifikace dokumentace standardů TDWG](https://github.com/tdwg/vocab/blob/master/sds/documentation-specification.md#44-vocabularies-term-lists-and-terms) popisují, jak by měla být základní metadata termínů vyjádřena ve strojově čitelných formátech, jako jsou serializace RDF.  Budoucí pracovní skupina by mohla vyvinout sémanticky bohatší strojově čitelnou ontologii podle postupů uvedených v [sekci 4 specifikace údržby slovníku TDWG](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements).

Jazykem normativní specifikace Audiovisual Core je angličtina, ale
to nijak neomezuje aplikace v používání štítků nebo obsahu
metadat v místních jazycích. Protože je jazykem normativního dokumentu angličtina, má každ
metadatová položka v normativním dokumentu anglický název (který
může být například součástí uživatelského rozhraní), ale ani tyto názvy
nemusí být aplikacemi používány, ačkoli se jejich použití důrazně
doporučuje, alespoň v dokumentaci.

Jak již bylo zmíněno, záznam metadat Audiovisual Core je soubor termínů
popisujících základní multimediální zdroj, který záznam popisuje.
Každý termín je identifikován jednotným identifikátorem zdroje (URI). Jedná se o URI atributu, nikoli základního zdroje, a pouze specifikují, který termín je poskytován. Existuje mnoho schémat URI, z nichž některá byla zaregistrována u Internet Assigned Names Authority (IANA). Všechny URI Audiovisual Core termínů jsou v souladu se schématem http URI. Toto bylo zvoleno proto, že toto široce používané schéma URI používá jako syntaxi URI známou syntaxi internetových adres URL. Tato známost však vede k častému omylu, a to že vložení URI do adresního řádku prohlížeče nebo jeho zadání do jiné aplikace, která respektuje protokol http, by mělo vést k tomu, že aplikace vrátí nějaké informace o objektu identifikovaném URI. Takové chování se obvykle nazývá rozlišení (nebo, technicky řečeno, rozlišení a dereference) URI a není v žádném případě zaručeno pro URI termínů Audiovisual Core. Pokud je to možné, snažíme se, aby adresy URI protokolu HTTP byly rozlišitelné a aby vrácené informace obsahovaly dokumentaci o tom, jak je atribut metadat identifikovaný touto adresou URI definován nebo používán. Zopakuji: v případě URI Audiovisual Core termínů takové řešení nikdy nebude obsahovat informace o popsaném multimediálním zdroji. Z tohoto důvodu by jen málo Audiovisual Core aplikací zaměřených na člověka mělo uživatelům vůbec zobrazovat URI, ani je používat jako propojovací mechanismy. (Jednou z možných výjimek je aplikace pro přiřazování metadat k multimediálním zdrojům, kde takové použití může poskytnout heslo v tezauru, které uživateli pomůže v sémantice vlastnosti metadat. Nicméně, vzhledem k náhodné povaze tohoto řešení a jeho nedostatečné dlouhodobé udržitelnosti, je třeba i tento přístup zvažovat s velkou opatrností.) Na závěr je třeba poznamenat, že některé externí řízené slovníky jsou definovány v PDF nebo jiných dokumentech, které neobsahují přímé odkazy URL na jednotlivé definované termíny. V těchto případech může jakékoli usnesení dostupné z normativního dokumentu odkazovat pouze na začátek dokumentu, takže je nutné vyhledat v dokumentu odkazovanou definici.

S každou vlastností Audiovisual Core je spojena její hodnota. Datový typ této hodnoty je rovněž specifikován v normativním dokumentu. Datové typy mohou zahrnovat volný text, konkrétní literály převzaté z kontrolovaného slovníku specifikovaného v normativním dokumentu nebo řadu dalších datových typů specifikovaných a popsaných v normativním dokumentu. V případě řízeného slovníku je důležité si uvědomit, že bez ohledu na to, co aplikace zobrazuje v uživatelském rozhraní, by při jakékoli výměně metadat Audiovisual Core měly být použity literály ze specifikovaného řízeného slovníku, pokud je specifikován, a to i v případě, že je záznam deklarován jako záznam v jiném jazyce než je jazyk řízeného termínu. Důležitým příkladem je pole metadat typu, které by mělo pocházet z odpovídajícího slovníku Dublin Core, doplněného o některá doporučení uvedená v normativním dokumentu. (K tomu přidáváme také volitelné pole Subtype.) Podobně agenti odpovídající na dotazy týkající se metadat Audiovisual Core MUSÍ být schopni zpracovávat a odpovídat na dotazy formulované pomocí kontrolovaného slovníku. Nic v normativním dokumentu nebrání poskytovateli dat Audiovisual Core tvrdit, že nemá žádné záznamy s daným řízeným termínem, ani provádět interní mapování mezi řízeným slovníkem a jeho interními atributy, jejichž názvy mohou být v jiném jazyce než v angličtině. Pouze malý počet vlastností Audiovisual Core má hodnoty v konkrétním, na angličtině založeném řízeném slovníku. To bude relevantní pouze pro výměnu metadat. Z povinných podmínek má takové požadavky pouze typ.

Záznam Audiovisual Core se skládá minimálně ze čtyř povinných polí (identifikátor, typ, jazyk metadat a prohlášení o autorských právech).

V některých případech jsou některé termíny metadat nutně spojeny s jinými (např. různé verze obrázku musí být spojeny s „hlavní“ verzí). Tabulky a jiné ploché zdroje metadat přispěvatelů jsou však považovány za obzvláště důležité a v mnoha z nich je obtížné takové strukturální vztahy znázornit. V důsledku toho je záznam Audiovisual Core sám o sobě převážně plochý, s výjimkou objektu vlastnosti s názvem _hasServiceAccessPoint_. Tento objekt sám o sobě má další vlastnosti, které popisují, jak načíst skutečná média popsaná záznamem AC. Jedním z důsledků toho je, že pro některé účely může být poskytovatel metadat nucen zpřístupnit několik záznamů metadat o stejném základním zdroji, protože specifikace Audiovisual Core, která je neutrální z hlediska reprezentace, ve většině případů neumožňuje „podvlastnosti“ svých vlastností ani vztahy. Důležitý případ se týká vícejazyčných metadat. Protože každý záznam metadat je v pevně daném jazyce specifikovaném vlastností Metadata Language (jedná se o jazyk záznamu, nikoli multimediálního zdroje, pokud nějaký má), může být nutné, aby poskytovatel nabídl několik záznamů metadat o stejném multimediálním zdroji. Hodnoty čtyř povinných termínů musí být uvedeny v každém záznamu metadat, i když se opakují v jiných záznamech metadat popisujících stejný zdroj.
V době psaní tohoto článku normativní dokument neposkytuje mechanismus pro identifikaci záznamu metadat, který by mohl být zastřešující, v tom smyslu, že jeho volitelné termíny mohou být považovány za výchozí pro všechny termíny, které nejsou specifikovány v jiných záznamech o stejném zdroji. Tento bod je diskutován na MRTG Wiki.

Mnohé položky se mohou v záznamu Audiovisual Core opakovat, ale některé nikoli, jak je uvedeno v normativním dokumentu. Například položka Modified odpovídá datu, kdy byl mediální zdroj upraven, a může se opakovat, aby odrážela historii zdroje. Naproti tomu datum dostupnosti je jedno datum nebo jeden rozsah dat, kdy se podkladový zdroj stal nebo stane dostupným.

## 10 Implementace a soulad s předpisy

Audiovisual Core je definován způsobem, který je co nejvíce neutrální z hlediska reprezentace. Poskytuje definice tříd, vlastností a instancí v přirozeném jazyce, které jsou identifikovány pomocí URI, a vydává doporučení ohledně použití a obsahu vlastností z jiných slovníků.

Zde definované URI mohou být použity v řadě technologií, jako jsou prostory jmen v dokumentech XML Schema-valid table, RDF a záhlaví sloupců v textových souborech oddělených čárkami.

Tento přístup usnadňuje:

- Začlenění Audiovisual Core dat do jiných standardů, jako jsou popisy vzorků nebo literatura.

- Rozšíření záznamů Audiovisual Core o další typy dat, jako jsou rozsáhlé geografické řízené slovníky Open Geospatial Consortium (OGC)

- Křížové procházení mezi technologiemi, jako jsou soubory s hodnotami oddělenými čárkami, grafy RDF, dokumenty XML a objekty JSON.

Samotný normativní standard Audiovisual Core, který je neutrální z hlediska reprezentace, neposkytuje hotový, samopotvrzující formát pro výměnu. Lze definovat více takových výměnných formátů splňujících různé požadavky a tato norma umožňuje jejich vzájemné mapování.

## 11 Další informace

- Charta skupiny pro údržbu Audiovisual Core
  https://github.com/tdwg/ac/blob/master/Audiovisual-core_maintenance-group_charter.md

- Diskuse o Audiovisual Core probíhá na
  https://github.com/tdwg/ac/issues

- Zaregistrujte se do mailing listu tdwg-content@lists.tdwg.org na adrese http://lists.tdwg.org/mailman/listinfo/tdwg-content. Tato e-mailová konference sleduje veškerou diskusi o obsahu standardů TDWG.

## 12 Příloha I: Slovníček pojmů

<table>
  <tbody>
    <tr>
      <td><a href="http://dublincore.org/documents/dcmi-terms/">DC</a></td>
      <td>Dublin Core. Sada metadatových prvků, která je standardem pro vyhledávání informačních zdrojů napříč doménami.</td>
    </tr>
    <tr>
      <td><a href="http://dublincore.org/">DCMI</a></td>
      <td>Dublin Core Metadata Initiative. Organizace zabývající se vývojem standardu metadat Dublin Core.</td>
    </tr>
    <tr>
      <td><a href="http://rs.tdwg.org/dwc/">DwC</a></td>
      <td>Darwin Core je standard TDWG pro reprezentaci záznamů o vzorcích. Již několik let se široce používá v řadě nestandardních, někdy nekonzistentních verzí. Nedávno přijatá standardní verze je k dispozici na adrese <a href="http://rs.tdwg.org/dwc/index.htm">http://rs.tdwg.org/dwc/index.htm</a>.</td>
    </tr>
    <tr>
      <td><a href="http://eol.org">EOL</a></td>
      <td>Encyclopedia of Life. Informace o mnoha druzích.</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Exchangeable_image_file_format">EXIF</a></td>
      <td>Široce používaný formát značek pro metadata digitálních obrázků, který je často vkládán do obrazových souborů, zejména moderními digitálními fotoaparáty. Mnoho aplikací pro vykreslování obrázků dokáže číst a zobrazovat data EXIF. Historie a popis viz <a href="http://en.wikipedia.org/wiki/Exchangeable_image_file_format">http://en.wikipedia.org/wiki/Exchangeable_image_file_format</a>.</td>
    </tr>
    <tr>
      <td><a href="http://www.gbif.org/">GBIF</a></td>
      <td>Global Biodiversity Information Facility. Interoperabilní síť databází biologické rozmanitosti a nástrojů informačních technologií.</td>
    </tr>
    <tr>
      <td><a href="http://www.iana.org">IANA</a></td>
      <td>Internet Assigned Names Authority. Specifikuje formy a registruje instance názvů různých protokolů používaných na internetu. Viz zejména informace o <a href="http://en.wikipedia.org/wiki/URI_scheme">schématu http URI IANA</a>.</td>
    </tr>
    <tr>
      <td><a href="http://www.iptc.org">IPTC</a></td>
      <td>IPTC je vyspělý standard Mezinárodní rady pro tisk a telekomunikace. Jeho práva duševního vlastnictví podporují jemnější kontrolované slovníky než DC, což zajišťuje lepší strojové zpracování pro vyhledávání a vhodnost pro použití. Aktuální verze je slovník pro XMP.</td>
    </tr>
    <tr>
      <td><a href="http://www.json.org/">JSON</a></td>
      <td>JavaScript Object Notation. Lehký formát pro výměnu dat.</td>
    </tr>
    <tr>
      <td><a href="http://www.morphbank.net/">Morphbank</a></td>
      <td>Úložiště obrázků vzorků.</td>
    </tr>
    <tr>
      <td><a href="http://www.metadataworkinggroup.org/">MWG</a></td>
      <td>Pracovní skupina pro metadata je průmyslové konsorcium (Adobe, Apple, Canon, Microsoft, Nokia a Sony), které bylo založeno za účelem specifikace způsobu využití platformy Adobe Extensible Metadata Platform, <a href="http://en.wikipedia.org/wiki/Extensible_Metadata_Platform">XMP</a>, pro vkládání metadat do běžných formátů obrazových souborů v několika široce používaných řízených slovnících. Ačkoli se MWG zaměřuje hlavně na spotřebitelské aplikace, více než dvě desítky open source a komerčních softwarových produktů a platforem podporují XMP a společnost Adobe uvolnila sadu nástrojů pro vývojáře pod open source licencí.</td>
    </tr>
    <tr>
      <td><a href="http://images.nbii.gov/">NBII</a></td>
      <td>Bývalá americká Národní infrastruktura biologických informací. Jeho obrazová knihovna, Library of Images From the Environment (LIFE), byla k dispozici na adrese <a href="http://images.nbii.gov/">http://images.nbii.gov/</a> nebo <a href="http://life.nbii.gov/">http://life.nbii.gov/</a>. Pokud se LIFE obnoví v jakékoli formě, mohlo by tam být nějaké spojení.</td>
    </tr>
    <tr>
      <td><a href="https://www.tdwg.org/standards/ncd/">NCD</a></td>
      <td>Popis přírodních sbírek je návrh datového standardu určený k popisu sbírek fyzických objektů, jako jsou například vzorky. Může pojmout sbírky mediálních objektů, ale nemůže je propojit s popisy samotných objektů.</td>
    </tr>
    <tr>
      <td><a href="http://www.opengeospatial.org/">OGC</a></td>
      <td>Open Geospatial Consortium. Poskytuje standardy pro reprezentaci a výměnu geoprostorových dat.</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Resource_Description_Framework">RDF</a></td>
      <td>Resource Description Framework. Lehký ontologický systém na podporu online výměny znalostí.</td>
    </tr>
    <tr>
      <td><a href="http://www.tdwg.org/">TDWG</a></td>
      <td>Taxonomic Databases Working Group. Nyní známá jako Biodiversity Information Standards (TDWG), je to mezinárodní pracovní skupina, která vyvíjí standardy a protokoly pro sdílení dat o biologické rozmanitosti.</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Uniform_Resource_Identifier">URI</a></td>
      <td>Unique Resource Identifier. Obecný termín pro propojení webových zdrojů včetně URL adres.</td>
    </tr>
    <tr>
      <td><a href="http://www.w3.org/XML/">XML</a></td>
      <td>Extensible Markup Language. Jednoduchý flexibilní textový formát, který hraje stále důležitější roli při výměně široké škály dat na webu.</td>
    </tr>
    <tr>
      <td><a href="http://www.adobe.com/devnet/xmp/">XMP</a></td>
      <td>Adobe Extensible Metadata Platform (XMP) je rámec pro vkládání metadat do mediálních souborů. Společnost Adobe poskytuje sadu nástrojů pro vývojáře XMP s licencí BSD, která obsahuje dokumentaci o tom, jak reprezentovat metadata v XMP. Specifikace XMP je licencována společností Adobe na základě <a href="http://wwwimages.adobe.com/www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/xmp_public_patent_license.pdf">&quot;Public Patent License&quot;</a>, kterou Adobe uděluje všem právo vytvářet komponenty svých aplikací kompatibilní s XMP, ale vyhrazuje si právo licenci odejmout v případě, že taková kompatibilní komponenta poruší &quot;základní nároky&quot; jakéhokoli patentu. Informace o stažení naleznete na <a href="http://www.adobe.com/devnet/xmp/">http://www.adobe.com/devnet/xmp/</a>. Viz také <a href="http://www.metadataworkinggroup.org/">MWG</a> v této tabulce.</td>
    </tr>
  </tbody>
</table>

## 13 Příloha II: Historie vývoje Audiovisual Core

Standard Audiovisual Core Multimedia Resources Metadata Schema (Audiovisual Core) je vyvrcholením práce na popisech multimediálních zdrojů, kterou provedly organizace Key to Nature, NBII Digital Image Library, Morphbank a další, spolu s příspěvky řady dalších zainteresovaných komunit, včetně Encyclopedia of Life (EOL), Biodiversity Heritage Library (BHL) a University of Massachusetts-Boston. Globální informační systém o biologické rozmanitosti (GBIF) pověřil v březnu 2008 „Pracovní skupinu pro multimediální zdroje (MRTG)“ a v prosinci 2009 byla tato skupina schválena organizací Biodiversity Information Standards (TDWG) jako „Společná pracovní skupina GBIF-TDWG pro multimediální zdroje v oblasti biologické rozmanitosti“.

Účastníci přípravy schématu (v abecedním pořadí)

- Mr. Mihail-Constantin Carausu, Danish Biodiversity Information
  Facility (DanBIF), Copenhagen, Denmark

- Dr. Vishwas Chavan, Global Biodiversity Information Facility,
  Copenhagen, Denmark

- Mr. Chris Freeland, Missouri Botanical Garden, St. Louis, USA

- Dr. Gregor Hagedorn, JKI, Federal Research Institute for Cultivated
  Plants, Berlin, Germany

- Prof. Robert A. Morris, University of Massachusetts at Boston, USA

- Dr. Dimitry Mozzherin, Encyclopedia of Life, Woods Hole, USA

- Dr Annette Olson, American Association for the Advancement of
  Science

- Prof. Greg Riccardi, Florida State University, Tallahassee, USA

- Dr. Éamonn Ó Tuama, Global Biodiversity Information Facility,
  Copenhagen, Denmark

Tato norma byla vyvinuta společnou pracovní skupinou tak, aby odpovídala souboru standardizovaných zdrojů pro správu dat, které vyvíjí GBIF.

Finanční prostředky poskytl Global Biodiversity Information Facility.

Velký dík patří Woods Hole Marine Biological Laboratory a
Encyclopedia of Life za uspořádání jednoho ze setkání. Tento dokument,
včetně některých popisů, je upravenou verzí odpovídajícího dokumentu
vypracovaného pracovní skupinou TDWG Natural Collections Descriptions (NCD).

### 13.1 Časová osa

2006, listopad Založena TDWG Image Interest Group

2008, březen GBIF pověřuje pracovní skupinu pro multimediální zdroje (MRTG)

2008, červen Pracovní skupina GBIF pro multimediální zdroje se sešla v Kodani, Dánsko

2008, srpen Setkání pracovní skupiny GBIF pro multimediální zdroje ve Woods Hole, USA

2008, říjen TDWG Image Interest Group se sešla ve Fremantle v Austrálii na ‘TDWG Annual Conference 2008’

2008, prosinec Společná pracovní skupina GBIF-TDWG pro multimediální zdroje v oblasti biologické rozmanitosti pověřena

2009, únor, se v dánské Kodani sešla pracovní skupina GBIF pro multimediální zdroje, aby zdokonalila schéma metadat

2009, březen GBIF – TDWG Multimedia Resources Metadata Schema (MRTG) ver.
0.4414 vypracováno a otevřeno pro neformální připomínky, vyvíjející se přes verzi 0.9

2010, únor Schéma v 0.9 předloženo TDWG k internímu hodnocení

2010, červenec Dokončeno 1. interní hodnocení TDWG

2010, listopad v1.0 předložena výkonnému výboru TDWG s odpovědí
na 1. interní hodnocení. Navrhovaná norma přejmenována na Audiovisual Core Multimedia
Resources Metadata Schema (AC).

2011, červen Probíhá reakce na 2. interní hodnocení.

2011, září Dokončeny odpovědi na 2 a 3 interní hodnocení a předloženy výkonnému výboru TDWG.

2011, listopad Připravené odpovědi na „Hodnocení g“ a „Hodnocení h“ a na některé připomínky vedoucího hodnocení, Stevea Baskaufa. Příprava podání žádosti o povolení k veřejnému připomínkování.

Leden–listopad 2012 Další přípravy na podání žádosti o povolení k veřejnému připomínkování

### 13.2 Historie revizí dokumentu

**0.7v1**

- Harmonizovaný dokument k tomu, že podtyp je v normativní verzi v0.7 volitelný

- Oprava nesprávně umístěné závorky, nadbytečné mezery, chybějící mezery atd.

**ACv1.0 docv1.0**

- Harmonizováno s verzí 1.0: nahraďte „MRTG“ výrazem „Audiovisual Core“, pokud je použit jako název schématu. Opravy drobných překlepů. Přidána předpona „dcterms“.

**ACv1.0 docv1.0**

- Další nahrazení MRTG termínem „Audiovisual Core“ neboli „AC“.

**AC v1.0 docv 1.2**

- Adresovat komentáře 2. interního hodnocení

- Oprava nesprávně umístěné závorky, nadbytečné mezery, chybějící mezery atd.

**AC v1.0 docv1.3**

- Odstranění požadavku na uvedení vlastníka autorských práv.

**AC v1.0 docv1.4**

- Vyčištění citací šesti povinných prvků namísto pěti.

**AC v1.0 docv1.5**

- Nahrazení „keytonature.eu“ za „species-id.net“, aby se zohlednilo přesunutí normativní wiki. Odebrání některých nepoužívaných termínů ze slovníku. Aktualizace docv na verzi 1.5

**AC v1.0docv1.6**

- Odebrání dcterms:title ze seznamu povinných položek. Přidání popisu je důrazně doporučeno. Přidání zmínky o xmpRights:Owner do položky Prohlášení o autorských právech v povinném seznamu. Změna počtu povinných prvků z „pěti“ na „čtyři“ nebo počet zcela vynechán, pokud je text jednoznačný. Uveden jmenný prostor acterms. Oprava jmenného prostoru Iptc4xmpExt na http://iptc.org/std/Iptc4xmpExt/2008-02-29/. Aktualizace docv na verzi 1.6.

**AC v1docv1.7**

- Vyjasnění vztahu tohoto dokumentu k normativním dokumentům. Nastavení hlavního textu na zarovnání vlevo, nevyrovnané.

**AC v1.0docv1.8**

- Odstranění zmínky o přechodech, protože již nejsou v normativním seznamu termínů.

- Na str. 5 vloženo URL termínů DwC do poznámky pod čarou.

- Improved language about use of literals with dcterms.

**C v1.0docv1.91**

- Various minor grammar and punctuation corrections.

- Reconciliation to current normative docs.

**AC v1.0docv1.92**

- More minor grammar fixes.

**AC v1.0docv1.93**

- Fixed inconsistent internal version references to current version. No substantive or grammatical changes. Note that v1.92 was submitted to TDWG executive committee with request for permission to hold public review.

**AC v1.0docv1.94**

- Change references from species-id wiki to gbif terms wiki. Adjust Fig 1

**AC v1.0docv1.95**

- Correct “hasAccentPoint” to “hasAcccessPoint”. Remove text suggesting this is a draft

## 14 Poznámky

<sup id="fn-1">[\[1\]](#cit-1)</sup> http://rs.tdwg.org/ac/doc/structure/

<sup id="fn-2">[\[2\]](#cit-2)</sup> http://rs.tdwg.org/ac/doc/termlist/

<sup id="fn-3">[\[3\]](#cit-3)</sup> [http://www.w3.org/RDF/](http://www.w3.org/RDF/)

<sup id="fn-4">[\[4\]](#cit-4)</sup> [http://www.w3.org/standards/xml/schema](http://www.w3.org/standards/xml/schema)

<sup id="fn-5">[\[5\]](#cit-5)</sup> [http://en.wikipedia.org/wiki/Comma-separated_values](http://en.wikipedia.org/wiki/Comma-separated_values)

<sup id="fn-6">[\[6\]](#cit-6)</sup> https://github.com/tdwg/ncd/blob/master/NCD-v090_TDWG/NCD-v090_TDWG-NonNormative.pdf

<sup id="fn-7">[\[7\]](#cit-7)</sup> [http://rs.tdwg.org/dwc/terms/](http://rs.tdwg.org/dwc/terms/)

<sup id="fn-8">[\[8\]](#cit-8)</sup> [http://rs.tdwg.org/dwc/index.htm](http://rs.tdwg.org/dwc/index.htm)

<sup id="fn-9">[\[9\]](#cit-9)</sup>
The Metadata Working Group (MWG,
[http://www.metadataworkinggroup.org/](http://www.metadataworkinggroup.org/)) is an industry consortium
(Adobe, Apple, Canon, Microsoft, Nokia, and Sony) organized to
specify how to exploit the Adobe Extensible Metadata Platform, XMP
([http://en.wikipedia.org/wiki/Extensible_Metadata_Platform](http://en.wikipedia.org/wiki/Extensible_Metadata_Platform)) for
embedding into common image file formats metadata in several widely
used controlled vocabularies. Ačkoli se MWG zaměřuje hlavně na
spotřebitelské aplikace, více než dvě desítky open source a komerčních
softwarových produktů a platforem podporují XMP a Adobe umístilo
Developers' Toolkit pod open source licenci. Spolu s
návrhy na standardní serializace reprezentace neutrálního
schématu Audiovisual Core hodlá MRTG navrhnout TDWG Best Practice
pro vkládání takových serializací do multimediálních souborů pomocí XMP.

<sup id="fn-10">[\[10\]](#cit-10)</sup>
IPTC is a mature standard from the International Press and
Telecommunications Council ([http://www.iptc.org](http://www.iptc.org)). Jeho práva duševního vlastnictví podporují jemnější řízené slovníky než
DC, což poskytuje lepší strojové zpracování pro vyhledávání a
vhodnost pro použití.
