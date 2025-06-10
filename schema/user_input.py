#pydantic model to validate incoming data
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities


class UserInput(BaseModel):
    age: Annotated[int, Field(..., ge=0, le=120, description="Age of the user")]
    weight: Annotated[float, Field(..., ge=0, description="Weight of the user in kg")]
    height: Annotated[float, Field(..., ge=0, lt=2.5, description="Height of the user in meters")]
    income_lpa: Annotated[float, Field(..., ge=0, description="Income of the user in lakhs per annum")] 
    smoker: Annotated[bool, Field(..., description="Is the user a smoker?")]
    city: Annotated[str, Field(..., description="City of the user")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]

    @field_validator('city')   #It validates the city field. Now if user input city in any case, it will be normalized to title case.
    @classmethod
    def normalize_city(cls, v: str) -> str:
        """Normalize city name to title case."""
        return v.strip().title()

    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate BMI from weight and height."""
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        """Determine lifestyle risk based on occupation."""
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        """Determine age group."""
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle-aged"
        else:
            return "senior"
        
    @computed_field
    @property
    def city_tier(self) -> str:
        """Determine city tier based on city name."""
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3