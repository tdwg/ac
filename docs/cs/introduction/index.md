# Úvod do Audiovisual Core

Název
: Úvod do Audiovisual Core

Datum vydání verze
: 2023-02-24

Datum vytvoření
: 2013-10-23

Součást TDWG Standardu
: <http://www.tdwg.org/standards/638>

Tato verze
: <http://rs.tdwg.org/ac/doc/introduction/2023-02-24>

Poslední verze
: <http://rs.tdwg.org/ac/doc/introduction/>

Předchozí verze
: <http://rs.tdwg.org/ac/doc/introduction/2013-10-23>

Abstrakt
: Audiovisual Core je soubor slovníků určených k reprezentaci metadat pro multimediální zdroje a sbírky týkající se biologické rozmanitosti. Cílem těchto slovníků je poskytnout informace, které pomohou před pořízením médií určit, zda je konkrétní zdroj nebo sbírka vhodná pro určitou aplikaci v oblasti vědy o biologické rozmanitosti. Slovníky se mimo jiné zabývají otázkami, jako je správa médií a sbírek, popisy jejich obsahu, jejich taxonomické, geografické a časové pokrytí a vhodné způsoby jejich vyhledávání, přiřazování a reprodukce.

Přispěvatelé
: [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) ([University of Massachusetts at Boston, USA](http://www.wikidata.org/entity/Q15144)), [Vijay Barve](https://orcid.org/0000-0002-4852-2567) (), [Mihail Carausu](https://orcid.org/0000-0002-8234-0599) ([Danish Biodiversity Information Facility (DanBIF), Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [Vishwas Chavan](https://orcid.org/0000-0002-3425-6499) ([Global Biodiversity Information Facility, Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [José Cuadra](http://www.wikidata.org/entity/Q51883873) (), [Chris Freeland](https://orcid.org/0000-0002-2541-5822) ([Missouri Botanical Garden, St. Louis, USA](http://www.wikidata.org/entity/Q1852803)), [Gregor Hagedorn](https://orcid.org/0000-0001-7023-7386) ([JKI, Federal Research Institute for Cultivated Plants, Berlin, Germany](http://www.wikidata.org/entity/Q832099)), [Patrick Leary](https://orcid.org/0000-0001-5172-8577) (), [Dimitry Mozzherin](https://orcid.org/0000-0003-1593-1417) ([Encyclopedia of Life, Woods Hole, USA](http://www.wikidata.org/entity/Q82486)), [Annette Olson](https://orcid.org/0000-0002-0772-0022) ([American Association for the Advancement of Science](http://www.wikidata.org/entity/Q40358)), [Greg Riccardi](https://orcid.org/0000-0002-3850-9983) ([Florida State University, Tallahassee, USA](http://www.wikidata.org/entity/Q861548)), [Ivan Teage](https://orcid.org/0000-0003-4176-2274) (), [Steve Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University, Nashville, TN, USA](http://www.wikidata.org/entity/Q29052))

Tvůrce
: GBIF/TDWG Pracovní skupina pro multimediální zdroje a Skupina pro údržbu audiovizuálního jádra

Bibliografická citace
: GBIF/TDWG Multimedia Resources Task Group and Audiovisual Core Maintenance Group. 2023. Úvod do Audiovisual Core. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/introduction/2023-02-24>

## 1. Úvod

Aububon Core Standard obsahuje čtyři dokumenty.  Tento dokument
poskytuje obecný úvod do standardu Audiovisual Core. Informace
o struktuře Audiovisual Core naleznete v dokumentu [Audiovisual Core Structure](../structure/).  Podrobnosti o termínech naleznete v dokumentu [Audiovisual Core Terms List](../termlist/).  
Podrobnější návod k používání Audiovisual Core naleznete v dokumentu
[Audiovisual Core Guide](../guide/).

### 1.1 Status obsahu tohoto dokumentu

Všechny části tohoto dokumentu jsou nenormativní.

### 1.2 Rozsah Audiovisual Core

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
již obsahují popisy svých médií vyjádřené v DwC nebo DC. Používáním
těchto slovníků tam, kde je to vhodné, chce AC zejména usnadnit
opětovné použití stávajících popisů v těchto sbírkách,
v případě potřeby doplněných o další
termíny

**Viz také:** Objevování a publikování primárních dat o biologické rozmanitosti
spojených s multimediálními zdroji: Audiovizuální základní strategie a
přístupy. R.
Morris et al., _Biodiversity Informatics,_ 8, červenec. 2013.

## 2 Základní pojmy Audiovisual Core

Záznam Audiovisual Core je popis multimediálního zdroje pomocí
[termínů Audiovisual Core](./terms). AC specifikuje dva druhy
termínů: termíny na úrovni záznamů a termíny na úrovni přístupu.
Termíny na úrovni záznamu se vztahují na popisovaný mediální zdroj. Téměř
všechny termíny jsou termíny na úrovni záznamu. Jeden z těchto termínů, _hasServiceAccessPoint_,
hraje zvláštní roli při získávání zdroje, který záznam
popisuje. Multimediální zdroj může mít více než jeden
hasServiceAccessPoint, z nichž každý poskytuje hodnoty jednoho nebo více
termínů přístupové úrovně. Podmínky přístupu dokumentují takové věci, jako je webová
adresa, na které lze získat digitální reprezentaci zdroje,
velikost takového získaného objektu atd. Záznam Audiovisual Core
je tedy popis používající sadu termínů, která odpovídá
normativním dokumentům a obsahuje alespoň čtyři povinné termíny,
které poskytují identifikátor, typ zdroje, jazyk
popisu a informace o autorských právech. Každý takový záznam popisuje
jediný multimediální zdroj (případně včetně sbírky). Identifikátor
mohl být zdroji přidělen externím
orgánem nebo poskytovatelem záznamu. Přísně vzato je
identifikátor vyžadován pouze pro sbírky, ale obecně se jeho použití důrazně doporučuje.

Každý termín Audiovisual Core má název v prostém textu, identifikátor termínu a
normativní definici v prostém textu. Identifikátory termínů odpovídají
specifikaci
[Universal Resource Identifier (URI)](http://tools.ietf.org/html/rfc2616#section-3.2).
Tyto identifikátory mají obvykle podobu, která je uživatelům prohlížečů známá jako
adresy webových stránek, začínající „http://“. Neformálně lze
toto pochopit takto: http URI má syntaxi webové adresy, ale
nelze očekávat, že jeho zadání do webového prohlížeče povede k
vrácení jakýchkoli informací do prohlížeče, a pokud ano,
vrácené informace nemusí mít žádný význam.

Protože adresy URL jsou poměrně dlouhé, dokumenty AC se řídí standardní
praxí zavádění krátké předpony sestávající z „kvalifikátoru jmenného prostoru“
odděleného dvojtečkou od mnemotechnického názvu úzce souvisejícího s
názvem termínu. Jmenný prostor s přibližně 50 % termínů, které jsou
převzaty z jiných slovníků, je jmenný prostor originálu. Jmenný prostor
termínů de novo AC je http://rs.tdwg.org/ac/terms/. V [Audiovisual Core Term List](../termlist/) má každý
záznam termínu řádek s názvem termínu. V souladu s praxí
[Darwin Core terms](http://rs.tdwg.org/dwc/terms/) je tento termín
obecně „nekvalifikovaným názvem“, před kterým je široce přijímaná předpona
označující zkratku pro jmenný prostor. Výsledek se nazývá
kvalifikovaný název. Například normativní wiki dokumentace pro
vypůjčený termín dcterms:identifier má URI
http://purl.org/dc/terms/identifier. První část,
"http://purl.org/dc/terms/", odpovídá jmennému prostoru. Většina
URI pro termíny převzaté z externích slovníků ve skutečnosti vytváří
relevantní dokumentaci pro daný externí standard, pokud jsou použity jako
URL webové stránky. Někdy to není přesné, protože dokumentace je ve formátu PDF
a několik (různých!) URI mohou zjevně vést
na stejné místo.

## 3 Implementace

The [AC Term List](../termlist/) and
[Audiovisual Core Structure](../structure/)
documents represent a _data model._ For actual use of Audiovisual Core, it
is necessary to select an implementation, preferably one with some
status designated by [TDWG](http://www.tdwg.org/). Známé
implementace budou uvedeny v doplňkových dokumentech, které nejsou součástí standardu Audiovisual Core.

## 4 Odkazy

\|   |  
\---|---|---
[\[ACISS\]](https://github.com/tdwg/ac/issues) | https://github.com/tdwg/ac/issues | AC issue tracker
[\[CHANGE\]](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#3-change-process) | http://rs.tdwg.org/vms/doc/specification/#3-change-process | TDWG vocabulary change policy |
[\[DCMIU\]](http://wiki.dublincore.org/index.php/User_Guide) | http://wiki.dublincore.org/index.php/User_Guide | Dublin Core User Guide                         |
[\[GUIDE\]](../guide/) | http://rs.tdwg.org/ac/doc/guide/ | AC User Guide
[\[STRCT\]](../structure/) | http://rs.tdwg.org/ac/doc/structure/ | Introduction to AC structure
[\[TERMS\]](../termlist/) | http://rs.tdwg.org/ac/doc/termlist/ | AC Term List                            |
