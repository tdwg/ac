# Summary record of comments received during public comment

Public comment period opened 2013 March 1

Subject: 	Re: [Taxacom] Public Review of Audubon Core
Date: 	Mon, 4 Mar 2013 11:15:46 -0500
From: 	David Campbell <pleuronaia@gmail.com>
To: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>
References: 	<5130E10B.9050806@vanderbilt.edu>

As a potential producer and consumer of biodiversity data, as far as I
can see the document focuses on what information the computer programs
need to have to communicate with each other.  This is a vital effort,
but I'm not certain how I, as a taxonomist, can tell how these data
types relate to actual biodiversity data and the pieces of information
that I want to see when I am looking for biodiversity data online.


-------------------------------
Subject: 	Audubon Core Review [1]
Date: 	Sun, 24 Mar 2013 11:04:46 -0700
From: 	<azinovjev@fastmail.fm>
To: 	<steve.baskauf@vanderbilt.edu>
CC: 	<webmaster@salicicola.com>

Steve,

… The immediate question:
How would I record most of my sawfly photos:  which are usually not
sawflies [adults or larvae] themselves but their galls, mines, 'holes in
leaves' (sometimes, by their shape, I can precisely identify species
produced it), etc., etc.  People will photograph nests, animal's traces,
record bird songs, but how such media would be tracked?  It seems to be
a very common situation.

Maybe I was a bit too tired (it's nearly midnight here) and did not read
list of terms carefully but I did not notice anything for such "product"
instead of animal itself. I should have seen a generic term somewhere
but don't remember neither the English or Latin word nor where could I
see it.

Not sure, but perhaps next time I'll try to test web tracker.

Alexey


--

  azinovjev@fastmail.fm



-------- Original Message --------
Subject: 	Re: [tdwg-content] reminder about the Audubon Core public review (ending April 1)
Date: 	Sun, 24 Mar 2013 16:51:24 -0400
From: 	Rob Stevenson <rdstevenson10@gmail.com>
To: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>
CC: 	Bob Morris <morris.bob@gmail.com>
References: 	<514D93C6.4030705@vanderbilt.edu>

Steve,

Some comments on Audubon Core

Rather than have Term Name: associatedSpecimenReference as a place for phylocode and a DNA barcode, should the standard support specific fields for a phylocode and a DNA barcode?  These seem to be independent approaches that might help anchor or tie together multimedia observations.  I can image people taking a picture of an insect and getting a DNA barcode but not having a Taxon Name or a set of characters completed. It seems that molecular data are becoming more and more important and their collection is becoming more and more automated.  For microbes, molecular characterization seems to be the main approach uses

Consider adding A Controlled Vocabulary for LTER Datasets to Notes of the Term Name: Iptc4xmpExt:CVterm

Last comment: Let's say I have a picture of a leaf with holes in it.  Is there a way to specify the taxon of the leaf and the taxon of the insect that made the holes.  Caterpillar species A eats Plant leaf Species B? If I know that caterpillar only made that shape hole when it was parasitized can I also specify the taxon of the parasite?  Another leaf example would be lichens and liverworts that colonize leaves.  One might be over growing another?

In general I would like to specific multiple taxa and relationships among the taxa in the image or movie, etc,

Thanks for all the work. We need standards such as these to make the semantic web work!

Best wishes

Rob Stevenson



----------------------------
-------- Original Message --------
Subject: 	Thanks for your comment on Audubon Core
Date: 	Wed, 03 Apr 2013 14:02:18 -0500
From: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>
Organization: 	Vanderbilt University Dept. of Biological Sciences
To: 	John Wieczorek <tuco@berkeley.edu>
CC: 	Bob Morris <morris.bob@gmail.com>

John,
Thanks for your comment on Audubon Core regarding broadening the scope
of depiction.  The issue
http://code.google.com/p/auduboncore/issues/detail?id=47 has been
accepted and is under consideration by the authors.
Steve


----------------------------
-------- Original Message --------
Subject: 	Audubon Core 1.0 Call For Public Review
Date: 	Wed, 27 Mar 2013 11:26:43 -0400
From: 	Andréa Matsunaga <ammatsun@acis.ufl.edu>

To: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>



Steve Baskauf.

    I would like to ask some questions about AC 1.0 to clarify my understanding of it and see if AC can be improved:

a) AC is defined as "a set of vocabularies designed to represent metadata for biodiversity multimedia resources and collections". While many terms have some guidance on how the term applies (or not) to a "multimedia resource" vs. "multimedia collections", not all terms display that guidance (e.g., xmp:CreateDate). I imagine that the larger a collection becomes, the harder it is to have a single value for most of the terms (e.g., dcterms:rights, ac:captureDevice, ac:providerID). Would it be possible for each term to display information on its applicability to "multimedia resource" vs. "multimedia collections", e.g. when to use repeatability of terms for describing collections?


