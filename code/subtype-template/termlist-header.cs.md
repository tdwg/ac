# {document_title}

Název
: {document_title}

Namespace IRI
: <http://rs.tdwg.org/acsubtype/values/>

Preferred namespace abbreviation
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

Abstrakt
: {abstract}

Přispěvatelé
: {contributors}

Tvůrce
: {creator}

Bibliografická citace
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Úvod (informativní)

This document includes terms intended to be used as a controlled value for Audiovisual Core terms `ac:subtype` and `ac:subtypeLiteral`. **Note:** Although this is a controlled vocabulary, the type of its terms is `rdfs:Class` rather than `skos:Concept` as in other controlled vocabularies because it indicates the type of the media item.

### 1.1 Status obsahu tohoto dokumentu

Oddíl 1 je informativní (nenormativní).

Oddíl 2 je normativní.

Section 3 is informative (non-normative).

V oddíle 4 jsou hodnoty `Term IRI`, `Definice` a `Kontrolovaná hodnota` normativní. Hodnota `Použití` (pokud pro daný termín existuje) je normativní. Hodnoty `Název termínu` nejsou normativní, ačkoli lze očekávat, že prefix zkratky jmenného prostoru je prefix běžně používaný pro jmenný prostor termínu.  `Štítek` a hodnoty všech ostatních vlastností nejsou normativní.

### 1.2 Klíčová slova RFC 2119

Klíčová slova "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" a "OPTIONAL" v tomto dokumentu je třeba interpretovat tak, jak je popsáno v [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) a [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), pokud a pouze pokud jsou uvedena velkými písmeny, jak je uvedeno zde.

## 2 Použití termínů

### 2.1 Vztah hodnotových typů k pojmům vlastnictví

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `ac:subtype`. Controlled value strings SHOULD be used as values of the property `ac:subtypeLiteral`.

### 2.2 Relationship between values of ac:subtypeLiteral and ac:subtype

An IRI for a term in this vocabulary denotes the same class as the class denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `ac:subtype` given a controlled value string for `ac:subtypeLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `ac:subtype` property in cases where providers only provide values for `ac:subtypeLiteral`.

## 3 Index termínů
