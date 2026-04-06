import sys
import os
import tkinter as tk
from tkinter import messagebox
import hashlib
from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39Languages,
    Bip39SeedGenerator,
    Bip44,
    Bip44Coins,
    Bip44Changes
)

# ==========================================
# STATIC APP STATE (FOR STANDALONE EXECUTION)
# ==========================================
class AppState:
    def __init__(self):
        self.SML_ver = "SecretML-Seed v1.0.0 (Open Source Edition)"
        self.root = None
        
        # File info
        self.source_file_path = "dummy_vault.psq"
        self.source_file_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        self.psq_available = True
        
        # Keys
        self.ver_final_key = "v1.0"
        self.final_key = "1234567890"  # Static mock key for PSQ mode
        
        # Mock Questions & Answers
        self.questions = [
            ("q1", "Question 1"),
            ("q2", "Question 2"),
            ("q3", "Question 3"),
            ("q4", "Question 4"),
            ("q5", "Question 5")
        ]
        self.answers = [
            "Answer 1", 
            "Answer 2", 
            "Answer 3", 
            "Answer 4", 
            "Answer 5"
        ]

app_state = AppState()
WINDOW_TITLE = app_state.SML_ver


# ==========================================
# UTILITY FUNCTIONS
# ==========================================
def center_window(root, width, height):
    """Centers the window on the screen."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

def resource_path(relative_path):
    """Gets absolute path to resource, works for dev and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# ==========================================
# UI: PROMPTS AND WINDOWS
# ==========================================
def prompt_seed_generation():
    """Asks the user whether to display the generated seed phrases."""
    result = messagebox.askyesno(
        "Warning",
        "Seed phrase generation is enabled in settings. Show the generated seed phrase?"
    )
    if result:
        show_seed_window()
    else:
        print("User cancelled seed phrase generation prompt.")

def show_seed_window(mode="12"):
    """Displays the main window with the generated seed phrase."""
    root = app_state.root

    dialog = tk.Toplevel(root)
    dialog.withdraw()
    dialog.title(f"SecretML-Seed ({mode} words)")
    dialog.geometry("600x420")

    try:
        dialog.iconbitmap(resource_path("assets/icon.ico"))
    except:
        pass  # Ignore if icon is not found

    center_window(dialog, 600, 420)

    frame = tk.Frame(dialog)
    frame.pack(expand=True, fill="both", padx=10, pady=5)

    # --- PSQ Validation ---
    source_path = getattr(app_state, "source_file_path", "")
    psq_available = source_path.lower().endswith(".psq")
    if psq_available:
        app_state.psq_available = True
    psq_available = getattr(app_state, "psq_available", False)

    version = getattr(app_state, "ver_final_key", None)
    version_label = f" ({version})" if version else ""

    # --- Mode Selection ---
    if mode == "12":
        seed_words = generate_12_word_seed(app_state)
    elif mode == "24":
        seed_words = generate_24_word_seed(app_state)
    elif mode == "psq" and psq_available:
        seed_words = generate_24_word_seed_psq(app_state)
    else:
        seed_words = generate_12_word_seed(app_state)

    mnemonic_phrase = " ".join(seed_words)

    # --- ETH Address Generation ---
    try:
        seed_bytes = Bip39SeedGenerator(
            mnemonic_phrase,
            lang=Bip39Languages.ENGLISH
        ).Generate()

        bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
        bip44_acc = (
            bip44_mst.Purpose()
            .Coin()
            .Account(0)
            .Change(Bip44Changes.CHAIN_EXT)
            .AddressIndex(0)
        )

        eth_address = bip44_acc.PublicKey().ToAddress()
        
    except Exception as e:
        eth_address = f"Error generating address: {e}"

    # --- Header Labels ---
    tk.Label(
        frame,
        text=f"ETH address: {eth_address}",
        font=("Arial", 9, "bold"),
        fg="#1a73e8",
        wraplength=580,
        justify="center"
    ).pack()

    tk.Label(
        frame,
        text="BIP39 SEED (m/44'/60'/0'/0/0)",
        font=("Arial", 9, "italic"),
        fg="#555555",
        pady=2,
        justify="center"
    ).pack()

    # --- Word Grid ---
    words_frame = tk.Frame(frame)
    words_frame.pack(expand=True)

    if mode == "12":
        col_count = 2
        row_size = 6
    else:
        col_count = 3
        row_size = 8

    for i, word in enumerate(seed_words):
        row = i % row_size
        col = i // row_size

        tk.Label(
            words_frame,
            text=f"{i+1}. {word}",
            font=("Arial", 12),
            anchor="center"
        ).grid(row=row, column=col, padx=20, pady=2, sticky="nsew")

    for c in range(col_count):
        words_frame.grid_columnconfigure(c, weight=1)

    # --- Mode Flow Handlers ---
    def get_next_mode(current_mode):
        order = ["12", "24", "psq"] if psq_available else ["12", "24"]
        idx = order.index(current_mode)
        return order[(idx + 1) % len(order)]

    def get_button_text(current_mode):
        if current_mode == "12":
            return "Switch to 24 words"
        if current_mode == "24":
            return f"Switch to PSQ{version_label}" if psq_available else "Switch to 12 words"
        if current_mode == "psq":
            return "Switch to 12 words"
        return "Switch"

    def switch_mode():
        dialog.destroy()
        show_seed_window(get_next_mode(mode))

    # --- Bottom Buttons ---
    btn_frame = tk.Frame(frame)
    btn_frame.pack(side="bottom", pady=8)

    tk.Button(
        btn_frame,
        text=get_button_text(mode),
        font=("Arial", 10),
        command=switch_mode
    ).pack(side="left", padx=5)

    tk.Button(
        btn_frame,
        text="Close",
        font=("Arial", 10),
        command=dialog.destroy
    ).pack(side="right", padx=5)

    dialog.deiconify()
    dialog.grab_set()
    dialog.focus_set()