b) An AC record is considered to contain "at least the four mandatory terms... One of these, the value of Identifier is a Globally Unique IDentifier (GUID)". However, the identifier term is further defined as "Required: Yes for media collections, No for media resources (but preferred if available)." What is the reasoning for not requiring a (GUID) identifier for media resources?



c) It is suggested that the dcterms:extent term be used for multiple purposes (e.g., image size in pixels as well as file size). However, the term is not repeatable. Wouldn't it be more appropriate to have a specific term for the object size in bytes? Having this information readily available in the metadata can help estimate the needed storage before getting the actual object.



d) When using the ac:variant "Offline", would it be appropriate to store an offline local file path to the resource in accessURI in the form "file://"?



e) In iDigBio (http://tinyurl.com/MISC-Media), some people have expressed the desire to have information about the magnification being used (to have a rough idea of the size of the object, potentially from data that is automatically retrieved from the capturing device) as well as the real world size depicted by a pixel (for the purposes of allowing one to make measurements on the image; this would require one to have a scale on an image and perform some arithmetic). Would it be possible to add such terms?



Note: posted to tdwg-content and Live Plant Image Group:
****
This subject came up as part of a comment on Audubon Core from Andréa Matsunaga:

"In iDigBio (http://tinyurl.com/MISC-Media), some people have expressed the desire to have information about the magnification being used (to have a rough idea of the size of the object, potentially from data that is automatically retrieved from the capturing device) as well as the real world size depicted by a pixel (for the purposes of allowing one to make measurements on the image; this would require one to have a scale on an image and perform some arithmetic). Would it be possible to add such terms?"

There are terms in the SpatialMetrics terms (section 9.1) of the MIX vocabulary (http://www.loc.gov/standards/mix/ ) that can encode this kind of information.  However, I would be interested in opinions about whether expressing this kind of information is a narrow need that is outside the scope of a fairly broad standard like Audubon Core or if the need for such terms is perceived as widespread.
****

f) Another important term for iDigBio is MD5 checksum for each variant. This allows users retrieving an object to automatically verify the integrity of the object. Would it be possible to add such a term for each access point?



g) A couple of auxiliary terms also identified in iDigBio, are terms to capture the funding source of the digitization effort. Would it be possible to add such terms?



Thank you,
--am
Andréa Matsunaga
Research Assistant Professor, Advanced Computing and Information Systems (ACIS) Laboratory
Department of Electrical and Computer Engineering, University of Florida
P.O. Box 116200, 334 Larsen Hall, Gainesville, FL 32611-6200
Tel: (352) 846-2466    Fax: (352) 392-5040

----------------------------------------


-------- Original Message --------
Subject: 	Re: [lpig] reminder about the Audubon Core public review (ending April 1)
Date: 	Sun, 31 Mar 2013 09:57:23 -0700
From: 	<azinovjev@fastmail.fm>

To: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>

CC: 	<webmaster@salicicola.com>

References: 	<514D949F.9040809@vanderbilt.edu>


Dear Steve,

I'm too busy these days (leaving SPb on Wednesday, I still have too much
to do) but I made a printout and managed to read the printed  copy of
the Audubon Term List while on the train even twice.

Introduction part (Borrowed Vocabulary):
  -- I would suggest adding here the namespaces, not only commonly used
  prefixes and abbreviations. These are namespaces that I (if  being a
  data provider) would like to see first and then copy and paste.

xmp:Rating
  -- I do not understand the meaning of the first sentence in the Notes:
  "The origin of the rating is not communicated".

[ac]:comments: "Best practice would also identify the commenter"
  -- Agree, but how would you suggest to identify the commenter, by
  asking him to add his/her name into the comment's body?
  -- I did not find the field 'commenter'. Could it exist, it might be
  difficult to implement this idea in a flat model (when having more
  than a single comment, though in XML format it could be done easily by
  using commenter as an attribute of a comment, e.g. <comment
  commenter="{name}"></comment>)

