----------------------------------------------------------------------------------------------------
LG
----------------------------------------------------------------------------------------------------
Solution: Remove data under """



class DuplicatedNode(Node):
"""
Within Location Graph, some Nodes may be created by more than one transform - eg "Name", "Phone"
and others - and these are recognised by being "DuplicatedNode"s.

There is no responsibility that a transform does not create duplicates to nodes from other

`

❌
"""
The relation between a SearchPlace and its Phones. See `ContactInfoAttribute
<https://developer.here.com/olp/documentation/here-map-content/topics_api/com.here.schema.rib.v2.contactinfoattribute.html>`_
where the `type` is `PHONE` or `FAX` or `MOBILE_PHONE` or `TOLL_FREE`.
"""




`
❌


@doc.parameter("node_label", _in="path", choices=sorted(GeometryForNode.Handled))
@doc.summary("Geometries for a node")
@doc.description(
"""Sometimes you want to put nodes on a map: like "where is the place that has this phone number?" """
"""or "show me what street segments are included in this district". This endpoint will walk the graph """
"""and create a "multi" geometry (for most things), or for nodes like District and "Subdistrict" """
"""it computes a derived (multi-) polygon."""

`

✅


class ReviewRating(DuplicatedNode):
"""
The `FeedbackAttribute.Review.ReviewRating
<https://developer.here.com/olp/documentation/here-map-content/topics_api/com.here.schema.rib.v2.feedbackattribute.review.rating.html>`_.
"""

label: str = "ReviewRating"

`
n batch_of_cra_ids:
cypher = f""" /* API/src/services/prepared_statements/connectedrestareas_alongsegments.py#L196 */
WITH {orjson.dumps(sorted(cra_ids)).decode("utf-8")} as cra_ids
MATCH (wp:HEREPlace) <-[:WAYPOINT]- (cra:ConnectedRestArea) -[CONTAINS]-> (hp:HEREPlace) -[CATEGORY]-> (pc:PlacesCategory)
WHERE cra.identifier in cra_ids
WITH wp, cra, hp, pc
OPTIONAL MATCH (hp) -[CHAIN]-> (c:Chain)

`
❌


and excluded (maphub.cit.api.here.com) TransitStop as the usage of this dict is not yet well authorised.
"""

ISOLATED_NODE_LABELS = {"KeyValuePair", "LoadStep", "PostalCode", "AbstractPlace"}
"""
The ISOLATED_NODE_LABELS are nodes which do not have any relations at all. There may, or may not, exist objects in the
databases.

`
❌
refuel, rest, or take refreshments.
here:pds:navteq-lcms:400-4300-0308 - Scenic Overlook Rest Area
A rest area that provides a location along a roadway with a regionally important panorama or overlook, or
a place where a driver can stop to observe the scenery.

I prioritise them, from least important to most important as:
`


❌
----------------------------------------------------------------------------------------------------
Solution:  Correct regex for Vehicle Data(License Plate)

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
