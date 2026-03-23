# Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

Namespace IRI
: <http://rs.tdwg.org/acpart/values/>

Preferred namespace abbreviation
: acpart:

バージョン発行日
: {ratification_date}

作成日
: {created_date}

TDWG標準での該当箇所
: <{standard_iri}>

このバージョン
: <{current_iri}{ratification_date}>

最新バージョン
: <{current_iri}>

前のバージョン
{previous_version_slot}

Abstract
: The Audiovisual Core term subjectPart describes the part of an organism morphology, behaviour, environment depicted in a media item or region of interest. The subjectPart Controlled Vocabulary provides terms that should be used as values for ac:subjectPart and its literal-valued analog ac:subjectPartLiteral.

貢献者
: {contributors}

作成者
: {creator}

書誌的引用
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for the Audiovisual Core terms `ac:subjectPart` and `ac:subjectPartLiteral`. A [JSON-LD representation](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart.json) (including translations to multiple languages) of this SKOS Concept Scheme is available. For more information about how to use this vocabulary, see the [subjectPart and subjectOrientation Controlled Vocabularies User Guide](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

### 1.1 この文書の内容のステータス

Section 1 is informative (non-normative).

Section 2 is normative except as noted.

Section 3 is informative.

セクション 4 では、`用語のIRI（Term IRI）`、`定義（Definition）`、`制御値（Controlled value）`の値が規範的なものです。 `使用法（Usage）`の値がもし存在する場合、それは規範的なものです。  `上位概念（Has broader concept）`の値は規範的です。 `用語の名前（Term Name）`の値は非規範的ですが、名前空間の略語の接頭辞はその用語の名前空間で一般的に使われるものであると予想できます。  `Label` and the values of all other properties (such as `Examples` or `Notes`) are non-normative.

### 1.2 RFC 2119 キーワード

この文書における "MUST"、"MUST NOT"、"REQUIRED"、"SHALL"、"SHALL NOT"、"SHOULD"、"SHOULD NOT"、"RECOMMENDED"、"MAY"、"OPTIONAL" というキーワードは、ここに示されているようにすべて大文字で記載されている場合に限り、[BCP 14](https://www.rfc-editor.org/info/bcp14)、[\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) 、[\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) に記述されているように解釈されます。

### 1.3 User feedback reports

For perspective on the development of this [vocabulary enhancement](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements), refer to the [final Feature Report](https://github.com/tdwg/ac/blob/master/views/final-requirements.md) used to determine the requirements for the vocabulary. The Implementation Experience Report was published in _Biodiversity Information Science and Standards_ 7:e94188 and is available at <http://doi.org/10.3897/biss.7.94188>

## 2 用語の使い方

### 2.1 Relationship of value types to property terms

In accordance with the [Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) document, unabbreviated term IRIs MUST be used as values of the property `ac:subjectPart`. Controlled value strings SHOULD be used as values of the property `ac:subjectPartLiteral`.

### 2.2 Relationships with other concept schemes and collections (informative)

Particular `ac:subjectOrientation` values are appropriate for some `ac:subjectPart` values. The relationships between concepts in these two schemes are described by a [JSON-LD serialized SKOS Collection for each subject part](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) that designates which subject orientations are appropriate for that part. Similarly, [JSON-LD serialized SKOS Collections have been established for some organism groups](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) to indicate which subject parts exist for members of those groups. These collections are provided to aid application developers in filtering the concepts that should be presented to users and they may also be used for validation.

Human-readable collection lists of controlled value strings are available for [subjectPart](https://ac.tdwg.org/part_collections) and [subjectOrientation](https://ac.tdwg.org/orient_collections).

Neither of these Collections are normative and they are maintained outside of the Audiovisual Core standards framework in order to make their development agile.

## 3 用語索引
