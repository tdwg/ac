# {document_title}

Název
: {document_title}

IRI jmenného prostoru
: <http://rs.tdwg.org/acformat/values/>

Preferovaná zkratka jmenného prostoru
: acformat:

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

Tento dokument obsahuje termíny, které mají být použity jako řízené hodnoty pro termíny Dublin Core `dc:format` a `dcterms:format`, které jsou převzaty z Audiovisual Core.

### 1.1 Status obsahu tohoto dokumentu

Oddíl 1 je informativní (nenormativní).

Oddíl 2 je normativní, pokud není uvedeno jinak.

Oddíl 3 je informativní.

V oddíle 4 jsou hodnoty `Term IRI`, `Definice` a `Kontrolovaná hodnota` normativní. Hodnota `Použití` (pokud pro daný termín existuje) je normativní.  Hodnoty `Má širší pojem` a `Má přesnou shodu` jsou normativní. Hodnoty `Název termínu` nejsou normativní, ačkoli lze očekávat, že prefix zkratky jmenného prostoru je prefix běžně používaný pro jmenný prostor termínu.  `Štítek` a hodnoty všech ostatních vlastností nejsou normativní.

### 1.2 Klíčová slova RFC 2119

Klíčová slova "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" a "OPTIONAL" v tomto dokumentu je třeba interpretovat tak, jak je popsáno v [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) a [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), pokud a pouze pokud jsou uvedena velkými písmeny, jak je uvedeno zde.

## 2 Použití termínů

### 2.1 Vztah hodnotových typů k pojmům vlastnictví

V souladu s [dokumentem Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) MUSÍ být jako hodnoty vlastnosti `dcterms:format` použity nezkrácené termíny IRI. Jako hodnoty vlastnosti `dc:format` by se MĚLY používat řízené hodnotové řetězce.

### 2.2 Vztah mezi pojmy a pojmovými schématy

Záznam pro vlastnost `dc:format` v [dokumentu se seznamem základních audiovizuálních termínů](http://rs.tdwg.org/ac/doc/termlist/#dc_format) uvádí, že se DOPORUČUJÍ tři druhy řetězcových hodnot: typy internetových médií (typy MIME), speciální řetězcové hodnoty pro fyzická média nebo běžně používané přípony souborů. Tento řízený slovník definuje dvě schémata pojmů SKOS, schéma pojmů pro typy médií a fyzická média (první dva druhy hodnot specifikované pro `dc:type`) a schéma pojmů pro přípony souborů (poslední doporučený druh hodnoty). Protože organizace Internet Assigned Numbers Authority (IANA) vede [registr typů médií](https://www.iana.org/assignments/media-types/media-types.xhtml) a Audiovisual Core vede řízený seznam typů fyzických médií, DOPORUČUJE se používat hodnoty z koncepčního schématu typů médií a fyzických médií namísto koncepčního schématu přípon souborů.

Koncepční schéma pro typy médií a fyzická média definuje vztah `skos:broader` mezi každým konkrétním typem média nebo fyzickým médiem a jedním ze šesti [typů médií nejvyšší úrovně definovaných v RFC 2046](https://tools.ietf.org/html/rfc2046#page-4V), které souvisejí s multimédii: aplikace, zvuk, obraz, model, text a video. Tento vztah MŮŽE být použit klienty k odvození obecné kategorie formátu mediálního prvku.

Koncepční schéma pro přípony souborů definuje pojmy pro mnoho běžných přípon souborů používaných pro soubory digitálních médií. Tyto pojmy jsou obvykle spojeny s jedním z typů médií a fyzickými médii pomocí relace `skos:exactMatch`. Tvůrci metadat MOHOU použít řízenou hodnotu ze schématu pojmů přípon souborů, ale kvůli deklarované relaci `skos:exactMatch` MOHOU agregátoři nahradit ekvivalentní hodnotu ze schématu pojmů typů médií a fyzických médií.

### 2.3 Příklady pracovních postupů (nenormativní)

Pracovní postup 1: Poskytovatel dat používá tabulky obsahující sloupec pro doslovné hodnoty pro `dc:format`. Tabulky jsou vyplněny příponami souborů, které jsou řízenými hodnotami řetězců z koncepčního schématu pro přípony souborů. Tabulky jsou poskytovány agregátoru, jehož software „vyhledává“ kontrolované řetězcové hodnoty v koncepčním schématu pro přípony souborů a určuje ekvivalentní pojmy z koncepčního schématu pro typy médií a fyzická média. IRI z koncepčního schématu pro typy médií a fyzická média se používají jako standardizované hodnoty pro `dcterms:format` v databázi agregátoru.

Pracovní postup 2: Agregátor dat získává data o multimediálních položkách, která zahrnují názvy souborů nebo adresy URL, ale neobsahují informace o formátu. Agregátor extrahuje přípony souborů ze souborů nebo adres URL a pomocí schémat pojmů přiřadí každé položce hodnotu IRI `dcterms:format` ze schématu pojmů pro typy médií a fyzická média. V případech, kdy má položka příponu souboru, která neodpovídá žádné z kontrolovaných hodnot v koncepčním schématu pro přípony souborů, agregátor použije tabulku alternativních hodnot přípon souborů spravovanou komunitou k určení vhodného formátu pro danou mediální položku.

Pracovní postup 3: Agregátor dat shromažďuje mediální položky z otevřeného úložiště dat. Vzdálený server poskytuje typ média prostřednictvím hlavičky `Content-Type` a přípona souboru se určuje podle názvu souboru. Agregátor porovnává hodnotu typu média s hodnotou přípony souboru a pomocí vztahů `skos:exactMatch` v koncepčních schématech SKOS určuje, zda jsou hodnoty konzistentní. Nekonzistentní páry hodnot jsou označeny pro ruční kontrolu. Dosud neznámé přípony souborů jsou označeny pro další výzkum a možné zařazení do komunitou spravované tabulky alternativních hodnot přípon souborů.

## 3 Index termínů
