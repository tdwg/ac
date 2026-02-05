# {document_title}

Title
: {document_title}

Namespace IRI
: <http://rs.tdwg.org/accd/values/>

Preferred namespace abbreviation
: accd:

Дата публикации версии
: {ratification_date}

Дата создания
: {created_date}

Часть стандарта TDWG
: <{standard_iri}>

Текущая версия
: <{current_iri}{ratification_date}>

Последняя версия: {current_iri}

Предыдущая версия {previous_version_slot}

Abstract
: {abstract}

Авторы: {contributors}

Создатель:{creator}

Библиографическая ссылка:{creator}. Год{year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVtermLiteral`.

### 1.1 Статус содержания документа

Section 1 is informative (non-normative).

Раздел 2 является нормативным.

Section 3 is informative (non-normative).

В разделе 4 значения `Термина IRI` и `Определения` являются нормативными. Значение `Использование` (если оно существует для данного термина) является нормативным. Значения `Term Name` не являются нормативными, хотя можно ожидать, что префикс сокращения пространства имен является одним из общепринятых префиксов, используемых для термина пространство имен.  `Label` and the values of all other properties are non-normative.

### 1.2 Ключевые слова RFC 2119

Ключевые слова «MUST», «MUST NOT», «REQUIRED», «SHALL», «SHALL NOT», «SHOULD», «SHOULD NOT», «RECOMMENDED», «MAY» и «OPTIONAL» в настоящем документе должны толковаться так, как это описано в [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) и [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) только тогда, когда они написаны заглавными буквами.

## 2 Применение терминов

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `Iptc4xmpExt:CVterm`. Controlled value strings SHOULD be used as values of the property `ac:CVtermLiteral`.

### 2.2 Relationship between values of ac:CVtermLiteral and Iptc4xmpExt:CVterm

An IRI for a term in this vocabulary denotes the same concept as the concept denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `Iptc4xmpExt:CVterm` given a controlled value string for `ac:CVtermLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `Iptc4xmpExt:CVterm` property in cases where providers only provide values for `ac:CVtermLiteral`.

## 3 Индексы терминов
