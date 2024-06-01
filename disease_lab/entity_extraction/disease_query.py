from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI

SYSTEM_PROMPT = """
You are an expert disease entity extractor.
Given a sentence, you need to extract the disease entities from it.
Please report only Diseases. Do not report any other entities like Genes, Proteins, Enzymes etc.
"""

aclient = instructor.patch(AsyncOpenAI())

class DiseaseList(BaseModel):
    """
    Holds the list of extracted diseases from a query.
    diseases: List of extracted entities
    """
    diseases: List[str] = Field(description="List of extracted entities")
    def report(self):
        dct = self.model_dump()
        dct["usage"] = self._raw_response.usage.model_dump()
        return dct

async def expand_disease_query(
    q, *, model: str = "gpt-4-turbo", temp: float = 0
) -> DiseaseList:
    """Expand a disease query using the specified model."""
    return await aclient.chat.completions.create(
        model=model,
        temperature=temp,
        response_mode=DiseaseList,
        messages=[
            {
                "role": "system", "content": SYSTEM_PROMPT,
            },
            {"role": "user", "content": q},
        ]
    )
