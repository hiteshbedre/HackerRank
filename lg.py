----------------------------------------------------------------------------------------------------
LG
----------------------------------------------------------------------------------------------------
Solution: Remove data under """


Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/Common/t_types/core.py#L770
Data Category: Contact Data
Data Element: Phone Number
Sensitivity: medium
Confidence: high
Matching string: Phone
Code: `

class DuplicatedNode(Node):
"""
Within Location Graph, some Nodes may be created by more than one transform - eg "Name", "Phone"
and others - and these are recognised by being "DuplicatedNode"s.

There is no responsibility that a transform does not create duplicates to nodes from other

`

❌
Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/Common/t_types/search_places.py#L201
Data Category: Contact Data
Data Element: Phone Number
Sensitivity: medium
Confidence: low
Matching string: PHONE
Code: `
"""
The relation between a SearchPlace and its Phones. See `ContactInfoAttribute
<https://developer.here.com/olp/documentation/here-map-content/topics_api/com.here.schema.rib.v2.contactinfoattribute.html>`_
where the `type` is `PHONE` or `FAX` or `MOBILE_PHONE` or `TOLL_FREE`.
"""




`
❌


Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/API/src/blueprints/services/data/geometry_for.py#L143
Data Category: Contact Data
Data Element: Phone Number
Sensitivity: medium
Confidence: low
Matching string: phone
Code: `
@doc.parameter("node_label", _in="path", choices=sorted(GeometryForNode.Handled))
@doc.summary("Geometries for a node")
@doc.description(
"""Sometimes you want to put nodes on a map: like "where is the place that has this phone number?" """
"""or "show me what street segments are included in this district". This endpoint will walk the graph """
"""and create a "multi" geometry (for most things), or for nodes like District and "Subdistrict" """
"""it computes a derived (multi-) polygon."""

`

✅


Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/Common/t_types/place_reference.py#L1077
Data Category: User Content Data
Data Element: Ratings
Sensitivity: medium
Confidence: high
Matching string: rating
Code: `
class ReviewRating(DuplicatedNode):
"""
The `FeedbackAttribute.Review.ReviewRating
<https://developer.here.com/olp/documentation/here-map-content/topics_api/com.here.schema.rib.v2.feedbackattribute.review.rating.html>`_.
"""

label: str = "ReviewRating"

`

❌
Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/API/src/services/prepared_statements/connectedrestareas_alongsegments.py#L197
Data Category: Location Data
Data Element: Location Data 2
Sensitivity: low
Confidence: low
Matching string: WAYPOINT
Code: `
for cra_ids in batch_of_cra_ids:
cypher = f""" /* API/src/services/prepared_statements/connectedrestareas_alongsegments.py#L196 */
WITH {orjson.dumps(sorted(cra_ids)).decode("utf-8")} as cra_ids
MATCH (wp:HEREPlace) <-[:WAYPOINT]- (cra:ConnectedRestArea) -[CONTAINS]-> (hp:HEREPlace) -[CATEGORY]-> (pc:PlacesCategory)
WHERE cra.identifier in cra_ids
WITH wp, cra, hp, pc
OPTIONAL MATCH (hp) -[CHAIN]-> (c:Chain)

`
❌


Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/Common/t_types/core.py#L1257
Data Category: Contact Data
Data Element: Address
Sensitivity: medium
Confidence: high
Matching string: PostalCode
Code: `
and excluded (maphub.cit.api.here.com) TransitStop as the usage of this dict is not yet well authorised.
"""

ISOLATED_NODE_LABELS = {"KeyValuePair", "LoadStep", "PostalCode", "AbstractPlace"}
"""
The ISOLATED_NODE_LABELS are nodes which do not have any relations at all. There may, or may not, exist objects in the
databases.

`
❌

Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/Relations/Infered/ConnectedRestArea/src/t_types.py#L412
Data Category: Personal Identification
Data Element: Driver
Sensitivity: low
Confidence: low
Matching string: driver
Code: `
refuel, rest, or take refreshments.
here:pds:navteq-lcms:400-4300-0308 - Scenic Overlook Rest Area
A rest area that provides a location along a roadway with a regionally important panorama or overlook, or
a place where a driver can stop to observe the scenery.

I prioritise them, from least important to most important as:
`


❌
----------------------------------------------------------------------------------------------------
Solution:  Correct regex for Vehicle Data(License Plate)

Reponame: LG
Filepath: https://main.gitlab.in.here.com/lg/LG/blob/master/Transform/HMC/src/rib_2_transform/com/here/schema/rib/v2/env_zone_attributes_pb2.py#L49
Data Category: Vehicle Data
Data Element: License Plate
Sensitivity: low
Confidence: low
Matching string: LICENSE_PLATE_ENDI
Code: `
serialized_options=None,
type=None),
_descriptor.EnumValueDescriptor(
name='LICENSE_PLATE_ENDING', index=2, number=2,
serialized_options=None,
type=None),
_descriptor.EnumValueDescriptor(

`
✅

----------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
