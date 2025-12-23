import numpy as np
from typing import List
from .models import ThoughtTemplate

class GovernanceBufferManager:
    def __init__(self):
        self.templates: List[ThoughtTemplate] = []

    def add_template(self, template: ThoughtTemplate):
        self.templates.append(template)

    def retrieve_top_k(self, distilled_query: dict, k: int = 2) -> List[ThoughtTemplate]:
        # Simulated semantic similarity scoring
        # In production, use cosine similarity on embeddings: Similarity(f(xd), f(DTi))
        scored_templates = []
        query_text = distilled_query["query"].lower()
        
        for t in self.templates:
            score = 0.0
            if t.category in query_text or any(step.lower() in query_text for step in t.steps):
                score += 0.5
            
            # Incorporate Fitness Score into retrieval logic
            effective_score = score * t.fitness_score
            scored_templates.append((t, effective_score))
        
        scored_templates.sort(key=lambda x: x[1], reverse=True)
        return [t[0] for t in scored_templates[:k]]

    def update_template_fitness(self, template_id: str, success: bool):
        for t in self.templates:
            if t.template_id == template_id:
                adjustment = 0.1 if success else -0.3
                t.fitness_score = max(0.1, min(2.0, t.fitness_score + adjustment))

    def prune_suboptimal(self, threshold: float = 0.5):
        initial_count = len(self.templates)
        self.templates = [t for t in self.templates if t.fitness_score >= threshold]
        return initial_count - len(self.templates)