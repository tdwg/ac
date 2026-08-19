# Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Espacio de nombres IRI
: <http://rs.tdwg.org/accd/values/>

Abreviatura preferida del namespce
: accd:

Fecha de publicación de la versión
: 2026-08-18

Fecha de creación
: 2026-08-18

Parte del Estándar TDWG
: <http://www.tdwg.org/standards/638>

Esta versión
: <http://rs.tdwg.org/ac/doc/3dmodality/2026-08-18>

Última versión
: <http://rs.tdwg.org/ac/doc/3dmodality/>

Resumen
: Audiovisual Core uses the terms ac:resourceCreationTechnique to provide a string describing technical aspects of the creation and digitization process of a media item. In the case of generic media items, that string is descriptive text. However, in the case of 3D media items, the string should be a controlled value from this vocabulary that describes the modality of image capture.

Colaboradores
: [Doug M. Boyer](https://orcid.org/0000-0002-8697-2999) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Jon Blundell](https://orcid.org/0000-0003-2493-9912) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Gary J. Motz](https://orcid.org/0000-0002-6712-2139) ([Indiana Geological and Water Survey](http://www.wikidata.org/entity/Q6023194)), [Adam N. Rountrey](https://orcid.org/0000-0003-0939-9102) ([University of Michigan Museum of Paleontology](http://www.wikidata.org/entity/Q96220204)), [Rebecca Snyder](https://orcid.org/0000-0002-0028-6139) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Jocelyn Triplett](https://orcid.org/0000-0003-3452-2408) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Kate Webbink](https://orcid.org/0000-0002-8347-0942) ([Field Museum of Natural History](http://www.wikidata.org/entity/Q1122595)), [Julie Winchester](https://orcid.org/0000-0001-6578-764X) ([Duke University](http://www.wikidata.org/entity/Q168751))

Creador
: TDWG Audiovisual Core 3D Enhancement Task Group

Cita bibliográfica
: TDWG Audiovisual Core 3D Enhancement Task Group. 2026. Controlled Vocabulary for Audiovisual Core 3D Image Capture Modality: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/3dmodality/2026-08-18>

## 1. Introducción (Informativa)

Este documento incluye términos destinados a ser utilizados como valores controlados para los términos principales de Audiovisual Core `Iptc4xmpExt:CVterm` y `ac:CVtermLiteral`.

### 1.1 Estado del contenido de este documento

La Sección 1 es informativa (no normativa).

La sección 2 es normativa.

La Sección 3 es informativa (no normativa).

En la Sección 4, los valores de `Término IRI`, `Definición` y `Valor controlado` son normativos. El valor de `Uso` (si existe para un término determinado) también es normativo. Los valores del `Nombre del término` no son normativos, aunque se puede esperar que el prefijo del namespace abreviado sea uno comúnmente utilizado para ese namespace.  La `Etiqueta` y los valores de todas las demás propiedades no son normativos.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

## 2 Uso de los Términos

### 2.1 Relación de los tipos de valor con los términos de propiedad

De acuerdo con el [documento de la Lista de Términos Básicos Audiovisuales](http://rs.tdwg.org/ac/doc/termlist/), los términos IRI no abreviados DEBEN usarse como valores de la propiedad `Iptc4xmpExt:CVterm`. Las cadenas de valores controlados DEBEN usarse como valores de la propiedad `ac:CVtermLiteral`.

### 2.2 Relación entre los valores de ac:CVtermLiteral y Iptc4xmpExt:CVterm

Una IRI para un término en este vocabulario denota la misma clase que la clase denotada por la cadena de valor controlado para el mismo término. Por lo tanto, un cliente PUEDE inferir un valor IRI para `Iptc4xmpExt:CVterm` dada una cadena de valor controlado para `ac:CVtermLiteral` incluso si ese IRI no se indica explícitamente. La implicación práctica es que los agregadores de datos PUEDEN materializar valores para la propiedad preferida `Iptc4xmpExt:CVterm` en los casos en que los proveedores solo proporcionan valores para `ac:CVtermLiteral`.

## 3 Índice de Términos



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

## 4 Vocabulario
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m"></a>Nombre de Término ac3dmodality:m</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m">http://rs.tdwg.org/ac3dmodality/values/m</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>3D modality controlled vocabulary</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>A SKOS ConceptScheme to be used as a controlled vocabulary for the Audiovisual Core term ac:resourceCreationTechnique</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0001"></a>Nombre de Término ac3dmodality:m0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0001">http://rs.tdwg.org/ac3dmodality/values/m0001</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0001-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0001-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Penetrative</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Imaging that uses any kind of penetrating wave.</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>penetrative</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0002"></a>Nombre de Término ac3dmodality:m0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0002">http://rs.tdwg.org/ac3dmodality/values/m0002</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0002-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0002-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>X-ray</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>X-Ray imaging is an imaging technique that uses X-rays to create images of the internal structures of an object. X-ray imaging is widely used in medical diagnosis and research, as well as in materials science and other fields to visualize the internal structure of objects.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/XRay">http://www.morphosource.org/terms/mscv/XRay</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>xRay</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0003"></a>Nombre de Término ac3dmodality:m0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0003">http://rs.tdwg.org/ac3dmodality/values/m0003</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0003-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0003-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>CT</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>X-Ray Computed Tomography (CT/microCT) is a non-invasive imaging technique that uses X-rays to produce cross-sectional images of an object. It involves rotating an X-ray source and detector around the object, collecting data that is processed by a computer to create a 3D image. CT is widely used in medical imaging, as well as in materials science, engineering, and geology to visualize the internal structure of objects. MicroCT is a variation of CT that uses higher resolution X-rays to produce images of smaller objects.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/MicroNanoXRayComputedTomography">http://www.morphosource.org/terms/mscv/MicroNanoXRayComputedTomography</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>ct</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0002">ac3dmodality:m0002</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0007"></a>Nombre de Término ac3dmodality:m0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0007">http://rs.tdwg.org/ac3dmodality/values/m0007</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0007-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0007-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Synchrotron</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Synchrotron Imaging is a type of X-ray imaging that uses synchrotron radiation, which is produced when high-energy particles are accelerated to near the speed of light. Synchrotron imaging can produce high-resolution, 3D images of a wide range of materials and structures.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/SynchrotronImaging">http://www.morphosource.org/terms/mscv/SynchrotronImaging</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>synchrotron</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0002">ac3dmodality:m0002</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0008"></a>Nombre de Término ac3dmodality:m0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0008">http://rs.tdwg.org/ac3dmodality/values/m0008</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0008-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0008-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Neutron</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Neutron Computed Tomography (NCT) is an imaging technique that uses neutrons instead of X-rays to create cross-sectional images of an object. NCT is particularly useful for imaging materials that are difficult to penetrate with X-rays, such as ceramics and rocks.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/NeutronComputedTomography">http://www.morphosource.org/terms/mscv/NeutronComputedTomography</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>neutron</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0009"></a>Nombre de Término ac3dmodality:m0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0009">http://rs.tdwg.org/ac3dmodality/values/m0009</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0009-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0009-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>MRI</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Magnetic Resonance Imaging (MRI) is a non-invasive imaging technique that uses a strong magnetic field and radio waves to produce detailed images of the body's internal structures. MRI is widely used in medical diagnosis and research, especially for imaging soft tissues like the brain, spinal cord, and organs.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/MagneticResonanceImaging">http://www.morphosource.org/terms/mscv/MagneticResonanceImaging</a> </td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>mri</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0010"></a>Nombre de Término ac3dmodality:m0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0010">http://rs.tdwg.org/ac3dmodality/values/m0010</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0010-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0010-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>PET</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Positron Emission Tomography (PET) is a non-invasive imaging technique that uses small amounts of radioactive tracers to visualize metabolic processes in the body. The tracer is injected into the body and collects in areas of high metabolic activity, emitting positrons that are detected by the PET scanner. PET is widely used in medical diagnosis and research, especially for imaging cancer, heart disease, and neurological disorders.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/PositronEmissionTomography">http://www.morphosource.org/terms/mscv/PositronEmissionTomography</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>pet</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0011"></a>Nombre de Término ac3dmodality:m0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0011">http://rs.tdwg.org/ac3dmodality/values/m0011</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0011-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0011-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>SPECT</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Single Photon Emission Computed Tomography (SPECT) is a non-invasive imaging technique that uses a small amount of radioactive tracer to produce 3D images of the body's internal structures. The tracer is injected into the body and emits gamma rays, which are detected by a SPECT scanner. SPECT is used in medical diagnosis and research, especially for imaging the brain, heart, and bones.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/SinglePhotonEmissionComputedTomography">http://www.morphosource.org/terms/mscv/SinglePhotonEmissionComputedTomography</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>spect</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0012"></a>Nombre de Término ac3dmodality:m0012</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0012">http://rs.tdwg.org/ac3dmodality/values/m0012</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0012-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0012-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Confocal microscopy</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Confocal Image Stacking is an imaging technique that uses a series of images taken at different depths to create a 3D image of an object. By focusing a laser beam on a specific point in the object and measuring the reflected light, confocal microscopy can create high-resolution 3D images of cells and tissues.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ConfocalImageStacking">http://www.morphosource.org/terms/mscv/ConfocalImageStacking</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>confocalMicroscopy</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0001">ac3dmodality:m0001</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0014"></a>Nombre de Término ac3dmodality:m0014</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0014">http://rs.tdwg.org/ac3dmodality/values/m0014</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0014-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0014-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Line of sight</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Imaging based on reflected waves.</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>lineOfSight</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0015"></a>Nombre de Término ac3dmodality:m0015</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0015">http://rs.tdwg.org/ac3dmodality/values/m0015</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0015-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0015-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Laser</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Laser Scan is an imaging technique that uses laser beams to create a 3D image of an object's surface. Laser scans are commonly used in industrial design and manufacturing to create accurate models of parts and components.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/LaserScan">http://www.morphosource.org/terms/mscv/LaserScan</a> </td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>laser</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0016"></a>Nombre de Término ac3dmodality:m0016</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0016">http://rs.tdwg.org/ac3dmodality/values/m0016</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0016-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0016-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Structured light</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Structured Light is an imaging technique that uses a pattern of light projected onto an object to create a 3D image. By analyzing how the pattern of light is distorted by the object, structured light can create high-resolution, accurate 3D models of complex shapes and structures.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="https://www.morphosource.org/terms/mscv/StructuredLight">https://www.morphosource.org/terms/mscv/StructuredLight</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>structuredLight</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0017"></a>Nombre de Término ac3dmodality:m0017</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0017">http://rs.tdwg.org/ac3dmodality/values/m0017</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0017-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0017-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Photogrammetry</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Photogrammetry is the use of photography to measure and map the physical properties of an object. Photogrammetry can be used to create 3D models of objects and structures from 2D photographs, allowing for accurate measurements and analysis.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="https://www.morphosource.org/terms/mscv/Photogrammetry">https://www.morphosource.org/terms/mscv/Photogrammetry</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>photogrammetry</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dmodality_m0018"></a>Nombre de Término ac3dmodality:m0018</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/m0018">http://rs.tdwg.org/ac3dmodality/values/m0018</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dmodality/values/version/m0018-2026-08-18">http://rs.tdwg.org/ac3dmodality/values/version/m0018-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>Image stacking</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Image Stacking is an imaging technique that uses a series of images taken at different depths to create a 3D image of an object.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ConfocalImageStacking">http://www.morphosource.org/terms/mscv/ConfocalImageStacking</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>imageStacking</td>
		</tr>
		<tr>
			<td>Tiene un concepto más amplio</td>
			<td><a href="#ac3dmodality_m0014">ac3dmodality:m0014</a></td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_63">http://rs.tdwg.org/decisions/decision-2026-08-18_63</a></td>
		</tr>
	</tbody>
</table>


