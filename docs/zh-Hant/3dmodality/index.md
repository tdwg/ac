# Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Namespace IRI
: <http://rs.tdwg.org/accd/values/>

Preferred namespace abbreviation
: accd:

版本發行日期
: 2026-08-18

建立日期

生物多樣性訊息標準的一部分
: <http://www.tdwg.org/standards/638>

此版本
: <http://rs.tdwg.org/ac/doc/3dmodality/2026-08-18>

最新版本
: <http://rs.tdwg.org/ac/doc/3dmodality/>

Abstract
: Audiovisual Core uses the terms ac:resourceCreationTechnique to provide a string describing technical aspects of the creation and digitization process of a media item. In the case of generic media items, that string is descriptive text. However, in the case of 3D media items, the string should be a controlled value from this vocabulary that describes the modality of image capture.

貢獻者
: [Doug M. Boyer](https://orcid.org/0000-0002-8697-2999) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Jon Blundell](https://orcid.org/0000-0003-2493-9912) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Gary J. Motz](https://orcid.org/0000-0002-6712-2139) ([Indiana Geological and Water Survey](http://www.wikidata.org/entity/Q6023194)), [Adam N. Rountrey](https://orcid.org/0000-0003-0939-9102) ([University of Michigan Museum of Paleontology](http://www.wikidata.org/entity/Q96220204)), [Rebecca Snyder](https://orcid.org/0000-0002-0028-6139) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Jocelyn Triplett](https://orcid.org/0000-0003-3452-2408) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Kate Webbink](https://orcid.org/0000-0002-8347-0942) ([Field Museum of Natural History](http://www.wikidata.org/entity/Q1122595)), [Julie Winchester](https://orcid.org/0000-0001-6578-764X) ([Duke University](http://www.wikidata.org/entity/Q168751))

建立者
: TDWG Audiovisual Core 3D Enhancement Task Group

書目引用
: TDWG Audiovisual Core 3D Enhancement Task Group. 2026. Controlled Vocabulary for Audiovisual Core 3D Image Capture Modality: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/3dmodality/2026-08-18>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVtermLiteral`.

### 1.1 本文件內容的現況

Section 1 is informative (non-normative).

第 2 節為規範性。

Section 3 is informative (non-normative).

在第 4 節中，`Term IRI`、`Definition`和`Controlled value`的值為規範性。 `Usage`的值 (如果它存在於特定術語中) 為規範性。 `Term Name`的值為非規範性，不過可以預期命名空間縮寫是術語命名空間的常用前綴。  `Label` and the values of all other properties are non-normative.

### 1.2 RFC 2119 關鍵字

關鍵字「必須」、「不得」、「要求」、「應」、「不應」、「應當」、「不應當」、「建議」、「可」、「可選」的定義，請參照[BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) 及 [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) 所定義之含義，惟詞彙須以全大寫形式呈現時方適用。

## 2 使用條款

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `Iptc4xmpExt:CVterm`. Controlled value strings SHOULD be used as values of the property `ac:CVtermLiteral`.

### 2.2 Relationship between values of ac:CVtermLiteral and Iptc4xmpExt:CVterm

An IRI for a term in this vocabulary denotes the same concept as the concept denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `Iptc4xmpExt:CVterm` given a controlled value string for `ac:CVtermLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `Iptc4xmpExt:CVterm` property in cases where providers only provide values for `ac:CVtermLiteral`.

## 3 術語索引



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

## 4 詞彙
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m"></a>term_name ac3dmodality:m</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m">http://rs.tdwg.org/ac3dmodality/values/m</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>3D modality controlled vocabulary</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>A SKOS ConceptScheme to be used as a controlled vocabulary for the Audiovisual Core term ac:resourceCreationTechnique</td>
		</tr>
		<tr>
			<td>type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0001"></a>term_name ac3dmodality:m0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0001">http://rs.tdwg.org/ac3dmodality/values/m0001</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0001-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0001-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Penetrative</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Imaging that uses any kind of penetrating wave.</td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>penetrative</td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0002"></a>term_name ac3dmodality:m0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0002">http://rs.tdwg.org/ac3dmodality/values/m0002</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0002-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0002-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>X-ray</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>X-Ray imaging is an imaging technique that uses X-rays to create images of the internal structures of an object. X-ray imaging is widely used in medical diagnosis and research, as well as in materials science and other fields to visualize the internal structure of objects.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/XRay">http://www.morphosource.org/terms/mscv/XRay</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>xRay</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0003"></a>term_name ac3dmodality:m0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0003">http://rs.tdwg.org/ac3dmodality/values/m0003</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0003-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0003-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>CT</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>X-Ray Computed Tomography (CT/microCT) is a non-invasive imaging technique that uses X-rays to produce cross-sectional images of an object. It involves rotating an X-ray source and detector around the object, collecting data that is processed by a computer to create a 3D image. CT is widely used in medical imaging, as well as in materials science, engineering, and geology to visualize the internal structure of objects. MicroCT is a variation of CT that uses higher resolution X-rays to produce images of smaller objects.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/MicroNanoXRayComputedTomography">http://www.morphosource.org/terms/mscv/MicroNanoXRayComputedTomography</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>ct</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0002">ac3dmodality:m0002</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0007"></a>term_name ac3dmodality:m0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0007">http://rs.tdwg.org/ac3dmodality/values/m0007</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0007-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0007-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Synchrotron</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Synchrotron Imaging is a type of X-ray imaging that uses synchrotron radiation, which is produced when high-energy particles are accelerated to near the speed of light. Synchrotron imaging can produce high-resolution, 3D images of a wide range of materials and structures.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/SynchrotronImaging">http://www.morphosource.org/terms/mscv/SynchrotronImaging</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>synchrotron</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0002">ac3dmodality:m0002</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0008"></a>term_name ac3dmodality:m0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0008">http://rs.tdwg.org/ac3dmodality/values/m0008</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0008-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0008-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Neutron</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Neutron Computed Tomography (NCT) is an imaging technique that uses neutrons instead of X-rays to create cross-sectional images of an object. NCT is particularly useful for imaging materials that are difficult to penetrate with X-rays, such as ceramics and rocks.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/NeutronComputedTomography">http://www.morphosource.org/terms/mscv/NeutronComputedTomography</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>neutron</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0009"></a>term_name ac3dmodality:m0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0009">http://rs.tdwg.org/ac3dmodality/values/m0009</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0009-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0009-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>MRI</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Magnetic Resonance Imaging (MRI) is a non-invasive imaging technique that uses a strong magnetic field and radio waves to produce detailed images of the body's internal structures. MRI is widely used in medical diagnosis and research, especially for imaging soft tissues like the brain, spinal cord, and organs.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/MagneticResonanceImaging">http://www.morphosource.org/terms/mscv/MagneticResonanceImaging</a> </td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>mri</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0010"></a>term_name ac3dmodality:m0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0010">http://rs.tdwg.org/ac3dmodality/values/m0010</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0010-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0010-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>PET</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Positron Emission Tomography (PET) is a non-invasive imaging technique that uses small amounts of radioactive tracers to visualize metabolic processes in the body. The tracer is injected into the body and collects in areas of high metabolic activity, emitting positrons that are detected by the PET scanner. PET is widely used in medical diagnosis and research, especially for imaging cancer, heart disease, and neurological disorders.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/PositronEmissionTomography">http://www.morphosource.org/terms/mscv/PositronEmissionTomography</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>pet</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0011"></a>term_name ac3dmodality:m0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0011">http://rs.tdwg.org/ac3dmodality/values/m0011</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0011-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0011-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>SPECT</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Single Photon Emission Computed Tomography (SPECT) is a non-invasive imaging technique that uses a small amount of radioactive tracer to produce 3D images of the body's internal structures. The tracer is injected into the body and emits gamma rays, which are detected by a SPECT scanner. SPECT is used in medical diagnosis and research, especially for imaging the brain, heart, and bones.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/SinglePhotonEmissionComputedTomography">http://www.morphosource.org/terms/mscv/SinglePhotonEmissionComputedTomography</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>spect</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0012"></a>term_name ac3dmodality:m0012</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0012">http://rs.tdwg.org/ac3dmodality/values/m0012</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0012-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0012-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Confocal microscopy</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Confocal Image Stacking is an imaging technique that uses a series of images taken at different depths to create a 3D image of an object. By focusing a laser beam on a specific point in the object and measuring the reflected light, confocal microscopy can create high-resolution 3D images of cells and tissues.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ConfocalImageStacking">http://www.morphosource.org/terms/mscv/ConfocalImageStacking</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>confocalMicroscopy</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0014"></a>term_name ac3dmodality:m0014</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0014">http://rs.tdwg.org/ac3dmodality/values/m0014</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0014-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0014-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Line of sight</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Imaging based on reflected waves.</td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>lineOfSight</td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0015"></a>term_name ac3dmodality:m0015</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0015">http://rs.tdwg.org/ac3dmodality/values/m0015</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0015-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0015-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Laser</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Laser Scan is an imaging technique that uses laser beams to create a 3D image of an object's surface. Laser scans are commonly used in industrial design and manufacturing to create accurate models of parts and components.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/LaserScan">http://www.morphosource.org/terms/mscv/LaserScan</a> </td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>laser</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0016"></a>term_name ac3dmodality:m0016</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0016">http://rs.tdwg.org/ac3dmodality/values/m0016</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0016-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0016-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Structured light</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Structured Light is an imaging technique that uses a pattern of light projected onto an object to create a 3D image. By analyzing how the pattern of light is distorted by the object, structured light can create high-resolution, accurate 3D models of complex shapes and structures.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="https://www.morphosource.org/terms/mscv/StructuredLight">https://www.morphosource.org/terms/mscv/StructuredLight</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>structuredLight</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0017"></a>term_name ac3dmodality:m0017</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0017">http://rs.tdwg.org/ac3dmodality/values/m0017</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0017-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0017-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Photogrammetry</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Photogrammetry is the use of photography to measure and map the physical properties of an object. Photogrammetry can be used to create 3D models of objects and structures from 2D photographs, allowing for accurate measurements and analysis.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="https://www.morphosource.org/terms/mscv/Photogrammetry">https://www.morphosource.org/terms/mscv/Photogrammetry</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>photogrammetry</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0018"></a>term_name ac3dmodality:m0018</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>術語IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0018">http://rs.tdwg.org/ac3dmodality/values/m0018</a></td>
		</tr>
		<tr>
			<td>已修改</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>術語版本IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0018-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0018-2026-08-18</a></td>
		</tr>
		<tr>
			<td>標籤</td>
			<td>Image stacking</td>
		</tr>
		<tr>
			<td>定義</td>
			<td>Image Stacking is an imaging technique that uses a series of images taken at different depths to create a 3D image of an object.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ConfocalImageStacking">http://www.morphosource.org/terms/mscv/ConfocalImageStacking</a></td>
		</tr>
		<tr>
			<td>控制值</td>
			<td>imageStacking</td>
		</tr>
		<tr>
			<td>有更廣泛的概念</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>type</td>
			<td>概念</td>
		</tr>
		<tr>
			<td>執行委員會決議</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>


