# Struktura Audiovisual Core

Název
: Struktura Audiovisual Core

Datum vydání verze
: 2023-02-24

Datum vytvoření
: 2013-10-23

Součást TDWG Standardu
: <http://www.tdwg.org/standards/638>

Tato verze
: <http://rs.tdwg.org/ac/doc/structure/2023-02-24>

Poslední verze
: <http://rs.tdwg.org/ac/doc/structure/>

Předchozí verze
: <http://rs.tdwg.org/ac/doc/structure/2021-10-05>

Abstrakt
: Dokument Audiovisual Core Structure poskytuje pokyny, jak lze multimediální záznamy serializovat jako XML a v tabulkové formě. Navrhuje také, jak lze hodnoty textového seznamu oddělit.

Přispěvatelé
: [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) ([University of Massachusetts at Boston, USA](http://www.wikidata.org/entity/Q15144)), [Vijay Barve](https://orcid.org/0000-0002-4852-2567) (), [Mihail Carausu](https://orcid.org/0000-0002-8234-0599) ([Danish Biodiversity Information Facility (DanBIF), Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [Vishwas Chavan](https://orcid.org/0000-0002-3425-6499) ([Global Biodiversity Information Facility, Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [José Cuadra](http://www.wikidata.org/entity/Q51883873) (), [Chris Freeland](https://orcid.org/0000-0002-2541-5822) ([Missouri Botanical Garden, St. Louis, USA](http://www.wikidata.org/entity/Q1852803)), [Gregor Hagedorn](https://orcid.org/0000-0001-7023-7386) ([JKI, Federal Research Institute for Cultivated Plants, Berlin, Germany](http://www.wikidata.org/entity/Q832099)), [Patrick Leary](https://orcid.org/0000-0001-5172-8577) (), [Dimitry Mozzherin](https://orcid.org/0000-0003-1593-1417) ([Encyclopedia of Life, Woods Hole, USA](http://www.wikidata.org/entity/Q82486)), [Annette Olson](https://orcid.org/0000-0002-0772-0022) ([American Association for the Advancement of Science](http://www.wikidata.org/entity/Q40358)), [Greg Riccardi](https://orcid.org/0000-0002-3850-9983) ([Florida State University, Tallahassee, USA](http://www.wikidata.org/entity/Q861548)), [Ivan Teage](https://orcid.org/0000-0003-4176-2274) (), [Steve Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University, Nashville, TN, USA](http://www.wikidata.org/entity/Q29052)), [Steve Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University, Nashville, TN, USA](http://www.wikidata.org/entity/Q29052))

Tvůrce
: GBIF/TDWG Pracovní skupina pro multimediální zdroje a Skupina pro údržbu audiovizuálního jádra

Bibliografická citace
: GBIF/TDWG Multimedia Resources Task Group and Audiovisual Core Maintenance Group. 2023. Struktura Audiovisual Core. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/structure/2023-02-24>

## 1. Úvod

Tato dokumentace popisuje strukturu standardu [TDWG](http://tdwg.org)
Audiovisual Core Multimedia Resources Metadata Standard (Audiovisual Core, nebo
jednoduše AC).

**Pokud nejste obeznámeni s Audiovisual Core, _prosím_ přečtěte si [Úvod do Audiovisual Core](../introduction) předtím, než začnete číst tento dokument.** Úvod vysvětluje, proč je vnímána potřeba metadatového schématu pro mediální zdroje týkající se biologické rozmanitosti a jak se standard snaží využívat stávající standardy metadat, kde je to možné.

Podrobnosti o termínech naleznete v dokumentu [Seznam základních termínů audiovizuální oblasti](../termlist) a podrobnějšího průvodce používáním základních termínů audiovizuální oblasti naleznete v dokumentu [Průvodce základními termíny audiovizuální oblasti](../guide).

Během vývoje bylo audiovizuální jádro neformálně známé jako MRTG, podle jeho vývojářů, společné pracovní skupiny GBIF-TDWG Joint Multimedia Resources Metadata Task Group. Podrobný popis historie vývoje naleznete v [Průvodci audiovizuálním jádrem](../guide) a také v [Historii vývoje MRTG](http://www.keytonature.eu/wiki/MRTG_Development_History).

### 1.1 Status obsahu tohoto dokumentu

Části 2 až 4 tohoto dokumentu jsou normativní, s výjimkou příkladových částí, které jsou označeny jako nenormativní.

### 1.2 Klíčová slova RFC 2119

Klíčová slova "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" a "OPTIONAL" v tomto dokumentu je třeba interpretovat podle popisu v [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 2 Terminologie této specifikace

Existuje mnoho způsobů, jak organizovat specifikace metadat, zejména pokud jde o
názvosloví složek metadat. Vezměte na vědomí
následující informace, které se vztahují k Audiovisual Core:

- _Multimediální zdroj_ je cokoli, co poskytovatel identifikuje jako
  patřící k jedné z možných hodnot termínu AC _Type_ a
  volitelně k jedné nebo více hodnotám termínu _Subtype_. Je k dispozici mechanismus, pomocí kterého mohou poskytovatelé dodávat soukromě definovaný podtyp, který nebude kolidovat s hodnotami podtypu definovanými AC.
- AC _záznam_ je soubor termínů s libovolnými hodnotami, které jsou v souladu s tímto dokumentem a které obsahují alespoň čtyři povinné termíny popsané v [Audiovisual Core Core Term List](../termlist) a které popisují jeden multimediální zdroj (případně včetně sbírky). Jednou z nich je hodnota _Identifier_, což je globálně jedinečný identifikátor (GUID), který může být přiřazen zdroji externí autoritou nebo poskytovatelem záznamu metadat.

V [seznamu termínů Audiovisual Core](../termlist) má každý termín AC _název termínu_ následující po položce tabulky _„Termín:“_, _URI_, normativní _definici_ v prostém textu, doporučený anglický _název_ a volitelný atribut _poznámky_. Kromě toho má termín atribut, který udává, zda je povinný, a atribut, který udává, zda je opakovatelný.

Metadata AC mohou popisovat buď jednotlivé multimediální zdroje, nebo sbírky zdrojů. Některé, ale ne všechny, vlastnosti AC mají pro sbírky jiné hodnoty než pro jednotlivá média. Pokud není takové rozlišení uvedeno, AC ho nepředpokládá.

Názvy termínů převzatých z jiných slovníků jsou ty, které se používají pro odpovídající termín v těchto slovnících. Názvy termínů jsou určeny především pro orientaci v dokumentaci AC. Štítky Term Labels jsou návrhy anglických označení v aplikacích. Jedná se pouze o doporučení, která jsou k dispozici pouze v angličtině, s tím, že by měla objasnit zamýšlené použití daného termínu.
Komunity mohou chtít vydat doporučení pro štítky v jiných jazycích nebo dokonce alternativní anglické štítky pro specializované publikum, např. školní děti. Štítky MOHOU být použity pro navigaci v rámci seznamu termínů a často se používají v samotném seznamu termínů, když je termín zmíněn v dokumentaci jiného termínu. Seznam termínů poskytuje rejstříky podle názvu i označení.

URI pro termíny odpovídají schématu http URI (viz http://en.wikipedia.org/wiki/URI_scheme, http://www.w3.org/TR/uri-clarification nebo http://www.ietf.org/rfc/rfc2396.txt). Neformálně lze toto pochopit následovně: http URI má syntaxi http URL, ale nelze očekávat, že jeho zadání do webového prohlížeče povede k vrácení jakýchkoli informací do prohlížeče, a pokud ano, nemusí to mít žádný význam. Tento požadavek na shodu se vztahuje pouze na URI, které identifikují termíny AC. Několik termínů AC umožňuje převzít **hodnoty** z jiného řízeného slovníku vybraného uživatelem. V tomto případě mohou tyto hodnoty zahrnovat URI odpovídající schématu danému tímto externím slovníkem a AC se k tomu, co je tím schématem, nevyjadřuje.

Pole Poznámky v dokumentaci k termínu odkazuje na další informace o termínu, pokud existují. Zejména u termínů převzatých z
jiných slovníků obsahuje toto pole obvykle odkaz na
dokumentaci původního slovníku pro daný
termín.

## 3 Multiplicita a kardinalita

Řada termínů se opakuje. Způsob implementace opakovatelnosti v
dané serializaci není definován Audiovisual Core. Následující
část obsahuje rady ohledně osvědčených postupů v kontextu
opakovatelnosti.

Nejjednodušším případem je jediný opakovatelný termín (např.
dcterms:identifier). V reprezentacích založených na schématu XML, které
umožňuje opakování prvků, lze takový termín jednoduše opakovat (např.
"`...<dcterms:identifier>http://example.com/123</dcterms:identifier><dcterms:identifier>http://example.com</dcterms:identifier>...`").
V serializacích, které se nehodí pro opakovatelné
prvky (např. „plochá“ schémata, kde se všechny prvky vyskytují pouze jednou
v jinak nestrukturovaném záznamu), je možné definovat
oddělovače pro podporu seznamu hodnot v rámci jednoho prvku (např.
„...<dcterms:identifier>http://example.com/123;
http://example.com/456</dcterms:identifier>...\`").

V některých případech se páry nebo dvojice vlastností opakují. V Audiovisual
Core k této situaci dochází například v následujících případech:

- Metadata závislá na jazyku, jako je název, popis atd., musí
  být spojena s `ac:metadataLanguage`. Jedním z přístupů je
  použít kompletní záznamy Audiovisual Core společně s vlastností [Metadata Language](../termlist#ac_metadataLanguage); další podrobnosti naleznete tam.
- Hodnoty vlastností týkající se přístupového bodu služby MUSÍ zůstat
  spojeny s tímto přístupovým bodem služby, i když existuje více
  přístupových bodů služby. Viz
  [ac:hasServiceAccessPoint](../termlist#ac_hasServiceAccessPoint)
  pro další podrobnosti.
- Termíny `dwc:scientificName` a `dwc:identificationQualifier` MOHOU
  být volitelně strukturovány do párů. (Viz poznámky k
  [dwc:identificationQualifier](../termlist#dwc_identificationQualifier).)
- Termíny [Recenzent](../termlist#ac_reviewer),  což je jméno osoby poskytující odbornou recenzi zdroje, a samotný text recenze v [Komentáře recenzenta](../termlist#ac_reviewerComments) je vhodné ukládat jako páry.

### 3.1 Strukturované serializace

Mnoho serializačních jazyků poskytuje dostatečně strukturované formy, aby
jednoznačně zpracovaly opakující se termíny. V XML můžeme definovat
kontejnerový prvek a použít vnořenou strukturu, jak je uvedeno v oddíle 3.1.1.  Alternativně můžeme v XML odkazovat na přístupové body pomocí identifikátoru, jak je uvedeno v oddíle 3.1.2.  Pokud takové struktury nejsou možné nebo nejsou žádoucí, alternativním
řešením je povolit pouze jeden přístupový bod na
kontejnerový prvek, ale opakovat kontejnerový prvek pro jeden mediální zdroj, jak je uvedeno v části 3.1.3. To je podobné
jedné z možností diskutovaných pro vícejazyčná metadata (viz [Metadata Language](../termlist#ac_metadataLanguage)).

Poznámka: V příkladech byly pro lepší srozumitelnost použity doslovné výrazy „dc:format“ a „ac:variantLiteral“. Za nejlepší postup se však považuje použití termínů s hodnotou IRI „dcterms:format“ a „ac:variant“ s kontrolovanými hodnotami IRI z [kontrolovaného slovníku pro formát](http://rs.tdwg.org/ac/doc/format/) a [kontrolovaného slovníku pro variantu](http://rs.tdwg.org/ac/doc/variant/).  Další informace naleznete v poznámkách k [dc:format](http://rs.tdwg.org/ac/doc/termlist/#dc_format) a [ac:variantLiteral](http://rs.tdwg.org/ac/doc/termlist/#ac_variantLiteral).

#### 3.1.1 Příklad vnořené struktury XML (nenormativní)

    ```
    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http//:example.com/pictures/thePicture.jpg</dcterms:identifier>
      ...
      <ac:hasServiceAccessPoint>
        <dc:format>image/jpeg</dc:format>
        <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
        ...
      </ac:hasServiceAccessPoint>
      <ac:hasServiceAccessPoint>
        ...
      </ac:hasServiceAccessPoint>
    <MEDIA_METADATA_CONTAINER>
    ```

#### 3.1.2 Příklad odkazu XML podle identifikátoru (nenormativní)

    ```
    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http://example.com/pictures/thePicture.jpg</dcterms:identifier>
      ...
      <ac:hasServiceAccessPoint>http://example.com/pictures/thePicture.jpg#ac0001</ac:hasServiceAccessPoint>
      <ac:hasServiceAccessPoint>http://example.com/pictures/thePicture.jpg#ac0002</ac:hasServiceAccessPoint>
      <ac:ServiceAccessPoint id="http://example.com/pictures/thePicture.jpg#ac0001">
        <dc:format>image/jpeg</dc:format>
        <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
        ...
      </ac:ServiceAccessPoint>
      ...
    <MEDIA_METADATA_CONTAINER>
    ```

#### 3.1.3 Příklad opakovaného prvku kontejneru XML (nenormativní)

    ```
    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http//:example.com/pictures/thePicture.jpg</dcterms:identifier>
      <dcterms:title>List červeného buku</dcterms:title>
      <dct:format>image/jpeg</dc:format>
      <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
      ...
    <MEDIA_METADATA_CONTAINER>
    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http://example.com/pictures/thePicture.jpg</dcterms:identifier>
      <dc:format>image/png</dc:format>
      <ac:accessURI>http://example.com/fullres/thePicture-hires.png</ac:accessURI>
      ...
    <MEDIA_METADATA_CONTAINER>
    ```

### 3.2 Tabulkové serializace

Stejná data jako v příkladech 3.1.1 až 3.1.3 lze serializovat jako „plochou“ tabulku podobnou tabulce v tabulkovém procesoru.

V příkladu v oddíle 3.2.1 se opakuje pouze požadovaný identifikátor, nikoli však
pole názvu. Zda se mají opakovat všechna pole, nebo zda se mají poskytnout všechna
pole pouze v prvním záznamu, přičemž pozdější záznamy se omezí na
identifikátor a vlastnosti přístupového bodu služby, je ponecháno na konkrétních
implementacích. V příkladu v části 3.2.1 je vlastnost `ac:hasServiceAccessPoint` potlačena
jako zbytečná.

#### 3.2.1 Příklad tabulky, ve které je každý přístupový bod služby uveden v samostatném řádku (nenormativní)

<table>
  <tbody>
    <tr>
      <td><strong>dcterms:identifier</strong></td>
      <td><strong>dcterms:title</strong></td>
      <td><strong>ac:variantLiteral</strong></td>
      <td><strong>dc:format</strong></td>
      <td><strong>ac:accessURI</strong></td>
    </tr>
    <tr>
      <td>http://example.com/pictures/thePicture.jpg</td>
      <td>List červeného buku</td>
      <td>Nejvyšší kvalita</td>
      <td>image/jpeg</td>
      <td>http://example.com/fullres/thePicture.jpg</td>
    </tr>
    <tr>
      <td>http://example.com/pictures/thePicture.jpg</td>
      <td>&nbsp;</td>
      <td>Nejvyšší kvalita</td>
      <td>image/png</td>
      <td>http://example.com/fullres/thePicture-hires.png</td>
    </tr>
    <tr>
      <td>http://example.com/pictures/thePicture.jpg</td>
      <td>&nbsp;</td>
      <td>Náhled</td>
      <td>image/png</td>
      <td>http://example.com/thumbs/thePicture-thumb.png</td>
    </tr>
  </tbody>
</table>

Další přístup (sekce 3.2.2) také eliminuje potřebu vlastnosti `ac:hasServiceAccessPoint` při
zploštění struktury ac. Je založeno na zavedení nových termínů
využívajících hodnoty [ac:variantLiteral](../termlist#ac_variantLiteral):
„Thumbnail“, „Trailer“, „Lower Quality“, „Medium Quality“, „Good
Quality“, „Best Quality“, „Offline“ jako předpony pro další
vlastnosti v novém jmenném prostoru.

#### 3.2.2 Příklad tabulky s metadaty pro všechny přístupové body služby ve stejném řádku (nenormativní)

<table>
  <tbody>
    <tr>
      <td><strong>dcterms:identifier</strong></td>
      <td><strong>dcterms:title</strong></td>
      <td><strong>acf:thumbnailAccessURI</strong></td>
      <td><strong>acf:thumbnailFormat</strong></td>
      <td><strong>acf:thumbnailImageWidth</strong></td>
      <td><strong>acf:thumbnailImageHeight</strong></td>
      <td><strong>acf:goodQualityAccessURI</strong></td>
      <td><strong>acf:goodQualityFormat</strong></td>
      <td><strong>acf:goodQualityImageWidth</strong></td>
      <td><strong>acf:goodQualityImageHeight</strong></td>
      <td><strong>acf:bestQualityAccessURI</strong></td>
      <td><strong>acf:bestQualityFormat</strong></td>
      <td><strong>acf:bestQualityImageWidth</strong></td>
      <td><strong>acf:bestQualityImageHeight</strong></td>
    </tr>
    <tr>
      <td>http://ex.com/pictures/thePicture.jpg</td>
      <td>List červeného buku</td>
      <td>http://example.com/thumb/thePic.jpg</td>
      <td>image/jpeg</td>
      <td>100</td>
      <td>100</td>
      <td>http://ex.com/img/thePic.jpg</td>
      <td>image/jpeg</td>
      <td>1000</td>
      <td>1000</td>
      <td>http://ex.com/hr/thePic.png</td>
      <td>image/png</td>
      <td>10000</td>
      <td>10000</td>
    </tr>
  </tbody>
</table>

Poznámka: `acf:` (zkratka pro „Audiovisual Core Flat“) je vymyšlený jmenný prostor.  Zájmové komunity mohou takové termíny vytvářet, aby mohly využívat tento druh struktury.

## 4 Seznamy hodnot v prostém textu

Některé termíny AC povolují hodnoty, které jsou seznamy, aby byly reprezentovány jako prostý
text. Volba způsobu oddělení položek seznamu je nakonec ponechána na
implementátorech AC. Typickým použitím je volba interpunkčního znaménka, jako je
„,“, „;“ nebo „|“. V těchto případech je třeba definovat speciální únikovou syntaxi
pro případy, kdy je oddělovač součástí hodnoty metadat.
Bohužel i u standardních formátů seznamů, jako je CSV, používají různé
softwarové balíčky různé metody únikových znaků, což brání
výměně dat. V případě, že neexistuje možnost volby specifická pro danou implementaci,
DOPORUČUJEME použít jako oddělovač znak "|" a jako escapovaný svislý pruh znak "\\|".
