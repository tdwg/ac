# Příručka Audiovisual Core

Název
: Příručka Audiovisual Core

Datum vydání verze
: 2023-02-24

Datum vytvoření
: 2013-10-15

Součást TDWG Standardu
: <http://www.tdwg.org/standards/638>

Tato verze
: <http://rs.tdwg.org/ac/doc/guide/2023-02-24>

Poslední verze
: <http://rs.tdwg.org/ac/doc/guide/>

Předchozí verze
: <http://rs.tdwg.org/ac/doc/guide/2013-10-15>

Abstrakt
: Audiovisual Core je soubor slovníků určených k reprezentaci metadat pro multimediální zdroje a sbírky týkající se biologické rozmanitosti. Tento nenormativní dokument poskytuje některé základní informace o cílech a použití normy.

Přispěvatelé
: [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) ([University of Massachusetts at Boston, USA](http://www.wikidata.org/entity/Q15144)), [Vijay Barve](https://orcid.org/0000-0002-4852-2567) (), [Mihail Carausu](https://orcid.org/0000-0002-8234-0599) ([Danish Biodiversity Information Facility (DanBIF), Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [Vishwas Chavan](https://orcid.org/0000-0002-3425-6499) ([Global Biodiversity Information Facility, Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [José Cuadra](http://www.wikidata.org/entity/Q51883873) (), [Chris Freeland](https://orcid.org/0000-0002-2541-5822) ([Missouri Botanical Garden, St. Louis, USA](http://www.wikidata.org/entity/Q1852803)), [Gregor Hagedorn](https://orcid.org/0000-0001-7023-7386) ([JKI, Federal Research Institute for Cultivated Plants, Berlin, Germany](http://www.wikidata.org/entity/Q832099)), [Patrick Leary](https://orcid.org/0000-0001-5172-8577) (), [Dimitry Mozzherin](https://orcid.org/0000-0003-1593-1417) ([Encyclopedia of Life, Woods Hole, USA](http://www.wikidata.org/entity/Q82486)), [Annette Olson](https://orcid.org/0000-0002-0772-0022) ([American Association for the Advancement of Science](http://www.wikidata.org/entity/Q40358)), [Greg Riccardi](https://orcid.org/0000-0002-3850-9983) ([Florida State University, Tallahassee, USA](http://www.wikidata.org/entity/Q861548)), [Ivan Teage](https://orcid.org/0000-0003-4176-2274) ()

Tvůrce
: GBIF/TDWG Pracovní skupina pro multimediální zdroje a Skupina pro údržbu audiovizuálního jádra

Bibliografická citace
: GBIF/TDWG Multimedia Resources Task Group and Audiovisual Core Maintenance Group. 2023. Příručka Audiovisual Core. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/guide/2023-02-24>

## 1. Úvod

Audiovisual Core Multimedia Resources Metadata Schema (Audiovisual Core) je datový standard pro výměnu dat popisujících multimediální zdroje a sbírky týkající se biologické rozmanitosti, který vytvořila společná pracovní skupina GBIF/TDWG pro metadata multimediálních zdrojů (MRTG).  Norma se skládá ze čtyř dokumentů.  Tento dokument je průvodcem po cílech a použití normy. The Audiovisual
Core Introduction document provides a brief introduction to the Audiovisual Core Standard. Podrobné informace o struktuře Audiovisual Core naleznete v dokumentu [Audiovisual Core Structure](structure).  Podrobnosti o termínech najdete v dokumentu [Seznam termínů Audiovisual Core](terms).

Zkratky a názvy institucí a projektů jsou uvedeny ve slovníku v
příloze I.

### 1.1 Status obsahu tohoto dokumentu

Všechny části tohoto dokumentu jsou nenormativní.

## 2 Shrnutí

Audiovisual Core Multimedia Resources Metadata schema („schéma AC“ nebo
jednoduše „AC“) je soubor slovníků metadat pro popis
multimediálních zdrojů a sbírek souvisejících s biologickou rozmanitostí. Specifikace
je nezávislá na tom, jak mohou být tyto slovníky
zobrazeny pro strojové využití.

Multimediální zdroje jsou digitální nebo fyzické artefakty, které obvykle
obsahují více než jen text. Mezi ně patří obrázky, umělecká díla, kresby,
fotografie, zvukové záznamy, videa, animace, prezentační materiály a
interaktivní online média, včetně např. identifikačních nástrojů. Multimediální
sbírka je souborem takovýchto objektů, ať už kurátorských
či nikoli, a ať už elektronicky přístupných či nikoli. Pro účely
tohoto dokumentu považujeme soubor multimediálních zdrojů sám o sobě
za ‘multimediální zdroj’. Kdykoli se diskuse nebo specifikace může
vztahovat pouze na sbírku nebo pouze na jeden mediální zdroj, výslovně to uvádíme.

Multimediální popisy jsou digitální záznamy, které dokumentují základní
multimediální zdroje nebo sbírky. AC se zaměřuje na
multimediální zdroje související s biologickou rozmanitostí. Sdílí terminologii a
zájmy s mnoha známými a důležitými standardy pro popis
přístupu k zdrojům, jako jsou Dublin Core (DC), Darwin Core (DwC),
Adobe Extensible Metadata Platform (XMP), International Press and
Telecommunications Council (IPTC), Metadata Working Group (MWG)
schema, Natural Collections Schema (NCD) a další. V případě
přesné shody s použitím těchto standardů přijímá AC jejich
identifikátory a definice. Mnohé sbírky multimédií o biologické rozmanitosti
již obsahují popisy svých médií vyjádřené v DwC nebo DC. Použitím
těchto slovníků tam, kde je to vhodné, chce AC zejména usnadnit
opětovné použití stávajících popisů v těchto sbírkách,
v případě potřeby doplněných o další termíny.

This guide accompanies the normative parts of the AC standard,
which are included in two documents: one that describes the structure of the document <sup id="cit-1">[\[1\]](#fn-1)</sup>
and a Term List document <sup id="cit-2">[\[2\]](#fn-2)</sup>. Seznam termínů
dokumentuje řadu termínů, z nichž každý je identifikován jedinečným
identifikátorem URI (Uniform Resource Identifier), spolu s normativními definicemi.
In addition, the Audiovisual Core Maintenance Group may develop recommended representations for AC
descriptions in several important forms including RDF <sup id="cit-3">[\[3\]](#fn-3)</sup>, XML
Schema <sup id="cit-4">[\[4\]](#fn-4)</sup>, and Comma Separated Values (CSV) <sup id="cit-5">[\[5\]](#fn-5)</sup>.

Figure 1 below augments a portion of Figure 2 of the non-normative
portion of the NCD document <sup id="cit-6">[\[6\]](#fn-6)</sup>. Ukazuje řadu druhů
zdrojů zaměřených na data o biologické rozmanitosti a ilustruje typické uživatelské
komunity, standardy dat a metadat a síťové služby, které
podporují vyhledávání, analýzu a integraci dat. Z údajů NCD jsme extrahovali
zdroje a vztahy mezi nimi, které
jsme doplnili o tři typy, které nespadají do hlavní působnosti NCD. Jedná se o:
Pozorování, ekologické modely a zaměření této práce, multimediální
zdroje. Applications exploiting each kind of these resources find
utility, or sometimes require the use of multimedia resources to
document them. Například Biological Heritage Library je projekt,
který poskytuje naskenované obrázky starší literatury v mnohem větším rozsahu,
než kolik může poskytnout digitalizovaných verzí založených na optickém rozpoznávání znaků,
a tyto obrázky zůstávají k dispozici jako zdroje pro jakékoli
následné odvozené produkty. Digitálně zpracovaná historická literatura je tedy
dokumentována pomocí obrázků stránek. Většina vědecké literatury je samozřejmě také ilustrována fotografiemi, grafy nebo jinými artefakty, které spadají do působnosti Audiovisual Core. Dokonce i poskytovatelé zdrojů „molekulární DNA“ někdy nabízejí původní data ve formě digitálních obrazů na mikročipech.

![](assets/images/guide_fig_1.png)

Obrázek 1. Vztahy multimediálních zdrojů k primárním typům
zdrojů biologické rozmanitosti

## 3 Audiovisual Core Terms

An Audiovisual Core record is a description, using the Audiovisual Core terms,
of a multimedia resource. AC specifikuje dva druhy termínů:
_termíny na úrovni záznamu_ a _termíny na úrovni přístupu._ Termíny na úrovni záznamu se vztahují
k popisovanému mediálnímu zdroji. Almost all terms are record-level
terms. One such term, _serviceAccessPoint_ plays a special role in
helping to retrieve the resource that the record describes. A multimedia
resource may have more than one serviceAccessPoint, each of which is
described by values of one or more access-level terms. The access-level
terms provide such things as a web address at which a digital
representation of the resource can be retrieved, the size of such a
retrieved object, etc.

An Audiovisual Core record is thus a set of terms that conforms to the
normative documents, contains at least the four mandatory terms
described below, and which provides metadata that describes a single
multimedia resource (possibly including a Collection). It usually
includes an identifier that may have been assigned to the resource by an
external authority or by the provider of the metadata record.

Every Audiovisual Core term has a plain text Name, a URI, and a plain text
normative Definition. Termíny mohou také obsahovat pokyny k použití, které vysvětlují, jak se termín používá v kontextu Audiovisual Core, a poznámky, které poskytují další informace a příklady.  URI pro termíny odpovídají schématu http URI.
Neformálně lze toto pochopit takto: http URI má syntaxi
http URL, ale neočekává se, že jeho zadání do webového
prohlížeče povede k vrácení jakýchkoli informací do prohlížeče,
a pokud ano, vrácené informace nemusí mít žádný význam.

Protože adresy URL jsou poměrně dlouhé, dokumenty AC se řídí standardní
praxí zavádění krátké předpony sestávající z „kvalifikátoru jmenného prostoru“
odděleného dvojtečkou od mnemotechnického názvu úzce souvisejícího s
názvem termínu. Jmenný prostor termínů převzatých z jiných slovníků je stejný jako jmenný prostor původních termínů. The namespace of denovo AC terms is
http://rs.tdwg.org/ac/terms/. V tabulce termínů má každý termínový záznam
řádek s názvem termínu. Following the practice of the Darwin Core term
list <sup id="cit-7">[\[7\]](#fn-7)</sup>, for borrowed terms, this term name is generally an
"unqualified name" preceded by a widely accepted prefix designating an
abbreviation for the namespace, whereas for denovo AC terms, no such
prefix is prepended. It is recommended that implementers who need a
namespace prefix for the AC namespace use "ac" wherever feasible. The
result is known as a qualified name. Například normativní wiki
dokumentace pro vypůjčený termín dcterms:identifier má URI
http://purl.org/dc/terms/identifier. V tomto dokumentu budeme dodržovat zavedenou
konvenci kvalifikovaných názvů. Ve
skutečnosti se většina URI pro termíny převzaté z externích slovníků
(asi polovina z nich) ve skutečnosti odkazuje na něco v příslušné
dokumentaci pro daný externí standard. Někdy to není přesné,
protože dokumentace je ve formátu PDF a několik (různých\!)
URI mohou zřejmě směřovat na stejné místo.

Příklady z termínového seznamu jsou uvedeny
níže.

<table>
	<tbody>
		<tr>
			<td>Název termínu:</td>
			<td>dcterms:type</td>
		</tr>
		<tr>
			<td>Normativní URI:</td>
			<td><a href="http://purl.org/dc/terms/type" rel="nofollow">http://purl.org/dc/terms/type</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>Typ</td>
		</tr>
		<tr>
			<td></td>
			<td>Layer:&nbsp;1 —&nbsp;Required:&nbsp;Yes —&nbsp;Repeatable:&nbsp;No</td>
		</tr>
		<tr>
			<td>Definice:</td>
			<td>Povaha nebo druh zdroje.</td>
		</tr>
		<tr>
			<td>Použití:</td>
			<td>A full URI preferably from among the type URIs specified in the DCMI Type Vocabulary, <a href="http://dublincore.org/documents/dcmi-type-vocabulary/#section-7-dcmi-type-vocabulary" rel="nofollow">http://dublincore.org/documents/dcmi-type-vocabulary/#section-7-dcmi-type-vocabulary</a>. Doporučené termíny jsou ty URI, jejichž označení jsou Collection, StillImage, Sound, MovingImage, InteractiveResource nebo Text (např. . Doporučujeme také úplné URI adresy ac:PanAndZoomImage, ac:3DStillImage a ac: 3DMovingImage. Hodnoty NESMÍ být řetězcem, ale URI s úplným jmenným prostorem (např. z řízeného slovníku. Implementátoři a komunity praxe mohou určit, zda je nutné používat konkrétní řízené slovníky. Pokud je zdroj sbírkou, tato položka neurčuje, jaké typy objektů může obsahovat. V souladu s doporučeními DC na adrese <a href="http://purl.org/dc/dcmitype/Text" rel="nofollow">http://purl.org/dc/dcmitype/Text</a> by obrázky textu měly mít tuto URI.</td>
		</tr>
		<tr>
			<td>Poznámky:</td>
			<td>V souladu s doporučeními DC pro typ textu <a href="http://purl.org/dc/terms/DCMIType" rel="nofollow">http://purl.org/dc/terms/DCMIType</a> by obrázky textu měly být uvedeny jako http://purl.org/dc/dcmitype/Text, pokud jsou uvedeny jako URI. Viz také heslo dc:type v dokumentu Audiovisual Core term list (Seznam základních audiovizuálních termínů) a viz DCMI FAQ on DC and DCTERMS Namespaces (Často kladené otázky týkající se jmenných prostorů DC a DCTERMS), <a href="https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md" rel="nofollow">https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, kde se diskutuje o důvodech pro použití termínů ve dvou jmenných prostorech. Obvyklým postupem je použít stejný štítek, pokud jsou k dispozici oba. Labels have no effect on information discovery and are only suggestions. At least one of dc:type and dcterms:type must be supplied but, when feasible, supplying both may make the metadata more widely useful. The values of each should designate the same type, but in case of ambiguity dcterms:type prevails.</td>
		</tr>
	</tbody>
</table>

<table>
	<tbody>
		<tr>
			<td>Název termínu:</td>
			<td>ac:reviewerLiteral</td>
		</tr>
		<tr>
			<td>Normativní URI:</td>
			<td><a href="http://rs.tdwg.org/ac/terms/reviewerLiteral" rel="nofollow">http://rs.tdwg.org/ac/terms/reviewerLiteral</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>Recenzent</td>
		</tr>
		<tr>
			<td></td>
			<td>Layer:&nbsp;2 —&nbsp;Required:&nbsp;No —&nbsp;Repeatable:&nbsp;Yes</td>
		</tr>
		<tr>
			<td>Definice:</td>
			<td>String providing the name of a reviewer. If present, then resource is peer-reviewed, even if Reviewer Comments is absent or empty. Its presence tells whether an expert in the subject featured in the media has reviewed the media item or collection and approved its metadata description; must display a name or the literal "anonymous" (= anonymously reviewed).</td>
		</tr>
		<tr>
			<td>Poznámky:</td>
			<td>Poskytovatel tvrdí, že tuto recenzi přijímá jako kompetentní. Viz také ac:reviewer a část Jmenné prostory, předpony a názvy termínů v dokumentu Audiovisual Core Term List, kde se diskutuje o důvodech pro oddělení termínů, které používají hodnoty URI, od termínů, které používají textové hodnoty, pokud jsou možné obě varianty. Obvyklým postupem je použít stejný štítek, pokud jsou k dispozici oba. Štítky nemají žádný vliv na vyhledávání informací a slouží pouze jako doporučení.</td>
		</tr>
	</tbody>
</table>

Hlavní kvalifikátory jmenného prostoru pro termínové URI v tomto dokumentu jsou

- **dcterms:** and **dc:** The DCMI vocabulary documented at
  http://dublincore.org/documents/dcmi-terms

- **dwc:** The Darwin Core vocabulary described at
  http://rs.tdwg.org/dwc/index.htm

- **Iptc4ampExt:** Geographic extensions to IPTC with namespace
  http://iptc.org/std/Iptc4xmpExt/2008-02-29/ documented in
  http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf

- **ac:** Terms in the namespace http://rs.tdwg.org/ac/terms not derived
  from other controlled vocabularies.  The normative definitions of these documents can be found in the [Audiovisual Core Term List document](termlist.md)

- **xmp:** Slovníky Adobe XMP s jmenným prostorem
  http://ns.adobe.com/xap/1.0/, dokumentované v oddíle 8.4 dokumentu
  https://wwwimages2.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2016-08/XMPSpecificationPart1.pdf

- **xmpRights:** Slovník práv Adobe XMP s jmenným prostorem
  http://ns.adobe.com/xap/1.0/rights, dokumentovaný v oddíle 8.5 na adrese
  https://wwwimages2.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2016-08/XMPSpecificationPart1.pdf

- **photoshop:** Další vlastnosti Adobe XMP s jmenným prostorem http://ns.adobe.com/photoshop/1.0/ jsou dokumentovány na adrese http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2014-12/XMPSpecificationPart2.pdf

- **exif:** slovník formátu Exchangeable Image File Format asociace Camera and Imaging Products Association s jmenným prostorem http://ns.adobe.com/exif/1.0/ zdokumentovaný v http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf

## 4 Motivace a odůvodnění

Existuje mnoho cenných multimediálních zdrojů, které neobsahují žádné informace uložené v databázích. Někteří mohou mít webovou prezentaci, jiní nikoli. I ty, které jsou
dostupné online, nemusí být pro vyhledávače dostatečně zjistitelné,
nebo se mohou ztratit v záplavě obrázků z nespolehlivých zdrojů. Stručný
popisný záznam, jak je definován standardem Audiovisual Core, může sloužit jako
„vizitka“ multimediálního zdroje a poskytovat dostatek
informací k identifikaci a vyhledání mediálních zdrojů výzkumníky,
agregátory, rozhodovacími činiteli, pedagogy nebo širokou veřejností.

Standard umožňuje agregaci popisů multimediálních zdrojů
z mnoha zdrojů a usnadňuje vyhledávání zdrojů, včetně
vytváření vztahů mezi multimediálními zdroji na několika
místech. Záznamy AC lze také použít jako pomůcku pro procesy správy multimediálních
zdrojů, což umožňuje instituci udělat krok
zpět a zjistit, které sbírky nejvíce potřebují konzervaci nebo by
měly vyšší prioritu pro katalogizaci na úrovni jednotlivých položek.

Mezi důležité využití identifikované pracovní skupinou, které jsou usnadněny
metadaty, patří:

1. Discovery;

2. Hodnocení vhodnosti použití před načtením zdroje
   (zejména relevantní pro offline zdroje);

3. Použití záznamů metadat jako potenciálního důkazu výskytu taxonu nebo
   jiných biologických závěrů, jako jsou důkazy o interakcích druhů, stanovištích a fenotypových variacích;

4. Identifikační pomůcky;

5. Snížení zátěže poskytovatelů a producentů multimediálních zdrojů při
   shromažďování a poskytování zdrojů od široké škály
   producentů a správců, zejména těch, kteří mají malé nebo žádné znalosti
   v oblasti IT nebo podpory.

Aby byly překážky použití co nejmenší, jsou pouze čtyři
vlastnosti záznamu Audiovisual Core považovány za povinné:

1. Identifier (dcterms:identifier): An arbitrary code that is unique
   for the resource, with the resource being either a provider,
   collection, or media item. Whereas the identifier must be globally
   unique for providers and collections (e. g. a URI), identifiers for
   media items may be unique only within the context of a collection or
   provider. In fact the standard strongly recommends but does not
   require an Identifier for media items, though it does so for a
   provider or collection.

2. Type (dcterms:type): Any dcmi type term from
   http://dublincore.org/documents/dcmi-type-vocabulary/#section-7-dcmi-type-vocabulary may be used.
   Recommended terms are Collection, StillImage, Sound, MovingImage,
   InteractiveResource, and Text.

3. Metadata Language (ac:MetadataLanguage): Language of description and
   other metadata (but not necessarily of the image itself)

4. Copyright Statement (dcterms:rights): Information about rights held
   in and over the resource. A full-text, readable copyright statement,
   as required by the national legislation of the copyright holder. On
   collections, this applies to all contained objects, unless the
   object itself has a different statement. When available, it is also
   recommended to provide the Copyright Owner using xmpRights:Owner

In addition it is strongly recommended to provide a concise title of the
resource, using dcterms:title

## 5 Stávající normy

The Audiovisual Core intends to provide metadata that describe either media
resources themselves or collections of them. There are several
well-known or newly emerging standards that address these concerns, so
one may ask: why not simply use them? In fact, AC does exactly that in
about half of its 80 elements, almost all of which are optional. Indeed,
as shown above, most of the mandatory terms come from external
controlled vocabularies. However, all existing controlled vocabularies,
most notably the widely used Dublin Core, present very few opportunities
to provide media resource content metadata that is specifically
biologically relevant. Use of the Dublin Core alone would make it
difficult to do media resource discovery with high precision. Thus, one
consequence of using Dublin Core alone would be that queries will not be
selective enough. By contrast the Darwin Core TDWG standard <sup id="cit-8">[\[8\]](#fn-8)</sup> has
more support for some such concerns, but little about important
intellectual property rights issues, or ways to express relationships
between alternate versions of media resources (e.g. different resolution
versions). In turn, neither of these controlled vocabularies has
mechanisms for capturing technical metadata, such as EXIF, which the
imaging systems themselves, or metadata embedding tools, such as Adobe
Photoshop(tm) and the GIMP open source image editor, can insert into
media files and streams. To address this, and in furtherance of the
above goals, the Audiovisual Core should be regarded as a synthesis of DC,
DwC, and, where those are inadequate, some forward looking metadata
standards that the camera manufacturers are presently planning to
support within the cameras themselves, much as they now use EXIF <sup id="cit-9">[\[9\]](#fn-9)</sup>.
Where any of these standards suffice, AC metadata terms and definitions
are those of such standards. In some instances, we find that none of
these address concerns that our experience suggests are held by a wide
variety of image contributors, especially those with limited access to
sophisticated IT staff or to Digital Librarians. The AC schema might be
regarded as an extension to the union of small subsets of several
accepted standards (together with a framework to insure that use of
metadata from these standards can be understood by people and machines
as referring to the same resource). Put another way, much of AC may be
viewed as a wrapper around DwC, DC, XMP, and IPTC <sup id="cit-10">[\[10\]](#fn-10)</sup>.

Since the overwhelming portion of the AC metadata fields are optional, a
resource provider that can already serve Dublin Core metadata, could
essentially serve little else but that, plus a suitable globally unique
identifier to tie all the metadata to the same object. Similarly, a
provider describing image content entirely with Darwin Core terms might
have little more to do. However, both such providers would find that
value-added services such as metadata-indexers and caching aggregators
and would be less likely to keep references to their media resources and
metadata than if they had richer metadata. This gives a clear strategy
for providers to increase the utility of their multimedia resources with
little or no impact on their IT cyberinfrastructure services. They may
need only to update mappings between their internal field names and the
metadata terms specified by AC, as personnel become available to do so.
As more resources become available to record additional metadata, and as
community annotation mechanisms arise to support this, they can add the
additional metadata at a pace determined by their own resources. If
harvesters of the metadata monitor the (optional) Metadata Date property
(xmp:MetadataDate), the updated metadata can automatically be pulled by
those value-added services, and more queries will return the provider's
metadata and references to its media resources.

## 6 Common Concerns with Other Biodiversity Information Standards

The Audiovisual Core regards Collections of Multimedia Resources themselves
as a kind of Resource. Many types of Collections are describable in the
pending TDWG Natural History Collections (NCD) proposed standard. If a
provider wishes only to provide for discovery of a multimedia Collection
without regard to discovery of and access to its contents (other than
sub Collections), it will often be immaterial whether NCD or AC
metadata, or both, are served. This is all the more so if the NCD
CollectionIdentifier and the Audiovisual Core Identifier have the same
value. While Audiovisual Core Collection types are richer than NCD types, it
is an open question whether Audiovisual Core's variety in this case is
useful.

There is substantial overlap with use of Darwin Core terms, notably with
respect to taxonomic, geographic, and temporal coverage of the data
being described by the metadata record. We use DwC terms for most of
those metadata and the entirety of the Darwin Core geolocation vocabulary
are included by reference. GPS point locations increasingly common in
image data created by cameras is easily mapped to the 'verbatim'
locality terms of Darwin Core.

## 7 Concerns Not Emphasized in Other Biodiversity Information Standards

Some of the concerns mentioned here are also those of bibliographic
metadata such as the Dublin Core. These are, however, not explicitly of
detailed concern in existing TDWG biodiversity standards, and some are
not adequately addressed by DC. Some such concerns are below.

**Size**: Individual multimedia resources such as images, and especially
video and sound are very large compared to specimen records, observation
data, or species descriptions. The main consequence of this is that
multimedia metadata must support use cases for which humans or software
agents can, without fetching the resource, attempt to assess the fitness
of the underlying media resource for the desired use, typically by use
of a search based on a fine-grained controlled vocabulary. However,
without hit-and-miss natural language searches, it is not possible, even
using both DC and DwC, for a metadata provider to answer a request of
the form "Supply me with sizes and URL access points for still images of
_Dictyophora indusiata_ and which have Spanish metatdata available.

**Intellectual Property Rights**: DwC describes physical objects, whose
ownership is generally governed by property laws not considered part of
the Intellectual Property Rights corpus of law. Some impending standards
about scientific literature address these, but rarely are publication
reproduction permission issues as varied as for multimedia, which have a
history of being treated as creative works of art, not necessarily as
facts.

**Provenance**: For any scientific data, it is clearly important to know
how and when the data may have been changed from its original gathering.
This is particularly important for media, which are commonly edited for
one or another purpose. If carelessly done, this may destroy some if the
modified object's utility. No TDWG standards or proposed standards seem
very robust about provenance, including Audiovisual Core, which provides
only the Derived From property in order to provide a reference to
another resource. This is somewhat akin to the NCD DerivedCollection
term, which identifies a Collection record as having been produced by a
query to another Collection. However, that apparently does not identify
the source collection or the query. A future version of Audiovisual Core
will add more provenance terms.

## 8 Multimedia Resource Descriptions

The term Multimedia Resources encompasses a wide variety of objects of
interest to biologists and the communities with whom they interact for
research, education, and public service. Some instances of multimedia
are familiar. These include:

- Still images from cameras, scanners, or medical and industrial
  imaging devices

- Movies with or without sound

- Audio recordings

In some of the above cases, these resources may exist in electronic or
non-electronic form or both. The electronic form may be analog or
digital, the latter being more amenable to storage and exchange with
computers. The digital form may have been born digital, i.e. originally
captured as a digital object, or it may have been created from a
non-digital object. As with biological specimen records, publications,
field notes, experimental data and other artifacts of the practice of
science, there is a large quantity of such material that has not yet
been digitized, yet which may be available, albeit with greater expense
and inconvenience than digital resources. These analog (including paper)
resources still require descriptive metadata to promote discovery and to
ascertain fitness-for-use. At least as important, some of the metadata
is itself of scientific and educational use even if the object is not
conveniently accessible. Evidence for georeferenced taxon occurrence is
one such use.

Audiovisual Core metadata also can describe resources less often thought of
as multimedia objects. These include:

- Interactive software applications, either on the web or available
  for stand-alone use

- Taxonomic identification keys

- Collections of multimedia resources

- Web sites not otherwise falling into one of the above categories

## 9 Audiovisual Core Records

The normative Audiovisual Core metadata record specification is independent
of the way in which those records are rendered into electronic form.
MRTG intends to publish specifications for such rendering represented
in, represented in XML constrained by an XML-Schema, and represented in
plain text as comma separated values (CSV). [Sections 4.4 to 4.5 of the TDWG Standards Documentation Specification](https://github.com/tdwg/vocab/blob/master/sds/documentation-specification.md#44-vocabularies-term-lists-and-terms) describe how basic term metadata should be expressed in machine-readable forms such as RDF serializations.  A future task group might develop a more semantically rich machine-readable ontology following the procedures listed in [Section 4 of the TDWG Vocabulary Maintenance Specification](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements).

The language of the normative Audiovisual Core specification is English, but
this in no way constrains applications from using labels or content of
the metadata in local languages. Because its language is English, each
metadata item in the normative document has an English label (which
might, for example be part of a user interface), but these, too, are not
required to be used by applications, although their use is strongly
encouraged, at least in documentation.

As mentioned earlier, an Audiovisual Core metadata record is a set of terms
describing the underlying multimedia resource that the record describes.
Each term is identified by a Uniform Resource Identifier (URI). These
are URIs of the attribute, not of the underlying resource, and they
simply specify which term is being provided. There are many URI schemes,
some of which have been registered with the Internet Assigned Names
Authority (IANA). All Audiovisual Core term URIs, conform to the http URI
Scheme. This is chosen because this widely used URI scheme uses the
familiar internet URL syntax as its URI syntax. But this familiarity
gives rise to a common misconception, namely that pasting the URI into a
browser URL line, or providing it to some other application that
respects the http protocol, should result in the application returning
some information about the object identified by the URI. Such behavior
is usually called resolution (or, more technically, resolution and
dereferencing) of the URI and is in no way guaranteed for Audiovisual Core
term URIs. Where possible, we in fact try to make http URIs be
resolvable, with the information returned being documentation for how
the metadata attribute identified by that URI is defined or use. To
reiterate: for Audiovisual Core term URIs, any such resolution will never
contain information about the underlying multimedia resource being
described. For this reason, few human-centric Audiovisual Core applications
should ever present the URIs to users, nor use them as linking
mechanisms. (One possible exception is an application for assigning
metadata to multimedia resources, where such a use may provide a
thesaurus entry aiding the user in the semantics of the metadata
property. However, the incidental nature of the resolution, and its lack
of guaranteed long term persistence, makes even this approach one that
should be considered with extreme caution.) Finally, note that some
external controlled vocabularies are defined in PDF or other documents
that do not have URL links directly to each defined term. In these
cases, any resolution available from the normative document may only
link to the beginning of the document, leaving it necessary to search in
the document for the referenced definition.

Associated to each Audiovisual Core property is its value. The datatype of
this value is also specified in the normative document. Datatypes can
include free text, specific literals taken from a controlled vocabulary
specified in the normative document, or a number of other datatypes
specified and described in the normative document. In the case of a
controlled vocabulary, it is important to note that whatever an
application may present in a user interface, any Audiovisual Core metadata
interchange should use the literals from a specified controlled
vocabulary when one is specified, even if the record is declared to be a
record in a different language than that of the controlled term. An
important example is the Type metadata field, which is recommended to
come from the corresponding vocabulary from Dublin Core, augmented by
some recommended in the normative document. (We also add to that an
optional field Subtype.) Similarly, agents answering Audiovisual Core
metadata queries MUST be able to consume and respond to queries framed
with the controlled vocabulary. Nothing in the normative document
prevents an Audiovisual Core data provider from asserting it has no records
with a given controlled term, nor from internally mapping between a
controlled vocabulary and its internal attributes, whose names may well
be in a language other than English. Only a small number of Audiovisual Core
properties take values in a specific, English-based controlled
vocabulary. This will become relevant only for metadata interchange. Of
the mandatory terms, only Type has any such requirements.

An Audiovisual Core record consists minimally of the four mandatory fields
(Identifier, Type, Metadata Language, and Copyright Statement).

In some cases, some metadata terms are necessarily related to others
(e.g. various versions of an image must be associated the "main"
version). However, spreadsheets and other flat sources of contributor
metadata are regarded as particularly important, and in many of these it
is difficult to represent such structural relationships. Consequently an
Audiovisual Core record is itself mainly flat, the exception being the
object of a property named _hasServiceAccessPoint_. This object itself
has further properties that describe how to fetch the actual media
described by the AC record. One consequence of this is that, for some
purposes, a metadata Provider might have to make several metadata
records available about the same underlying resource, because the
representation-neutral Audiovisual Core specification does not provide for
“subproperties” on its properties, or for relations in most cases. An
important case surrounds multilingual metadata. Because each metadata
record is in a fixed language specified by the Metadata Language
property (this is the language of the record, not the multimedia
resource, in case it should have one), a Provider might have to offer
several metadata records about the same multimedia resource. The values
of the four required terms must be provided in every metadata record,
even if repeated in other metadata records describing the same resource.
At the date of this writing, the normative document does not provide a
mechanism for identifying a metadata record that might be overarching,
in the sense that its optional terms may be regarded as defaults for any
not specified in other records about the same resource. This point is
under discussion on the MRTG Wiki.

Many items may be repeated in an Audiovisual Core record, but some may not,
as indicated in the normative document. For example the Modified item
corresponds to a date at which the media resource was modified and may
be repeated to reflect the history of the resource. By contrast, Date
Available is a single date or a single range of dates at which the
underlying resource became, or will become, available.

## 10 Implementation and Compliance

Audiovisual Core is defined in a way that is as representation-neutral as
possible. It provides natural language definitions of classes,
properties and instances that are identified by URIs and it makes
recommendations on the use and content of properties from other
vocabularies.

The URIs defined here may be used across a number of technologies, such
as namespaces in XML Schema-valid table documents, RDF, and column
headings in comma delimited text files.

This approach facilitates:

- Embedding of Audiovisual Core data within other standards such as
  descriptions of specimens or literature.

- The extension of Audiovisual Core records with other data types such as
  the extensive geographic controlled vocabularies of the Open
  Geospatial Consortium (OGC)

- Cross walking between technologies such as a Comma Separated Value
  file, an RDF graph, an XML document and a JSON object.

The Audiovisual Core representation-neutral normative standard itself does
not provide an off-the-shelf, self validating exchange format. Multiple
such exchange formats meeting different requirements can be defined and
this standard allows mapping between them.

## 11 Further Information

- Audiovisual Core Maintenance Group Charter
  https://github.com/tdwg/ac/blob/master/Audiovisual-core_maintenance-group_charter.md

- Discussion of the Audiovisual Core takes place at
  https://github.com/tdwg/ac/issues

- Register for the mailing list tdwg-content@lists.tdwg.org at http://lists.tdwg.org/mailman/listinfo/tdwg-content. This email list tracks all discussion about the content of TDWG standards.

## 12 Appendix I: Glossary

<table>
  <tbody>
    <tr>
      <td><a href="http://dublincore.org/documents/dcmi-terms/">DC</a></td>
      <td>Dublin Core. Metadata element set that is a standard for cross-domain information  resource discovery.</td>
    </tr>
    <tr>
      <td><a href="http://dublincore.org/">DCMI</a></td>
      <td>Dublin Core Metadata Initiative. The organization engaged in developing Dublin Core metadata standard.</td>
    </tr>
    <tr>
      <td><a href="http://rs.tdwg.org/dwc/">DwC</a></td>
      <td>The Darwin Core is a TDWG standard for representation of specimen records. It has been in wide use for several years in a number of nonstandard, sometimes inconsistent, versions. A recently adopted standard version is at <a href="http://rs.tdwg.org/dwc/index.htm">http://rs.tdwg.org/dwc/index.htm</a>.</td>
    </tr>
    <tr>
      <td><a href="http://eol.org">EOL</a></td>
      <td>Encyclopedia of Life. Information about many species.</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Exchangeable_image_file_format">EXIF</a></td>
      <td>A widely used tagging format for digital image metadata that is often embedded in the image files, particularly by modern digital cameras. Many image rendering applications can read and display EXIF data. See <a href="http://en.wikipedia.org/wiki/Exchangeable_image_file_format">http://en.wikipedia.org/wiki/Exchangeable_image_file_format</a> for a history and description.</td>
    </tr>
    <tr>
      <td><a href="http://www.gbif.org/">GBIF</a></td>
      <td>Global Biodiversity Information Facility. Interoperable network of biodiversity databases and information technology tools.</td>
    </tr>
    <tr>
      <td><a href="http://www.iana.org">IANA</a></td>
      <td>Internet Assigned Names Authority. Specifies the forms of, and registers instances of, names of various protocols in use on the internet. See especially information on the <a href="http://en.wikipedia.org/wiki/URI_scheme">IANA http URI scheme</a>.</td>
    </tr>
    <tr>
      <td><a href="http://www.iptc.org">IPTC</a></td>
      <td>IPTC is a mature standard from the International Press and Telecommunications Council. Its Intellectual Property Rights support finer-grained controlled vocabularies than DC, providing better machine processing for discovery and fitness-for-use. The current version is a vocabulary for XMP.</td>
    </tr>
    <tr>
      <td><a href="http://www.json.org/">JSON</a></td>
      <td>JavaScript Object Notation. Lightweight data-interchange format.</td>
    </tr>
    <tr>
      <td><a href="http://www.morphbank.net/">Morphbank</a></td>
      <td>A specimen image repository.</td>
    </tr>
    <tr>
      <td><a href="http://www.metadataworkinggroup.org/">MWG</a></td>
      <td>The Metadata Working Group is an industry consortium (Adobe, Apple, Canon, Microsoft, Nokia, and Sony) organized to specify how to exploit the Adobe Extensible Metadata Platform, <a href="http://en.wikipedia.org/wiki/Extensible_Metadata_Platform">XMP</a>, for embedding metadata into common image file formats in several widely used controlled vocabularies. Although MWG's thrust is mainly toward consumer applications, over two dozen open source and commercial software products and platforms support XMP and Adobe has placed a Developers' Toolkit under an open source license.</td>
    </tr>
    <tr>
      <td><a href="http://images.nbii.gov/">NBII</a></td>
      <td>The former U.S. National Biological Information Infrastructure. Its image library, the Library of Images From the Environment (LIFE), was at <a href="http://images.nbii.gov/">http://images.nbii.gov/</a> or <a href="http://life.nbii.gov/">http://life.nbii.gov/</a>. If LIFE is reconstituted in any form, there might be a link there.</td>
    </tr>
    <tr>
      <td><a href="https://www.tdwg.org/standards/ncd/">NCD</a></td>
      <td>Natural Collections Description is a draft data standard designed to describe collections of physical objects such as specimens. It can accommodate collections of media objects, but cannot relate them to descriptions of the objects themselves.</td>
    </tr>
    <tr>
      <td><a href="http://www.opengeospatial.org/">OGC</a></td>
      <td>Open Geospatial Consortium. Provides standards for geospatial data representation and exchange.</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Resource_Description_Framework">RDF</a></td>
      <td>Resource Description Framework. Lightweight ontology system to support knowledge exchange online.</td>
    </tr>
    <tr>
      <td><a href="http://www.tdwg.org/">TDWG</a></td>
      <td>Taxonomic Databases Working Group. Now known as the Biodiversity Information Standards (TDWG), it is an international working group that develops standards and protocols for sharing biodiversity data.</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Uniform_Resource_Identifier">URI</a></td>
      <td>Unique Resource Identifier. Generic term for linking web resources including URLs.</td>
    </tr>
    <tr>
      <td><a href="http://www.w3.org/XML/">XML</a></td>
      <td>Extensible Markup Language. A simple flexible text format playing an increasingly important role in the exchange of a wide variety of data on the Web.</td>
    </tr>
    <tr>
      <td><a href="http://www.adobe.com/devnet/xmp/">XMP</a></td>
      <td>Adobe Extensible Metadata Platform (XMP) is a framework for embedding metadata into media files. Adobe provides a BSD-licensed open-source XMP developer’s toolkit which includes documentation about how to represent metadata in XMP. The XMP specification itself is licensed by Adobe under a <a href="http://wwwimages.adobe.com/www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/xmp_public_patent_license.pdf">&quot;Public Patent License&quot;</a> by which Adobe grants everyone the right to make XMP-compliant components of their applications, but it reserves the right to withdraw the license in case such a compliant component infringes &quot;Essential Claims&quot; of any patent. See <a href="http://www.adobe.com/devnet/xmp/">http://www.adobe.com/devnet/xmp/</a> for download information. See also <a href="http://www.metadataworkinggroup.org/">MWG</a> in this table.</td>
    </tr>
  </tbody>
</table>

## 13 Appendix II: Audiovisual Core Development History

The Audiovisual Core Multimedia Resources Metadata Schema (Audiovisual Core) standard is the culmination of work on multimedia
resource descriptions carried out by Key to Nature, the NBII Digital
Image Library, Morphbank, and others, together with input from a number
of other stakeholder communities including Encyclopedia of Life (EOL),
the Biodiversity Heritage Library (BHL) and the University of
Massachusetts-Boston. The Global Biodiversity Information Facility
(GBIF) commissioned the ‘Multimedia Resources Task Group (MRTG)’ in
March 2008 and the group was approved in December 2009 by Biodiversity
Information Standards (TDWG) as the ‘Joint GBIF-TDWG Task Group on
Multimedia Resources in Biodiversity’.

Participants in drafting the schema (in alphabetical order)

- Mr. Mihail-Constantin Carausu, Danish Biodiversity Information
  Facility (DanBIF), Copenhagen, Denmark

- Dr. Vishwas Chavan, Global Biodiversity Information Facility,
  Copenhagen, Denmark

- Mr. Chris Freeland, Missouri Botanical Garden, St. Louis, USA

- Dr. Gregor Hagedorn, JKI, Federal Research Institute for Cultivated
  Plants, Berlin, Germany

- Prof. Robert A. Morris, University of Massachusetts at Boston, USA

- Dr. Dimitry Mozzherin, Encyclopedia of Life, Woods Hole, USA

- Dr Annette Olson, American Association for the Advancement of
  Science

- Prof. Greg Riccardi, Florida State University, Tallahassee, USA

- Dr. Éamonn Ó Tuama, Global Biodiversity Information Facility,
  Copenhagen, Denmark

The standard was developed by the Joint Task Group to fit with the suite of standards-based data management resources being developed by GBIF.

Funding was provided by the Global Biodiversity Information Facility.

Grateful thanks go to Woods Hole Marine Biological Laboratory and the
Encyclopedia of Life for hosting one of the meetings. This document,
including some narrative is adapted from a corresponding document
produced by the TDWG Natural Collections Descriptions (NCD) task group.

### 13.1 Timeline

2006, November TDWG Image Interest Group initiated

2008, March GBIF commissions Multimedia Resources Task Group (MRTG)

2008, June GBIF Multimedia Resources Task Group met in Copenhagen,
Denmark

2008, August GBIF Multimedia Resources Task Group meeting in Woods Hole,
USA

2008, October TDWG Image Interest Group met in Fremantle, Australia at
the ‘TDWG Annual Conference 2008’

2008, December Joint GBIF-TDWG Task Group on Multimedia Resources in
Biodiversity commissioned

2009, February GBIF Multimedia Resources Task Group met in Copenhagen,
Denmark to refine the metadata schema

2009, March GBIF – TDWG Multimedia Resources Metadata Schema (MRTG) ver.
0.4414 drafted and opened for informal comment, evolving through v 0.9

2010, February Schema v 0.9 submitted to TDWG for internal Review

2010, July TDWG Internal Review 1 completed

2010, November v1.0 submitted to TDWG Executive committee with response
to Internal Review 1. Proposed Standard renamed Audiovisual Core Multimedia
Resources Metadata Schema (AC).

2011, June Response to Internal Review 2 under way.

2011, September Responses to Internal Review 2 and 3 completed and
submitted to TDWG Executive Committee

2011, November Prepared responses to “Review g” and “Review h” and to
some comments of the Review Manager, Steve Baskauf. Prepare submission
for permission to have public comment.

January-November 2012 Further preparation for submission for permission
to have public comment

### 13.2 Document revision history

**0.7v1**

- Harmonized document to the fact that Subtype is optional in normative v0.7

- Fix mismatched parentheses, extra spaces, missing spaces, etc.

**ACv1.0 docv1.0**

- Harmonized to v1.0: replace “MRTG” with “Audiovisual Core” where used as name of schema. Correct minor typos. Add “dcterms” as prefix.

**ACv1.0 docv1.0**

- Further replacement of MRTG with “Audiovisual Core” or “AC”.

**AC v1.0 docv 1.2**

- Address Internal Review 2 comments

- Fix mismatched parentheses, extra spaces, missing spaces, etc.

**AC v1.0 docv1.3**

- Remove requirement to have Copyright Owner provided.

**AC v1.0 docv1.4**

- Clean up citations of six mandatory elements instead of five.

**AC v1.0 docv1.5**

- Replace “keytonature.eu” with “species-id.net” to reflect move of normative wiki. Remove some unused Glossary terms. Update docv to 1.5

**AC v1.0docv1.6**

- Remove dcterms:title from mandatory list. Add description of it as strongly recommended. Add mention of xmpRights:Owner in Copyright Statement item in the mandatory list. Change to “four” the references of “five” mandatory elements or remove the count altogether where text becomes unambiguous. Mention acterms namespace. Correct Iptc4xmpExt namespace to http://iptc.org/std/Iptc4xmpExt/2008-02-29/. Update docv to 1.6.

**AC v1docv1.7**

- Clarify relation of this document to the normative docs. Set major major text to left-align, unjustified.

**AC v1.0docv1.8**

- Remove mention of crosswalks since no longer in normative termlist.

- On p. 5 force URL of DwC terms into footnote.

- Improved language about use of literals with dcterms.

**C v1.0docv1.91**

- Various minor grammar and punctuation corrections.

- Reconciliation to current normative docs.

**AC v1.0docv1.92**

- More minor grammar fixes.

**AC v1.0docv1.93**

- Fixed inconsistent internal version references to current version. No substantive or grammatical changes. Note that v1.92 was submitted to TDWG executive committee with request for permission to hold public review.

**AC v1.0docv1.94**

- Change references from species-id wiki to gbif terms wiki. Adjust Fig 1

**AC v1.0docv1.95**

- Correct “hasAccentPoint” to “hasAcccessPoint”. Remove text suggesting this is a draft

## 14 Endnotes

<sup id="fn-1">[\[1\]](#cit-1)</sup> http://rs.tdwg.org/ac/doc/structure/

<sup id="fn-2">[\[2\]](#cit-2)</sup> http://rs.tdwg.org/ac/doc/termlist/

<sup id="fn-3">[\[3\]](#cit-3)</sup> [http://www.w3.org/RDF/](http://www.w3.org/RDF/)

<sup id="fn-4">[\[4\]](#cit-4)</sup> [http://www.w3.org/standards/xml/schema](http://www.w3.org/standards/xml/schema)

<sup id="fn-5">[\[5\]](#cit-5)</sup> [http://en.wikipedia.org/wiki/Comma-separated_values](http://en.wikipedia.org/wiki/Comma-separated_values)

<sup id="fn-6">[\[6\]](#cit-6)</sup> https://github.com/tdwg/ncd/blob/master/NCD-v090_TDWG/NCD-v090_TDWG-NonNormative.pdf

<sup id="fn-7">[\[7\]](#cit-7)</sup> [http://rs.tdwg.org/dwc/terms/](http://rs.tdwg.org/dwc/terms/)

<sup id="fn-8">[\[8\]](#cit-8)</sup> [http://rs.tdwg.org/dwc/index.htm](http://rs.tdwg.org/dwc/index.htm)

<sup id="fn-9">[\[9\]](#cit-9)</sup>
The Metadata Working Group (MWG,
[http://www.metadataworkinggroup.org/](http://www.metadataworkinggroup.org/)) is an industry consortium
(Adobe, Apple, Canon, Microsoft, Nokia, and Sony) organized to
specify how to exploit the Adobe Extensible Metadata Platform, XMP
([http://en.wikipedia.org/wiki/Extensible_Metadata_Platform](http://en.wikipedia.org/wiki/Extensible_Metadata_Platform)) for
embedding into common image file formats metadata in several widely
used controlled vocabularies. Although MWG's thrust is mainly toward
consumer applications, over two dozen open source and commercial
software products and platforms support XMP and Adobe has placed a
Developers' Toolkit under an open source license. Along with
proposals for standard serializations of the representation-neutral
Audiovisual Core schema, MRTG intends to propose a TDWG Best Practice
for embedding such serializations in multimedia files using XMP.

<sup id="fn-10">[\[10\]](#cit-10)</sup>
IPTC is a mature standard from the International Press and
Telecommunications Council ([http://www.iptc.org](http://www.iptc.org)). Its Intellectual
Property Rights supports finer grained controlled vocabularies than
DC, providing better machine processing for discovery and
fitness-for-use.
