# Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

Namespace IRI
: <http://rs.tdwg.org/acpart/values/>

Preferred namespace abbreviation
: acpart:

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
: The Audiovisual Core term subjectPart describes the part of an organism morphology, behaviour, environment depicted in a media item or region of interest. The subjectPart Controlled Vocabulary provides terms that should be used as values for ac:subjectPart and its literal-valued analog ac:subjectPartLiteral.

Contributeurs
: {contributors}

Créateur :
{creator}

Citation :
{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for the Audiovisual Core terms `ac:subjectPart` and `ac:subjectPartLiteral`. A [JSON-LD representation](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart.json) (including translations to multiple languages) of this SKOS Concept Scheme is available. For more information about how to use this vocabulary, see the [subjectPart and subjectOrientation Controlled Vocabularies User Guide](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

### 1.1 Statut du contenu de ce document

Section 1 is informative (non-normative).

Section 2 is normative except as noted.

Section 3 is informative.

Dans la section 4, les valeurs de l'`IRI du terme`, de la `Définition` et de la `Valeur contrôlée` sont normatives. La valeur de `Utilisation` (si elle existe pour un terme donné) est normative.  La valeur de `Has broader concept` (a pour concept plus large) est normative. Les valeurs de `Nom du Terme` ne sont pas normatives, bien que l'on puisse s'attendre à ce que le préfixe de l'abréviation de l'espace de noms soit celui couramment utilisé pour l'espace de noms du terme.  `Label` and the values of all other properties (such as `Examples` or `Notes`) are non-normative.

### 1.2 Mots clés RFC 2119

Les mots clés "MUST/DOIT", "MUST NOT/NE DOIT PAS", "REQUIRED/OBLIGATOIRE", "SHALL/DEVRA", "SHALL NOT/NE DEVRA PAS", "SHOULD/DEVRAIT", "SHOULD NOT/NE DEVRAIT PAS", "RECOMMENDED/RECOMMANDÉ", "MAY/POURRAIT", et "OPTIONAL/OPTIONNEL" dans ce document doivent être interprétés comme défini dans les références [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) et [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174)] uniquement lorsqu’ils apparaissent en majuscules, comme ci-dessus.

### 1.3 User feedback reports

For perspective on the development of this [vocabulary enhancement](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements), refer to the [final Feature Report](https://github.com/tdwg/ac/blob/master/views/final-requirements.md) used to determine the requirements for the vocabulary. The Implementation Experience Report was published in _Biodiversity Information Science and Standards_ 7:e94188 and is available at <http://doi.org/10.3897/biss.7.94188>

## 2 Utilisation des termes

### 2.1 Relationship of value types to property terms

In accordance with the [Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) document, unabbreviated term IRIs MUST be used as values of the property `ac:subjectPart`. Controlled value strings SHOULD be used as values of the property `ac:subjectPartLiteral`.

### 2.2 Relationships with other concept schemes and collections (informative)

Particular `ac:subjectOrientation` values are appropriate for some `ac:subjectPart` values. The relationships between concepts in these two schemes are described by a [JSON-LD serialized SKOS Collection for each subject part](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) that designates which subject orientations are appropriate for that part. Similarly, [JSON-LD serialized SKOS Collections have been established for some organism groups](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) to indicate which subject parts exist for members of those groups. These collections are provided to aid application developers in filtering the concepts that should be presented to users and they may also be used for validation.

Human-readable collection lists of controlled value strings are available for [subjectPart](https://ac.tdwg.org/part_collections) and [subjectOrientation](https://ac.tdwg.org/orient_collections).

Neither of these Collections are normative and they are maintained outside of the Audiovisual Core standards framework in order to make their development agile.

## 3 Index des termes
