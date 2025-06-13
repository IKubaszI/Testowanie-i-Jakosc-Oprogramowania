import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, Toplevel, ttk
import tkinter.font as tkFont
import os
import re
from modules.gemini_client import GeminiClient
from PIL import Image, ImageTk

LAST_RESPONSE_PATH = os.path.join('config', 'last_response.txt')
HISTORY_PATH = os.path.join('config', 'history.txt')

client = GeminiClient()
history_list = []
last_ai_response = "" 

LIGHT_COLORS = {
    "bg": "#f5f7fa",
    "fg": "#373737",
    "code_bg": "#fafeff",
    "code_fg": "#2d3436",
    "resp_bg": "#f9f6ec",
    "resp_fg": "#373737",
    "highlight": "#e7eaf3",
    "codeblock_bg": "#f4f4f4"
}
DARK_COLORS = {
    "bg": "#22272e",
    "fg": "#d3d3d3",
    "code_bg": "#1e1e1e",
    "code_fg": "#f8f8f2",
    "resp_bg": "#25272d",
    "resp_fg": "#d3d3d3",
    "highlight": "#444c56",
    "codeblock_bg": "#999709"
}
UI_MODE = "light"

def get_colors():
    """Zwraca bieżący słownik kolorów dla aktywnego trybu."""
    return DARK_COLORS if UI_MODE == "dark" else LIGHT_COLORS


def apply_styles(root: tk.Tk) -> None:
    style = ttk.Style(root)
    style.theme_use("clam")
    c = get_colors()
    style.configure("TFrame", background=c["bg"])
    style.configure("TLabel", background=c["bg"], foreground=c["fg"], font=("Segoe UI", 11))
    style.configure("Header.TLabel", font=("Segoe UI", 18, "bold"), foreground="#345")
    style.configure("Section.TLabelframe", background=c["highlight"], borderwidth=2, relief="groove")
    style.configure("Section.TLabelframe.Label", font=("Segoe UI", 12, "bold"))
    style.configure("Accent.TButton", font=("Segoe UI", 11, "bold"), foreground="white", background="#4f8cff")
    style.map("Accent.TButton", background=[("active", "#367ce4")])
    style.configure("Danger.TButton", font=("Segoe UI", 11), foreground="white", background="#e46c6c")
    style.map("Danger.TButton", background=[("active", "#c44545")])
    style.configure("TButton", font=("Segoe UI", 10), padding=4)
def show_intro_popup():
    intro = tk.Toplevel()
    intro.title("Witaj!")
    intro.geometry("460x400")
    intro.resizable(False, False)
    intro.configure(bg="#fdfdfd")
    intro.attributes("-topmost", True)
    gif_path = "assets/kotek.gif"
    frames = []

    try:
        img = Image.open(gif_path)
        while True:
            frame = ImageTk.PhotoImage(img.copy().convert("RGBA"))
            frames.append(frame)
            img.seek(len(frames)) 
    except EOFError:
        pass 
    except Exception as e:
        print(f"Nie udało się załadować GIF-a: {e}")

    if not frames:
        label = tk.Label(intro, text="(brak kotka)", bg="#fdfdfd")
        label.pack(pady=(10, 0))
    else:
        label = tk.Label(intro, bg="#fdfdfd")
        label.pack(pady=(10, 0))

        def animate(idx=0):
            label.configure(image=frames[idx])
            intro.after(100, animate, (idx + 1) % len(frames))

        animate()

    info = (
        "\U0001F408 Hej! Jestem pomocnym czatem AI \U0001F408\n\n"
        "Potrafię dla Ciebie:\n"
        "• Analizować kod\n"
        "• Wykrywać błędy i naruszenia SOLID\n"
        "• Proponować poprawki\n"
        "• Generować testy jednostkowe\n"
        "• Tworzyć przypadki testowe\n"
        "• Pomagać dokumentować testy\n"
        "•I wiele Wiecej :) Śmiało przetestuj mnie."
    )

    msg = tk.Label(intro, text=info, bg="#fdfdfd", fg="#333", justify="left",
                   font=("Segoe UI", 11))
    msg.pack(padx=20, pady=(5, 10))

    ttk.Button(intro, text="OK", command=intro.destroy).pack(pady=(0, 16))
    intro.transient()
    intro.grab_set()
    intro.wait_window()



