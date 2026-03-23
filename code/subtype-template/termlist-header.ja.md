# Controlled Vocabulary for Audiovisual Core subtype: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subtype: List of Terms

Namespace IRI
: <http://rs.tdwg.org/acsubtype/values/>

Preferred namespace abbreviation
: acsubtype:

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
: Audiovisual Core uses the terms ac:subtype and ac:subtypeLiteral to refine the type of a media item to a level more specific than the Dublin Core Type Vocabulary, http://purl.org/dc/dcmitype/. This controlled vocabulary provides values for ac:subtype and ac:subtypeLiteral.

貢献者
: {contributors}

作成者
: {creator}

書誌的引用
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as a controlled value for Audiovisual Core terms `ac:subtype` and `ac:subtypeLiteral`. **Note:** Although this is a controlled vocabulary, the type of its terms is `rdfs:Class` rather than `skos:Concept` as in other controlled vocabularies because it indicates the type of the media item.

### 1.1 この文書の内容のステータス

Section 1 is informative (non-normative).

第2節は規範的な内容です。

Section 3 is informative (non-normative).

セクション 4 では、`用語のIRI（Term IRI）`、`定義（Definition）`、`制御値（Controlled value）`の値が規範的なものです。 `使用法（Usage）`の値がもし存在する場合、それは規範的なものです。 `用語の名前（Term Name）`の値は非規範的ですが、名前空間の略語の接頭辞はその用語の名前空間で一般的に使われるものであると予想できます。  `Label` and the values of all other properties are non-normative.

### 1.2 RFC 2119 キーワード

この文書における "MUST"、"MUST NOT"、"REQUIRED"、"SHALL"、"SHALL NOT"、"SHOULD"、"SHOULD NOT"、"RECOMMENDED"、"MAY"、"OPTIONAL" というキーワードは、ここに示されているようにすべて大文字で記載されている場合に限り、[BCP 14](https://www.rfc-editor.org/info/bcp14)、[\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) 、[\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) に記述されているように解釈されます。

## 2 用語の使い方

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `ac:subtype`. Controlled value strings SHOULD be used as values of the property `ac:subtypeLiteral`.

### 2.2 Relationship between values of ac:subtypeLiteral and ac:subtype

An IRI for a term in this vocabulary denotes the same class as the class denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `ac:subtype` given a controlled value string for `ac:subtypeLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `ac:subtype` property in cases where providers only provide values for `ac:subtypeLiteral`.

## 3 用語索引
