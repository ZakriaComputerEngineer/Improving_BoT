from typing import List

class ThoughtTemplate:
    def __init__(self, template_id: str, description: str, steps: List[str], category: str):
        self.template_id = template_id
        self.description = description
        self.steps = steps
        self.category = category
        self.fitness_score = 1.0
        self.usage_history = []

    def to_prompt(self) -> str:
        return "\n".join([f"Step {i+1}: {step}" for i, step in enumerate(self.steps)])