def format_ai_response_widget(widget: tk.Text, text: str) -> None:
    widget.config(state="normal")
    widget.delete("1.0", tk.END)

    colors = get_colors()
    widget.tag_configure("bold", font=("Segoe UI", 13, "bold"))
    widget.tag_configure("italic", font=("Segoe UI", 13, "italic"))
    widget.tag_configure("codeblock", font=("Consolas", 11),
                         background=colors["codeblock_bg"], foreground=colors["code_fg"],
                         lmargin1=10, lmargin2=10, spacing1=4, spacing3=4)
    widget.tag_configure("heading", font=("Segoe UI", 14, "bold"))
    widget.tag_configure("bullet", lmargin1=20, lmargin2=30, font=("Segoe UI", 13))
    widget.tag_configure("normal", font=("Segoe UI", 13))

    code_re = re.compile(r"```(.*?)```", re.DOTALL)
    pos = 0
    for m in code_re.finditer(text):
        insert_markdown_fragment(widget, text[pos:m.start()])
        widget.insert(tk.END, m.group(1).strip() + "\n", "codeblock")
        pos = m.end()

    insert_markdown_fragment(widget, text[pos:])
    widget.config(state="disabled")

def update_theme():
    colors = get_colors()
    root.configure(bg=colors["bg"])
    code_text.config(bg=colors["code_bg"], fg=colors["code_fg"],
                     insertbackground=colors["fg"])
    response_text.config(bg=colors["resp_bg"], fg=colors["resp_fg"],
                         insertbackground=colors["fg"])
    apply_styles(root)


def toggle_ui_mode():
    global UI_MODE
    UI_MODE = "dark" if UI_MODE == "light" else "light"
    update_theme()


def save_last_response(response: str):
    with open(LAST_RESPONSE_PATH, 'w', encoding='utf-8') as f:
        f.write(response)


