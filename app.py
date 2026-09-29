import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def vygeneruj_graf():
    x = np.linspace(-10, 30, 1000)
    y = x ** 2

    plt.style.use("seaborn-v0_8-darkgrid")
    fig, ax = plt.subplots(figsize=(11, 7), dpi=140)

    fig.patch.set_facecolor("#0b1020")
    ax.set_facecolor("#111827")

    ax.plot(x, y, color="#38bdf8", linewidth=3)
    ax.fill_between(x, y, 0, where=y >= 0, color="#38bdf8", alpha=0.18)

    ax.set_title("Parabola: y = x²", fontsize=20, fontweight="bold",
                 color="#e2e8f0", pad=18)
    ax.set_xlabel("x", fontsize=12, color="#cbd5e1")
    ax.set_ylabel("y", fontsize=12, color="#cbd5e1")
    ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.45)

    ax.axhline(0, color="#94a3b8", linewidth=1)
    ax.axvline(0, color="#94a3b8", linewidth=1)

    ax.annotate(
        "Minimum",
        xy=(0, 0),
        xytext=(-5, 24),
        textcoords="offset points",
        color="#f8fafc",
        fontsize=11,
        arrowprops=dict(arrowstyle="->", lw=2, color="#f8fafc")
    )

    ax.set_xlim(-10, 30)
    ax.set_ylim(-10, 900)
    plt.tight_layout()

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "parabola.png"
    fig.savefig(output_path, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)

    print(f"\nGraf byl uložen do: {output_path}")


def main():
    print("=" * 60)
    print("        VÍTÁM TĚ V KRÁSNÉM PYTHON PROGRAMU")
    print("=" * 60)

    jmeno = input("Jak se jmenuješ? ").strip() or "příteli"
    print(f"\nAhoj, {jmeno}! Rád tě poznávám.")
    print("Teď ti vygeneruji krásný graf paraboly.")

    vygeneruj_graf()

    pocitani_matic()
    visualizace_matic()

    print("\nDěkuji, že jsi použil můj program. Doufám, že se ti líbil!")
    print("\nMěj se krásně! ✨")

def pocitani_matic():
    Matice_A = np.array([[1, 2], [3, 4]])
    Matice_B = np.array([[5, 6], [7, 8]])

    Soucin = Matice_A @ Matice_B
    print("Součin matic A a B je:") 
    print(Soucin)


def visualizace_matic():
   ctverec = np.array([[0, 1, 1, 0, 0],
                    [0, 0, 1, 1, 0]])
   

if __name__ == "__main__":
    main()
