# {document_title}

Název
: {document_title}

Datum vydání verze
: {ratification_date}

Datum vytvoření
: {created_date}

Část standardu TDWG
: <{standard_iri}>

Tato verze
: <{current_iri}{ratification_date}>

Aktuální verze
: <{current_iri}>

{previous_version_slot}

Abstrakt
: {abstract}

Přispěvatelé
: {contributors}

Tvůrce
: {creator}

Bibliografická citace
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1. Úvod

Audiovisual Core Standard obsahuje řadu dokumentů.  Tento dokument obsahuje podrobné informace o podmínkách obsažených ve verzi {ratification_date} slovníku Audiovisual Core. Dokument [Audiovisual Core Introduction](../introduction/) poskytuje stručný úvod do Audiovisual Core Standard. Informace o struktuře Audiovisual Core naleznete v dokumentu [Audiovisual Core Structure](../structure/).  Podrobnější návod k používání Audiovisual Core naleznete v dokumentu [Audiovisual Core Guide](../guide/).

### 1.1 Status obsahu tohoto dokumentu

Oddíly 1.3 až 5 jsou normativní, s výjimkou tabulky 1.  V oddíle 7 a jeho pododdílech jsou hodnoty Normativní URI, Definice, Požadované a Opakovatelné normativní. Hodnota použití (pokud existuje pro daný termín) je normativní v tom smyslu, že určuje, jak by měl být vypůjčený termín používán jako součást Audiovisual Core.  Hodnoty Term Name nejsou normativní, i když lze očekávat, že předpona zkratky jmenného prostoru je běžně používaná pro jmenný prostor termínů.  Štítky a hodnoty všech ostatních vlastností (například poznámky) nejsou normativní.

### 1.2 Klíčová slova RFC 2119

Klíčová slova "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" a "OPTIONAL" v tomto dokumentu je třeba interpretovat tak, jak je popsáno v [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) a [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), pokud a pouze pokud jsou uvedena velkými písmeny, jak je uvedeno zde.

### 1.3 Kategorie pojmů

Záznam Audiovisual Core (AC) je popis multimediálního zdroje
pomocí slovníků AC. Tento dokument specifikuje tři druhy termínů:
termíny, které popisují aspekty médií nezávislé na reprezentaci,
termíny, které popisují aspekty závislé na reprezentaci, a termíny, které označují specifikované části mediálního prvku.
Většina termínů je nezávislá na reprezentaci a odkazuje na „abstraktní
multimediální zdroj“. Jeden z těchto termínů, `ac:hasServiceAccessPoint`, odkazuje na
nebo obsahuje metadata přístupového bodu služby závislá na reprezentaci,
která popisují digitální reprezentaci abstraktního multimediálního zdroje (instance třídy `ac:ServiceAccessPoint`).
Tato metadata popisují například webovou adresu, na které lze digitální
reprezentaci získat, a formát, rozsah nebo licence,
které popisují konkrétní reprezentaci. Multimediální zdroj
může poskytovat několik přístupových bodů pro různé reprezentace (např.
různá rozlišení). Zdroj může být také propojen s jednou nebo více oblastmi zájmu (ROI), které definují části v rámci mediální položky (instance třídy `ac:RegionOfInterest`).

## 2 Převzatý slovník

Při přebírání termínů z jiných slovníků používá AC URI,
běžné zkratky a předpony jmenných prostorů používané v těchto
slovnících. URI jsou normativní, ale zkratky a předpony jmenných prostorů
nemají žádný vliv, kromě toho, že usnadňují čtení dokumentace.

Tabulka 1. Slovníky, ze kterých byly termíny převzaty (nenormativní)

Poznámka: URI pro termíny ve většině těchto jmenných prostorů neodkazují na nic.  Autoritativní dokumentaci lze získat kliknutím na názvy slovníku v tabulce.