dcterms:available:
  -- According to Notes, it could be particularly useful when metadata
  exists without media itself. Correct?
  -- I did not check the links, and don't know how it could be done
  (when media will never be available). -- I would suggest giving an
  example.

[ac]:hasServiceAccessPoint
  -- When start reading the entry, I thought (erroneously?) that this
  will be a Boolean field (yes/no). -- Did I understand it correctly
  that this is a field with child nodes? Of course I know that in some
  languages, it could be interpreted as 'true' but I doubt that using
  the name starting with 'has...' is a good choice for non Boolean field
  in a usual sense. In any case, perhaps this is one of the most
  important parts where examples(S) are needed.

Geography Vocabulary
  -- This is the MOST confusing part. When reading List for the first
  time, I was wondering why there are so few fields. -- Particularly
  when reading the introduction with index -- What happens with all
  other commonly used terms? -- And only when reading CAREFULLY the
  introduction part to the Geography part, I noticed that 'all
  geographic terms from DarwincCore are included'
  -- You should NOT do it in that hidden way. Ideally to list all
  'included' terms, or maybe to create a special entry.

Iptc4xmpExt:City, which is actually could be nearly ANY place name.
 -- I don't understand why field should be called City if it is NOT (at
 least in most situation).
I think that people will just ignore this term as being laughable.
I also did not understand why Audubon Core terms should rely on IPTC
terms at all.
Could it be up to me to decide, I would add the missing terms as AC
ones, and in this particular case would name it 'PlaceName' or
something.

ncd:taxonCoverage
  -- I did not think about it thoroughly but 'this somewhat expands the
  usage of ncd:taxonCoverage' raise a question, why not using
  ac:taxonCoverage, i.e., to put it into ac namespace.

ac:accessURI
  -- Are you sure that this should not be repeatable? I have a feeling
  that just this is a case when you could have more than a single URI
  leading to the same resource. The most common example on the web is a
  'www' prefix, which frequently could be omitted. And how about
  mirroring?

dcterms:extent
  -- This is not AC term, but I personally have a feeling that using the
  same term for essentially different things like size of the file (on a
  disk) and pixel size is hardly acceptable.

I have some more generic questions (or doubts) but this would need much
more time to write it down and I don't have it (time). -- Perhaps I'll
have it only at the end of the week or during the next one.

I'm sending this as an email but on re-reading it, I may try to submit
SOME of these comments via tracker (during the next hour or two, at
most).

That's it for now,
Alexey
19:50 31.03.2013
--

  azinovjev@fastmail.fm



-------- Original Message --------
Subject: 	RE: [tdwg-content] reminder about the Audubon Core public review (ending April 1)
Date: 	Thu, 4 Apr 2013 09:24:29 +0200
From: 	"Dröge, Gabriele" <g.droege@BGBM.ORG>
To: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>
References: 	<514D93C6.4030705@vanderbilt.edu>


Dear Steve,
. . .

We have discussed the GBIF - Audubon Core TDWG Multimedia Resources Metadata Schema in our
department and with our colleagues involved in the development of ABCD and would like to send
you some feedback.
At first we agree that a Multimedia standard is definitely required. Please find below our
comments:

Why are detailed technical facts about a multimedia item are not part of the standard, e.g.
color space, chromaticities, width, height, resolution, lens aperture, exposure time, compression
scheme, saturation, modified date, manipulated etc. ?

It seems as some important IPR facts are missing, e.g. TermsOfUse, Disclaimer, Copyright Statement
URI, etc. In ABCD we included detailed IPR statements. Maybe you should have a look at it:
http://www.bgbm.org/tdwg/codata/schema/ABCD_2.06/HTML/ABCD_2.06.html#element_IPR_Link0315B6C8


Additionally to locality, country etc. GPS data would be useful.


We would furthermore suggest following parameters: Relation to other multimedia units, sequence
and position in sequence, reference/link to antecessor and successor of this unit



Page 2, footnotes:          Links 1 and 2 are outdated, better to publish the new GBIF urls


Page 4, figure 1:               we know that this figure is based on another figure that's part
of the NCD document, but nevertheless would suggest some changes; molecular DNA is much more
than GenBank only; we would prefer to either delete "(GenBank)" or to complete the figure with
the following:
Sequence data have multimedia items (Pherograms), DNA samples have multimedia items (gel images),
tissue samples have multimedia items (microscope photographs, REM etc.)

