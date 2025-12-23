class ProblemDistiller:
    def distill(self, raw_query: str) -> dict:
        # In a production environment, this would call an LLM to extract variables and constraints.
        # This PoC uses a simplified extraction logic.
        distilled = {
            "query": raw_query,
            "constraints": self._extract_constraints(raw_query),
            "logic_type": self._classify_logic(raw_query)
        }
        return distilled

    def _extract_constraints(self, text: str) -> List[str]:
        constraints = []
        if "prime" in text.lower():
            constraints.append("Result must be a prime number")
        if "factor" in text.lower():
            constraints.append("Result must be a factor of a specific value")
        return constraints

    def _classify_logic(self, text: str) -> str:
        if any(kw in text.lower() for kw in ["solve", "x =", "equation"]):
            return "mathematical"
        return "general"