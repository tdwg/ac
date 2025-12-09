# Controlled Vocabulary for Audiovisual Core subtype: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subtype: List of Terms

IRI Jmenného prostoru
: <http://rs.tdwg.org/acsubtype/values/>

Preferovaná zkratka jmenného prostoru
: acsubtype:

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

Abstract
: Audiovisual Core uses the terms ac:subtype and ac:subtypeLiteral to refine the type of a media item to a level more specific than the Dublin Core Type Vocabulary, http://purl.org/dc/dcmitype/. This controlled vocabulary provides values for ac:subtype and ac:subtypeLiteral.

Přispěvatelé
: {contributors}

Tvůrce
: {creator}

Bibliografická citace
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Úvod (informativní)

Tento dokument obsahuje termíny, které mají být použity jako řízené hodnoty pro audiovizuální základní termíny `ac:subtype` a `ac:subtypeLiteral`. **Poznámka:** Ačkoli se jedná o řízený slovník, typ jeho termínů je `rdfs:Class`, nikoli `skos:Concept` jako v jiných kontrolovaných slovnících, protože označuje typ mediálního prvku.

### 1.1 Status obsahu tohoto dokumentu

Oddíl 1 je informativní (nenormativní).

Oddíl 2 je normativní.

Oddíl 3 je informativní (nenormativní).

V oddíle 4 jsou hodnoty `Term IRI`, `Definice` a `Kontrolovaná hodnota` normativní. Hodnota `Použití` (pokud pro daný termín existuje) je normativní. Hodnoty `Název termínu` nejsou normativní, ačkoli lze očekávat, že prefix zkratky jmenného prostoru je prefix běžně používaný pro jmenný prostor termínu.  `Štítek` a hodnoty všech ostatních vlastností nejsou normativní.

### 1.2 Klíčová slova RFC 2119

Klíčová slova "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" a "OPTIONAL" v tomto dokumentu je třeba interpretovat tak, jak je popsáno v [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) a [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), pokud a pouze pokud jsou uvedena velkými písmeny, jak je uvedeno zde.

## 2 Použití termínů

### 2.1 Vztah hodnotových typů k pojmům vlastnictví

V souladu s [dokumentem Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) by se jako hodnoty vlastnosti `ac:subtype` MĚLY používat nezkrácené termíny IRI. Jako hodnoty vlastnosti `ac:subtypeLiteral` by se MĚLY používat řízené hodnotové řetězce.

### 2.2 Vztah mezi hodnotami ac:subtypeLiteral a ac:subtype

IRI pro termín v tomto slovníku označuje stejnou třídu jako třída označená řetězcem řízené hodnoty pro stejný termín. Klient tedy MŮŽE odvodit hodnotu IRI pro `ac:subtype` na základě kontrolovaného řetězce hodnoty pro `ac:subtypeLiteral`, i když tato hodnota IRI není výslovně uvedena. Praktickým důsledkem je, že agregátoři dat MOHOU materializovat hodnoty pro preferovanou vlastnost `ac:subtype` v případech, kdy poskytovatelé poskytují pouze hodnoty pro `ac:subtypeLiteral`.

## 3 Index termínů
