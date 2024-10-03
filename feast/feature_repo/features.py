from datetime import timedelta
from feast import (Entity, FeatureView, RedshiftSource)
from feast.types import Int64, String
from feast.field import Field

# Define the Entity
zipcode = Entity(name="zipcode", join_keys=["zipcode"])

# Define the Redshift source for zipcode features
zipcode_source = RedshiftSource(
    query="SELECT * FROM spectrum.zipcode_features",
    table="zipcode_features",
    created_timestamp_column="created_timestamp",
)

# Define the FeatureView for zipcode features
zipcode_features = FeatureView(
    name="zipcode_features",
    entities=[zipcode],
    ttl=timedelta(days=3650),
    schema=[
        Field(name="city", dtype=String),
        Field(name="state", dtype=String),
        Field(name="location_type", dtype=String),
        Field(name="tax_returns_filed", dtype=Int64),
        Field(name="population", dtype=Int64),
        Field(name="total_wages", dtype=Int64),
    ],
    source=zipcode_source,
)

# Define the Entity for dob_ssn
dob_ssn = Entity(
    name="dob_ssn",
    join_keys=["dob_ssn"],
    description="Date of birth and last four digits of social security number",
)

# Define the Redshift source for credit history features
credit_history_source = RedshiftSource(
    query="SELECT * FROM spectrum.credit_history",
    table="credit_history",  # Correct the table name
    created_timestamp_column="created_timestamp",
)

# Define the FeatureView for credit history
credit_history = FeatureView(
    name="credit_history",
    entities=[dob_ssn],
    ttl=timedelta(days=90),
    schema=[
        Field(name="credit_card_due", dtype=Int64),
        Field(name="mortgage_due", dtype=Int64),
        Field(name="student_loan_due", dtype=Int64),
        Field(name="vehicle_loan_due", dtype=Int64),
        Field(name="hard_pulls", dtype=Int64),
        Field(name="missed_payments_2y", dtype=Int64),
        Field(name="missed_payments_1y", dtype=Int64),
        Field(name="missed_payments_6m", dtype=Int64),
        Field(name="bankruptcies", dtype=Int64),
    ],
    source=credit_history_source,
)


# from datetime import timedelta

# from feast import (Entity, Feature, FeatureView, RedshiftSource,
#                    ValueType)
# from feast.infra.offline_stores.file_source import FileSource
# zipcode = Entity(name="zipcode", value_type=ValueType.INT64)

# zipcode_source = RedshiftSource(
#     query="SELECT * FROM spectrum.zipcode_features",
#     table="zipcode_features",
#     # event_timestamp_column="event_timestamp",
#     created_timestamp_column="created_timestamp",
# )

# zipcode_features = FeatureView(
#     name="zipcode_features",
#     entities=["zipcode"],
#     ttl=timedelta(days=3650),
#     features=[
#         Feature(name="city", dtype=ValueType.STRING),
#         Feature(name="state", dtype=ValueType.STRING),
#         Feature(name="location_type", dtype=ValueType.STRING),
#         Feature(name="tax_returns_filed", dtype=ValueType.INT64),
#         Feature(name="population", dtype=ValueType.INT64),
#         Feature(name="total_wages", dtype=ValueType.INT64),
#     ],
#     batch_source=zipcode_source,
# )

# dob_ssn = Entity(
#     name="dob_ssn",
#     value_type=ValueType.STRING,
#     description="Date of birth and last four digits of social security number",
# )

# credit_history_source = RedshiftSource(
#     query="SELECT * FROM spectrum.credit_history",
#     # event_timestamp_column="event_timestamp",
#     table="zipcode_features",
#     created_timestamp_column="created_timestamp",
# )

# credit_history = FeatureView(
#     name="credit_history",
#     entities=["dob_ssn"],
#     ttl=timedelta(days=90),
#     features=[
#         Feature(name="credit_card_due", dtype=ValueType.INT64),
#         Feature(name="mortgage_due", dtype=ValueType.INT64),
#         Feature(name="student_loan_due", dtype=ValueType.INT64),
#         Feature(name="vehicle_loan_due", dtype=ValueType.INT64),
#         Feature(name="hard_pulls", dtype=ValueType.INT64),
#         Feature(name="missed_payments_2y", dtype=ValueType.INT64),
#         Feature(name="missed_payments_1y", dtype=ValueType.INT64),
#         Feature(name="missed_payments_6m", dtype=ValueType.INT64),
#         Feature(name="bankruptcies", dtype=ValueType.INT64),
#     ],
#     batch_source=credit_history_source,
# )
