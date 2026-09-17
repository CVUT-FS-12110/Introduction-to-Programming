# --- Bug 1: Mutable default argument ---

def add_to_cart_buggy(item: str, cart: list = []) -> list:
    cart.append(item)
    return cart


def add_to_cart(item: str, cart: list | None = None) -> list:
    if cart is None:
        cart = []
    cart.append(item)
    return cart


# --- Bug 2: Unintentional mutation of an argument ---

def get_top_scores_buggy(scores: list[int], n: int) -> list[int]:
    scores.sort(reverse=True)  # Modifies the caller's list!
    return scores[:n]


def get_top_scores(scores: list[int], n: int) -> list[int]:
    return sorted(scores, reverse=True)[:n]


if __name__ == "__main__":
    print("=== Bug 1: Mutable default argument ===")
    cart_a = add_to_cart_buggy("apple")
    cart_b = add_to_cart_buggy("banana")  # Expects a fresh cart
    print("Cart A:", cart_a)   # ['apple', 'banana'] - unexpected!
    print("Cart B:", cart_b)   # ['apple', 'banana'] - same object!
    print("Same object?", cart_a is cart_b)

    print()
    print("=== Fix 1: Use None as default ===")
    cart_c = add_to_cart("apple")
    cart_d = add_to_cart("banana")
    print("Cart C:", cart_c)   # ['apple']
    print("Cart D:", cart_d)   # ['banana']

    print()
    print("=== Bug 2: Unintentional argument mutation ===")
    results = [55, 90, 72, 88, 61]
    top = get_top_scores_buggy(results, 3)
    print("Top 3:", top)
    print("Original after call:", results)  # Sorted! Original was changed.

    print()
    print("=== Fix 2: Work on a copy ===")
    results = [55, 90, 72, 88, 61]
    top = get_top_scores(results, 3)
    print("Top 3:", top)
    print("Original after call:", results)  # Unchanged
