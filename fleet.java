----------
Fleet Api
----------------------------------------------------------------------------------------------------
Solution: Added message under negative word


w LoggedUserException( HttpStatus.BAD_REQUEST.value(), contextId, "Service time settings for Pickups/Drops must be an integer", "Pickup/Drop cannot parse Service time: " + v, log, e);
}
continue;
}

if ( constrSubStringParts[ j ].isEmpty() )  continue;

final String usermessage= "Unsupported type of constraint. Use one from: " + ShippingParams.PICKUP.prefix + "," + ShippingParams.DROP.prefix + "," + ShippingParams.LOAD.prefix + ".";
final String internalmessage= "Unsupported type of constraint." + escapeJava( constrStringParts[ i ] );
throw new LoggedUserException( HttpStatus.BAD_REQUEST.value(), usermessage, internalmessage, log );
}

ShippingConstraint shippingConstraint= get( shippingId );

`
❌

----------------------------------------------------------------------------------------------------
Need to verify result with existing rule: Sample under double quatation

nks (li), maneuvers (mn), length (le), travelTime (tt), baseTime (bt), trafficTime (tm). Also supported: shape (sh), boundingBox (bb), turnbyturnmaneuvers (mm), none. Can be excluded in the response by putting a hyphen in the front. e.g. -mn. Also in RouteMatch mode legAttributes=mn is supported.")
@RequestParam(value="legAttributes"             , required=false) final String legAttributes,
@ApiParam(value = "Define optional attributes to be returned for each link. Defaults to shape (sh), length (le), remainTime (rt), remainDistance (rd), functionalClass (fc), warnings (wn), confidence (cd). Also supported: cost (co), maneuver (ma), timezone (tz), none. Can be excluded in the response by putting a hyphen in the front. e.g. -ma")
@RequestParam(value="linkAttributes"            , required=false) final String linkAttributes,
@ApiParam(hidden = true, value = "Identifier of a profile to learn and use speed characteristics. Profiles can be defined arbitrarily, e.g by driver, vehicle, departure time or a combination of them. Parameter is used to learn while route matching or to apply learnings while routing.")
@RequestParam(value="learnIdSpeed"				, required=false) final String learnIdSpeed,
@ApiParam(hidden = true, value = "Identifier of a profile to learn stop characteristics. Profiles can be defined arbitrarily, e.g by driver, vehicle, departure time or a combination of them. Parameter is used to learn while route matching. Cannot be used together with learnedStopsId.")
@RequestParam(value="learnStopsId"				, required=false) final String learnStopsId,
@ApiParam(hidden = true, value = "Identifier of a profile to use stop characteristics. Profiles can be defined arbitrarily, e.g by driver, vehicle, departure time or a combination of them. Parameter is to apply learnings while routing. Cannot be used together with learnStopsId.")
@RequestParam
`

✅

case "HISP_NH_PI": return "Hispanic or Latino: Native Hawaiian and Other Pacific Islander alone";
case "HISP_OTHER": return "Hispanic or Latino: Some other race alone";
case "HISP_TWO": return "Hispanic or Latino: Two or more races";
case "M_ALL": return "Total male population";
case "M_UNDER_5": return "Total male population under 5 years";
case "M_5_9": return "Total male population 5 to 9 years";
case "M_10_14": return "Total male population 10 to 14 years";

`
✅

Connection.commit();
jdbcConnection.getDatabaseConnection().setAutoCommit(bAutoCommit);
log.info(iNumFiles + " files inserted into TMP_JVSAR_FILES");
}
❌

@Override
public String getAttributeDescription(String columnName, String tableName) throws Exception
{
if (columnName == null)
return "Locations of 2D Junctions and 2D Signs with references to their SVG (Scalable Vector Graphics) files.<br/>" +
"Applications lookup the available formats for a Junction View, and therefrom create following 5 file paths:<br/>" +
"- The style sheet for the 2D Signs. Path = customcolors.css. For each map region there is only one sign style sheet, so it only has to be loaded once.<br>" +
"- The style sheet for the 2D Junctions. Path = BD/ASP/JV_STYLE.css, where BD is B (bird view) or D (driver view) and ASP is the aspect ratio, e.g. 5x3. For each map region there is only one sign style sheet (per bird/driver and aspect ratio), so it only has to be loaded once.<br>" +
"- The sky background. Path = BD/ASP/JV_SKY.svg. For each map region there is only one sky (per bird/driver and aspect ratio), so it only has to be loaded once.<br>" +
"- The 2D Junction. Path = BD/ASP/FILENAME, where filename is taken from the JV_FILE column, e.g. JV_TW_4711.svg<br/>" +
"- The 2D Sign. Path = ASP/FILENAME, where filename is taken from the SAR_FILE column, e.g. SR_TW_4711.svg<br/>" +
"Applications then load the files from the PDE Web service using the file resource.<br/>" +
"The style sheets and the sky are referenced within the junction/sign files, so applications must either create a matching file structure or embed them into the junction/sign files.<
`
✅
case "M_UNDER_5": return "Total male population under 5 years";
case "M_5_9": return "Total male population 5 to 9 years";
case "M_10_14": return "Total male population 10 to 14 years";
case "M_15_17": return "Total male population 15 to 17 years";
case "M_18_19": return "Total male population 18 and 19 years";
case "M_20": return "Total male population 20 years";
case "M_21": return "Total male population 21 years";

