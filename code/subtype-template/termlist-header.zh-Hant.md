# {document_title}

Title
: {document_title}

Namespace IRI
: <http://rs.tdwg.org/acsubtype/values/>

Preferred namespace abbreviation
: acsubtype:

版本發行日期
: {ratification_date}

建立日期

生物多樣性訊息標準的一部分
: <{standard_iri}>

此版本
: <{current_iri}{ratification_date}>

最新版本
: <{current_iri}>

{previous_version_slot}

Abstract
: {abstract}

貢獻者
: {contributors}

建立者
: {creator}

書目引用
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as a controlled value for Audiovisual Core terms `ac:subtype` and `ac:subtypeLiteral`. **Note:** Although this is a controlled vocabulary, the type of its terms is `rdfs:Class` rather than `skos:Concept` as in other controlled vocabularies because it indicates the type of the media item.

### 1.1 本文件內容的現況

Section 1 is informative (non-normative).

第 2 節為規範性。

Section 3 is informative (non-normative).

在第 4 節中，`Term IRI`、`Definition`和`Controlled value`的值為規範性。 `Usage`的值 (如果它存在於特定術語中) 為規範性。 `Term Name`的值為非規範性，不過可以預期命名空間縮寫是術語命名空間的常用前綴。  `Label` and the values of all other properties are non-normative.

### 1.2 RFC 2119 關鍵字

關鍵字「必須」、「不得」、「要求」、「應」、「不應」、「應當」、「不應當」、「建議」、「可」、「可選」的定義，請參照[BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) 及 [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) 所定義之含義，惟詞彙須以全大寫形式呈現時方適用。

## 2 使用條款

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `ac:subtype`. Controlled value strings SHOULD be used as values of the property `ac:subtypeLiteral`.

### 2.2 Relationship between values of ac:subtypeLiteral and ac:subtype

An IRI for a term in this vocabulary denotes the same class as the class denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `ac:subtype` given a controlled value string for `ac:subtypeLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `ac:subtype` property in cases where providers only provide values for `ac:subtypeLiteral`.

## 3 術語索引