| Slovník                                                                                                                                                                                                | Zkratka | Jmenné prostory a zkratky                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | --------------------------------------------------------------------------------------- |
| [Darwin Core](http://rs.tdwg.org/dwc/doc/list/)                                                                                                                                                        | DwC     | `dwc: = http://rs.tdwg.org/dwc/terms/`                                                  |
| [Dublin Core](http://dublincore.org/documents/dcmi-terms/)                                                                                                                                             | DC      | `dc: = http://purl.org/dc/elements/1.1/, dcterms: = http://purl.org/dc/terms/`          |
| [Adobe XMP Core Properties](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart1.pdf)                                                                                         | XMP     | `xmp: = http://ns.adobe.com/xap/1.0/, xmpRights: = http://ns.adobe.com/xap/1.0/rights/` |
| [Adobe XMP Additional Properties](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart2.pdf)                                                                                   | XMP     | `photoshop: = http://ns.adobe.com/photoshop/1.0/`                                       |
| [International Press and Telecommunications Council Photo Metadata Standard,Extension Schema 1.1](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf) | IPTC    | `Iptc4xmpExt: = http://iptc.org/std/Iptc4xmpExt/2008-02-29/`                            |
| [Camera and Imaging Products Association Exchangeable Image File Format](http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf)                                                                         | EXIF    | `exif: = http://ns.adobe.com/exif/1.0/`                                                 |
| [Music Ontology](http://musicontology.com/specification/)                                                                                                                                              | MO      | `mo: = http://purl.org/ontology/mo/`                                                    |
| [TDWG Natural Collection Description LSID Ontology](https://github.com/tdwg/ontology/blob/master/ontology/voc/Collection.rdf) (odkazováno v metadatech, ale žádné výrazy převzaty)  | NCD     | `ncd: = http://rs.tdwg.org/ontology/voc/Collection#`                                    |

## 3 Jmenné prostory, předpony a názvy termínů

Jmenný prostor termínů převzatých z jiných slovníků je stejný jako
původní. Jmenný prostor termínů de novo AC je
`http://rs.tdwg.org/ac/terms/`. V tabulce termínů má každý termínový záznam
řádek s názvem termínu. Tento termín je obecně „nekvalifikovaným
názvem“, před kterým je široce přijímaná předpona označující zkratku
pro jmenný prostor. DOPORUČUJE se, aby implementátoři, kteří potřebují
předponu jmenného prostoru pro jmenný prostor AC, použili `ac`. V tomto webovém dokumentu
se po najetí kurzorem na termín v seznamu [Index podle názvu termínu](#61-index-by-term-name)
zobrazí úplná URL adresa, kterou lze použít v jiných webových
dokumentech k odkazování na _tento_ dokument, který se zabývá daným termínem, i když
pochází z převzatého slovníku. Je velmi důležité si uvědomit, že některé
slovníky, např. slovníky
[Dublin Core Metadata Initiative (DCMI)](https://www.dublincore.org/),
poskytují verze stejného termínu ve dvou různých jmenných prostorech, z nichž jeden
poskytuje řetězcové hodnoty a druhý poskytuje URI, i když je toto
oddělení pouze doporučením, nikoli povinností. Viz tento
[záznam na wiki DCMI](https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md)
k tomuto tématu. U slovníků, kde se taková praxe používá, ji
často dodržujeme a v poznámkách k popisu termínů odkazujeme
na sesterskou verzi termínu. Příkladem je dvojice
[dc:type](#dc_type) a [dcterms:type](#dcterms_type). Pokud takový pár umožňuje opakované instance (např. jako u [dc:source](#dc_source) a [dcterms:source](#dcterms_source)), může být v některých
implementacích AC zapotřebí zvláštní opatrnost, protože
některé implementace nemusí poskytovat dostatečnou strukturu k jasnému vyjádření
vztahu mezi členy páru v případě více
hodnot každého z nich. Jedná se o zvláštní případ problému, který je řešen v
normativním materiálu o [multiplicitě a kardinalitě](../structure/#3-multiplicity-and-cardinality) v dokumentu Audiovisual Core Structure.

## 4 Vrstvy

(Vlastnost Audiovisual Core layer byla k 27. 1. 2020 označena jako zastaralá)

## 5 Termíny s doslovnou hodnotou vs. termíny s hodnotou URI

Některé termíny mají dvě verze, jedna očekává hodnotu doslovného řetězce a
druhá URI. Za těchto okolností je verze očekávající řetězec
pojmenována s příponou „Literal“, např. `ac:metadataLanguageLiteral`. V
takových případech MŮŽOU být poskytnuty obě formy, ale je třeba dbát na to,
aby použití odráželo stejný záměr. V případě nejednoznačnosti má přednost
verze URI. Všechny termíny, včetně těch, které mají nebo nemají
specifickou příponu „Literal“, specifikují ve své definici, zda jsou
požadované hodnoty řetězce nebo URI.

## 6 Slovníkové indexy (nenormativní)