`
✅
----------------------------------------------------------------------------------------------------

Solution: Eliminate with static values
such as Regex: (SAMPLE)(\s)?=(\s)?([0-9])

//Bit values for payment methods
public static final int BIT_PAYMENT_METHOD_CASH = 1;
public static final int BIT_PAYMENT_METHOD_BANK_CARD = 2;
public static final int BIT_PAYMENT_METHOD_CREDIT_CARD = 4;
public static final int BIT_PAYMENT_METHOD_PASS_SUBSCRIPTION = 8;
public static final int BIT_PAYMENT_METHOD_TRANSPONDER = 16;
public static final int BIT_PAYMENT_METHOD_VIDEO_TOLL_CHARGE = 32;

`
❌

//String constants for payment methods
public static final String PAYMENT_METHOD_CASH = "CASH";
public static final String PAYMENT_METHOD_BANK_CARD = "BANK CARD";
public static final String PAYMENT_METHOD_CREDIT_CARD = "CREDIT CARD";
public static final String PAYMENT_METHOD_PASS_SUBSCRIPTION = "PASS/SUBSCRIPTION";
public static final String PAYMENT_METHOD_TRANSPONDER = "TRANSPONDER";
public static final String PAYMENT_METHOD_VIDEO_TOLL_CHARGE = "VIDEO TOLL CHARGE";

`
✅


private static final String NT_POI_ENTITIY_ID = "NT_POI_Entity_ID";
private static final String POI_ENTITIY_ID = "POI_Entity_ID";
private static final String POI_NAME = "POI_Name";
private static final String LINK_ID = "LinkID";
private static final String CATEGORY_ID = "Category_ID";
private static final String OPEN_24_HOURS = "Open_24_Hours";
private static final String PRIVATE_ACCESS = "Private_Access";

`
LinkID
✅


private static final String LONGITUDE = "Longitude";
private static final String SIDE_OF_STREET = "Side_of_Street";
private static final String PERCENT_FROM_REFNODE = "Percent_from_RefNode";
private static final String PAYMENT_METHOD = "PaymentMethod";

private static final String POI_TAG = "POI";
private static final String POI_XML_DELIVERY_PACKAGE_TAG = "DeliveryPackage";

`

❌

trian routing with public transport (multi modal)
* Matrix routing
* Permitted driving maneuvers (where u-turns are admin wide restricted)
**/
public class Router
{
private static final long[]       EMPTY_LONG_ARRAY   = new long[0];
public  static        boolean     DEBUG              = false;
private static final long         PENALTY_TRANSPORT_VERIFIED_ENTRY_MSEC   = 10 * 60 * 1000; // 10 minute cost penalty for entering a non-transport-verified road in a vehicle with measures specified
private static final double       PENALTY_TRANSPORT_VERIFIED_DRIVE_FACTOR = 0.5;            // ... and double link traversal cost
private static final String       licensePlateEnding                      = "LicensePlateEnding";
private static final String       licensePlate                            = "LicensePlate";

// input parameters


`


✅


----------------------------------------------------------------------------------------------------
Solution: Check why this populated


* */
public static Integer parseWeightToKg(String weight) throws NumberFormatException
{
double weightKg = 0;
weight = weight.trim(); // remove any spaces
if		(weight.endsWith("t"  )) weightKg = Double.parseDouble(weight.substring(0, weight.length() - 1)) * 1000.0;
else if	(weight.endsWith("kg" )) weightKg = Double.parseDouble(weight.substring(0, weight.length() - 2));

`
❌


String unit = restriction.get("unit");
String operator = restriction.get("operator");
double value = Double.parseDouble(restriction.get("value"));
double weightKg = 0;
String retrictionType = restriction.get("dimension");
if (unit != null && !unit.isEmpty() && !(unit.equalsIgnoreCase("t") || unit.equalsIgnoreCase("kg") || unit.equalsIgnoreCase("lbs")) )
throw new UserException("Feature: " + opId + ", unsupported unit '" + unit + "' for dimension " + retrictionType + ". Supported are 't', 'kg', 'lbs'.");
if (!operator.equalsIgnoreCase("GREATER")) throw new UserException("Feature: " + opId + ", unsupported operator: " + operator + ". Only support 'GREATER'");
if (unit == null) unit = ""; // To avoid NPE, compound restrictions from YMC data come without unit
if (unit.isEmpty()) {
if (Math.ab
`

❌
----------------------------------------------------------------------------------------------------
Remove same excerpt for same data-element:
Ref: Fleet Api : Cookies
