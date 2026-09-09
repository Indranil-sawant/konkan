// main.js - 2026 Konkan Guide Interactive Logic

document.addEventListener('DOMContentLoaded', function() {
    
    // Header Frosted Scroll Effect
    const header = document.getElementById('main-header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 30) {
                header.classList.add('bg-white/95', 'shadow-md', 'border-slate-200/90');
                header.classList.remove('bg-white/80', 'border-slate-200/60');
            } else {
                header.classList.remove('bg-white/95', 'shadow-md', 'border-slate-200/90');
                header.classList.add('bg-white/80', 'border-slate-200/60');
            }
        });
    }

    // Modal Interaction (Search Modal keyboard & outside click)
    const searchModal = document.getElementById('search-modal');
    if (searchModal) {
        window.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && !searchModal.classList.contains('hidden')) {
                searchModal.classList.add('hidden');
            }
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                searchModal.classList.remove('hidden');
                const searchInput = document.getElementById('search-input-modal');
                if (searchInput) searchInput.focus();
            }
        });

        searchModal.addEventListener('click', function(e) {
            if (e.target === searchModal) {
                searchModal.classList.add('hidden');
            }
        });
    }

    // Auto Lazy-loading for performance
    const images = document.querySelectorAll('img:not([loading])');
    images.forEach(img => {
        img.setAttribute('loading', 'lazy');
    });

});
