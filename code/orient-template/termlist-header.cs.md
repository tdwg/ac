# {document_title}

Název
: {document_title}

IRI Jmenného prostoru
: <http://rs.tdwg.org/acorient/values/>

Preferovaná zkratka jmenného prostoru
: acorient:

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

Tento dokument obsahuje termíny, které mají být použity jako řízené hodnoty pro Audiovisual Core termíny `ac:subjectOrientation` a `ac:subjectOrientationLiteral`. K dispozici je [JSON-LD reprezentace](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient.json) (včetně překladů do více jazyků) tohoto schématu pojmů SKOS. Další informace o používání této slovní zásoby naleznete v [uživatelské příručce k řízeným slovníkům subjectPart a subjectOrientation](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

### 1.1 Status obsahu tohoto dokumentu

Oddíl 1 je informativní (nenormativní).

Oddíl 2 je normativní, pokud není uvedeno jinak.

Oddíl 3 je informativní.

V oddíle 4 jsou hodnoty `Term IRI`, `Definice` a `Kontrolovaná hodnota` normativní. Hodnota `Použití` (pokud pro daný termín existuje) je normativní.  Hodnota `Má širší pojem` je normativní. Hodnoty `Název termínu` nejsou normativní, ačkoli lze očekávat, že prefix zkratky jmenného prostoru je prefix běžně používaný pro jmenný prostor termínu.  `Label` and the values of all other properties (such as `Examples` or `Notes`) are non-normative.

### 1.2 Klíčová slova RFC 2119

Klíčová slova "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" a "OPTIONAL" v tomto dokumentu je třeba interpretovat tak, jak je popsáno v [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) a [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), pokud a pouze pokud jsou uvedena velkými písmeny, jak je uvedeno zde.

### 1.3 Hodnocení od uživatelů

Pro přehled o vývoji tohoto [rozšíření slovníku](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements) se podívejte na [závěrečnou zprávu o funkcích](https://github.com/tdwg/ac/blob/master/views/ final-requirements.md), která byla použita k určení požadavků na slovník. Zpráva o zkušenostech s implementací byla publikována v časopise _Biodiversity Information Science and Standards_ 7:e94188 a je k dispozici na <http://doi.org/10.3897/biss.7.94188>

## 2 Použití termínů

### 2.1 Vztah hodnotových typů k pojmům vlastnictví

V souladu s dokumentem [Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) MUSÍ být jako hodnoty vlastnosti `ac:subjectOrientation` použity nezkrácené termíny IRI. Jako hodnoty vlastnosti `ac:subjectOrientationLiteral` by se MĚLY používat řízené hodnotové řetězce.

### 2.2 Vztahy k jiným koncepčním schématům a sbírkám (informativní)

Konkrétní hodnoty `ac:subjectOrientation` jsou vhodné pro některé hodnoty `ac:subjectPart`. Vztahy mezi pojmy v těchto dvou schématech jsou popsány pomocí [JSON-LD serializované SKOS kolekce pro každou část předmětu](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json), která určuje, které orientace předmětu jsou pro danou část vhodné. Podobně byly [pro některé skupiny organismů vytvořeny serializované SKOS kolekce JSON-LD](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json), které označují, které části předmětu existují pro členy těchto skupin. Tyto sbírky jsou poskytovány s cílem pomoci vývojářům aplikací při filtrování pojmů, které by měly být uživatelům prezentovány, a mohou být také použity pro ověřování.

Seznamy řízených hodnotových řetězců, které jsou čitelné pro člověka, jsou k dispozici pro [subjectPart](https://ac.tdwg.org/part_collections) a [subjectOrientation](https://ac.tdwg.org/orient_collections).

Žádná z těchto sbírek není normativní a jsou spravovány mimo rámec standardů Audiovisual Core, aby byl jejich vývoj agilní.

## 3 Index termínů