Sequence data
(GenBank/EMBL/DDBJ)
  Is defined from
       |
DNA samples
(Global Genome Biodiversity Network)
  Is extracted from
      |
Tissue samples
(Global Genome Biodiversity Network)
Is taken from
      |
specimens
(Global Biodiversity Information Facility)



We hope this feedback and thoughts might help you. Please don't hesitate to contact us if you
have any further questions.
Best regards
Gabi

-----------------------------------------------------------------
Gabriele Droege
Coordinator - DNA Bank Network
Global Genome Biodiversity Network (GGBN)
Berlin-Dahlem DNA Bank
Deputy Women's Officer ZE BGBM

Botanic Garden and Botanical Museum Berlin-Dahlem
Freie Universität Berlin
Koenigin-Luise-Str. 6-8
14195 Berlin
Germany

+49 30 838 50 139

www.dnabank-network.org
www.ggbn.org
www.bgbm.org

-------- Original Message --------
Subject: 	RE: [lpig] magnification/extent of objects present in images
Date: 	Fri, 5 Apr 2013 20:27:54 +0000
From: 	Boyce Tankersley <btankers@chicagobotanic.org>
To: 	steve.baskauf@vanderbilt.edu <steve.baskauf@vanderbilt.edu>, TDWG Content Mailing List <tdwg-content@lists.tdwg.org>
References: 	<515C9790.3040507@vanderbilt.edu>
For those living specimens where measurements are critical we include a scale next to the plant part in the image.  
We currently have 25 photographers using their own cameras and I am not sure how we would be able to determine and/or document magnification levels without the use of a scale.  
If we were working with a single make and model of a camera attached to a microscope I think the issue of magnification of the raw image would be easier to determine.
Boyce Tankersley
Director of Living Plant Documentation
Chicago Botanic Garden

