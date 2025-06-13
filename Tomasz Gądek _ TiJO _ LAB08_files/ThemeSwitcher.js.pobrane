class ThemeSwitcher {
    constructor(toggleButtonId, themeLinkId) {
        this.toggleButton = document.getElementById(toggleButtonId);
        this.themeLink = document.getElementById(themeLinkId);
        this.init();
    }

    init() {
        // Pobieramy nazwę pliku z localStorage (lub ustawiamy domyślną wartość)
        const savedTheme = localStorage.getItem('theme') || 'general.css';
        this.setTheme(savedTheme);

        // Nasłuchujemy kliknięcia w przycisk
        this.toggleButton.addEventListener('click', (e) => {
            e.preventDefault();
            this.toggleTheme();
        });
    }

    getCurrentThemeFile() {
        const href = this.themeLink.getAttribute('href');  
        return href.split('/').pop(); // Pobieramy tylko nazwę pliku z pełnej ścieżki
    }

    setTheme(themeFile) {
        // Pobieramy katalog, w którym znajduje się aktualny plik CSS
        const currentHref = this.themeLink.getAttribute('href');
        const basePath = currentHref.substring(0, currentHref.lastIndexOf('/') + 1);
        
        // Aktualizujemy link do arkusza stylów
        this.themeLink.setAttribute('href', basePath + themeFile);
        localStorage.setItem('theme', themeFile);

        // Aktualizujemy tekst/ikonę przycisku
        this.toggleButton.textContent = (themeFile === 'general-light.css') ? '☁️' : '☀️';
    }

    toggleTheme() {
        const currentTheme = this.getCurrentThemeFile();
        const newTheme = (currentTheme === 'general.css') ? 'general-light.css' : 'general.css';
        this.setTheme(newTheme);
    }
}

// Tworzymy instancję klasy ThemeSwitcher
const themeSwitcher = new ThemeSwitcher('theme-toggle', 'theme-style');
