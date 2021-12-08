CREATE TABLE petl1.AnnualTicketSales (
	YEAR text,
	TICKETS_SOLD text,
	TOTAL_BOX_OFFICE text,
	TOTAL_INFLATION_ADJUSTED_BOX_OFFICE text,
	AVERAGE_TICKET_PRICE text
);

CREATE TABLE petl1.HighestGrossers (
	YEAR text,
	MOVIE text,
	GENRE text,
	MPAA_RATING text,
	DISTRIBUTOR text,
	TOTAL_FOR_YEAR text,
	TOTAL_IN_2019_DOLLARS text,
	TICKETS_SOLD text
);

CREATE TABLE petl1.PopularCreativeTypes (
	RANK text,
	CREATIVE_TYPES text,
	MOVIES text,
	TOTAL_GROSS text,
	AVERAGE_GROSS text,
	MARKET_SHARE text
);

CREATE TABLE petl1.TopDistributors (
	RANK text,
	DISTRIBUTORS text,
	MOVIES text,
	TOTAL_GROSS text,
	AVERAGE_GROSS text,
	MARKET_SHARE text
);

CREATE TABLE petl1.TopGenres (
	RANK text,
	GENRES text,
	MOVIES text,
	TOTAL_GROSS text,
	AVERAGE_GROSS text,
	MARKET_SHARE text
);

CREATE TABLE petl1.TopGrossingRatings (
	RANK text,
	MPAA_RATINGS text,
	MOVIES text,
	TOTAL_GROSS text,
	AVERAGE_GROSS text,
	MARKET_SHARE text
);

CREATE TABLE petl1.TopGrossingSources (
	RANK text,
	SOURCES text,
	MOVIES text,
	TOTAL_GROSS text,
	AVERAGE_GROSS text,
	MARKET_SHARE text
);

CREATE TABLE petl1.TopProductionMethods (
	RANK text,
	PRODUCTION_METHODS text,
	MOVIES text,
	TOTAL_GROSS text,
	AVERAGE_GROSS text,
	MARKET_SHARE text
);

CREATE TABLE petl1.WideReleasesCount (
	YEAR text,
	WARNER_BROS text,
	WALT_DISNEY text,
	TWENTIETH_CENTURY_FOX text,
	PARAMOUNT_PICTURES text,
	SONY_PICTURES text,
	UNIVERSAL text,
	TOTAL_MAJOR_6 text,
	TOTAL_OTHER_STUDIOS text
);