-----Original Message-----
From: live-plant-image-group@googlegroups.com [mailto:live-plant-image-group@googlegroups.com] On Behalf Of Steve Baskauf
Sent: Wednesday, April 03, 2013 3:57 PM
To: TDWG Content Mailing List
Cc: live-plant-image-group@googlegroups.com
Subject: [lpig] magnification/extent of objects present in images
I am cross-posting this to the Live Plant Image email list in addition to tdwg-content because this is a subject that was previously discussed there.  However, as this is part of the public review of the draft Audubon Core TDWG standard, I would request that you reply only to the tdwg-content list, so that any additional discussion will take place there for the record.  If you aren't on that list and would like to reply, please send your responses to steve.baskauf@vanderbilt.edu and I will post it for you.
This subject came up as part of a comment on Audubon Core from Andréa Matsunaga:
"In iDigBio (http://tinyurl.com/MISC-Media), some people have expressed the desire to have information about the magnification being used (to have a rough idea of the size of the object, potentially from data that is automatically retrieved from the capturing device) as well as the real world size depicted by a pixel (for the purposes of allowing one to make measurements on the image; this would require one to have a scale on an image and perform some arithmetic). Would it be possible to add such terms?"
There are terms in the SpatialMetrics terms (section 9.1) of the MIX vocabulary (http://www.loc.gov/standards/mix/ ) that can encode this kind of information.  However, I would be interested in opinions about whether expressing this kind of information is a narrow need that is outside the scope of a fairly broad standard like Audubon Core or if the need for such terms is perceived as widespread.
Steve



-------- Original Message --------
Subject: 	Re: Comments on Audubon Core
Date: 	Sat, 06 Apr 2013 17:09:06 -0500
From: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>
Organization: 	Vanderbilt University Dept. of Biological Sciences
To: 	Paul Flemons <Paul.Flemons@austmus.gov.au>
CC: 	Morris, Robert (SAM) <Robert.Morris@samuseum.sa.gov.au>, Aaron Wilton (WiltonA@landcareresearch.co.nz) <WiltonA@landcareresearch.co.nz>, Bob Morris <morris.bob@gmail.com>
References: 	<0D6CDDF65AE0F546A7D53B9E56D9A5589638D762@AMMAIL3.austmus.gov.au>



Paul Flemons wrote:
Steve,
Please find below a very rough assemblage of comments from members of the Museum and Herbaria communities in Australia.

It does seem very image-orientated as most of the examples are concerned with images. My concern would be that perhaps they have not concentrated sufficiently on multimedia like soundfiles, so I am not confident that they haven’t left anything out. For example, they have a term photoshop:credit in the Attribution vocabulary, but there doesn’t seem to be an equivalent for soundfile editing. I know that our soundfiles have/will be been chopped up, enhanced, etc. using various editing techniques by a variety of people who perhaps should be credited.


Which leads me to ask: why didn’t they make the few genuinely different terms of the Audubon Core simply an extension of the Darwin Core? I assume because the multimedia they are considering are not necessarily specific, registerable, collection objects relating to (observations of) species occurrences?

physicalSetting – this definition appears ambiguous and possibly unnecessarily restrictive, only applying to “Unmodified” objects  (definition of unmodified?) in either natural setting of the unmodified object or the artificial setting.  What about an organism that occurs in an unnaturallsetting, or a “natural” setting that has been slightly modified by weeds or other disturbance? It is useful to be able to express these type of properties, and suspect this is confounding two factors in the definition (removing reference to the state of the object being photographed would be a good start).


Excuse me if I’ve missed something, but I wonder whether the mandatory terms (outlined in this document) should include the equivalent of institutionCode to aid discoverability of the resource? This schema is intended to make multimedia resources more discoverable, including non-digital resources, which means that the potential user meeds a path to track back to the owner/publisher/holder of that resource – which is not always the creator or copyright holder. The recommendation might be to suggest provider as a mandatory field?



The only ‘desirable’ but not essential element that might be good from our perspective is something like ‘attributionText’ – with our goal of pushing all multimedia resources out with open licences to encourage re-use, it’d be great to supply the required attribution so that people don’t need to chase us for it when it is to be used, but I think we can orchestrate that through careful use of the suggested AC fields rights and credit, and as we get better at publishing our stuff online ourselves, attributionLinkURL.



Any response to these would be appreciated as a means of our communities understanding Audubon Core better, if not for improving it from your perspective.

Regards
Paul


Paul K J Flemons
Manager, Collection Informatics
Team Lead, Atlas of Living Australia Biodiversity Volunteer Portal
Biodiversity Information Standards (TDWG) Representative for Oceania
Australian Museum 6 College Street Sydney NSW 2010 Australia
t 61 2 9320 6343 m 0413458649  f 61 2 9320 6021
Visit: http://www.australianmuseum.net.au
Like: http://www.facebook.com/australianmuseum
Follow: http://www.twitter.com/austmus
Watch: http://www.youtube.com/austmus


Inspiring the exploration of nature and cultures


-------- Original Message --------
Subject: 	Re: Public Review of Audubon Core
Date: 	Mon, 08 Apr 2013 20:39:17 -0500
From: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>
Organization: 	Vanderbilt University Dept. of Biological Sciences
To: 	Joyce Gross <joyceg@berkeley.edu>
CC: 	Bob Morris <morris.bob@gmail.com>, John Wieczorek <tuco@berkeley.edu>
References: 	<5130F200.3000908@vanderbilt.edu> <5130F743.3000302@berkeley.edu> <51615568.1050409@vanderbilt.edu> <51631EB8.1000103@berkeley.edu>



Joyce Gross wrote:
> Hi Steve,
>
> I have a couple of things you can maybe help with -- but I'm not sure
> if this helps the Audubon Core review or not.
>
> First fyi -- I'm more or less the only person who works on CalPhotos,
> and I work on 12 other projects as well. So that gives you an idea of
> how much time I can spend on CalPhotos.
>
> In one of my other projects we are connecting media from Artos (Museum
> of Vertebrate Zoology) with CalPhotos, and trying to come up with a
> list of matches between CalPhotos fields and some standard fields,
> whether from Darwin Core, Dublin Core, or Audubon Core.
>
> I've been stumped on a few fields. If you have any suggestions for
> where they might fit into the Audubon Core, let me know. I still have
> the feeling I haven't spent enough time pouring over the Dublin Core
> and Audubon Core standards -- and that I am missing things that may be
> obvious to others. But so far MVZ folks have not been able to fill in
> the gaps either.
>
> 1) contact: CalPhotos has a field with this name that contains both
> the name of the person/organization to contact for permission to use
> an image or for acquiring high res images, etc. The contact name/email
> is not necessarily that of the photographer or organization providing
> the images. I did not see such a field in the AC or anywhere else. Any
> suggestions, or is it something that could be added?



