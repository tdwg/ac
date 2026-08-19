# Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Namespace IRI
: <http://rs.tdwg.org/accd/values/>

Preferred namespace abbreviation
: accd:

Date de publication de la dernière mise à jour
: 2026-08-18

Date de création
: 2026-08-18

Fait partie du standard TDWG
: <http://www.tdwg.org/standards/638>

Cette version
: <http://rs.tdwg.org/ac/doc/3dmodality/2026-08-18>

Dernière version
: <http://rs.tdwg.org/ac/doc/3dmodality/>

Version précédente
: Abstract
: Audiovisual Core uses the terms ac:resourceCreationTechnique to provide a string describing technical aspects of the creation and digitization process of a media item. In the case of generic media items, that string is descriptive text. However, in the case of 3D media items, the string should be a controlled value from this vocabulary that describes the modality of image capture.

Contributeurs
: [Doug M. Boyer](https://orcid.org/0000-0002-8697-2999) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Jon Blundell](https://orcid.org/0000-0003-2493-9912) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Gary J. Motz](https://orcid.org/0000-0002-6712-2139) ([Indiana Geological and Water Survey](http://www.wikidata.org/entity/Q6023194)), [Adam N. Rountrey](https://orcid.org/0000-0003-0939-9102) ([University of Michigan Museum of Paleontology](http://www.wikidata.org/entity/Q96220204)), [Rebecca Snyder](https://orcid.org/0000-0002-0028-6139) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Jocelyn Triplett](https://orcid.org/0000-0003-3452-2408) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Kate Webbink](https://orcid.org/0000-0002-8347-0942) ([Field Museum of Natural History](http://www.wikidata.org/entity/Q1122595)), [Julie Winchester](https://orcid.org/0000-0001-6578-764X) ([Duke University](http://www.wikidata.org/entity/Q168751))

Créateur :
TDWG Audiovisual Core 3D Enhancement Task Group

Citation :
TDWG Audiovisual Core 3D Enhancement Task Group. 2026. Controlled Vocabulary for Audiovisual Core 3D Image Capture Modality: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/3dmodality/2026-08-18>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVtermLiteral`.

### 1.1 Statut du contenu de ce document

Section 1 is informative (non-normative).

La section 2 est normative.

Section 3 is informative (non-normative).

Dans la section 4, les valeurs de l'`IRI du terme`, de la `Définition` et de la `Valeur contrôlée` sont normatives. La valeur de `Utilisation` (si elle existe pour un terme donné) est normative. Les valeurs de `Nom du Terme` ne sont pas normatives, bien que l'on puisse s'attendre à ce que le préfixe de l'abréviation de l'espace de noms soit celui couramment utilisé pour l'espace de noms du terme.  `Label` and the values of all other properties are non-normative.

### 1.2 Mots clés RFC 2119

Les mots clés "MUST/DOIT", "MUST NOT/NE DOIT PAS", "REQUIRED/OBLIGATOIRE", "SHALL/DEVRA", "SHALL NOT/NE DEVRA PAS", "SHOULD/DEVRAIT", "SHOULD NOT/NE DEVRAIT PAS", "RECOMMENDED/RECOMMANDÉ", "MAY/POURRAIT", et "OPTIONAL/OPTIONNEL" dans ce document doivent être interprétés comme défini dans les références [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) et [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174)] uniquement lorsqu’ils apparaissent en majuscules, comme ci-dessus.

## 2 Utilisation des termes

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `Iptc4xmpExt:CVterm`. Controlled value strings SHOULD be used as values of the property `ac:CVtermLiteral`.

### 2.2 Relationship between values of ac:CVtermLiteral and Iptc4xmpExt:CVterm

An IRI for a term in this vocabulary denotes the same concept as the concept denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `Iptc4xmpExt:CVterm` given a controlled value string for `ac:CVtermLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `Iptc4xmpExt:CVterm` property in cases where providers only provide values for `ac:CVtermLiteral`.

## 3 Index des termes



[3D modality controlled vocabulary](#ac3dmodality_m) |
[Confocal microscopy](#ac3dmodality_m0012) |
[CT](#ac3dmodality_m0003) |
[Image stacking](#ac3dmodality_m0018) |
[Laser](#ac3dmodality_m0015) |
[Line of sight](#ac3dmodality_m0014) |
[MRI](#ac3dmodality_m0009) |
[Neutron](#ac3dmodality_m0008) |
[Penetrative](#ac3dmodality_m0001) |
[PET](#ac3dmodality_m0010) |
[Photogrammetry](#ac3dmodality_m0017) |
[SPECT](#ac3dmodality_m0011) |
[Structured light](#ac3dmodality_m0016) |
[Synchrotron](#ac3dmodality_m0007) |
[X-ray](#ac3dmodality_m0002)

## 4 Vocabulaire
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m"></a>Nom du Terme ac3dmodality:m</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m">http://rs.tdwg.org/ac3dmodality/values/m</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>3D modality controlled vocabulary</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>A SKOS ConceptScheme to be used as a controlled vocabulary for the Audiovisual Core term ac:resourceCreationTechnique</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0001"></a>Nom du Terme ac3dmodality:m0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0001">http://rs.tdwg.org/ac3dmodality/values/m0001</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0001-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0001-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Penetrative</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Imaging that uses any kind of penetrating wave.</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>penetrative</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0002"></a>Nom du Terme ac3dmodality:m0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0002">http://rs.tdwg.org/ac3dmodality/values/m0002</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0002-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0002-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>X-ray</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>X-Ray imaging is an imaging technique that uses X-rays to create images of the internal structures of an object. X-ray imaging is widely used in medical diagnosis and research, as well as in materials science and other fields to visualize the internal structure of objects.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/XRay">http://www.morphosource.org/terms/mscv/XRay</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>xRay</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0003"></a>Nom du Terme ac3dmodality:m0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0003">http://rs.tdwg.org/ac3dmodality/values/m0003</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0003-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0003-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>CT</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>X-Ray Computed Tomography (CT/microCT) is a non-invasive imaging technique that uses X-rays to produce cross-sectional images of an object. It involves rotating an X-ray source and detector around the object, collecting data that is processed by a computer to create a 3D image. CT is widely used in medical imaging, as well as in materials science, engineering, and geology to visualize the internal structure of objects. MicroCT is a variation of CT that uses higher resolution X-rays to produce images of smaller objects.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/MicroNanoXRayComputedTomography">http://www.morphosource.org/terms/mscv/MicroNanoXRayComputedTomography</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>ct</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0002">ac3dmodality:m0002</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0007"></a>Nom du Terme ac3dmodality:m0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0007">http://rs.tdwg.org/ac3dmodality/values/m0007</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0007-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0007-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Synchrotron</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Synchrotron Imaging is a type of X-ray imaging that uses synchrotron radiation, which is produced when high-energy particles are accelerated to near the speed of light. Synchrotron imaging can produce high-resolution, 3D images of a wide range of materials and structures.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/SynchrotronImaging">http://www.morphosource.org/terms/mscv/SynchrotronImaging</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>synchrotron</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0002">ac3dmodality:m0002</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0008"></a>Nom du Terme ac3dmodality:m0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0008">http://rs.tdwg.org/ac3dmodality/values/m0008</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0008-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0008-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Neutron</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Neutron Computed Tomography (NCT) is an imaging technique that uses neutrons instead of X-rays to create cross-sectional images of an object. NCT is particularly useful for imaging materials that are difficult to penetrate with X-rays, such as ceramics and rocks.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/NeutronComputedTomography">http://www.morphosource.org/terms/mscv/NeutronComputedTomography</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>neutron</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0009"></a>Nom du Terme ac3dmodality:m0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0009">http://rs.tdwg.org/ac3dmodality/values/m0009</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0009-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0009-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>MRI</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Magnetic Resonance Imaging (MRI) is a non-invasive imaging technique that uses a strong magnetic field and radio waves to produce detailed images of the body's internal structures. MRI is widely used in medical diagnosis and research, especially for imaging soft tissues like the brain, spinal cord, and organs.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/MagneticResonanceImaging">http://www.morphosource.org/terms/mscv/MagneticResonanceImaging</a> </td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>mri</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0010"></a>Nom du Terme ac3dmodality:m0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0010">http://rs.tdwg.org/ac3dmodality/values/m0010</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0010-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0010-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>PET</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Positron Emission Tomography (PET) is a non-invasive imaging technique that uses small amounts of radioactive tracers to visualize metabolic processes in the body. The tracer is injected into the body and collects in areas of high metabolic activity, emitting positrons that are detected by the PET scanner. PET is widely used in medical diagnosis and research, especially for imaging cancer, heart disease, and neurological disorders.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/PositronEmissionTomography">http://www.morphosource.org/terms/mscv/PositronEmissionTomography</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>pet</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0011"></a>Nom du Terme ac3dmodality:m0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0011">http://rs.tdwg.org/ac3dmodality/values/m0011</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0011-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0011-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>SPECT</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Single Photon Emission Computed Tomography (SPECT) is a non-invasive imaging technique that uses a small amount of radioactive tracer to produce 3D images of the body's internal structures. The tracer is injected into the body and emits gamma rays, which are detected by a SPECT scanner. SPECT is used in medical diagnosis and research, especially for imaging the brain, heart, and bones.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/SinglePhotonEmissionComputedTomography">http://www.morphosource.org/terms/mscv/SinglePhotonEmissionComputedTomography</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>spect</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0012"></a>Nom du Terme ac3dmodality:m0012</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0012">http://rs.tdwg.org/ac3dmodality/values/m0012</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0012-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0012-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Confocal microscopy</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Confocal Image Stacking is an imaging technique that uses a series of images taken at different depths to create a 3D image of an object. By focusing a laser beam on a specific point in the object and measuring the reflected light, confocal microscopy can create high-resolution 3D images of cells and tissues.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ConfocalImageStacking">http://www.morphosource.org/terms/mscv/ConfocalImageStacking</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>confocalMicroscopy</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0014"></a>Nom du Terme ac3dmodality:m0014</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0014">http://rs.tdwg.org/ac3dmodality/values/m0014</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0014-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0014-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Line of sight</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Imaging based on reflected waves.</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>lineOfSight</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0015"></a>Nom du Terme ac3dmodality:m0015</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0015">http://rs.tdwg.org/ac3dmodality/values/m0015</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0015-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0015-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Laser</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Laser Scan is an imaging technique that uses laser beams to create a 3D image of an object's surface. Laser scans are commonly used in industrial design and manufacturing to create accurate models of parts and components.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/LaserScan">http://www.morphosource.org/terms/mscv/LaserScan</a> </td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>laser</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0016"></a>Nom du Terme ac3dmodality:m0016</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0016">http://rs.tdwg.org/ac3dmodality/values/m0016</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0016-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0016-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Structured light</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Structured Light is an imaging technique that uses a pattern of light projected onto an object to create a 3D image. By analyzing how the pattern of light is distorted by the object, structured light can create high-resolution, accurate 3D models of complex shapes and structures.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="https://www.morphosource.org/terms/mscv/StructuredLight">https://www.morphosource.org/terms/mscv/StructuredLight</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>structuredLight</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0017"></a>Nom du Terme ac3dmodality:m0017</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0017">http://rs.tdwg.org/ac3dmodality/values/m0017</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0017-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0017-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Photogrammetry</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Photogrammetry is the use of photography to measure and map the physical properties of an object. Photogrammetry can be used to create 3D models of objects and structures from 2D photographs, allowing for accurate measurements and analysis.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="https://www.morphosource.org/terms/mscv/Photogrammetry">https://www.morphosource.org/terms/mscv/Photogrammetry</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>photogrammetry</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0018"></a>Nom du Terme ac3dmodality:m0018</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0018">http://rs.tdwg.org/ac3dmodality/values/m0018</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0018-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0018-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Image stacking</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Image Stacking is an imaging technique that uses a series of images taken at different depths to create a 3D image of an object.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ConfocalImageStacking">http://www.morphosource.org/terms/mscv/ConfocalImageStacking</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>imageStacking</td>
		</tr>
		<tr>
			<td>A pour concept plus large</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>


