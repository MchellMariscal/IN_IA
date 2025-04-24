import random

def sample_cloudy():
    return random.random() < 0.5

def sample_sprinkler(cloudy):
    if cloudy:
        return random.random() < 0.1
    else:
        return random.random() < 0.5

def wetgrass_prob(sprinkler):
    return 0.9 if sprinkler else 0.2

def likelihood_weighting(n_samples=10000, evidence={'WetGrass': True}):
    weighted_samples = []

    for _ in range(n_samples):
        sample = {}
        weight = 1.0

        # 1. Sample Cloudy
        cloudy = sample_cloudy()
        sample['Cloudy'] = cloudy

        # 2. Sample Sprinkler given Cloudy
        sprinkler = sample_sprinkler(cloudy)
        sample['Sprinkler'] = sprinkler

        # 3. Don't sample WetGrass, just weight it
        wet_prob = wetgrass_prob(sprinkler)
        weight *= wet_prob if evidence['WetGrass'] else (1 - wet_prob)

        weighted_samples.append((sample, weight))

    # 4. Estimate P(Cloudy=True | WetGrass=True)
    cloudy_true = sum(weight for (s, weight) in weighted_samples if s['Cloudy'])
    total_weight = sum(weight for (_, weight) in weighted_samples)

    return cloudy_true / total_weight

# Ejecutar
resultado = likelihood_weighting()
print(f"P(Cloudy=True | WetGrass=True) ≈ {resultado:.4f}")