>
> 2) additional taxa: CalPhotos has a field where one can list
> additional taxa that appear in an image, comma separated. Ie, a list
> of scientific names. (Of course there are also fields for scientific
> name, family, order, class, phylum -- for the primary taxon. Most
> CalPhotos images have one primary taxon, but we like to be able to
> informally list additional taxa if there are any.)



>
> To keep this short I'm going to stop now. There are a few other
> CalPhotos fields I haven't matched with a "Core" field yet, but they
> are more quirky and can likely be squeezed into some existing field
> somehow, or else they are just too quirky for anyone else to bother
> thinking about!
>
> Thanks for any suggestions about the above two fields, and maybe with
> some luck this is helpful for the review too.
>
> Joyce
>
>


-------- Original Message --------
Subject: 	RE: Public Review of Audubon Core
Date: 	Mon, 8 Apr 2013 22:06:10 +0000
From: 	Moore, Gerry - NRCS, Greensboro, NC <Gerry.Moore@gnb.usda.gov>
To: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>
References: 	<5130E94B.4040302@vanderbilt.edu> <2379CA27CD42644B8E68CB6F45D2B9981FFF09@001FSN2MPN1-031.001f.mgd2.msft.net> <51615577.2060107@vanderbilt.edu> <2379CA27CD42644B8E68CB6F45D2B998261585@001FSN2MPN1-032.001f.mgd2.msft.net> <516219FB.5090504@vanderbilt.edu>



Hi Steve,

  See attached. My comments focused on the taxonomy section, and represent issues that we have struggled with here at PLANTS. Cheers, Gerry



Label Scientific Taxon Name
It is recommended to provide author citation to scientific names, to avoid ambiguities in the presence of homonyms (the same name created by different authors for different taxa).
It should be noted that there are different classes of homonyms when talking about nomenclature of all living things.
Some are perfectly legitimate and unavoidable when the names are governed by different Codes of nomenclature. For example there is a beetle genus Tribolium and a grass genus Tribolium. However,  homonyms governed by the same Code of nomenclature cannot be in use. Thus,  Rhynchospora pallida M.A.Curtis and Rhynchopsora pallida Steud. cannot both be used as the latter is an illegitimate later homonym that is not be taken up.
Also citation of the author names would help in avoiding ambiguities but it would not solve the problem as sometimes the same author published the same name for different taxa. Linnaeus did it, for example: Mimosa cinera L. (Sp. Pl.: 517. 1753) and Mimosa cinera L. (Sp. Pl.: 520. 1753). Thus, homonyms are defined not as the same name published by different authors, but the same name with different types. Homonyms are usually published by different authors but not always.

Label Identification Qualifier  
The following is given: Examples: 1) For the determinations “cf. Quercus agrifolia var. oxyadenia”, “Quercus cf. agrifolia var. oxyadenia”, “Quercus agrifolia cf. var. oxyadenia”, Scientific Taxon Name would always be “Quercus agrifolia var. oxyadenia”, with Identification Qualifier “cf. genus”, “cf. species” and “cf. var.”, respectively.
These examples seem odd.  For example “cf. Quercus agrifolia var. oxyadenia” implies that it is not clear if the entity in question is properly identified to belong to the genus Quercus but is confidently placed in the species and variety. But how can this be since the species and variety identification is contingent upon the proper generic placement?

Label Name According To
The following is stated: “Definition: The taxonomic authority used to apply the name to the taxon, e. g., a book or web service from which the name comes. Notes: Examples are ‘ITIS’, ‘Catalogue of Life’, ‘Peterson Field Guide to Birds of North America’.”
The examples cited are not primary sources for taxonomic names. The names certainly did not come (originate) from there but came from somewhere else. The sources cited – assuming they provide a complete synonymy – may provide a concept for the taxon that goes by the name provided. However, even in those cases the concept likely originated from another source, such as a taxonomic treatment or a regional flora.

