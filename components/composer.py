from typing import List
from .models import ThoughtTemplate

class TemplateComposer:
    def compose(self, templates: List[ThoughtTemplate], constraints: List[str]) -> str:
        # This component synthesizes a single meta-template from multiple retrieved sources.
        # It ensures that constraints from the distiller are integrated into the reasoning path.
        
        composed_steps = []
        for t in templates:
            composed_steps.extend(t.steps)
        
        # Deduplication of steps
        unique_steps = list(dict.fromkeys(composed_steps))
        
        # Integration of constraints
        final_structure = "Synthetic Reasoning Path:\n"
        for i, step in enumerate(unique_steps):
            final_structure += f"{i+1}. {step}\n"
        
        if constraints:
            final_structure += "Mandatory Constraints to Verify:\n"
            for c in constraints:
                final_structure += f"- {c}\n"
                
        return final_structure