# ==========================================
# CRYPTOGRAPHY & SEED GENERATION
# ==========================================
def generate_12_word_seed(state):
    """Generates a 12-word seed using Q&A and file hash entropy."""
    base = "".join(
        f"{q_text}{answer}" 
        for (_, q_text), answer in zip(state.questions, state.answers)
    )
    base += getattr(state, "source_file_hash", "")
    base += "OPENSOURCE_SALT_12"  # Replaced confidential data with generic salt

    entropy = hashlib.sha256(base.encode("utf-8")).digest()[:16]  # 128 bit for 12 words
    mnemonic = Bip39MnemonicGenerator().FromEntropy(entropy)
    return mnemonic.ToStr().split(" ")


def generate_24_word_seed(state):
    """Generates a 24-word seed using Q&A and file hash entropy."""
    base = "".join(
        f"{q_text}{answer}" 
        for (_, q_text), answer in zip(state.questions, state.answers)
    )
    base += getattr(state, "source_file_hash", "")
    base += "OPENSOURCE_SALT_24"  # Replaced confidential data with generic salt

    entropy = hashlib.sha256(base.encode("utf-8")).digest()  # 256 bit for 24 words
    mnemonic = Bip39MnemonicGenerator().FromEntropy(entropy)
    return mnemonic.ToStr().split(" ")


def generate_24_word_seed_psq(state):
    """Generates a 24-word seed derived directly from the PSQ final key."""
    final_key = getattr(state, "final_key", None)

    if not final_key:
        raise ValueError("final_key not available")

    if isinstance(final_key, bytes):
        entropy = final_key[:32]
    else:
        entropy = hashlib.sha256(str(final_key).encode("utf-8")).digest()

    mnemonic = Bip39MnemonicGenerator().FromEntropy(entropy)
    return mnemonic.ToStr().split(" ")


# ==========================================
# ENTRY POINT
# ==========================================
if __name__ == "__main__":
    # Initialize the invisible root Tkinter window
    app_state.root = tk.Tk()
    app_state.root.withdraw()
    
    # Start the application flow
    prompt_seed_generation()
    
    # Run the event loop
    app_state.root.mainloop()
