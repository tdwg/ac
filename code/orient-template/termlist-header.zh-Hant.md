# Controlled Vocabulary for Audiovisual Core subjectOrientation: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subjectOrientation: List of Terms

Namespace IRI
: <http://rs.tdwg.org/acorient/values/>

Preferred namespace abbreviation
: acorient:

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
: The Audiovisual Core term subjectOrientation describes the viewing orientation relative to an organism or part of an organism depicted in a media item or region of interest. The subjectOrientation Controlled Vocabulary provides terms that should be used as values for ac:subjectOrientation and its literal-valued analog ac:subjectOrientationLiteral.

貢獻者
: {contributors}

建立者
: {creator}

書目引用
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for the Audiovisual Core terms `ac:subjectOrientation` and `ac:subjectOrientationLiteral`. A [JSON-LD representation](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient.json) (including translations to multiple languages) of this SKOS Concept Scheme is available. For more information about how to use this vocabulary, see the [subjectPart and subjectOrientation Controlled Vocabularies User Guide](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

### 1.1 本文件內容的現況

Section 1 is informative (non-normative).

Section 2 is normative except as noted.

Section 3 is informative.

在第 4 節中，`Term IRI`、`Definition`和`Controlled value`的值為規範性。 `Usage`的值 (如果它存在於特定術語中) 為規範性。  「Has broader concept」的值為規範性。 `Term Name`的值為非規範性，不過可以預期命名空間縮寫是術語命名空間的常用前綴。  `Label` and the values of all other properties (such as `Examples` or `Notes`) are non-normative.

### 1.2 RFC 2119 關鍵字

關鍵字「必須」、「不得」、「要求」、「應」、「不應」、「應當」、「不應當」、「建議」、「可」、「可選」的定義，請參照[BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) 及 [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) 所定義之含義，惟詞彙須以全大寫形式呈現時方適用。

### 1.3 User feedback reports

For perspective on the development of this [vocabulary enhancement](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements), refer to the [final Feature Report](https://github.com/tdwg/ac/blob/master/views/final-requirements.md) used to determine the requirements for the vocabulary. The Implementation Experience Report was published in _Biodiversity Information Science and Standards_ 7:e94188 and is available at <http://doi.org/10.3897/biss.7.94188>

## 2 使用條款

### 2.1 Relationship of value types to property terms

In accordance with the [Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) document, unabbreviated term IRIs MUST be used as values of the property `ac:subjectOrientation`. Controlled value strings SHOULD be used as values of the property `ac:subjectOrientationLiteral`.

### 2.2 Relationships with other concept schemes and collections (informative)

Particular `ac:subjectOrientation` values are appropriate for some `ac:subjectPart` values. The relationships between concepts in these two schemes are described by a [JSON-LD serialized SKOS Collection for each subject part](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) that designates which subject orientations are appropriate for that part. Similarly, [JSON-LD serialized SKOS Collections have been established for some organism groups](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) to indicate which subject parts exist for members of those groups. These collections are provided to aid application developers in filtering the concepts that should be presented to users and they may also be used for validation.

Human-readable collection lists of controlled value strings are available for [subjectPart](https://ac.tdwg.org/part_collections) and [subjectOrientation](https://ac.tdwg.org/orient_collections).

Neither of these Collections are normative and they are maintained outside of the Audiovisual Core standards framework in order to make their development agile.

## 3 術語索引
