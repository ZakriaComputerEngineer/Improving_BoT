from bot_engine import EnhancedBoTEngine

def main():
    engine = EnhancedBoTEngine()
    
    # Example hybrid query: requires mathematical and constraint logic
    query = "Solve 3x + 10 = 25, where x must be a prime factor of 30."
    
    engine.run(query)
    
    # Demonstrate Pruning logic
    pruned = engine.buffer_manager.prune_suboptimal(threshold=0.8)
    print(f"\n[Buffer Maintenance] Templates pruned: {pruned}")

if __name__ == "__main__":
    main()