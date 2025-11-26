# {document_title}

Title
: {document_title}

Namespace IRI
: <http://rs.tdwg.org/acsubtype/values/>

Preferred namespace abbreviation
: acsubtype:

Date de publication de la dernière mise à jour
: {ratification_date}

Date de création
: {created_date}

Fait partie du standard TDWG
: <{standard_iri}>

Cette version
: <{current_iri}{ratification_date}>

Dernière version
: <{current_iri}>

Version précédente
: {previous_version_slot}

Abstract
: {abstract}

Contributeurs
: {contributors}

Créateur :
{creator}

Citation :
{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as a controlled value for Audiovisual Core terms `ac:subtype` and `ac:subtypeLiteral`. **Note:** Although this is a controlled vocabulary, the type of its terms is `rdfs:Class` rather than `skos:Concept` as in other controlled vocabularies because it indicates the type of the media item.

### 1.1 Statut du contenu de ce document

Section 1 is informative (non-normative).

La section 2 est normative.

Section 3 is informative (non-normative).

Dans la section 4, les valeurs de l'`IRI du terme`, de la `Définition` et de la `Valeur contrôlée` sont normatives. La valeur de `Utilisation` (si elle existe pour un terme donné) est normative. Les valeurs de `Nom du Terme` ne sont pas normatives, bien que l'on puisse s'attendre à ce que le préfixe de l'abréviation de l'espace de noms soit celui couramment utilisé pour l'espace de noms du terme.  `Label` and the values of all other properties are non-normative.

### 1.2 Mots clés RFC 2119

Les mots clés "MUST/DOIT", "MUST NOT/NE DOIT PAS", "REQUIRED/OBLIGATOIRE", "SHALL/DEVRA", "SHALL NOT/NE DEVRA PAS", "SHOULD/DEVRAIT", "SHOULD NOT/NE DEVRAIT PAS", "RECOMMENDED/RECOMMANDÉ", "MAY/POURRAIT", et "OPTIONAL/OPTIONNEL" dans ce document doivent être interprétés comme défini dans les références [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) et [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174)] uniquement lorsqu’ils apparaissent en majuscules, comme ci-dessus.

## 2 Utilisation des termes

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `ac:subtype`. Controlled value strings SHOULD be used as values of the property `ac:subtypeLiteral`.

### 2.2 Relationship between values of ac:subtypeLiteral and ac:subtype

An IRI for a term in this vocabulary denotes the same class as the class denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `ac:subtype` given a controlled value string for `ac:subtypeLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `ac:subtype` property in cases where providers only provide values for `ac:subtypeLiteral`.

## 3 Index des termes
