<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_Digital3DResource"></a>Term Name ac:Digital3DResource</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/Digital3DResource">http://rs.tdwg.org/ac/terms/Digital3DResource</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-09-01</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/Digital3DResource-2025-09-01">http://rs.tdwg.org/ac/terms/version/Digital3DResource-2025-09-01</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Digital 3D Resource</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> </td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>One or more binary files primarily intended to hold information about the three-dimensional geometry (surface or volume) of a real or non-real object, set of objects, or scene.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The term IRI should be used as a value for dcterms:type (<a href="http://purl.org/dc/terms/type">http://purl.org/dc/terms/type</a>). The controlled value string should be used as a value for dc:type (<a href="http://purl.org/dc/elements/1.1/type">http://purl.org/dc/elements/1.1/type</a>).</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Such files can be used by software to digitally render views of the subject, make measurements, conduct analyses, and create physical 3D replicas. This term includes resources composed of one or more files that are used to compute a 3D geometry (e.g., X-ray projections for computed tomography scans or photograph sets for photogrammetry). For avoidance of doubt, 2D renderings (views) produced from a Digital3DResource should not be included in this class, but stereo image pairs, anaglyphs, and other formats that hold information about 3D geometry may be included.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Class</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2025-09-01_52">http://rs.tdwg.org/decisions/decision-2025-09-01_52</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_CVterm"></a>Term Name Iptc4xmpExt:CVterm</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/CVterm">http://iptc.org/std/Iptc4xmpExt/2008-02-29/CVterm</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-09-01</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Category (IRI)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A term to describe the content of the image by a value from a Controlled Vocabulary. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values MUST be IRIs from a controlled vocabulary of subjects to support broad classification of media items. IRIs from the Audiovisual Core Content Description controlled vocabulary are preferred, but other controlled vocabularies may be used as long as the term is uniquely identified by an IRI. This term MAY be used to describe the content of a region of interest within an media item. These guidelines on value format are less restrictive than is specified by the IPTC guidelines and this property MAY be used with any media type, not only images.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_CVtermLiteral"></a>Term Name ac:CVtermLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/CVtermLiteral">http://rs.tdwg.org/ac/terms/CVtermLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-09-01</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/CVtermLiteral-2025-09-01">http://rs.tdwg.org/ac/terms/version/CVtermLiteral-2025-09-01</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Category (literal)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A term to describe the content of a image or a region of interest within an image using a controlled value string.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values SHOULD be selected from the Audiovisual Core Content Description controlled vocabulary or a vocabulary that can be identified using ac:subjectCategoryVocabulary. If a value is from the Audiovisual Core Content Description controlled vocabulary, it is not necessary to provide a value for ac:subjectCategoryVocabulary. Multiple values MAY be provided and separated by space vertical bar space ( | ), however they MUST be from a single vocabulary. It is best practice to use Iptc4xmpExt:CVterm instead of ac:CVtermLiteral whenever practical.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2025-09-01_52">http://rs.tdwg.org/decisions/decision-2025-09-01_52</a></td>
		</tr>
	</tbody>
</table>


<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_filterHighPass"></a>Term Name ac:filterHighPass</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/filterHighPass">http://rs.tdwg.org/ac/terms/filterHighPass</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-09-01</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/filterHighPass-2025-09-01">http://rs.tdwg.org/ac/terms/version/filterHighPass-2025-09-01</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>High-pass Filter Frequency</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>High-pass filter frequency used in the recording/preprocessing of the multimedia item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Numeric value in hertz (Hz)</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2025-09-01_52">http://rs.tdwg.org/decisions/decision-2025-09-01_52</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_filterLowPass"></a>Term Name ac:filterLowPass</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/filterLowPass">http://rs.tdwg.org/ac/terms/filterLowPass</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-09-01</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/filterLowPass-2025-09-01">http://rs.tdwg.org/ac/terms/version/filterLowPass-2025-09-01</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Low-pass Filter Frequency</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Low-pass filter frequency used in the recording/preprocessing of the multimedia item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Numeric value in hertz (Hz)</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2025-09-01_52">http://rs.tdwg.org/decisions/decision-2025-09-01_52</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subjectCategoryVocabulary"></a>Term Name ac:subjectCategoryVocabulary</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subjectCategoryVocabulary">http://rs.tdwg.org/ac/terms/subjectCategoryVocabulary</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2025-09-01</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subjectCategoryVocabulary-2025-09-01">http://rs.tdwg.org/ac/terms/version/subjectCategoryVocabulary-2025-09-01</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Category Vocabulary</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Any controlled vocabulary from which values for ac:CVtermLiteral have been drawn.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The value SHOULD be a stable URL for the vocabulary if one is available.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If controlled string values for ac:CVtermLiteral are taken from the Audiovisual Core Subject Category controlled vocabulary, it is not necessary to provide a value for this property. If pipe separated strings are used to provide multiple values for ac:CVtermLiteral, this term MUST NOT be repeated. It MAY be repeated if data structuring allows particular ac:CVtermLiteral string values to be associated with particular values for this term.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2019-12-01_19">http://rs.tdwg.org/decisions/decision-2019-12-01_19</a></td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2025-09-01_52">http://rs.tdwg.org/decisions/decision-2025-09-01_52</a></td>
		</tr>
	</tbody>
</table>

