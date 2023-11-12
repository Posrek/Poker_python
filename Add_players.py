def players(n):
    if n > 8:
        print("Error: Too many players. Maximum allowed is 8.")
        return None
    return {f'P{i}': [] for i in range(1, n + 1)}