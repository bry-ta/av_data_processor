from math import nan, isnan
from typing import Any, Annotated, Optional, TypeVar
from datetime import datetime
from data_models.sf311.fields import *
from pydantic import BaseModel, HttpUrl, Field, computed_field
from pydantic_extra_types.coordinate import Coordinate
from pydantic.functional_validators import AfterValidator, BeforeValidator
from utils.helpers import primary_type_or_na_or_redacted, primary_type_or_redacted, coerce_nan_to_none, compare_if_numeric, coerce_nan_to, coerce_str_to_number, numeric_str_to_float
from utils.regex import numeric_re, redacted_re, na_re, missing_field_re, not_provided_re

class Cases(BaseModel):
    case_id: int = Field(alias='CaseID') # str = Field(alias='CaseID', pattern='\d+')
    opened: datetime = Field(alias='Opened')
    closed: Annotated[datetime | str, AfterValidator(lambda x: primary_type_or_na_or_redacted(x, datetime)), Field(alias='Closed')]
    updated: datetime = Field(alias='Updated')
    status: str = Field(alias='Status')
    status_note: str = Field(alias='Status Notes')
    responsible_agency: str = Field(alias='Responsible Agency')
    category: str = Field(alias='Category')
    request_type: str = Field(alias='Request Type')
    request_details: str = Field(alias='Request Details')
    address:str = Field(alias='Address')
    street_address: str = Field(alias='Street Address')
    supervisor_district: int = Field(alias='Supervisor District')
    neighborhood: str = Field(alias='Neighborhood')
    analysis_neighborhood: str = Field(alias='Analysis Neighborhood')
    police_district: str = Field(alias='Police District')
    latitude: float = Field(alias='Latitude')
    longitude: float = Field(alias='Longitude')
    point: Coordinate = Field(alias='point_geom')
    source: str = Field(alias='Source')
    media_url: HttpUrl = Field(alias='Media URL')
    bos_2012: int = Field(alias='BOS_2012')
    data_as_of: datetime = Field(alias='data_as_of')
    data_loaded_at: datetime = Field(alias='data_loaded_at')
