
from datetime import timedelta

from feast import (
    Entity,
    FeatureView,
    FeatureService,
    Field,
    FileSource
)

from feast.types import Float32


# ==========================================
# 1. ENTITY
# ==========================================

student = Entity(
    name="student",

    join_keys=[
        "student_id"
    ],

    description="CSE graduate/student identified by Student ID"
)


# ==========================================
# 2. DATA SOURCE
# ==========================================

skillgap_source = FileSource(

    name="skillgap_source",

    path="data/skillgap_features.parquet",

    timestamp_field="event_timestamp"
)


# ==========================================
# 3. FEATURE VIEW
# ==========================================

skillgap_feature_view = FeatureView(

    name="skillgap_features",

    entities=[
        student
    ],

    ttl=timedelta(
        days=365
    ),

    schema=[

        # ----------------------------------
        # Student Skills
        # ----------------------------------

        Field(
            name="programming",
            dtype=Float32
        ),

        Field(
            name="database",
            dtype=Float32
        ),

        Field(
            name="problem_solving",
            dtype=Float32
        ),

        Field(
            name="communication",
            dtype=Float32
        ),

        Field(
            name="cloud_computing",
            dtype=Float32
        ),

        Field(
            name="teamwork",
            dtype=Float32
        ),

        Field(
            name="aptitude",
            dtype=Float32
        ),


        # ----------------------------------
        # Industry Requirements
        # ----------------------------------

        Field(
            name="industry_programming_requirement",
            dtype=Float32
        ),

        Field(
            name="industry_database_requirement",
            dtype=Float32
        ),

        Field(
            name="industry_problem_solving_requirement",
            dtype=Float32
        ),

        Field(
            name="industry_communication_requirement",
            dtype=Float32
        ),

        Field(
            name="industry_cloud_computing_requirement",
            dtype=Float32
        ),

        Field(
            name="industry_teamwork_requirement",
            dtype=Float32
        ),

        Field(
            name="industry_aptitude_requirement",
            dtype=Float32
        ),


        # ----------------------------------
        # Individual Skill Gaps
        # ----------------------------------

        Field(
            name="programming_gap",
            dtype=Float32
        ),

        Field(
            name="database_gap",
            dtype=Float32
        ),

        Field(
            name="problem_solving_gap",
            dtype=Float32
        ),

        Field(
            name="communication_gap",
            dtype=Float32
        ),

        Field(
            name="cloud_computing_gap",
            dtype=Float32
        ),

        Field(
            name="teamwork_gap",
            dtype=Float32
        ),

        Field(
            name="aptitude_gap",
            dtype=Float32
        ),


        # ----------------------------------
        # Engineered Features
        # ----------------------------------

        Field(
            name="technical_skill_avg",
            dtype=Float32
        ),

        Field(
            name="industry_requirement_avg",
            dtype=Float32
        ),

        Field(
            name="calculated_skill_gap",
            dtype=Float32
        ),

        Field(
            name="requirement_difference",
            dtype=Float32
        )
    ],

    source=skillgap_source,

    online=True
)


# ==========================================
# 4. FEATURE SERVICE
# ==========================================

skillgap_prediction_service = FeatureService(

    name="skillgap_prediction_service",

    features=[
        skillgap_feature_view
    ]
)