Label Scientific Name Synonym
“The primary purpose of this is in support of resource discovery, not developing a taxonomic synonymy. Misidentification or misspellings may thus be of interest.”
Primary purpose aside, I don’t like conflating true synonyms with other things, such as orthographic variants and misapplications/misidentifications.
True synonyms are of two types, nomenclatural (objective) and taxonomic (subjective), the former being objective because they are based on the same type, such as Scirpus maritimus L. and Schoenoplectus maritimus ( L. ) Lye, and the latter being subjective because they are based on different types and are deemed to be the same (taxonomically) based on the subjective judgment of a taxonomist.  
Spelling variants of the same name are not really synonyms as they are merely variations of the same name. Misapplications of a name to a taxon is in some ways the opposite of a synonym as the name’s type is not considered the same as the taxon it has oftentimes been associated.
By “lumping” these different attributes under “synonymy” confusion is oftentimes generated. PLANTS  is guilty of this too but it promotes confusion. For example one will oftentimes see an earlier Linnaean name as a synonym of a later name published by a post-Linnaean author.  However, the rules of nomenclature make clear that an earlier name is generally not to be the synonym of a later accepted name. Currently PLANTS is working on establishing a separate category for misapplied names and orthographic variants so they appear in fields separate from bona fide synonyms.


------------------------
The following is from the comment #2 for Issue 55 of the Issue Tracker .  It includes quotes from several emails sent during the public comment.  

Comment from Andréa Matsunaga <ammatsun@acis.ufl.edu> during public review:

"e) In iDigBio (http://tinyurl.com/MISC-Media), some people have expressed the desire to have information about the magnification being used (to have a rough idea of the size of the object, potentially from data that is automatically retrieved from the capturing device) as well as the real world size depicted by a pixel (for the purposes of allowing one to make measurements on the image; this would require one to have a scale on an image and perform some arithmetic). Would it be possible to add such terms?"

Comment from Steve: I put out a request for discussion on this issue to the tdwg-content list and Live Plant Imaging Group list and received only one reply from Boyce Tankersley <btankers@chicagobotanic.org>:

"For those living specimens where measurements are critical we include a scale next to the plant part in the image.  

We currently have 25 photographers using their own cameras and I am not sure how we would be able to determine and/or document magnification levels without the use of a scale.  

If we were working with a single make and model of a camera attached to a microscope I think the issue of magnification of the raw image would be easier to determine."


----------------------------------------
Text from Issue Tracker Issue 67 http://code.google.com/p/auduboncore/issues/detail?id=67

Reported by gtuco.btuco, Apr 12 (6 days ago)
1. Provide an ac Term Name or Label. A link to the Normative Term List is
also helpful. This can be easily done at one of the <a ref="http://terms.gb
if.org/wiki/Audubon_Core_Term_List_(DRAFT_of_1.0_normative)#Vocabulary_Indi
ces" Vocabulary Indices</a>

ncd:taxonCoverage

http://terms.gbif.org/wiki/Audubon_Core_Term_List_%281.0_normative%29#ncd:taxonCoverage


2. Describe the defect or lack of clarity you find in the term. If you have
an opinion for a change, please add it here, perhaps with pros and cons.

AC recommneds the use of the term taxonCoverage from the Natural Collections Description draft standard, which in turn adopts it from the TDWG Ontology work (http://rs.tdwg.org/ontology/voc/Collection#taxonCoverage
).

The NCD is currently orphaned in its ratification process and none of the TDWG Ontology has any standing as a standard whatsoever. Because of the state of NCD, Darwin Core created terms for ratification under its namespace that were proposed in NCD but had no standing (collectionCode, collectionID, institutionCode, institutionID, and ownerInstitutionCode). Rather than get mired in the dubious state of NCD and the TDWG Ontology, I propose that Audubon Core create a new term for taxonCoverage. Failing that, perhaps propose it for Darwin Core where it has a chance to be ratified more quickly than sorting out NCD, which currently has no champion.

 I asked John to post this issue to the tdwg-content email list for discussion.  Here is the text of his email:
-------- Original Message --------
Subject: 	[tdwg-content] (no subject)
Date: 	Mon, 15 Apr 2013 12:45:33 -0300
From: 	John Wieczorek <tuco@berkeley.edu>
Reply-To: 	<tuco@berkeley.edu>
To: 	TDWG Content Mailing List <tdwg-content@lists.tdwg.org>

Dear all,