def load_last_response() -> str:
    if os.path.exists(LAST_RESPONSE_PATH):
        with open(LAST_RESPONSE_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


def save_history():
    with open(HISTORY_PATH, 'w', encoding='utf-8') as f:
        for idx, entry in enumerate(history_list, 1):
            f.write(f"[{idx}]\nKod:\n{entry['code']}\nOdpowiedź:\n{entry['response']}\n{'-'*40}\n")


def load_history():
    loaded = []
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r', encoding='utf-8') as f:
            content = f.read().split('----------------------------------------\n')
            for block in content:
                if block.strip():
                    try:
                        code = block.split("Kod:\n")[1].split("\nOdpowiedź:\n")[0]
                        response = block.split("\nOdpowiedź:\n")[1].strip()
                        loaded.append({"code": code, "response": response})
                    except Exception:
                        continue
    return loaded


def send_query():
    code = code_text.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Brak kodu", "Wklej lub napisz kod do analizy!")
        return

    response_text.config(state='normal')
    response_text.delete("1.0", tk.END)
    response_text.config(state='disabled')

    prompt = client.tune or client.config.get('default_tune', '')

    if generate_code_only.get():
        prompt += (
            "\n\nZwróć odpowiedź tylko jako kod (bez żadnych komentarzy, opisów, tekstu przed kodem ani po kodzie). "
            "Jeśli to możliwe, daj pełny blok kodu gotowy do użycia."
        )
    prompt += f"\n\nKod do analizy:\n{code}"

    response = client.generate_response(prompt, "user")

    global last_ai_response
    last_ai_response = response

    format_ai_response_widget(response_text, response)

    save_last_response(response)
    history_list.append({"code": code, "response": response})
    save_history()


def clear_history():
    if not messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz wyczyścić historię?"):
        return
    global history_list
    history_list = []
    save_history()
    client.clear_chat_history()
    messagebox.showinfo("Wyczyszczono", "Historia została wyczyszczona.")



def save_response_choice():
    rendered = response_text.get("1.0", tk.END).strip()
    if not rendered:
        messagebox.showwarning("Brak odpowiedzi", "Nie ma odpowiedzi do zapisania.")
        return

    win = tk.Toplevel(root)
    win.title("Co chcesz zapisać?")
    win.geometry("340x120")
    tk.Label(win, text="Wybierz co chcesz zapisać:").pack(pady=8)

    def save(type_: str):
        raw = last_ai_response or rendered
        to_save = raw if type_ == "all" else extract_code_blocks(raw)
        if not to_save:
            messagebox.showwarning("Brak kodu", "Nie znaleziono kodu w odpowiedzi.")
            return

        filetypes = [
            ("Pliki Python", "*.py"),
            ("Pliki JavaScript", "*.js"),
            ("Pliki tekstowe", "*.txt"),
            ("Wszystkie pliki", "*.*")
        ] if type_ == "code" else [
            ("Pliki tekstowe", "*.txt"),
            ("Wszystkie pliki", "*.*")
        ]

        file_path = filedialog.asksaveasfilename(
            title="Zapisz plik",
            defaultextension="",
            filetypes=filetypes,
            initialfile="response"
        )

        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(to_save)
            messagebox.showinfo("Zapisano", f"Zapisano do {file_path}")
        win.destroy()

    ttk.Button(win, text="Cała odpowiedź", command=lambda: save("all")
               ).pack(fill="x", padx=40, pady=5)
    ttk.Button(win, text="Tylko kod", command=lambda: save("code")
               ).pack(fill="x", padx=40, pady=5)


def extract_code_blocks(text: str) -> str:
    """
    Zwraca połączone bloki kodu wyłuskane z treści odpowiedzi AI.
    1) Najpierw poprawne płotki ``` … ``` (usuwamy linię z nazwą języka).
    2) Gdy brak – niedomknięty płotek (od otwarcia do końca tekstu).
    3) Gdy dalej brak – ≥2 wcięte linie (blok z 4 spacjami / tabem).
    4) Gdy nadal brak – fragment po linii z nazwą języka (python/js/…).
    """
    code_blocks: list[str] = []


    fenced = re.finditer(
        r"```[ \t]*([\w.+-]+)?[ \t]*\n(.*?)```", text, re.DOTALL)
    for m in fenced:
        code_blocks.append(m.group(2).rstrip())

    if not code_blocks:
        m = re.search(r"```[ \t]*([\w.+-]+)?[ \t]*\n(.*)$",
                      text, re.DOTALL)
        if m:
            code_blocks.append(m.group(2).rstrip())

    if not code_blocks:
        indented = re.finditer(
            r"(?:^|\n)(?: {4}|\t).+?(?:\n(?: {4}|\t).+)+",
            text, re.DOTALL)
        for m in indented:
            lines = [ln.lstrip() for ln in m.group(0).splitlines()]
            code_blocks.append("\n".join(lines).rstrip())

    if not code_blocks:
        lang_block = re.finditer(
            r"(?:^|\n)(python|js|javascript|bash|sh|shell|sql|java|c\+\+|cpp|c#|cs|go|ruby|php|html|css)\s*\n(.*?)(?:\n{2,}|\Z)",
            text, re.DOTALL | re.IGNORECASE)
        for m in lang_block:
            code_blocks.append(m.group(2).rstrip())

    return "\n\n".join(code_blocks).strip()


def load_file_into_code_text():
    file_path = filedialog.askopenfilename(
        title="Wczytaj plik z kodem",
        filetypes=[
            ("Pliki Python", "*.py"),
            ("Pliki JavaScript", "*.js"),
            ("Pliki tekstowe", "*.txt"),
            ("Wszystkie pliki", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            code_text.delete("1.0", tk.END)
            code_text.insert(tk.END, file_content)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się wczytać pliku:\n{e}")


def edit_tune():
    win = tk.Toplevel(root)
    win.title("Edytuj prompt (tune)")
    win.minsize(800, 400)
    win.geometry("950x600")
    win.grab_set()
    win.columnconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)

    ttk.Label(win, text="Prompt systemowy (tune):",
              font=("Segoe UI", 12, "bold")).grid(
        row=0, column=0, sticky="w", padx=14, pady=(16, 6))

    tune_entry = scrolledtext.ScrolledText(
        win, wrap="word", font=("Consolas", 12))
    tune_entry.grid(row=1, column=0, sticky="nsew", padx=14, pady=(0, 10))
    tune_entry.insert(tk.END, client.tune)

    btn_frame = ttk.Frame(win)
    btn_frame.grid(row=2, column=0, pady=(0, 16), sticky="ew")
    btn_frame.columnconfigure((0, 1, 2), weight=1)

    def save_new_tune():
        client.change_tune(tune_entry.get("1.0", tk.END).strip())
        win.destroy()
        messagebox.showinfo("Tune zmieniony", "Nowy prompt systemowy został zapisany.")

    def restore_default_tune():
        tune_entry.delete("1.0", tk.END)
        tune_entry.insert(tk.END, client.config.get('default_tune', ''))

    ttk.Button(btn_frame, text="Zapisz", command=save_new_tune,
               style="Accent.TButton").grid(row=0, column=0, sticky="ew", padx=6)
    ttk.Button(btn_frame, text="Przywróć domyślny prompt",
               command=restore_default_tune).grid(row=0, column=1, sticky="ew", padx=6)
    ttk.Button(btn_frame, text="Zamknij", command=win.destroy,
               style="Danger.TButton").grid(row=0, column=2, sticky="ew", padx=6)

    def resize(event):
        tune_entry.config(width=max(60, int(win.winfo_width() / 10)),
                          height=max(10, int(win.winfo_height() / 30)))
    win.bind('<Configure>', resize)


def show_history_window():
    history_window = Toplevel(root)
    history_window.title("Historia zapytań i odpowiedzi")
    history_window.geometry("850x600")
    hist_box = scrolledtext.ScrolledText(
        history_window, width=100, height=35, state='normal',
        bg="#e8e8f5", font=("Consolas", 10), wrap="word")
    hist_box.pack(padx=10, pady=10, fill="both", expand=True)
    for idx, entry in enumerate(history_list, 1):
        hist_box.insert(tk.END,
                        f"[{idx}]\nKod:\n{entry['code']}\nOdpowiedź:\n{entry['response']}\n{'-'*40}\n")
    hist_box.config(state='disabled')
    ttk.Button(history_window, text="Wyczyść historię",
               command=clear_history, style="Danger.TButton").pack(pady=8)

def _insert_inline(widget: tk.Text, text: str, base_tag="normal") -> None:
    """
    Wstawia tekst, usuwając znaczniki **bold** i _italic_,
    oraz nakłada odpowiadające im tagi.
    """
    pattern = re.compile(r"\*\*(.+?)\*\*|_(.+?)_")
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            widget.insert(tk.END, text[pos:m.start()], base_tag)

        widget.insert(
            tk.END,
            m.group(1) or m.group(2),
            (base_tag, "bold") if m.group(1) else (base_tag, "italic")
        )
        pos = m.end()

    if pos < len(text):
        widget.insert(tk.END, text[pos:], base_tag)


def insert_markdown_fragment(widget: tk.Text, fragment: str) -> None:
    for raw in fragment.splitlines():
        line = raw.rstrip()
        if not line:
            widget.insert(tk.END, "\n")
            continue

        if re.match(r"\s*#+\s", line):
            content = re.sub(r"^\s*#+\s*", "", line)
            widget.insert(tk.END, content + "\n", "heading")
            continue

        bullet = re.match(r"\s*[-*•]\s+(.*)", line)
        if bullet:
            widget.insert(tk.END, "• ", "bullet")
            _insert_inline(widget, bullet.group(1), "bullet")
            widget.insert(tk.END, "\n")
            continue

        _insert_inline(widget, line)
        widget.insert(tk.END, "\n")


def format_ai_response_widget(widget: tk.Text, text: str) -> None:
    widget.config(state="normal")
    widget.delete("1.0", tk.END)

    colors = get_colors()
    widget.tag_configure("bold", font=("Segoe UI", 13, "bold"))
    widget.tag_configure("italic", font=("Segoe UI", 13, "italic"))
    widget.tag_configure("codeblock", font=("Consolas", 11),
                         background=colors["codeblock_bg"], foreground=colors["code_fg"],
                         lmargin1=10, lmargin2=10, spacing1=4, spacing3=4)
    widget.tag_configure("heading", font=("Segoe UI", 14, "bold"))
    widget.tag_configure("bullet", lmargin1=20, lmargin2=30, font=("Segoe UI", 13))
    widget.tag_configure("normal", font=("Segoe UI", 13))

    code_re = re.compile(r"```(.*?)```", re.DOTALL)
    pos = 0
    for m in code_re.finditer(text):
        insert_markdown_fragment(widget, text[pos:m.start()])
        widget.insert(tk.END, m.group(1).strip() + "\n", "codeblock")
        pos = m.end()

    insert_markdown_fragment(widget, text[pos:])
    widget.config(state="disabled")

root = tk.Tk()
root.title("Asystent AI dla Testera Oprogramowania - Gemini 2.0")
root.geometry("980x870")
apply_styles(root)

ttk.Label(root, text="Asystent AI dla Testera Oprogramowania",
          style="Header.TLabel").pack(pady=(16, 8))

code_frame = ttk.LabelFrame(root, text="Kod do analizy",
                            style="Section.TLabelframe")
code_frame.pack(fill="x", padx=24, pady=(8, 4))
code_text = scrolledtext.ScrolledText(
    code_frame, width=110, height=12,
    font=("Consolas", 11),
    bg=LIGHT_COLORS["code_bg"], fg=LIGHT_COLORS["code_fg"],
    wrap="word")
code_text.pack(fill="both", padx=12, pady=8)
ttk.Button(code_frame, text="Wczytaj plik…",
           command=load_file_into_code_text, width=17).pack(
    anchor='w', padx=12, pady=(0, 6))

options_frame = ttk.Frame(root)
options_frame.pack(fill="x", padx=24, pady=(0, 7))
generate_code_only = tk.BooleanVar(value=False)
ttk.Checkbutton(options_frame, text="Generuj odpowiedź tylko jako kod",
                variable=generate_code_only).pack(anchor='w', padx=2)

ttk.Button(root, text="Wyślij do Asystenta", command=send_query,
           style="Accent.TButton", width=27).pack(pady=(8, 10))

response_frame = ttk.LabelFrame(root, text="Odpowiedź asystenta",
                                style="Section.TLabelframe")
response_frame.pack(fill="x", padx=24, pady=(2, 0))
response_text = scrolledtext.ScrolledText(
    response_frame, width=110, height=13,
    state='disabled',
    font=("Segoe UI", 13),
    bg=LIGHT_COLORS["resp_bg"], fg=LIGHT_COLORS["resp_fg"],
    wrap="word")
response_text.pack(padx=12, pady=8)

btn_frame = ttk.Frame(root)
btn_frame.pack(fill="x", padx=24, pady=(8, 16))
btn_frame.columnconfigure((0, 1, 2, 3), weight=1)

ttk.Button(btn_frame, text="Zapisz odpowiedź", command=save_response_choice,
           width=17).grid(row=0, column=0, padx=5, sticky="ew")
ttk.Button(btn_frame, text="Edytuj prompt (tune)", command=edit_tune,
           width=19).grid(row=0, column=1, padx=5, sticky="ew")
ttk.Button(btn_frame, text="Tryb jasny/ciemny", command=toggle_ui_mode,
           width=17).grid(row=0, column=2, padx=5, sticky="ew")
ttk.Button(btn_frame, text="Historia", command=show_history_window,
           width=13).grid(row=0, column=3, padx=5, sticky="ew")

history_list = load_history()
update_theme()

if history_list:
    last_ai_response = history_list[-1]["response"]
    format_ai_response_widget(response_text, last_ai_response)

show_intro_popup()
root.mainloop()
