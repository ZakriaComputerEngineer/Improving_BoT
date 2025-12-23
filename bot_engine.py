from components.distiller import ProblemDistiller
from components.buffer_manager import GovernanceBufferManager
from components.composer import TemplateComposer
from components.models import ThoughtTemplate

class EnhancedBoTEngine:
    def __init__(self):
        self.distiller = ProblemDistiller()
        self.buffer_manager = GovernanceBufferManager()
        self.composer = TemplateComposer()
        self._seed_buffer()

    def _seed_buffer(self):
        self.buffer_manager.add_template(ThoughtTemplate(
            "math_core", "Algebraic equation solving", 
            ["Identify variables", "Isolate variable", "Verify solution"], "mathematical"
        ))
        self.buffer_manager.add_template(ThoughtTemplate(
            "constraint_logic", "Conditional constraint satisfaction", 
            ["Identify rules", "Check mutual exclusivity", "Verify boundaries"], "logic"
        ))

    def run(self, query: str):
        # 1. Distillation
        distilled = self.distiller.distill(query)
        
        # 2. Multi-Head Retrieval
        top_templates = self.buffer_manager.retrieve_top_k(distilled, k=2)
        
        # 3. Dynamic Composition
        synthetic_template = self.composer.compose(top_templates, distilled["constraints"])
        
        # 4. Final Reasoner (Simulated LLM call)
        print(f"Executing reasoning for query: {query}")
        print("-" * 30)
        print(synthetic_template)
        
        # 5. Feedback Loop (Simulated success)
        success = True 
        for t in top_templates:
            self.buffer_manager.update_template_fitness(t.template_id, success)