I have been asked to cross-post here from a comment on the GBIF Community site discussion of "The Management of TDWG Ontologies and Darwin Core" (http://community.gbif.org/pg/forum/topic/29426/discussion-of-management-of-the-tdwg-ontologies-and-darwin-core/). Given the subject matter, I feel like the whole discussion should take place in the broader audience reached by this list.

While managing the Darwin Core, I advocated not to re-use any term that had no status as a standard. It was partially for this reason that geo:lat and geo:long were rejected (see http://code.google.com/p/darwincore/issues/detail?id=82). It worries me a little to see a non-standard term (ncd:taxonCoverage, adopted in turn from the TDWG Ontology, also not a standard, see http://rs.tdwg.org/ontology/voc/Collection#taxonCoverage) being proposed for adoption into the Audubon Core (see http://terms.gbif.org/wiki/Audubon_Core_Term_List_%281.0_normative%29#ncd:taxonCoverage). Does that bother anyone else? The alternative, sadly, is to make up a new term for ratification with the new standard.

So, questions. If Audubon Core is ratified with the Natural Collections Descriptions (NCD) term in it, does that one term from NCD become a standard term? Under what governance? What about the rest of the NCD namespace? What about the TDWG Ontology. A lot of work went into both of those, but each lost its champions and they remain incompletely reviewed, especially in the context of all that has come to pass since they were active. I know that people refer to the TDWG Ontology fairly often in discussions, and that activity is still fomenting around that work with the imminent publication of the RDF Guide for Darwin Core. But what about NCD. What should we do with it? Does more than one person, group, or project still want to use it? If not, there isn't a lot of reason to go to the trouble of creating a data sharing standard if no one will use it to share. But if its need is still alive and active, who can take up the standard and promote its completion, review, and ratification?

Cheers,

John
------
There were several responses, but none of them directly spoke to the issue.  The status of unratified standards that have languished in limbo for years is an issue that the Vocabulary Management Task Group (VoMaG) has taken up.  See http://community.gbif.org/pg/forum/topic/29426/discussion-of-management-of-the-tdwg-ontologies-and-darwin-core/



-------- Original Message --------
Subject: 	Comments on Audubon Core
Date: 	Wed, 24 Apr 2013 16:41:12 -0400
From: 	Cynthia Parr <parrc@si.edu>

To: 	Steve Baskauf <steve.baskauf@vanderbilt.edu>

CC: 	Katja Schulz <schulzk@si.edu>

. . .
So, here are my comments.  Many are just suggestions to clarify notes.
 In general, while I'm sure one could really go crazy with even more
detail I think you must stop somewhere and I don't see any really
fatal flaws.

Re Subtypes: Any of Drawing, Painting, Logo, Icon, Illustration,
Graphic, Photograph, Animation, Film, SlideShow, DesignPlan, Diagram,
Map, MusicalNotation, IdentificationKey, ScannedText, RecordedText,
RecordedOrganism, TaxonPage, MultimediaLearningObject,
VirtualRealityEnvironment, GlossaryPage.

Are there definitions for these suggested values anywhere?  


What does
"This does not apply to Collection objects" mean.


Re comments
Any comment provided on the media resource, as free-form text. Best
practice would also identify the commenter.
any recommendation for how to identify the commenter?

Re: License Terms
EOL uses the same URI to hold a URL pointer to a CC license such as
(see http://eol.org/schema/media_extension.xml). In the AC notes, you
seems to conflate the license itself and the text to display about the
license. Would be best to clarify in the notes -- if both are
acceptable, then show examples of both.


Re: dcterms:source
We have trouble  explaining this one to our providers. In many if not
most cases, the published source is the provider's own page (e.g. if
the image is original to a particular website, we want the URL of the
web page which provides the context in which it first appeared).   So
an example like this in the Notes would be helpful.

Agents vocabulary
EOL has a richer agents extension available here:
http://eol.org/schema/agent_extension.xml
While I don't think it accounts for metadataCreators, it does account
for some other roles that may be relevant. Is there any chance of
borrowing from this?


If the resource has been assigned a GUID or is also associated with an
identifier issued by a previous agent or project, where would that go?


I hope this is helpful.  Sorry it has taken me so long to get to it.
I've had to do everything by multitasking lately and this kind of
review just won't work like that.

Best of luck in the rest of the process,
Cyndy

Cynthia Sims Parr
Chief Scientist and Director, Species Pages Group
Encyclopedia of Life http://www.eol.org
Office: 202.633.9513, Fax: 202.633.8742
Room W118

Mailing address:
National Museum of Natural History
Smithsonian Institution
P.O. Box 37012, MRC 106
Washington, DC 20013-7012

Public comment period closed 2013 April 25
